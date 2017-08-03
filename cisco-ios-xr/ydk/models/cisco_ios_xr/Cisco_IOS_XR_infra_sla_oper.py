""" Cisco_IOS_XR_infra_sla_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-sla package operational data.

This module contains definitions
for the following management objects\:
  sla\: SLA oper commands
  sla\-nodes\: sla nodes

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Sla(Entity):
    """
    SLA oper commands
    
    .. attribute:: protocols
    
    	Table of all SLA protocols
    	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols>`
    
    

    """

    _prefix = 'infra-sla-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sla, self).__init__()
        self._top_entity = None

        self.yang_name = "sla"
        self.yang_parent_name = "Cisco-IOS-XR-infra-sla-oper"

        self.protocols = Sla.Protocols()
        self.protocols.parent = self
        self._children_name_map["protocols"] = "protocols"
        self._children_yang_names.add("protocols")


    class Protocols(Entity):
        """
        Table of all SLA protocols
        
        .. attribute:: ethernet
        
        	The Ethernet SLA protocol
        	**type**\:   :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet>`
        
        

        """

        _prefix = 'infra-sla-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sla.Protocols, self).__init__()

            self.yang_name = "protocols"
            self.yang_parent_name = "sla"

            self.ethernet = Sla.Protocols.Ethernet()
            self.ethernet.parent = self
            self._children_name_map["ethernet"] = "ethernet"
            self._children_yang_names.add("ethernet")


        class Ethernet(Entity):
            """
            The Ethernet SLA protocol
            
            .. attribute:: config_errors
            
            	Table of SLA configuration errors on configured operations
            	**type**\:   :py:class:`ConfigErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.ConfigErrors>`
            
            .. attribute:: on_demand_operations
            
            	Table of SLA on\-demand operations
            	**type**\:   :py:class:`OnDemandOperations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations>`
            
            .. attribute:: operations
            
            	Table of SLA operations
            	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations>`
            
            .. attribute:: statistics_currents
            
            	Table of current statistics for SLA operations
            	**type**\:   :py:class:`StatisticsCurrents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents>`
            
            .. attribute:: statistics_historicals
            
            	Table of historical statistics for SLA operations
            	**type**\:   :py:class:`StatisticsHistoricals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals>`
            
            .. attribute:: statistics_on_demand_currents
            
            	Table of current statistics for SLA on\-demand operations
            	**type**\:   :py:class:`StatisticsOnDemandCurrents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents>`
            
            .. attribute:: statistics_on_demand_historicals
            
            	Table of historical statistics for SLA on\-demand operations
            	**type**\:   :py:class:`StatisticsOnDemandHistoricals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sla.Protocols.Ethernet, self).__init__()

                self.yang_name = "ethernet"
                self.yang_parent_name = "protocols"

                self.config_errors = Sla.Protocols.Ethernet.ConfigErrors()
                self.config_errors.parent = self
                self._children_name_map["config_errors"] = "config-errors"
                self._children_yang_names.add("config-errors")

                self.on_demand_operations = Sla.Protocols.Ethernet.OnDemandOperations()
                self.on_demand_operations.parent = self
                self._children_name_map["on_demand_operations"] = "on-demand-operations"
                self._children_yang_names.add("on-demand-operations")

                self.operations = Sla.Protocols.Ethernet.Operations()
                self.operations.parent = self
                self._children_name_map["operations"] = "operations"
                self._children_yang_names.add("operations")

                self.statistics_currents = Sla.Protocols.Ethernet.StatisticsCurrents()
                self.statistics_currents.parent = self
                self._children_name_map["statistics_currents"] = "statistics-currents"
                self._children_yang_names.add("statistics-currents")

                self.statistics_historicals = Sla.Protocols.Ethernet.StatisticsHistoricals()
                self.statistics_historicals.parent = self
                self._children_name_map["statistics_historicals"] = "statistics-historicals"
                self._children_yang_names.add("statistics-historicals")

                self.statistics_on_demand_currents = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents()
                self.statistics_on_demand_currents.parent = self
                self._children_name_map["statistics_on_demand_currents"] = "statistics-on-demand-currents"
                self._children_yang_names.add("statistics-on-demand-currents")

                self.statistics_on_demand_historicals = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals()
                self.statistics_on_demand_historicals.parent = self
                self._children_name_map["statistics_on_demand_historicals"] = "statistics-on-demand-historicals"
                self._children_yang_names.add("statistics-on-demand-historicals")


            class StatisticsOnDemandCurrents(Entity):
                """
                Table of current statistics for SLA on\-demand
                operations
                
                .. attribute:: statistics_on_demand_current
                
                	Current statistics data for an SLA on\-demand operation
                	**type**\: list of    :py:class:`StatisticsOnDemandCurrent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents, self).__init__()

                    self.yang_name = "statistics-on-demand-currents"
                    self.yang_parent_name = "ethernet"

                    self.statistics_on_demand_current = YList(self)

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
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents, self).__setattr__(name, value)


                class StatisticsOnDemandCurrent(Entity):
                    """
                    Current statistics data for an SLA on\-demand
                    operation
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: flr_calculation_interval
                    
                    	Interval between FLR calculations for SLM, in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\:  int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: operation_id
                    
                    	Operation ID
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: operation_metric
                    
                    	Metrics gathered for the operation
                    	**type**\: list of    :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric>`
                    
                    .. attribute:: operation_schedule
                    
                    	Operation schedule
                    	**type**\:   :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule>`
                    
                    .. attribute:: probe_type
                    
                    	Type of probe used by the operation
                    	**type**\:  str
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:   :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent, self).__init__()

                        self.yang_name = "statistics-on-demand-current"
                        self.yang_parent_name = "statistics-on-demand-currents"

                        self.display_long = YLeaf(YType.str, "display-long")

                        self.display_short = YLeaf(YType.str, "display-short")

                        self.domain_name = YLeaf(YType.str, "domain-name")

                        self.flr_calculation_interval = YLeaf(YType.uint32, "flr-calculation-interval")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.mep_id = YLeaf(YType.uint32, "mep-id")

                        self.operation_id = YLeaf(YType.uint32, "operation-id")

                        self.probe_type = YLeaf(YType.str, "probe-type")

                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule()
                        self.operation_schedule.parent = self
                        self._children_name_map["operation_schedule"] = "operation-schedule"
                        self._children_yang_names.add("operation-schedule")

                        self.specific_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"
                        self._children_yang_names.add("specific-options")

                        self.operation_metric = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("display_long",
                                        "display_short",
                                        "domain_name",
                                        "flr_calculation_interval",
                                        "interface_name",
                                        "mac_address",
                                        "mep_id",
                                        "operation_id",
                                        "probe_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent, self).__setattr__(name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:   :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:   :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:   :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "statistics-on-demand-current"

                            self.oper_type = YLeaf(YType.enumeration, "oper-type")

                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"
                            self._children_yang_names.add("configured-operation-options")

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._children_yang_names.add("ondemand-operation-options")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("oper_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions, self).__setattr__(name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.profile_name = YLeaf(YType.str, "profile-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "configured-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.ondemand_operation_id = YLeaf(YType.uint32, "ondemand-operation-id")

                                self.probe_count = YLeaf(YType.uint8, "probe-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ondemand_operation_id",
                                                "probe_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ondemand_operation_id.is_set or
                                    self.probe_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ondemand_operation_id.yfilter != YFilter.not_set or
                                    self.probe_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ondemand-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ondemand_operation_id.is_set or self.ondemand_operation_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ondemand_operation_id.get_name_leafdata())
                                if (self.probe_count.is_set or self.probe_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.probe_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ondemand-operation-id" or name == "probe-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ondemand-operation-id"):
                                    self.ondemand_operation_id = value
                                    self.ondemand_operation_id.value_namespace = name_space
                                    self.ondemand_operation_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "probe-count"):
                                    self.probe_count = value
                                    self.probe_count.value_namespace = name_space
                                    self.probe_count.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.oper_type.is_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_data()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.oper_type.yfilter != YFilter.not_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_operation()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "specific-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.oper_type.is_set or self.oper_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oper_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "configured-operation-options"):
                                if (self.configured_operation_options is None):
                                    self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions()
                                    self.configured_operation_options.parent = self
                                    self._children_name_map["configured_operation_options"] = "configured-operation-options"
                                return self.configured_operation_options

                            if (child_yang_name == "ondemand-operation-options"):
                                if (self.ondemand_operation_options is None):
                                    self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions()
                                    self.ondemand_operation_options.parent = self
                                    self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                                return self.ondemand_operation_options

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "configured-operation-options" or name == "ondemand-operation-options" or name == "oper-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "oper-type"):
                                self.oper_type = value
                                self.oper_type.value_namespace = name_space
                                self.oper_type.value_namespace_prefix = name_space_prefix


                    class OperationSchedule(Entity):
                        """
                        Operation schedule
                        
                        .. attribute:: schedule_duration
                        
                        	Duration of a probe for the operation in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: schedule_interval
                        
                        	Interval between the start times of consecutive probes,  in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time
                        
                        	Start time of the first probe, in seconds since the Unix Epoch
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time_configured
                        
                        	Whether or not the operation start time was explicitly configured
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule, self).__init__()

                            self.yang_name = "operation-schedule"
                            self.yang_parent_name = "statistics-on-demand-current"

                            self.schedule_duration = YLeaf(YType.uint32, "schedule-duration")

                            self.schedule_interval = YLeaf(YType.uint32, "schedule-interval")

                            self.start_time = YLeaf(YType.uint32, "start-time")

                            self.start_time_configured = YLeaf(YType.boolean, "start-time-configured")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("schedule_duration",
                                            "schedule_interval",
                                            "start_time",
                                            "start_time_configured") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.schedule_duration.is_set or
                                self.schedule_interval.is_set or
                                self.start_time.is_set or
                                self.start_time_configured.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.schedule_duration.yfilter != YFilter.not_set or
                                self.schedule_interval.yfilter != YFilter.not_set or
                                self.start_time.yfilter != YFilter.not_set or
                                self.start_time_configured.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operation-schedule" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.schedule_duration.is_set or self.schedule_duration.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.schedule_duration.get_name_leafdata())
                            if (self.schedule_interval.is_set or self.schedule_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.schedule_interval.get_name_leafdata())
                            if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time.get_name_leafdata())
                            if (self.start_time_configured.is_set or self.start_time_configured.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time_configured.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "schedule-duration" or name == "schedule-interval" or name == "start-time" or name == "start-time-configured"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "schedule-duration"):
                                self.schedule_duration = value
                                self.schedule_duration.value_namespace = name_space
                                self.schedule_duration.value_namespace_prefix = name_space_prefix
                            if(value_path == "schedule-interval"):
                                self.schedule_interval = value
                                self.schedule_interval.value_namespace = name_space
                                self.schedule_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time"):
                                self.start_time = value
                                self.start_time.value_namespace = name_space
                                self.start_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time-configured"):
                                self.start_time_configured = value
                                self.start_time_configured.value_namespace = name_space
                                self.start_time_configured.value_namespace_prefix = name_space_prefix


                    class OperationMetric(Entity):
                        """
                        Metrics gathered for the operation
                        
                        .. attribute:: bucket
                        
                        	Buckets stored for the metric
                        	**type**\: list of    :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket>`
                        
                        .. attribute:: config
                        
                        	Configuration of the metric
                        	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric, self).__init__()

                            self.yang_name = "operation-metric"
                            self.yang_parent_name = "statistics-on-demand-current"

                            self.config = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.bucket = YList(self)

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
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric, self).__setattr__(name, value)


                        class Config(Entity):
                            """
                            Configuration of the metric
                            
                            .. attribute:: bins_count
                            
                            	Total number of bins into which to aggregate. 0 if no aggregation
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bins_width
                            
                            	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bucket_size
                            
                            	Size of buckets into which measurements are collected
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: bucket_size_unit
                            
                            	Whether bucket size is 'per\-probe' or 'probes'
                            	**type**\:   :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:   :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "operation-metric"

                                self.bins_count = YLeaf(YType.uint16, "bins-count")

                                self.bins_width = YLeaf(YType.uint16, "bins-width")

                                self.bucket_size = YLeaf(YType.uint8, "bucket-size")

                                self.bucket_size_unit = YLeaf(YType.enumeration, "bucket-size-unit")

                                self.buckets_archive = YLeaf(YType.uint32, "buckets-archive")

                                self.metric_type = YLeaf(YType.enumeration, "metric-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bins_count",
                                                "bins_width",
                                                "bucket_size",
                                                "bucket_size_unit",
                                                "buckets_archive",
                                                "metric_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bins_count.is_set or
                                    self.bins_width.is_set or
                                    self.bucket_size.is_set or
                                    self.bucket_size_unit.is_set or
                                    self.buckets_archive.is_set or
                                    self.metric_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bins_count.yfilter != YFilter.not_set or
                                    self.bins_width.yfilter != YFilter.not_set or
                                    self.bucket_size.yfilter != YFilter.not_set or
                                    self.bucket_size_unit.yfilter != YFilter.not_set or
                                    self.buckets_archive.yfilter != YFilter.not_set or
                                    self.metric_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "config" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bins_count.is_set or self.bins_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bins_count.get_name_leafdata())
                                if (self.bins_width.is_set or self.bins_width.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bins_width.get_name_leafdata())
                                if (self.bucket_size.is_set or self.bucket_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bucket_size.get_name_leafdata())
                                if (self.bucket_size_unit.is_set or self.bucket_size_unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bucket_size_unit.get_name_leafdata())
                                if (self.buckets_archive.is_set or self.buckets_archive.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.buckets_archive.get_name_leafdata())
                                if (self.metric_type.is_set or self.metric_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.metric_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bins-count" or name == "bins-width" or name == "bucket-size" or name == "bucket-size-unit" or name == "buckets-archive" or name == "metric-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bins-count"):
                                    self.bins_count = value
                                    self.bins_count.value_namespace = name_space
                                    self.bins_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "bins-width"):
                                    self.bins_width = value
                                    self.bins_width.value_namespace = name_space
                                    self.bins_width.value_namespace_prefix = name_space_prefix
                                if(value_path == "bucket-size"):
                                    self.bucket_size = value
                                    self.bucket_size.value_namespace = name_space
                                    self.bucket_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "bucket-size-unit"):
                                    self.bucket_size_unit = value
                                    self.bucket_size_unit.value_namespace = name_space
                                    self.bucket_size_unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "buckets-archive"):
                                    self.buckets_archive = value
                                    self.buckets_archive.value_namespace = name_space
                                    self.buckets_archive.value_namespace_prefix = name_space_prefix
                                if(value_path == "metric-type"):
                                    self.metric_type = value
                                    self.metric_type.value_namespace = name_space
                                    self.metric_type.value_namespace_prefix = name_space_prefix


                        class Bucket(Entity):
                            """
                            Buckets stored for the metric
                            
                            .. attribute:: average
                            
                            	Mean of the results in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: contents
                            
                            	The contents of the bucket; bins or samples
                            	**type**\:   :py:class:`Contents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents>`
                            
                            .. attribute:: corrupt
                            
                            	Number of corrupt packets in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_lost_count
                            
                            	The number of data packets lost across the bucket, used in the calculation of overall FLR
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_sent_count
                            
                            	The number of data packets sent across the bucket, used in the calculation of overall FLR
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplicates
                            
                            	Number of duplicate packets received in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duration
                            
                            	Length of time for which the bucket is being filled in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: lost
                            
                            	Number of lost packets in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: minimum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: out_of_order
                            
                            	Number of packets recieved out\-of\-order in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: overall_flr
                            
                            	Frame Loss Ratio across the whole bucket, in millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: percentage
                            
                            .. attribute:: premature_reason
                            
                            	If the probe ended prematurely, the error that caused a probe to end
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: premature_reason_string
                            
                            	Description of the error code that caused the probe to end prematurely. For informational purposes only
                            	**type**\:  str
                            
                            .. attribute:: result_count
                            
                            	The count of samples collected in the bucket
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sent
                            
                            	Number of packets sent in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: standard_deviation
                            
                            	Standard deviation of the results in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: start_at
                            
                            	Absolute time that the bucket started being filled at
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suspect_cleared_mid_bucket
                            
                            	Results suspect as bucket was cleared mid\-way through being filled
                            	**type**\:  bool
                            
                            .. attribute:: suspect_clock_drift
                            
                            	Results suspect as more than 10 seconds time drift detected
                            	**type**\:  bool
                            
                            .. attribute:: suspect_flr_low_packet_count
                            
                            	Results suspect as FLR calculated based on a low packet count
                            	**type**\:  bool
                            
                            .. attribute:: suspect_management_latency
                            
                            	Results suspect as processing of results has been delayed
                            	**type**\:  bool
                            
                            .. attribute:: suspect_memory_allocation_failed
                            
                            	Results suspect due to a memory allocation failure
                            	**type**\:  bool
                            
                            .. attribute:: suspect_misordering
                            
                            	Results suspect as misordering has been detected , affecting results
                            	**type**\:  bool
                            
                            .. attribute:: suspect_multiple_buckets
                            
                            	Results suspect as the probe has been configured across multiple buckets
                            	**type**\:  bool
                            
                            .. attribute:: suspect_premature_end
                            
                            	Results suspect due to a probe ending prematurely
                            	**type**\:  bool
                            
                            .. attribute:: suspect_probe_restarted
                            
                            	Results suspect as probe restarted mid\-way through the bucket
                            	**type**\:  bool
                            
                            .. attribute:: suspect_schedule_latency
                            
                            	Results suspect due to scheduling latency causing one or more packets to not be sent
                            	**type**\:  bool
                            
                            .. attribute:: suspect_send_fail
                            
                            	Results suspect due to failure to send one or more packets
                            	**type**\:  bool
                            
                            .. attribute:: suspect_start_mid_bucket
                            
                            	Results suspect due to a probe starting mid\-way through a bucket
                            	**type**\:  bool
                            
                            .. attribute:: time_of_maximum
                            
                            	Absolute time that the maximum value was recorded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_of_minimum
                            
                            	Absolute time that the minimum value was recorded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket, self).__init__()

                                self.yang_name = "bucket"
                                self.yang_parent_name = "operation-metric"

                                self.average = YLeaf(YType.int32, "average")

                                self.corrupt = YLeaf(YType.uint32, "corrupt")

                                self.data_lost_count = YLeaf(YType.uint32, "data-lost-count")

                                self.data_sent_count = YLeaf(YType.uint32, "data-sent-count")

                                self.duplicates = YLeaf(YType.uint32, "duplicates")

                                self.duration = YLeaf(YType.uint32, "duration")

                                self.lost = YLeaf(YType.uint32, "lost")

                                self.maximum = YLeaf(YType.int32, "maximum")

                                self.minimum = YLeaf(YType.int32, "minimum")

                                self.out_of_order = YLeaf(YType.uint32, "out-of-order")

                                self.overall_flr = YLeaf(YType.int32, "overall-flr")

                                self.premature_reason = YLeaf(YType.uint32, "premature-reason")

                                self.premature_reason_string = YLeaf(YType.str, "premature-reason-string")

                                self.result_count = YLeaf(YType.uint32, "result-count")

                                self.sent = YLeaf(YType.uint32, "sent")

                                self.standard_deviation = YLeaf(YType.int32, "standard-deviation")

                                self.start_at = YLeaf(YType.uint32, "start-at")

                                self.suspect_cleared_mid_bucket = YLeaf(YType.boolean, "suspect-cleared-mid-bucket")

                                self.suspect_clock_drift = YLeaf(YType.boolean, "suspect-clock-drift")

                                self.suspect_flr_low_packet_count = YLeaf(YType.boolean, "suspect-flr-low-packet-count")

                                self.suspect_management_latency = YLeaf(YType.boolean, "suspect-management-latency")

                                self.suspect_memory_allocation_failed = YLeaf(YType.boolean, "suspect-memory-allocation-failed")

                                self.suspect_misordering = YLeaf(YType.boolean, "suspect-misordering")

                                self.suspect_multiple_buckets = YLeaf(YType.boolean, "suspect-multiple-buckets")

                                self.suspect_premature_end = YLeaf(YType.boolean, "suspect-premature-end")

                                self.suspect_probe_restarted = YLeaf(YType.boolean, "suspect-probe-restarted")

                                self.suspect_schedule_latency = YLeaf(YType.boolean, "suspect-schedule-latency")

                                self.suspect_send_fail = YLeaf(YType.boolean, "suspect-send-fail")

                                self.suspect_start_mid_bucket = YLeaf(YType.boolean, "suspect-start-mid-bucket")

                                self.time_of_maximum = YLeaf(YType.uint32, "time-of-maximum")

                                self.time_of_minimum = YLeaf(YType.uint32, "time-of-minimum")

                                self.contents = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self._children_name_map["contents"] = "contents"
                                self._children_yang_names.add("contents")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("average",
                                                "corrupt",
                                                "data_lost_count",
                                                "data_sent_count",
                                                "duplicates",
                                                "duration",
                                                "lost",
                                                "maximum",
                                                "minimum",
                                                "out_of_order",
                                                "overall_flr",
                                                "premature_reason",
                                                "premature_reason_string",
                                                "result_count",
                                                "sent",
                                                "standard_deviation",
                                                "start_at",
                                                "suspect_cleared_mid_bucket",
                                                "suspect_clock_drift",
                                                "suspect_flr_low_packet_count",
                                                "suspect_management_latency",
                                                "suspect_memory_allocation_failed",
                                                "suspect_misordering",
                                                "suspect_multiple_buckets",
                                                "suspect_premature_end",
                                                "suspect_probe_restarted",
                                                "suspect_schedule_latency",
                                                "suspect_send_fail",
                                                "suspect_start_mid_bucket",
                                                "time_of_maximum",
                                                "time_of_minimum") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket, self).__setattr__(name, value)


                            class Contents(Entity):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:   :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:   :py:class:`SlaOperBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucket>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:   :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents, self).__init__()

                                    self.yang_name = "contents"
                                    self.yang_parent_name = "bucket"

                                    self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self._children_name_map["aggregated"] = "aggregated"
                                    self._children_yang_names.add("aggregated")

                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self
                                    self._children_name_map["unaggregated"] = "unaggregated"
                                    self._children_yang_names.add("unaggregated")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bucket_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents, self).__setattr__(name, value)


                                class Aggregated(Entity):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated, self).__init__()

                                        self.yang_name = "aggregated"
                                        self.yang_parent_name = "contents"

                                        self.bins = YList(self)

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
                                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated, self).__setattr__(name, value)


                                    class Bins(Entity):
                                        """
                                        The bins of an SLA metric bucket
                                        
                                        .. attribute:: count
                                        
                                        	The total number of results in the bin
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lower_bound
                                        
                                        	Lower bound (inclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: lower_bound_tenths
                                        
                                        	Lower bound (inclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: sum
                                        
                                        	The sum of the results in the bin, in microseconds or millionths of a percent
                                        	**type**\:  int
                                        
                                        	**range:** \-9223372036854775808..9223372036854775807
                                        
                                        .. attribute:: upper_bound
                                        
                                        	Upper bound (exclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: upper_bound_tenths
                                        
                                        	Upper bound (exclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__init__()

                                            self.yang_name = "bins"
                                            self.yang_parent_name = "aggregated"

                                            self.count = YLeaf(YType.uint32, "count")

                                            self.lower_bound = YLeaf(YType.int32, "lower-bound")

                                            self.lower_bound_tenths = YLeaf(YType.int32, "lower-bound-tenths")

                                            self.sum = YLeaf(YType.int64, "sum")

                                            self.upper_bound = YLeaf(YType.int32, "upper-bound")

                                            self.upper_bound_tenths = YLeaf(YType.int32, "upper-bound-tenths")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("count",
                                                            "lower_bound",
                                                            "lower_bound_tenths",
                                                            "sum",
                                                            "upper_bound",
                                                            "upper_bound_tenths") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.count.is_set or
                                                self.lower_bound.is_set or
                                                self.lower_bound_tenths.is_set or
                                                self.sum.is_set or
                                                self.upper_bound.is_set or
                                                self.upper_bound_tenths.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.count.yfilter != YFilter.not_set or
                                                self.lower_bound.yfilter != YFilter.not_set or
                                                self.lower_bound_tenths.yfilter != YFilter.not_set or
                                                self.sum.yfilter != YFilter.not_set or
                                                self.upper_bound.yfilter != YFilter.not_set or
                                                self.upper_bound_tenths.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "bins" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/contents/aggregated/%s" % self.get_segment_path()
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.count.get_name_leafdata())
                                            if (self.lower_bound.is_set or self.lower_bound.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.lower_bound.get_name_leafdata())
                                            if (self.lower_bound_tenths.is_set or self.lower_bound_tenths.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.lower_bound_tenths.get_name_leafdata())
                                            if (self.sum.is_set or self.sum.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sum.get_name_leafdata())
                                            if (self.upper_bound.is_set or self.upper_bound.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.upper_bound.get_name_leafdata())
                                            if (self.upper_bound_tenths.is_set or self.upper_bound_tenths.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.upper_bound_tenths.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "count" or name == "lower-bound" or name == "lower-bound-tenths" or name == "sum" or name == "upper-bound" or name == "upper-bound-tenths"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "count"):
                                                self.count = value
                                                self.count.value_namespace = name_space
                                                self.count.value_namespace_prefix = name_space_prefix
                                            if(value_path == "lower-bound"):
                                                self.lower_bound = value
                                                self.lower_bound.value_namespace = name_space
                                                self.lower_bound.value_namespace_prefix = name_space_prefix
                                            if(value_path == "lower-bound-tenths"):
                                                self.lower_bound_tenths = value
                                                self.lower_bound_tenths.value_namespace = name_space
                                                self.lower_bound_tenths.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sum"):
                                                self.sum = value
                                                self.sum.value_namespace = name_space
                                                self.sum.value_namespace_prefix = name_space_prefix
                                            if(value_path == "upper-bound"):
                                                self.upper_bound = value
                                                self.upper_bound.value_namespace = name_space
                                                self.upper_bound.value_namespace_prefix = name_space_prefix
                                            if(value_path == "upper-bound-tenths"):
                                                self.upper_bound_tenths = value
                                                self.upper_bound_tenths.value_namespace = name_space
                                                self.upper_bound_tenths.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.bins:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.bins:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "aggregated" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/contents/%s" % self.get_segment_path()
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "bins"):
                                            for c in self.bins:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.bins.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "bins"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class Unaggregated(Entity):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated, self).__init__()

                                        self.yang_name = "unaggregated"
                                        self.yang_parent_name = "contents"

                                        self.sample = YList(self)

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
                                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated, self).__setattr__(name, value)


                                    class Sample(Entity):
                                        """
                                        The samples of an SLA metric bucket
                                        
                                        .. attribute:: corrupt
                                        
                                        	Whether the sample packet was corrupt
                                        	**type**\:  bool
                                        
                                        .. attribute:: frames_lost
                                        
                                        	For FLR measurements, the number of frames lost, if available
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: frames_sent
                                        
                                        	For FLR measurements, the number of frames sent, if available
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: no_data_packets
                                        
                                        	Whether a measurement could not be made because no data packets were sent in the sample period. Only applicable for LMM measurements
                                        	**type**\:  bool
                                        
                                        .. attribute:: out_of_order
                                        
                                        	Whether the sample packet was received out\-of\-order
                                        	**type**\:  bool
                                        
                                        .. attribute:: result
                                        
                                        	The result (in microseconds or millionths of a percent) of the sample, if available
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: sent
                                        
                                        	Whether the sample packet was sucessfully sent
                                        	**type**\:  bool
                                        
                                        .. attribute:: sent_at
                                        
                                        	The time (in milliseconds relative to the start time of the bucket) that the sample was sent at
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: timed_out
                                        
                                        	Whether the sample packet timed out
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__init__()

                                            self.yang_name = "sample"
                                            self.yang_parent_name = "unaggregated"

                                            self.corrupt = YLeaf(YType.boolean, "corrupt")

                                            self.frames_lost = YLeaf(YType.uint32, "frames-lost")

                                            self.frames_sent = YLeaf(YType.uint32, "frames-sent")

                                            self.no_data_packets = YLeaf(YType.boolean, "no-data-packets")

                                            self.out_of_order = YLeaf(YType.boolean, "out-of-order")

                                            self.result = YLeaf(YType.int32, "result")

                                            self.sent = YLeaf(YType.boolean, "sent")

                                            self.sent_at = YLeaf(YType.uint32, "sent-at")

                                            self.timed_out = YLeaf(YType.boolean, "timed-out")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("corrupt",
                                                            "frames_lost",
                                                            "frames_sent",
                                                            "no_data_packets",
                                                            "out_of_order",
                                                            "result",
                                                            "sent",
                                                            "sent_at",
                                                            "timed_out") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.corrupt.is_set or
                                                self.frames_lost.is_set or
                                                self.frames_sent.is_set or
                                                self.no_data_packets.is_set or
                                                self.out_of_order.is_set or
                                                self.result.is_set or
                                                self.sent.is_set or
                                                self.sent_at.is_set or
                                                self.timed_out.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.corrupt.yfilter != YFilter.not_set or
                                                self.frames_lost.yfilter != YFilter.not_set or
                                                self.frames_sent.yfilter != YFilter.not_set or
                                                self.no_data_packets.yfilter != YFilter.not_set or
                                                self.out_of_order.yfilter != YFilter.not_set or
                                                self.result.yfilter != YFilter.not_set or
                                                self.sent.yfilter != YFilter.not_set or
                                                self.sent_at.yfilter != YFilter.not_set or
                                                self.timed_out.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "sample" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/contents/unaggregated/%s" % self.get_segment_path()
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.corrupt.is_set or self.corrupt.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.corrupt.get_name_leafdata())
                                            if (self.frames_lost.is_set or self.frames_lost.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.frames_lost.get_name_leafdata())
                                            if (self.frames_sent.is_set or self.frames_sent.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.frames_sent.get_name_leafdata())
                                            if (self.no_data_packets.is_set or self.no_data_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.no_data_packets.get_name_leafdata())
                                            if (self.out_of_order.is_set or self.out_of_order.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.out_of_order.get_name_leafdata())
                                            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.result.get_name_leafdata())
                                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sent.get_name_leafdata())
                                            if (self.sent_at.is_set or self.sent_at.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sent_at.get_name_leafdata())
                                            if (self.timed_out.is_set or self.timed_out.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.timed_out.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "corrupt" or name == "frames-lost" or name == "frames-sent" or name == "no-data-packets" or name == "out-of-order" or name == "result" or name == "sent" or name == "sent-at" or name == "timed-out"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "corrupt"):
                                                self.corrupt = value
                                                self.corrupt.value_namespace = name_space
                                                self.corrupt.value_namespace_prefix = name_space_prefix
                                            if(value_path == "frames-lost"):
                                                self.frames_lost = value
                                                self.frames_lost.value_namespace = name_space
                                                self.frames_lost.value_namespace_prefix = name_space_prefix
                                            if(value_path == "frames-sent"):
                                                self.frames_sent = value
                                                self.frames_sent.value_namespace = name_space
                                                self.frames_sent.value_namespace_prefix = name_space_prefix
                                            if(value_path == "no-data-packets"):
                                                self.no_data_packets = value
                                                self.no_data_packets.value_namespace = name_space
                                                self.no_data_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "out-of-order"):
                                                self.out_of_order = value
                                                self.out_of_order.value_namespace = name_space
                                                self.out_of_order.value_namespace_prefix = name_space_prefix
                                            if(value_path == "result"):
                                                self.result = value
                                                self.result.value_namespace = name_space
                                                self.result.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sent"):
                                                self.sent = value
                                                self.sent.value_namespace = name_space
                                                self.sent.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sent-at"):
                                                self.sent_at = value
                                                self.sent_at.value_namespace = name_space
                                                self.sent_at.value_namespace_prefix = name_space_prefix
                                            if(value_path == "timed-out"):
                                                self.timed_out = value
                                                self.timed_out.value_namespace = name_space
                                                self.timed_out.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.sample:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.sample:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unaggregated" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/contents/%s" % self.get_segment_path()
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "sample"):
                                            for c in self.sample:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.sample.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "sample"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.bucket_type.is_set or
                                        (self.aggregated is not None and self.aggregated.has_data()) or
                                        (self.unaggregated is not None and self.unaggregated.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bucket_type.yfilter != YFilter.not_set or
                                        (self.aggregated is not None and self.aggregated.has_operation()) or
                                        (self.unaggregated is not None and self.unaggregated.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "contents" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/%s" % self.get_segment_path()
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bucket_type.is_set or self.bucket_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "aggregated"):
                                        if (self.aggregated is None):
                                            self.aggregated = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated()
                                            self.aggregated.parent = self
                                            self._children_name_map["aggregated"] = "aggregated"
                                        return self.aggregated

                                    if (child_yang_name == "unaggregated"):
                                        if (self.unaggregated is None):
                                            self.unaggregated = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated()
                                            self.unaggregated.parent = self
                                            self._children_name_map["unaggregated"] = "unaggregated"
                                        return self.unaggregated

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "aggregated" or name == "unaggregated" or name == "bucket-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bucket-type"):
                                        self.bucket_type = value
                                        self.bucket_type.value_namespace = name_space
                                        self.bucket_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.average.is_set or
                                    self.corrupt.is_set or
                                    self.data_lost_count.is_set or
                                    self.data_sent_count.is_set or
                                    self.duplicates.is_set or
                                    self.duration.is_set or
                                    self.lost.is_set or
                                    self.maximum.is_set or
                                    self.minimum.is_set or
                                    self.out_of_order.is_set or
                                    self.overall_flr.is_set or
                                    self.premature_reason.is_set or
                                    self.premature_reason_string.is_set or
                                    self.result_count.is_set or
                                    self.sent.is_set or
                                    self.standard_deviation.is_set or
                                    self.start_at.is_set or
                                    self.suspect_cleared_mid_bucket.is_set or
                                    self.suspect_clock_drift.is_set or
                                    self.suspect_flr_low_packet_count.is_set or
                                    self.suspect_management_latency.is_set or
                                    self.suspect_memory_allocation_failed.is_set or
                                    self.suspect_misordering.is_set or
                                    self.suspect_multiple_buckets.is_set or
                                    self.suspect_premature_end.is_set or
                                    self.suspect_probe_restarted.is_set or
                                    self.suspect_schedule_latency.is_set or
                                    self.suspect_send_fail.is_set or
                                    self.suspect_start_mid_bucket.is_set or
                                    self.time_of_maximum.is_set or
                                    self.time_of_minimum.is_set or
                                    (self.contents is not None and self.contents.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.average.yfilter != YFilter.not_set or
                                    self.corrupt.yfilter != YFilter.not_set or
                                    self.data_lost_count.yfilter != YFilter.not_set or
                                    self.data_sent_count.yfilter != YFilter.not_set or
                                    self.duplicates.yfilter != YFilter.not_set or
                                    self.duration.yfilter != YFilter.not_set or
                                    self.lost.yfilter != YFilter.not_set or
                                    self.maximum.yfilter != YFilter.not_set or
                                    self.minimum.yfilter != YFilter.not_set or
                                    self.out_of_order.yfilter != YFilter.not_set or
                                    self.overall_flr.yfilter != YFilter.not_set or
                                    self.premature_reason.yfilter != YFilter.not_set or
                                    self.premature_reason_string.yfilter != YFilter.not_set or
                                    self.result_count.yfilter != YFilter.not_set or
                                    self.sent.yfilter != YFilter.not_set or
                                    self.standard_deviation.yfilter != YFilter.not_set or
                                    self.start_at.yfilter != YFilter.not_set or
                                    self.suspect_cleared_mid_bucket.yfilter != YFilter.not_set or
                                    self.suspect_clock_drift.yfilter != YFilter.not_set or
                                    self.suspect_flr_low_packet_count.yfilter != YFilter.not_set or
                                    self.suspect_management_latency.yfilter != YFilter.not_set or
                                    self.suspect_memory_allocation_failed.yfilter != YFilter.not_set or
                                    self.suspect_misordering.yfilter != YFilter.not_set or
                                    self.suspect_multiple_buckets.yfilter != YFilter.not_set or
                                    self.suspect_premature_end.yfilter != YFilter.not_set or
                                    self.suspect_probe_restarted.yfilter != YFilter.not_set or
                                    self.suspect_schedule_latency.yfilter != YFilter.not_set or
                                    self.suspect_send_fail.yfilter != YFilter.not_set or
                                    self.suspect_start_mid_bucket.yfilter != YFilter.not_set or
                                    self.time_of_maximum.yfilter != YFilter.not_set or
                                    self.time_of_minimum.yfilter != YFilter.not_set or
                                    (self.contents is not None and self.contents.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bucket" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.average.is_set or self.average.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.average.get_name_leafdata())
                                if (self.corrupt.is_set or self.corrupt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.corrupt.get_name_leafdata())
                                if (self.data_lost_count.is_set or self.data_lost_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_lost_count.get_name_leafdata())
                                if (self.data_sent_count.is_set or self.data_sent_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_sent_count.get_name_leafdata())
                                if (self.duplicates.is_set or self.duplicates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duplicates.get_name_leafdata())
                                if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duration.get_name_leafdata())
                                if (self.lost.is_set or self.lost.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lost.get_name_leafdata())
                                if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.maximum.get_name_leafdata())
                                if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.minimum.get_name_leafdata())
                                if (self.out_of_order.is_set or self.out_of_order.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_of_order.get_name_leafdata())
                                if (self.overall_flr.is_set or self.overall_flr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.overall_flr.get_name_leafdata())
                                if (self.premature_reason.is_set or self.premature_reason.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.premature_reason.get_name_leafdata())
                                if (self.premature_reason_string.is_set or self.premature_reason_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.premature_reason_string.get_name_leafdata())
                                if (self.result_count.is_set or self.result_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.result_count.get_name_leafdata())
                                if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sent.get_name_leafdata())
                                if (self.standard_deviation.is_set or self.standard_deviation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.standard_deviation.get_name_leafdata())
                                if (self.start_at.is_set or self.start_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_at.get_name_leafdata())
                                if (self.suspect_cleared_mid_bucket.is_set or self.suspect_cleared_mid_bucket.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_cleared_mid_bucket.get_name_leafdata())
                                if (self.suspect_clock_drift.is_set or self.suspect_clock_drift.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_clock_drift.get_name_leafdata())
                                if (self.suspect_flr_low_packet_count.is_set or self.suspect_flr_low_packet_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_flr_low_packet_count.get_name_leafdata())
                                if (self.suspect_management_latency.is_set or self.suspect_management_latency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_management_latency.get_name_leafdata())
                                if (self.suspect_memory_allocation_failed.is_set or self.suspect_memory_allocation_failed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_memory_allocation_failed.get_name_leafdata())
                                if (self.suspect_misordering.is_set or self.suspect_misordering.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_misordering.get_name_leafdata())
                                if (self.suspect_multiple_buckets.is_set or self.suspect_multiple_buckets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_multiple_buckets.get_name_leafdata())
                                if (self.suspect_premature_end.is_set or self.suspect_premature_end.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_premature_end.get_name_leafdata())
                                if (self.suspect_probe_restarted.is_set or self.suspect_probe_restarted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_probe_restarted.get_name_leafdata())
                                if (self.suspect_schedule_latency.is_set or self.suspect_schedule_latency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_schedule_latency.get_name_leafdata())
                                if (self.suspect_send_fail.is_set or self.suspect_send_fail.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_send_fail.get_name_leafdata())
                                if (self.suspect_start_mid_bucket.is_set or self.suspect_start_mid_bucket.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_start_mid_bucket.get_name_leafdata())
                                if (self.time_of_maximum.is_set or self.time_of_maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_of_maximum.get_name_leafdata())
                                if (self.time_of_minimum.is_set or self.time_of_minimum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_of_minimum.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "contents"):
                                    if (self.contents is None):
                                        self.contents = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents()
                                        self.contents.parent = self
                                        self._children_name_map["contents"] = "contents"
                                    return self.contents

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "contents" or name == "average" or name == "corrupt" or name == "data-lost-count" or name == "data-sent-count" or name == "duplicates" or name == "duration" or name == "lost" or name == "maximum" or name == "minimum" or name == "out-of-order" or name == "overall-flr" or name == "premature-reason" or name == "premature-reason-string" or name == "result-count" or name == "sent" or name == "standard-deviation" or name == "start-at" or name == "suspect-cleared-mid-bucket" or name == "suspect-clock-drift" or name == "suspect-flr-low-packet-count" or name == "suspect-management-latency" or name == "suspect-memory-allocation-failed" or name == "suspect-misordering" or name == "suspect-multiple-buckets" or name == "suspect-premature-end" or name == "suspect-probe-restarted" or name == "suspect-schedule-latency" or name == "suspect-send-fail" or name == "suspect-start-mid-bucket" or name == "time-of-maximum" or name == "time-of-minimum"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "average"):
                                    self.average = value
                                    self.average.value_namespace = name_space
                                    self.average.value_namespace_prefix = name_space_prefix
                                if(value_path == "corrupt"):
                                    self.corrupt = value
                                    self.corrupt.value_namespace = name_space
                                    self.corrupt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-lost-count"):
                                    self.data_lost_count = value
                                    self.data_lost_count.value_namespace = name_space
                                    self.data_lost_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-sent-count"):
                                    self.data_sent_count = value
                                    self.data_sent_count.value_namespace = name_space
                                    self.data_sent_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "duplicates"):
                                    self.duplicates = value
                                    self.duplicates.value_namespace = name_space
                                    self.duplicates.value_namespace_prefix = name_space_prefix
                                if(value_path == "duration"):
                                    self.duration = value
                                    self.duration.value_namespace = name_space
                                    self.duration.value_namespace_prefix = name_space_prefix
                                if(value_path == "lost"):
                                    self.lost = value
                                    self.lost.value_namespace = name_space
                                    self.lost.value_namespace_prefix = name_space_prefix
                                if(value_path == "maximum"):
                                    self.maximum = value
                                    self.maximum.value_namespace = name_space
                                    self.maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "minimum"):
                                    self.minimum = value
                                    self.minimum.value_namespace = name_space
                                    self.minimum.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-of-order"):
                                    self.out_of_order = value
                                    self.out_of_order.value_namespace = name_space
                                    self.out_of_order.value_namespace_prefix = name_space_prefix
                                if(value_path == "overall-flr"):
                                    self.overall_flr = value
                                    self.overall_flr.value_namespace = name_space
                                    self.overall_flr.value_namespace_prefix = name_space_prefix
                                if(value_path == "premature-reason"):
                                    self.premature_reason = value
                                    self.premature_reason.value_namespace = name_space
                                    self.premature_reason.value_namespace_prefix = name_space_prefix
                                if(value_path == "premature-reason-string"):
                                    self.premature_reason_string = value
                                    self.premature_reason_string.value_namespace = name_space
                                    self.premature_reason_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "result-count"):
                                    self.result_count = value
                                    self.result_count.value_namespace = name_space
                                    self.result_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "sent"):
                                    self.sent = value
                                    self.sent.value_namespace = name_space
                                    self.sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "standard-deviation"):
                                    self.standard_deviation = value
                                    self.standard_deviation.value_namespace = name_space
                                    self.standard_deviation.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-at"):
                                    self.start_at = value
                                    self.start_at.value_namespace = name_space
                                    self.start_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-cleared-mid-bucket"):
                                    self.suspect_cleared_mid_bucket = value
                                    self.suspect_cleared_mid_bucket.value_namespace = name_space
                                    self.suspect_cleared_mid_bucket.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-clock-drift"):
                                    self.suspect_clock_drift = value
                                    self.suspect_clock_drift.value_namespace = name_space
                                    self.suspect_clock_drift.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-flr-low-packet-count"):
                                    self.suspect_flr_low_packet_count = value
                                    self.suspect_flr_low_packet_count.value_namespace = name_space
                                    self.suspect_flr_low_packet_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-management-latency"):
                                    self.suspect_management_latency = value
                                    self.suspect_management_latency.value_namespace = name_space
                                    self.suspect_management_latency.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-memory-allocation-failed"):
                                    self.suspect_memory_allocation_failed = value
                                    self.suspect_memory_allocation_failed.value_namespace = name_space
                                    self.suspect_memory_allocation_failed.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-misordering"):
                                    self.suspect_misordering = value
                                    self.suspect_misordering.value_namespace = name_space
                                    self.suspect_misordering.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-multiple-buckets"):
                                    self.suspect_multiple_buckets = value
                                    self.suspect_multiple_buckets.value_namespace = name_space
                                    self.suspect_multiple_buckets.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-premature-end"):
                                    self.suspect_premature_end = value
                                    self.suspect_premature_end.value_namespace = name_space
                                    self.suspect_premature_end.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-probe-restarted"):
                                    self.suspect_probe_restarted = value
                                    self.suspect_probe_restarted.value_namespace = name_space
                                    self.suspect_probe_restarted.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-schedule-latency"):
                                    self.suspect_schedule_latency = value
                                    self.suspect_schedule_latency.value_namespace = name_space
                                    self.suspect_schedule_latency.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-send-fail"):
                                    self.suspect_send_fail = value
                                    self.suspect_send_fail.value_namespace = name_space
                                    self.suspect_send_fail.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-start-mid-bucket"):
                                    self.suspect_start_mid_bucket = value
                                    self.suspect_start_mid_bucket.value_namespace = name_space
                                    self.suspect_start_mid_bucket.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-of-maximum"):
                                    self.time_of_maximum = value
                                    self.time_of_maximum.value_namespace = name_space
                                    self.time_of_maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-of-minimum"):
                                    self.time_of_minimum = value
                                    self.time_of_minimum.value_namespace = name_space
                                    self.time_of_minimum.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.bucket:
                                if (c.has_data()):
                                    return True
                            return (self.config is not None and self.config.has_data())

                        def has_operation(self):
                            for c in self.bucket:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operation-metric" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "bucket"):
                                for c in self.bucket:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.bucket.append(c)
                                return c

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bucket" or name == "config"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        for c in self.operation_metric:
                            if (c.has_data()):
                                return True
                        return (
                            self.display_long.is_set or
                            self.display_short.is_set or
                            self.domain_name.is_set or
                            self.flr_calculation_interval.is_set or
                            self.interface_name.is_set or
                            self.mac_address.is_set or
                            self.mep_id.is_set or
                            self.operation_id.is_set or
                            self.probe_type.is_set or
                            (self.operation_schedule is not None and self.operation_schedule.has_data()) or
                            (self.specific_options is not None and self.specific_options.has_data()))

                    def has_operation(self):
                        for c in self.operation_metric:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.display_long.yfilter != YFilter.not_set or
                            self.display_short.yfilter != YFilter.not_set or
                            self.domain_name.yfilter != YFilter.not_set or
                            self.flr_calculation_interval.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.mep_id.yfilter != YFilter.not_set or
                            self.operation_id.yfilter != YFilter.not_set or
                            self.probe_type.yfilter != YFilter.not_set or
                            (self.operation_schedule is not None and self.operation_schedule.has_operation()) or
                            (self.specific_options is not None and self.specific_options.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics-on-demand-current" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.display_long.is_set or self.display_long.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_long.get_name_leafdata())
                        if (self.display_short.is_set or self.display_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_short.get_name_leafdata())
                        if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_name.get_name_leafdata())
                        if (self.flr_calculation_interval.is_set or self.flr_calculation_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flr_calculation_interval.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.mep_id.is_set or self.mep_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mep_id.get_name_leafdata())
                        if (self.operation_id.is_set or self.operation_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.operation_id.get_name_leafdata())
                        if (self.probe_type.is_set or self.probe_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.probe_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "operation-metric"):
                            for c in self.operation_metric:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.operation_metric.append(c)
                            return c

                        if (child_yang_name == "operation-schedule"):
                            if (self.operation_schedule is None):
                                self.operation_schedule = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule()
                                self.operation_schedule.parent = self
                                self._children_name_map["operation_schedule"] = "operation-schedule"
                            return self.operation_schedule

                        if (child_yang_name == "specific-options"):
                            if (self.specific_options is None):
                                self.specific_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions()
                                self.specific_options.parent = self
                                self._children_name_map["specific_options"] = "specific-options"
                            return self.specific_options

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "operation-metric" or name == "operation-schedule" or name == "specific-options" or name == "display-long" or name == "display-short" or name == "domain-name" or name == "flr-calculation-interval" or name == "interface-name" or name == "mac-address" or name == "mep-id" or name == "operation-id" or name == "probe-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "display-long"):
                            self.display_long = value
                            self.display_long.value_namespace = name_space
                            self.display_long.value_namespace_prefix = name_space_prefix
                        if(value_path == "display-short"):
                            self.display_short = value
                            self.display_short.value_namespace = name_space
                            self.display_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-name"):
                            self.domain_name = value
                            self.domain_name.value_namespace = name_space
                            self.domain_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "flr-calculation-interval"):
                            self.flr_calculation_interval = value
                            self.flr_calculation_interval.value_namespace = name_space
                            self.flr_calculation_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mep-id"):
                            self.mep_id = value
                            self.mep_id.value_namespace = name_space
                            self.mep_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "operation-id"):
                            self.operation_id = value
                            self.operation_id.value_namespace = name_space
                            self.operation_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "probe-type"):
                            self.probe_type = value
                            self.probe_type.value_namespace = name_space
                            self.probe_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.statistics_on_demand_current:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.statistics_on_demand_current:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics-on-demand-currents" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "statistics-on-demand-current"):
                        for c in self.statistics_on_demand_current:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.statistics_on_demand_current.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statistics-on-demand-current"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Operations(Entity):
                """
                Table of SLA operations
                
                .. attribute:: operation_
                
                	SLA operation to get operation data for
                	**type**\: list of    :py:class:`Operation_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.Operations, self).__init__()

                    self.yang_name = "operations"
                    self.yang_parent_name = "ethernet"

                    self.operation_ = YList(self)

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
                                super(Sla.Protocols.Ethernet.Operations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sla.Protocols.Ethernet.Operations, self).__setattr__(name, value)


                class Operation_(Entity):
                    """
                    SLA operation to get operation data for
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: last_run
                    
                    	Time that the last probe for the operation was run, NULL if never run
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\:  int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: profile_name
                    
                    	Profile Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: profile_options
                    
                    	Options that are only valid if the operation has a profile
                    	**type**\:   :py:class:`ProfileOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions>`
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:   :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.Operations.Operation_, self).__init__()

                        self.yang_name = "operation"
                        self.yang_parent_name = "operations"

                        self.display_long = YLeaf(YType.str, "display-long")

                        self.display_short = YLeaf(YType.str, "display-short")

                        self.domain_name = YLeaf(YType.str, "domain-name")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.last_run = YLeaf(YType.uint32, "last-run")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.mep_id = YLeaf(YType.uint32, "mep-id")

                        self.profile_name = YLeaf(YType.str, "profile-name")

                        self.profile_options = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions()
                        self.profile_options.parent = self
                        self._children_name_map["profile_options"] = "profile-options"
                        self._children_yang_names.add("profile-options")

                        self.specific_options = Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"
                        self._children_yang_names.add("specific-options")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("display_long",
                                        "display_short",
                                        "domain_name",
                                        "interface_name",
                                        "last_run",
                                        "mac_address",
                                        "mep_id",
                                        "profile_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sla.Protocols.Ethernet.Operations.Operation_, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sla.Protocols.Ethernet.Operations.Operation_, self).__setattr__(name, value)


                    class ProfileOptions(Entity):
                        """
                        Options that are only valid if the operation has
                        a profile
                        
                        .. attribute:: bursts_per_probe
                        
                        	Number of bursts sent per probe
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flr_calculation_interval
                        
                        	Interval between FLR calculations for SLM, in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: inter_burst_interval
                        
                        	Interval between bursts within a probe in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: inter_packet_interval
                        
                        	Interval between packets within a burst in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**units**\: millisecond
                        
                        .. attribute:: operation_metric
                        
                        	Array of the metrics that are measured by the operation
                        	**type**\: list of    :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric>`
                        
                        .. attribute:: operation_schedule
                        
                        	Operation schedule
                        	**type**\:   :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationSchedule>`
                        
                        .. attribute:: packet_padding
                        
                        	Configuration of the packet padding
                        	**type**\:   :py:class:`PacketPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.PacketPadding>`
                        
                        .. attribute:: packets_per_burst
                        
                        	Number of packets sent per burst
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: priority
                        
                        	Priority at which to send the packet, if configured
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.Priority>`
                        
                        .. attribute:: probe_type
                        
                        	Type of probe used by the operation
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions, self).__init__()

                            self.yang_name = "profile-options"
                            self.yang_parent_name = "operation"

                            self.bursts_per_probe = YLeaf(YType.uint32, "bursts-per-probe")

                            self.flr_calculation_interval = YLeaf(YType.uint32, "flr-calculation-interval")

                            self.inter_burst_interval = YLeaf(YType.uint32, "inter-burst-interval")

                            self.inter_packet_interval = YLeaf(YType.uint16, "inter-packet-interval")

                            self.packets_per_burst = YLeaf(YType.uint16, "packets-per-burst")

                            self.probe_type = YLeaf(YType.str, "probe-type")

                            self.operation_schedule = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationSchedule()
                            self.operation_schedule.parent = self
                            self._children_name_map["operation_schedule"] = "operation-schedule"
                            self._children_yang_names.add("operation-schedule")

                            self.packet_padding = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.PacketPadding()
                            self.packet_padding.parent = self
                            self._children_name_map["packet_padding"] = "packet-padding"
                            self._children_yang_names.add("packet-padding")

                            self.priority = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.Priority()
                            self.priority.parent = self
                            self._children_name_map["priority"] = "priority"
                            self._children_yang_names.add("priority")

                            self.operation_metric = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bursts_per_probe",
                                            "flr_calculation_interval",
                                            "inter_burst_interval",
                                            "inter_packet_interval",
                                            "packets_per_burst",
                                            "probe_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions, self).__setattr__(name, value)


                        class PacketPadding(Entity):
                            """
                            Configuration of the packet padding
                            
                            .. attribute:: packet_pad_size
                            
                            	Size that packets are being padded to
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: test_pattern_pad_hex_string
                            
                            	Hex string that is used in the packet padding
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: test_pattern_pad_scheme
                            
                            	Test pattern scheme that is used in the packet padding
                            	**type**\:   :py:class:`SlaOperTestPatternScheme <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperTestPatternScheme>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.PacketPadding, self).__init__()

                                self.yang_name = "packet-padding"
                                self.yang_parent_name = "profile-options"

                                self.packet_pad_size = YLeaf(YType.uint16, "packet-pad-size")

                                self.test_pattern_pad_hex_string = YLeaf(YType.uint32, "test-pattern-pad-hex-string")

                                self.test_pattern_pad_scheme = YLeaf(YType.enumeration, "test-pattern-pad-scheme")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("packet_pad_size",
                                                "test_pattern_pad_hex_string",
                                                "test_pattern_pad_scheme") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.PacketPadding, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.PacketPadding, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.packet_pad_size.is_set or
                                    self.test_pattern_pad_hex_string.is_set or
                                    self.test_pattern_pad_scheme.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.packet_pad_size.yfilter != YFilter.not_set or
                                    self.test_pattern_pad_hex_string.yfilter != YFilter.not_set or
                                    self.test_pattern_pad_scheme.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-padding" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.packet_pad_size.is_set or self.packet_pad_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packet_pad_size.get_name_leafdata())
                                if (self.test_pattern_pad_hex_string.is_set or self.test_pattern_pad_hex_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.test_pattern_pad_hex_string.get_name_leafdata())
                                if (self.test_pattern_pad_scheme.is_set or self.test_pattern_pad_scheme.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.test_pattern_pad_scheme.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "packet-pad-size" or name == "test-pattern-pad-hex-string" or name == "test-pattern-pad-scheme"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "packet-pad-size"):
                                    self.packet_pad_size = value
                                    self.packet_pad_size.value_namespace = name_space
                                    self.packet_pad_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "test-pattern-pad-hex-string"):
                                    self.test_pattern_pad_hex_string = value
                                    self.test_pattern_pad_hex_string.value_namespace = name_space
                                    self.test_pattern_pad_hex_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "test-pattern-pad-scheme"):
                                    self.test_pattern_pad_scheme = value
                                    self.test_pattern_pad_scheme.value_namespace = name_space
                                    self.test_pattern_pad_scheme.value_namespace_prefix = name_space_prefix


                        class Priority(Entity):
                            """
                            Priority at which to send the packet, if
                            configured
                            
                            .. attribute:: cos
                            
                            	3\-bit COS priority value applied to packets
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: priority_type
                            
                            	PriorityType
                            	**type**\:   :py:class:`SlaOperPacketPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperPacketPriority>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "profile-options"

                                self.cos = YLeaf(YType.uint8, "cos")

                                self.priority_type = YLeaf(YType.enumeration, "priority-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("cos",
                                                "priority_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.Priority, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.Priority, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.cos.is_set or
                                    self.priority_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.cos.yfilter != YFilter.not_set or
                                    self.priority_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "priority" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cos.get_name_leafdata())
                                if (self.priority_type.is_set or self.priority_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "cos" or name == "priority-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "cos"):
                                    self.cos = value
                                    self.cos.value_namespace = name_space
                                    self.cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority-type"):
                                    self.priority_type = value
                                    self.priority_type.value_namespace = name_space
                                    self.priority_type.value_namespace_prefix = name_space_prefix


                        class OperationSchedule(Entity):
                            """
                            Operation schedule
                            
                            .. attribute:: schedule_duration
                            
                            	Duration of a probe for the operation in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: schedule_interval
                            
                            	Interval between the start times of consecutive probes,  in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: start_time
                            
                            	Start time of the first probe, in seconds since the Unix Epoch
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: start_time_configured
                            
                            	Whether or not the operation start time was explicitly configured
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationSchedule, self).__init__()

                                self.yang_name = "operation-schedule"
                                self.yang_parent_name = "profile-options"

                                self.schedule_duration = YLeaf(YType.uint32, "schedule-duration")

                                self.schedule_interval = YLeaf(YType.uint32, "schedule-interval")

                                self.start_time = YLeaf(YType.uint32, "start-time")

                                self.start_time_configured = YLeaf(YType.boolean, "start-time-configured")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("schedule_duration",
                                                "schedule_interval",
                                                "start_time",
                                                "start_time_configured") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationSchedule, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationSchedule, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.schedule_duration.is_set or
                                    self.schedule_interval.is_set or
                                    self.start_time.is_set or
                                    self.start_time_configured.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.schedule_duration.yfilter != YFilter.not_set or
                                    self.schedule_interval.yfilter != YFilter.not_set or
                                    self.start_time.yfilter != YFilter.not_set or
                                    self.start_time_configured.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operation-schedule" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.schedule_duration.is_set or self.schedule_duration.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.schedule_duration.get_name_leafdata())
                                if (self.schedule_interval.is_set or self.schedule_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.schedule_interval.get_name_leafdata())
                                if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_time.get_name_leafdata())
                                if (self.start_time_configured.is_set or self.start_time_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_time_configured.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "schedule-duration" or name == "schedule-interval" or name == "start-time" or name == "start-time-configured"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "schedule-duration"):
                                    self.schedule_duration = value
                                    self.schedule_duration.value_namespace = name_space
                                    self.schedule_duration.value_namespace_prefix = name_space_prefix
                                if(value_path == "schedule-interval"):
                                    self.schedule_interval = value
                                    self.schedule_interval.value_namespace = name_space
                                    self.schedule_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-time"):
                                    self.start_time = value
                                    self.start_time.value_namespace = name_space
                                    self.start_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-time-configured"):
                                    self.start_time_configured = value
                                    self.start_time_configured.value_namespace = name_space
                                    self.start_time_configured.value_namespace_prefix = name_space_prefix


                        class OperationMetric(Entity):
                            """
                            Array of the metrics that are measured by the
                            operation
                            
                            .. attribute:: current_buckets_archive
                            
                            	Number of valid buckets currently in the buckets archive
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_config
                            
                            	Configuration of the metric
                            	**type**\:   :py:class:`MetricConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric.MetricConfig>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric, self).__init__()

                                self.yang_name = "operation-metric"
                                self.yang_parent_name = "profile-options"

                                self.current_buckets_archive = YLeaf(YType.uint32, "current-buckets-archive")

                                self.metric_config = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric.MetricConfig()
                                self.metric_config.parent = self
                                self._children_name_map["metric_config"] = "metric-config"
                                self._children_yang_names.add("metric-config")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("current_buckets_archive") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric, self).__setattr__(name, value)


                            class MetricConfig(Entity):
                                """
                                Configuration of the metric
                                
                                .. attribute:: bins_count
                                
                                	Total number of bins into which to aggregate. 0 if no aggregation
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: bins_width
                                
                                	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: bucket_size
                                
                                	Size of buckets into which measurements are collected
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: bucket_size_unit
                                
                                	Whether bucket size is 'per\-probe' or 'probes'
                                	**type**\:   :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                                
                                .. attribute:: buckets_archive
                                
                                	Maximum number of buckets to store in memory
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric_type
                                
                                	Type of metric to which this configuration applies
                                	**type**\:   :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric.MetricConfig, self).__init__()

                                    self.yang_name = "metric-config"
                                    self.yang_parent_name = "operation-metric"

                                    self.bins_count = YLeaf(YType.uint16, "bins-count")

                                    self.bins_width = YLeaf(YType.uint16, "bins-width")

                                    self.bucket_size = YLeaf(YType.uint8, "bucket-size")

                                    self.bucket_size_unit = YLeaf(YType.enumeration, "bucket-size-unit")

                                    self.buckets_archive = YLeaf(YType.uint32, "buckets-archive")

                                    self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bins_count",
                                                    "bins_width",
                                                    "bucket_size",
                                                    "bucket_size_unit",
                                                    "buckets_archive",
                                                    "metric_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric.MetricConfig, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric.MetricConfig, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.bins_count.is_set or
                                        self.bins_width.is_set or
                                        self.bucket_size.is_set or
                                        self.bucket_size_unit.is_set or
                                        self.buckets_archive.is_set or
                                        self.metric_type.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bins_count.yfilter != YFilter.not_set or
                                        self.bins_width.yfilter != YFilter.not_set or
                                        self.bucket_size.yfilter != YFilter.not_set or
                                        self.bucket_size_unit.yfilter != YFilter.not_set or
                                        self.buckets_archive.yfilter != YFilter.not_set or
                                        self.metric_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "metric-config" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/operation-metric/%s" % self.get_segment_path()
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bins_count.is_set or self.bins_count.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bins_count.get_name_leafdata())
                                    if (self.bins_width.is_set or self.bins_width.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bins_width.get_name_leafdata())
                                    if (self.bucket_size.is_set or self.bucket_size.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_size.get_name_leafdata())
                                    if (self.bucket_size_unit.is_set or self.bucket_size_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_size_unit.get_name_leafdata())
                                    if (self.buckets_archive.is_set or self.buckets_archive.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.buckets_archive.get_name_leafdata())
                                    if (self.metric_type.is_set or self.metric_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.metric_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "bins-count" or name == "bins-width" or name == "bucket-size" or name == "bucket-size-unit" or name == "buckets-archive" or name == "metric-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bins-count"):
                                        self.bins_count = value
                                        self.bins_count.value_namespace = name_space
                                        self.bins_count.value_namespace_prefix = name_space_prefix
                                    if(value_path == "bins-width"):
                                        self.bins_width = value
                                        self.bins_width.value_namespace = name_space
                                        self.bins_width.value_namespace_prefix = name_space_prefix
                                    if(value_path == "bucket-size"):
                                        self.bucket_size = value
                                        self.bucket_size.value_namespace = name_space
                                        self.bucket_size.value_namespace_prefix = name_space_prefix
                                    if(value_path == "bucket-size-unit"):
                                        self.bucket_size_unit = value
                                        self.bucket_size_unit.value_namespace = name_space
                                        self.bucket_size_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "buckets-archive"):
                                        self.buckets_archive = value
                                        self.buckets_archive.value_namespace = name_space
                                        self.buckets_archive.value_namespace_prefix = name_space_prefix
                                    if(value_path == "metric-type"):
                                        self.metric_type = value
                                        self.metric_type.value_namespace = name_space
                                        self.metric_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.current_buckets_archive.is_set or
                                    (self.metric_config is not None and self.metric_config.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.current_buckets_archive.yfilter != YFilter.not_set or
                                    (self.metric_config is not None and self.metric_config.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operation-metric" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.current_buckets_archive.is_set or self.current_buckets_archive.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.current_buckets_archive.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "metric-config"):
                                    if (self.metric_config is None):
                                        self.metric_config = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric.MetricConfig()
                                        self.metric_config.parent = self
                                        self._children_name_map["metric_config"] = "metric-config"
                                    return self.metric_config

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "metric-config" or name == "current-buckets-archive"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "current-buckets-archive"):
                                    self.current_buckets_archive = value
                                    self.current_buckets_archive.value_namespace = name_space
                                    self.current_buckets_archive.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.operation_metric:
                                if (c.has_data()):
                                    return True
                            return (
                                self.bursts_per_probe.is_set or
                                self.flr_calculation_interval.is_set or
                                self.inter_burst_interval.is_set or
                                self.inter_packet_interval.is_set or
                                self.packets_per_burst.is_set or
                                self.probe_type.is_set or
                                (self.operation_schedule is not None and self.operation_schedule.has_data()) or
                                (self.packet_padding is not None and self.packet_padding.has_data()) or
                                (self.priority is not None and self.priority.has_data()))

                        def has_operation(self):
                            for c in self.operation_metric:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bursts_per_probe.yfilter != YFilter.not_set or
                                self.flr_calculation_interval.yfilter != YFilter.not_set or
                                self.inter_burst_interval.yfilter != YFilter.not_set or
                                self.inter_packet_interval.yfilter != YFilter.not_set or
                                self.packets_per_burst.yfilter != YFilter.not_set or
                                self.probe_type.yfilter != YFilter.not_set or
                                (self.operation_schedule is not None and self.operation_schedule.has_operation()) or
                                (self.packet_padding is not None and self.packet_padding.has_operation()) or
                                (self.priority is not None and self.priority.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "profile-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bursts_per_probe.is_set or self.bursts_per_probe.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bursts_per_probe.get_name_leafdata())
                            if (self.flr_calculation_interval.is_set or self.flr_calculation_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flr_calculation_interval.get_name_leafdata())
                            if (self.inter_burst_interval.is_set or self.inter_burst_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.inter_burst_interval.get_name_leafdata())
                            if (self.inter_packet_interval.is_set or self.inter_packet_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.inter_packet_interval.get_name_leafdata())
                            if (self.packets_per_burst.is_set or self.packets_per_burst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_per_burst.get_name_leafdata())
                            if (self.probe_type.is_set or self.probe_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "operation-metric"):
                                for c in self.operation_metric:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationMetric()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.operation_metric.append(c)
                                return c

                            if (child_yang_name == "operation-schedule"):
                                if (self.operation_schedule is None):
                                    self.operation_schedule = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.OperationSchedule()
                                    self.operation_schedule.parent = self
                                    self._children_name_map["operation_schedule"] = "operation-schedule"
                                return self.operation_schedule

                            if (child_yang_name == "packet-padding"):
                                if (self.packet_padding is None):
                                    self.packet_padding = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.PacketPadding()
                                    self.packet_padding.parent = self
                                    self._children_name_map["packet_padding"] = "packet-padding"
                                return self.packet_padding

                            if (child_yang_name == "priority"):
                                if (self.priority is None):
                                    self.priority = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions.Priority()
                                    self.priority.parent = self
                                    self._children_name_map["priority"] = "priority"
                                return self.priority

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "operation-metric" or name == "operation-schedule" or name == "packet-padding" or name == "priority" or name == "bursts-per-probe" or name == "flr-calculation-interval" or name == "inter-burst-interval" or name == "inter-packet-interval" or name == "packets-per-burst" or name == "probe-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bursts-per-probe"):
                                self.bursts_per_probe = value
                                self.bursts_per_probe.value_namespace = name_space
                                self.bursts_per_probe.value_namespace_prefix = name_space_prefix
                            if(value_path == "flr-calculation-interval"):
                                self.flr_calculation_interval = value
                                self.flr_calculation_interval.value_namespace = name_space
                                self.flr_calculation_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "inter-burst-interval"):
                                self.inter_burst_interval = value
                                self.inter_burst_interval.value_namespace = name_space
                                self.inter_burst_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "inter-packet-interval"):
                                self.inter_packet_interval = value
                                self.inter_packet_interval.value_namespace = name_space
                                self.inter_packet_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-per-burst"):
                                self.packets_per_burst = value
                                self.packets_per_burst.value_namespace = name_space
                                self.packets_per_burst.value_namespace_prefix = name_space_prefix
                            if(value_path == "probe-type"):
                                self.probe_type = value
                                self.probe_type.value_namespace = name_space
                                self.probe_type.value_namespace_prefix = name_space_prefix


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:   :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:   :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:   :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "operation"

                            self.oper_type = YLeaf(YType.enumeration, "oper-type")

                            self.configured_operation_options = Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"
                            self._children_yang_names.add("configured-operation-options")

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._children_yang_names.add("ondemand-operation-options")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("oper_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions, self).__setattr__(name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.profile_name = YLeaf(YType.str, "profile-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "configured-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.ondemand_operation_id = YLeaf(YType.uint32, "ondemand-operation-id")

                                self.probe_count = YLeaf(YType.uint8, "probe-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ondemand_operation_id",
                                                "probe_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ondemand_operation_id.is_set or
                                    self.probe_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ondemand_operation_id.yfilter != YFilter.not_set or
                                    self.probe_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ondemand-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ondemand_operation_id.is_set or self.ondemand_operation_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ondemand_operation_id.get_name_leafdata())
                                if (self.probe_count.is_set or self.probe_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.probe_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ondemand-operation-id" or name == "probe-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ondemand-operation-id"):
                                    self.ondemand_operation_id = value
                                    self.ondemand_operation_id.value_namespace = name_space
                                    self.ondemand_operation_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "probe-count"):
                                    self.probe_count = value
                                    self.probe_count.value_namespace = name_space
                                    self.probe_count.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.oper_type.is_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_data()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.oper_type.yfilter != YFilter.not_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_operation()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "specific-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.oper_type.is_set or self.oper_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oper_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "configured-operation-options"):
                                if (self.configured_operation_options is None):
                                    self.configured_operation_options = Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.ConfiguredOperationOptions()
                                    self.configured_operation_options.parent = self
                                    self._children_name_map["configured_operation_options"] = "configured-operation-options"
                                return self.configured_operation_options

                            if (child_yang_name == "ondemand-operation-options"):
                                if (self.ondemand_operation_options is None):
                                    self.ondemand_operation_options = Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions.OndemandOperationOptions()
                                    self.ondemand_operation_options.parent = self
                                    self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                                return self.ondemand_operation_options

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "configured-operation-options" or name == "ondemand-operation-options" or name == "oper-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "oper-type"):
                                self.oper_type = value
                                self.oper_type.value_namespace = name_space
                                self.oper_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.display_long.is_set or
                            self.display_short.is_set or
                            self.domain_name.is_set or
                            self.interface_name.is_set or
                            self.last_run.is_set or
                            self.mac_address.is_set or
                            self.mep_id.is_set or
                            self.profile_name.is_set or
                            (self.profile_options is not None and self.profile_options.has_data()) or
                            (self.specific_options is not None and self.specific_options.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.display_long.yfilter != YFilter.not_set or
                            self.display_short.yfilter != YFilter.not_set or
                            self.domain_name.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.last_run.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.mep_id.yfilter != YFilter.not_set or
                            self.profile_name.yfilter != YFilter.not_set or
                            (self.profile_options is not None and self.profile_options.has_operation()) or
                            (self.specific_options is not None and self.specific_options.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "operation" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.display_long.is_set or self.display_long.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_long.get_name_leafdata())
                        if (self.display_short.is_set or self.display_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_short.get_name_leafdata())
                        if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_name.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.last_run.is_set or self.last_run.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_run.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.mep_id.is_set or self.mep_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mep_id.get_name_leafdata())
                        if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.profile_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "profile-options"):
                            if (self.profile_options is None):
                                self.profile_options = Sla.Protocols.Ethernet.Operations.Operation_.ProfileOptions()
                                self.profile_options.parent = self
                                self._children_name_map["profile_options"] = "profile-options"
                            return self.profile_options

                        if (child_yang_name == "specific-options"):
                            if (self.specific_options is None):
                                self.specific_options = Sla.Protocols.Ethernet.Operations.Operation_.SpecificOptions()
                                self.specific_options.parent = self
                                self._children_name_map["specific_options"] = "specific-options"
                            return self.specific_options

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "profile-options" or name == "specific-options" or name == "display-long" or name == "display-short" or name == "domain-name" or name == "interface-name" or name == "last-run" or name == "mac-address" or name == "mep-id" or name == "profile-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "display-long"):
                            self.display_long = value
                            self.display_long.value_namespace = name_space
                            self.display_long.value_namespace_prefix = name_space_prefix
                        if(value_path == "display-short"):
                            self.display_short = value
                            self.display_short.value_namespace = name_space
                            self.display_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-name"):
                            self.domain_name = value
                            self.domain_name.value_namespace = name_space
                            self.domain_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-run"):
                            self.last_run = value
                            self.last_run.value_namespace = name_space
                            self.last_run.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mep-id"):
                            self.mep_id = value
                            self.mep_id.value_namespace = name_space
                            self.mep_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "profile-name"):
                            self.profile_name = value
                            self.profile_name.value_namespace = name_space
                            self.profile_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.operation_:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.operation_:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "operations" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "operation"):
                        for c in self.operation_:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sla.Protocols.Ethernet.Operations.Operation_()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.operation_.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "operation"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class StatisticsHistoricals(Entity):
                """
                Table of historical statistics for SLA
                operations
                
                .. attribute:: statistics_historical
                
                	Historical statistics data for an SLA configured operation
                	**type**\: list of    :py:class:`StatisticsHistorical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.StatisticsHistoricals, self).__init__()

                    self.yang_name = "statistics-historicals"
                    self.yang_parent_name = "ethernet"

                    self.statistics_historical = YList(self)

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
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sla.Protocols.Ethernet.StatisticsHistoricals, self).__setattr__(name, value)


                class StatisticsHistorical(Entity):
                    """
                    Historical statistics data for an SLA
                    configured operation
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: flr_calculation_interval
                    
                    	Interval between FLR calculations for SLM, in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\:  int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: operation_metric
                    
                    	Metrics gathered for the operation
                    	**type**\: list of    :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric>`
                    
                    .. attribute:: operation_schedule
                    
                    	Operation schedule
                    	**type**\:   :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule>`
                    
                    .. attribute:: probe_type
                    
                    	Type of probe used by the operation
                    	**type**\:  str
                    
                    .. attribute:: profile_name
                    
                    	Profile Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:   :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical, self).__init__()

                        self.yang_name = "statistics-historical"
                        self.yang_parent_name = "statistics-historicals"

                        self.display_long = YLeaf(YType.str, "display-long")

                        self.display_short = YLeaf(YType.str, "display-short")

                        self.domain_name = YLeaf(YType.str, "domain-name")

                        self.flr_calculation_interval = YLeaf(YType.uint32, "flr-calculation-interval")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.mep_id = YLeaf(YType.uint32, "mep-id")

                        self.probe_type = YLeaf(YType.str, "probe-type")

                        self.profile_name = YLeaf(YType.str, "profile-name")

                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule()
                        self.operation_schedule.parent = self
                        self._children_name_map["operation_schedule"] = "operation-schedule"
                        self._children_yang_names.add("operation-schedule")

                        self.specific_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"
                        self._children_yang_names.add("specific-options")

                        self.operation_metric = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("display_long",
                                        "display_short",
                                        "domain_name",
                                        "flr_calculation_interval",
                                        "interface_name",
                                        "mac_address",
                                        "mep_id",
                                        "probe_type",
                                        "profile_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical, self).__setattr__(name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:   :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:   :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:   :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "statistics-historical"

                            self.oper_type = YLeaf(YType.enumeration, "oper-type")

                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"
                            self._children_yang_names.add("configured-operation-options")

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._children_yang_names.add("ondemand-operation-options")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("oper_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions, self).__setattr__(name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.profile_name = YLeaf(YType.str, "profile-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "configured-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.ondemand_operation_id = YLeaf(YType.uint32, "ondemand-operation-id")

                                self.probe_count = YLeaf(YType.uint8, "probe-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ondemand_operation_id",
                                                "probe_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ondemand_operation_id.is_set or
                                    self.probe_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ondemand_operation_id.yfilter != YFilter.not_set or
                                    self.probe_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ondemand-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ondemand_operation_id.is_set or self.ondemand_operation_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ondemand_operation_id.get_name_leafdata())
                                if (self.probe_count.is_set or self.probe_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.probe_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ondemand-operation-id" or name == "probe-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ondemand-operation-id"):
                                    self.ondemand_operation_id = value
                                    self.ondemand_operation_id.value_namespace = name_space
                                    self.ondemand_operation_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "probe-count"):
                                    self.probe_count = value
                                    self.probe_count.value_namespace = name_space
                                    self.probe_count.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.oper_type.is_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_data()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.oper_type.yfilter != YFilter.not_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_operation()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "specific-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.oper_type.is_set or self.oper_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oper_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "configured-operation-options"):
                                if (self.configured_operation_options is None):
                                    self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions()
                                    self.configured_operation_options.parent = self
                                    self._children_name_map["configured_operation_options"] = "configured-operation-options"
                                return self.configured_operation_options

                            if (child_yang_name == "ondemand-operation-options"):
                                if (self.ondemand_operation_options is None):
                                    self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions()
                                    self.ondemand_operation_options.parent = self
                                    self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                                return self.ondemand_operation_options

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "configured-operation-options" or name == "ondemand-operation-options" or name == "oper-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "oper-type"):
                                self.oper_type = value
                                self.oper_type.value_namespace = name_space
                                self.oper_type.value_namespace_prefix = name_space_prefix


                    class OperationSchedule(Entity):
                        """
                        Operation schedule
                        
                        .. attribute:: schedule_duration
                        
                        	Duration of a probe for the operation in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: schedule_interval
                        
                        	Interval between the start times of consecutive probes,  in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time
                        
                        	Start time of the first probe, in seconds since the Unix Epoch
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time_configured
                        
                        	Whether or not the operation start time was explicitly configured
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule, self).__init__()

                            self.yang_name = "operation-schedule"
                            self.yang_parent_name = "statistics-historical"

                            self.schedule_duration = YLeaf(YType.uint32, "schedule-duration")

                            self.schedule_interval = YLeaf(YType.uint32, "schedule-interval")

                            self.start_time = YLeaf(YType.uint32, "start-time")

                            self.start_time_configured = YLeaf(YType.boolean, "start-time-configured")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("schedule_duration",
                                            "schedule_interval",
                                            "start_time",
                                            "start_time_configured") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.schedule_duration.is_set or
                                self.schedule_interval.is_set or
                                self.start_time.is_set or
                                self.start_time_configured.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.schedule_duration.yfilter != YFilter.not_set or
                                self.schedule_interval.yfilter != YFilter.not_set or
                                self.start_time.yfilter != YFilter.not_set or
                                self.start_time_configured.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operation-schedule" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.schedule_duration.is_set or self.schedule_duration.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.schedule_duration.get_name_leafdata())
                            if (self.schedule_interval.is_set or self.schedule_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.schedule_interval.get_name_leafdata())
                            if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time.get_name_leafdata())
                            if (self.start_time_configured.is_set or self.start_time_configured.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time_configured.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "schedule-duration" or name == "schedule-interval" or name == "start-time" or name == "start-time-configured"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "schedule-duration"):
                                self.schedule_duration = value
                                self.schedule_duration.value_namespace = name_space
                                self.schedule_duration.value_namespace_prefix = name_space_prefix
                            if(value_path == "schedule-interval"):
                                self.schedule_interval = value
                                self.schedule_interval.value_namespace = name_space
                                self.schedule_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time"):
                                self.start_time = value
                                self.start_time.value_namespace = name_space
                                self.start_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time-configured"):
                                self.start_time_configured = value
                                self.start_time_configured.value_namespace = name_space
                                self.start_time_configured.value_namespace_prefix = name_space_prefix


                    class OperationMetric(Entity):
                        """
                        Metrics gathered for the operation
                        
                        .. attribute:: bucket
                        
                        	Buckets stored for the metric
                        	**type**\: list of    :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket>`
                        
                        .. attribute:: config
                        
                        	Configuration of the metric
                        	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric, self).__init__()

                            self.yang_name = "operation-metric"
                            self.yang_parent_name = "statistics-historical"

                            self.config = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.bucket = YList(self)

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
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric, self).__setattr__(name, value)


                        class Config(Entity):
                            """
                            Configuration of the metric
                            
                            .. attribute:: bins_count
                            
                            	Total number of bins into which to aggregate. 0 if no aggregation
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bins_width
                            
                            	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bucket_size
                            
                            	Size of buckets into which measurements are collected
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: bucket_size_unit
                            
                            	Whether bucket size is 'per\-probe' or 'probes'
                            	**type**\:   :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:   :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "operation-metric"

                                self.bins_count = YLeaf(YType.uint16, "bins-count")

                                self.bins_width = YLeaf(YType.uint16, "bins-width")

                                self.bucket_size = YLeaf(YType.uint8, "bucket-size")

                                self.bucket_size_unit = YLeaf(YType.enumeration, "bucket-size-unit")

                                self.buckets_archive = YLeaf(YType.uint32, "buckets-archive")

                                self.metric_type = YLeaf(YType.enumeration, "metric-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bins_count",
                                                "bins_width",
                                                "bucket_size",
                                                "bucket_size_unit",
                                                "buckets_archive",
                                                "metric_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bins_count.is_set or
                                    self.bins_width.is_set or
                                    self.bucket_size.is_set or
                                    self.bucket_size_unit.is_set or
                                    self.buckets_archive.is_set or
                                    self.metric_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bins_count.yfilter != YFilter.not_set or
                                    self.bins_width.yfilter != YFilter.not_set or
                                    self.bucket_size.yfilter != YFilter.not_set or
                                    self.bucket_size_unit.yfilter != YFilter.not_set or
                                    self.buckets_archive.yfilter != YFilter.not_set or
                                    self.metric_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "config" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bins_count.is_set or self.bins_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bins_count.get_name_leafdata())
                                if (self.bins_width.is_set or self.bins_width.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bins_width.get_name_leafdata())
                                if (self.bucket_size.is_set or self.bucket_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bucket_size.get_name_leafdata())
                                if (self.bucket_size_unit.is_set or self.bucket_size_unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bucket_size_unit.get_name_leafdata())
                                if (self.buckets_archive.is_set or self.buckets_archive.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.buckets_archive.get_name_leafdata())
                                if (self.metric_type.is_set or self.metric_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.metric_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bins-count" or name == "bins-width" or name == "bucket-size" or name == "bucket-size-unit" or name == "buckets-archive" or name == "metric-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bins-count"):
                                    self.bins_count = value
                                    self.bins_count.value_namespace = name_space
                                    self.bins_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "bins-width"):
                                    self.bins_width = value
                                    self.bins_width.value_namespace = name_space
                                    self.bins_width.value_namespace_prefix = name_space_prefix
                                if(value_path == "bucket-size"):
                                    self.bucket_size = value
                                    self.bucket_size.value_namespace = name_space
                                    self.bucket_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "bucket-size-unit"):
                                    self.bucket_size_unit = value
                                    self.bucket_size_unit.value_namespace = name_space
                                    self.bucket_size_unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "buckets-archive"):
                                    self.buckets_archive = value
                                    self.buckets_archive.value_namespace = name_space
                                    self.buckets_archive.value_namespace_prefix = name_space_prefix
                                if(value_path == "metric-type"):
                                    self.metric_type = value
                                    self.metric_type.value_namespace = name_space
                                    self.metric_type.value_namespace_prefix = name_space_prefix


                        class Bucket(Entity):
                            """
                            Buckets stored for the metric
                            
                            .. attribute:: average
                            
                            	Mean of the results in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: contents
                            
                            	The contents of the bucket; bins or samples
                            	**type**\:   :py:class:`Contents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents>`
                            
                            .. attribute:: corrupt
                            
                            	Number of corrupt packets in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_lost_count
                            
                            	The number of data packets lost across the bucket, used in the calculation of overall FLR
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_sent_count
                            
                            	The number of data packets sent across the bucket, used in the calculation of overall FLR
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplicates
                            
                            	Number of duplicate packets received in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duration
                            
                            	Length of time for which the bucket is being filled in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: lost
                            
                            	Number of lost packets in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: minimum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: out_of_order
                            
                            	Number of packets recieved out\-of\-order in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: overall_flr
                            
                            	Frame Loss Ratio across the whole bucket, in millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: percentage
                            
                            .. attribute:: premature_reason
                            
                            	If the probe ended prematurely, the error that caused a probe to end
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: premature_reason_string
                            
                            	Description of the error code that caused the probe to end prematurely. For informational purposes only
                            	**type**\:  str
                            
                            .. attribute:: result_count
                            
                            	The count of samples collected in the bucket
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sent
                            
                            	Number of packets sent in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: standard_deviation
                            
                            	Standard deviation of the results in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: start_at
                            
                            	Absolute time that the bucket started being filled at
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suspect_cleared_mid_bucket
                            
                            	Results suspect as bucket was cleared mid\-way through being filled
                            	**type**\:  bool
                            
                            .. attribute:: suspect_clock_drift
                            
                            	Results suspect as more than 10 seconds time drift detected
                            	**type**\:  bool
                            
                            .. attribute:: suspect_flr_low_packet_count
                            
                            	Results suspect as FLR calculated based on a low packet count
                            	**type**\:  bool
                            
                            .. attribute:: suspect_management_latency
                            
                            	Results suspect as processing of results has been delayed
                            	**type**\:  bool
                            
                            .. attribute:: suspect_memory_allocation_failed
                            
                            	Results suspect due to a memory allocation failure
                            	**type**\:  bool
                            
                            .. attribute:: suspect_misordering
                            
                            	Results suspect as misordering has been detected , affecting results
                            	**type**\:  bool
                            
                            .. attribute:: suspect_multiple_buckets
                            
                            	Results suspect as the probe has been configured across multiple buckets
                            	**type**\:  bool
                            
                            .. attribute:: suspect_premature_end
                            
                            	Results suspect due to a probe ending prematurely
                            	**type**\:  bool
                            
                            .. attribute:: suspect_probe_restarted
                            
                            	Results suspect as probe restarted mid\-way through the bucket
                            	**type**\:  bool
                            
                            .. attribute:: suspect_schedule_latency
                            
                            	Results suspect due to scheduling latency causing one or more packets to not be sent
                            	**type**\:  bool
                            
                            .. attribute:: suspect_send_fail
                            
                            	Results suspect due to failure to send one or more packets
                            	**type**\:  bool
                            
                            .. attribute:: suspect_start_mid_bucket
                            
                            	Results suspect due to a probe starting mid\-way through a bucket
                            	**type**\:  bool
                            
                            .. attribute:: time_of_maximum
                            
                            	Absolute time that the maximum value was recorded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_of_minimum
                            
                            	Absolute time that the minimum value was recorded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket, self).__init__()

                                self.yang_name = "bucket"
                                self.yang_parent_name = "operation-metric"

                                self.average = YLeaf(YType.int32, "average")

                                self.corrupt = YLeaf(YType.uint32, "corrupt")

                                self.data_lost_count = YLeaf(YType.uint32, "data-lost-count")

                                self.data_sent_count = YLeaf(YType.uint32, "data-sent-count")

                                self.duplicates = YLeaf(YType.uint32, "duplicates")

                                self.duration = YLeaf(YType.uint32, "duration")

                                self.lost = YLeaf(YType.uint32, "lost")

                                self.maximum = YLeaf(YType.int32, "maximum")

                                self.minimum = YLeaf(YType.int32, "minimum")

                                self.out_of_order = YLeaf(YType.uint32, "out-of-order")

                                self.overall_flr = YLeaf(YType.int32, "overall-flr")

                                self.premature_reason = YLeaf(YType.uint32, "premature-reason")

                                self.premature_reason_string = YLeaf(YType.str, "premature-reason-string")

                                self.result_count = YLeaf(YType.uint32, "result-count")

                                self.sent = YLeaf(YType.uint32, "sent")

                                self.standard_deviation = YLeaf(YType.int32, "standard-deviation")

                                self.start_at = YLeaf(YType.uint32, "start-at")

                                self.suspect_cleared_mid_bucket = YLeaf(YType.boolean, "suspect-cleared-mid-bucket")

                                self.suspect_clock_drift = YLeaf(YType.boolean, "suspect-clock-drift")

                                self.suspect_flr_low_packet_count = YLeaf(YType.boolean, "suspect-flr-low-packet-count")

                                self.suspect_management_latency = YLeaf(YType.boolean, "suspect-management-latency")

                                self.suspect_memory_allocation_failed = YLeaf(YType.boolean, "suspect-memory-allocation-failed")

                                self.suspect_misordering = YLeaf(YType.boolean, "suspect-misordering")

                                self.suspect_multiple_buckets = YLeaf(YType.boolean, "suspect-multiple-buckets")

                                self.suspect_premature_end = YLeaf(YType.boolean, "suspect-premature-end")

                                self.suspect_probe_restarted = YLeaf(YType.boolean, "suspect-probe-restarted")

                                self.suspect_schedule_latency = YLeaf(YType.boolean, "suspect-schedule-latency")

                                self.suspect_send_fail = YLeaf(YType.boolean, "suspect-send-fail")

                                self.suspect_start_mid_bucket = YLeaf(YType.boolean, "suspect-start-mid-bucket")

                                self.time_of_maximum = YLeaf(YType.uint32, "time-of-maximum")

                                self.time_of_minimum = YLeaf(YType.uint32, "time-of-minimum")

                                self.contents = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self._children_name_map["contents"] = "contents"
                                self._children_yang_names.add("contents")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("average",
                                                "corrupt",
                                                "data_lost_count",
                                                "data_sent_count",
                                                "duplicates",
                                                "duration",
                                                "lost",
                                                "maximum",
                                                "minimum",
                                                "out_of_order",
                                                "overall_flr",
                                                "premature_reason",
                                                "premature_reason_string",
                                                "result_count",
                                                "sent",
                                                "standard_deviation",
                                                "start_at",
                                                "suspect_cleared_mid_bucket",
                                                "suspect_clock_drift",
                                                "suspect_flr_low_packet_count",
                                                "suspect_management_latency",
                                                "suspect_memory_allocation_failed",
                                                "suspect_misordering",
                                                "suspect_multiple_buckets",
                                                "suspect_premature_end",
                                                "suspect_probe_restarted",
                                                "suspect_schedule_latency",
                                                "suspect_send_fail",
                                                "suspect_start_mid_bucket",
                                                "time_of_maximum",
                                                "time_of_minimum") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket, self).__setattr__(name, value)


                            class Contents(Entity):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:   :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:   :py:class:`SlaOperBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucket>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:   :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents, self).__init__()

                                    self.yang_name = "contents"
                                    self.yang_parent_name = "bucket"

                                    self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self._children_name_map["aggregated"] = "aggregated"
                                    self._children_yang_names.add("aggregated")

                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self
                                    self._children_name_map["unaggregated"] = "unaggregated"
                                    self._children_yang_names.add("unaggregated")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bucket_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents, self).__setattr__(name, value)


                                class Aggregated(Entity):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated, self).__init__()

                                        self.yang_name = "aggregated"
                                        self.yang_parent_name = "contents"

                                        self.bins = YList(self)

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
                                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated, self).__setattr__(name, value)


                                    class Bins(Entity):
                                        """
                                        The bins of an SLA metric bucket
                                        
                                        .. attribute:: count
                                        
                                        	The total number of results in the bin
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lower_bound
                                        
                                        	Lower bound (inclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: lower_bound_tenths
                                        
                                        	Lower bound (inclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: sum
                                        
                                        	The sum of the results in the bin, in microseconds or millionths of a percent
                                        	**type**\:  int
                                        
                                        	**range:** \-9223372036854775808..9223372036854775807
                                        
                                        .. attribute:: upper_bound
                                        
                                        	Upper bound (exclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: upper_bound_tenths
                                        
                                        	Upper bound (exclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__init__()

                                            self.yang_name = "bins"
                                            self.yang_parent_name = "aggregated"

                                            self.count = YLeaf(YType.uint32, "count")

                                            self.lower_bound = YLeaf(YType.int32, "lower-bound")

                                            self.lower_bound_tenths = YLeaf(YType.int32, "lower-bound-tenths")

                                            self.sum = YLeaf(YType.int64, "sum")

                                            self.upper_bound = YLeaf(YType.int32, "upper-bound")

                                            self.upper_bound_tenths = YLeaf(YType.int32, "upper-bound-tenths")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("count",
                                                            "lower_bound",
                                                            "lower_bound_tenths",
                                                            "sum",
                                                            "upper_bound",
                                                            "upper_bound_tenths") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.count.is_set or
                                                self.lower_bound.is_set or
                                                self.lower_bound_tenths.is_set or
                                                self.sum.is_set or
                                                self.upper_bound.is_set or
                                                self.upper_bound_tenths.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.count.yfilter != YFilter.not_set or
                                                self.lower_bound.yfilter != YFilter.not_set or
                                                self.lower_bound_tenths.yfilter != YFilter.not_set or
                                                self.sum.yfilter != YFilter.not_set or
                                                self.upper_bound.yfilter != YFilter.not_set or
                                                self.upper_bound_tenths.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "bins" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/contents/aggregated/%s" % self.get_segment_path()
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.count.get_name_leafdata())
                                            if (self.lower_bound.is_set or self.lower_bound.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.lower_bound.get_name_leafdata())
                                            if (self.lower_bound_tenths.is_set or self.lower_bound_tenths.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.lower_bound_tenths.get_name_leafdata())
                                            if (self.sum.is_set or self.sum.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sum.get_name_leafdata())
                                            if (self.upper_bound.is_set or self.upper_bound.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.upper_bound.get_name_leafdata())
                                            if (self.upper_bound_tenths.is_set or self.upper_bound_tenths.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.upper_bound_tenths.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "count" or name == "lower-bound" or name == "lower-bound-tenths" or name == "sum" or name == "upper-bound" or name == "upper-bound-tenths"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "count"):
                                                self.count = value
                                                self.count.value_namespace = name_space
                                                self.count.value_namespace_prefix = name_space_prefix
                                            if(value_path == "lower-bound"):
                                                self.lower_bound = value
                                                self.lower_bound.value_namespace = name_space
                                                self.lower_bound.value_namespace_prefix = name_space_prefix
                                            if(value_path == "lower-bound-tenths"):
                                                self.lower_bound_tenths = value
                                                self.lower_bound_tenths.value_namespace = name_space
                                                self.lower_bound_tenths.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sum"):
                                                self.sum = value
                                                self.sum.value_namespace = name_space
                                                self.sum.value_namespace_prefix = name_space_prefix
                                            if(value_path == "upper-bound"):
                                                self.upper_bound = value
                                                self.upper_bound.value_namespace = name_space
                                                self.upper_bound.value_namespace_prefix = name_space_prefix
                                            if(value_path == "upper-bound-tenths"):
                                                self.upper_bound_tenths = value
                                                self.upper_bound_tenths.value_namespace = name_space
                                                self.upper_bound_tenths.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.bins:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.bins:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "aggregated" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/contents/%s" % self.get_segment_path()
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "bins"):
                                            for c in self.bins:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.bins.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "bins"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class Unaggregated(Entity):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated, self).__init__()

                                        self.yang_name = "unaggregated"
                                        self.yang_parent_name = "contents"

                                        self.sample = YList(self)

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
                                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated, self).__setattr__(name, value)


                                    class Sample(Entity):
                                        """
                                        The samples of an SLA metric bucket
                                        
                                        .. attribute:: corrupt
                                        
                                        	Whether the sample packet was corrupt
                                        	**type**\:  bool
                                        
                                        .. attribute:: frames_lost
                                        
                                        	For FLR measurements, the number of frames lost, if available
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: frames_sent
                                        
                                        	For FLR measurements, the number of frames sent, if available
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: no_data_packets
                                        
                                        	Whether a measurement could not be made because no data packets were sent in the sample period. Only applicable for LMM measurements
                                        	**type**\:  bool
                                        
                                        .. attribute:: out_of_order
                                        
                                        	Whether the sample packet was received out\-of\-order
                                        	**type**\:  bool
                                        
                                        .. attribute:: result
                                        
                                        	The result (in microseconds or millionths of a percent) of the sample, if available
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: sent
                                        
                                        	Whether the sample packet was sucessfully sent
                                        	**type**\:  bool
                                        
                                        .. attribute:: sent_at
                                        
                                        	The time (in milliseconds relative to the start time of the bucket) that the sample was sent at
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: timed_out
                                        
                                        	Whether the sample packet timed out
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__init__()

                                            self.yang_name = "sample"
                                            self.yang_parent_name = "unaggregated"

                                            self.corrupt = YLeaf(YType.boolean, "corrupt")

                                            self.frames_lost = YLeaf(YType.uint32, "frames-lost")

                                            self.frames_sent = YLeaf(YType.uint32, "frames-sent")

                                            self.no_data_packets = YLeaf(YType.boolean, "no-data-packets")

                                            self.out_of_order = YLeaf(YType.boolean, "out-of-order")

                                            self.result = YLeaf(YType.int32, "result")

                                            self.sent = YLeaf(YType.boolean, "sent")

                                            self.sent_at = YLeaf(YType.uint32, "sent-at")

                                            self.timed_out = YLeaf(YType.boolean, "timed-out")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("corrupt",
                                                            "frames_lost",
                                                            "frames_sent",
                                                            "no_data_packets",
                                                            "out_of_order",
                                                            "result",
                                                            "sent",
                                                            "sent_at",
                                                            "timed_out") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.corrupt.is_set or
                                                self.frames_lost.is_set or
                                                self.frames_sent.is_set or
                                                self.no_data_packets.is_set or
                                                self.out_of_order.is_set or
                                                self.result.is_set or
                                                self.sent.is_set or
                                                self.sent_at.is_set or
                                                self.timed_out.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.corrupt.yfilter != YFilter.not_set or
                                                self.frames_lost.yfilter != YFilter.not_set or
                                                self.frames_sent.yfilter != YFilter.not_set or
                                                self.no_data_packets.yfilter != YFilter.not_set or
                                                self.out_of_order.yfilter != YFilter.not_set or
                                                self.result.yfilter != YFilter.not_set or
                                                self.sent.yfilter != YFilter.not_set or
                                                self.sent_at.yfilter != YFilter.not_set or
                                                self.timed_out.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "sample" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/contents/unaggregated/%s" % self.get_segment_path()
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.corrupt.is_set or self.corrupt.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.corrupt.get_name_leafdata())
                                            if (self.frames_lost.is_set or self.frames_lost.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.frames_lost.get_name_leafdata())
                                            if (self.frames_sent.is_set or self.frames_sent.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.frames_sent.get_name_leafdata())
                                            if (self.no_data_packets.is_set or self.no_data_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.no_data_packets.get_name_leafdata())
                                            if (self.out_of_order.is_set or self.out_of_order.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.out_of_order.get_name_leafdata())
                                            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.result.get_name_leafdata())
                                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sent.get_name_leafdata())
                                            if (self.sent_at.is_set or self.sent_at.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sent_at.get_name_leafdata())
                                            if (self.timed_out.is_set or self.timed_out.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.timed_out.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "corrupt" or name == "frames-lost" or name == "frames-sent" or name == "no-data-packets" or name == "out-of-order" or name == "result" or name == "sent" or name == "sent-at" or name == "timed-out"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "corrupt"):
                                                self.corrupt = value
                                                self.corrupt.value_namespace = name_space
                                                self.corrupt.value_namespace_prefix = name_space_prefix
                                            if(value_path == "frames-lost"):
                                                self.frames_lost = value
                                                self.frames_lost.value_namespace = name_space
                                                self.frames_lost.value_namespace_prefix = name_space_prefix
                                            if(value_path == "frames-sent"):
                                                self.frames_sent = value
                                                self.frames_sent.value_namespace = name_space
                                                self.frames_sent.value_namespace_prefix = name_space_prefix
                                            if(value_path == "no-data-packets"):
                                                self.no_data_packets = value
                                                self.no_data_packets.value_namespace = name_space
                                                self.no_data_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "out-of-order"):
                                                self.out_of_order = value
                                                self.out_of_order.value_namespace = name_space
                                                self.out_of_order.value_namespace_prefix = name_space_prefix
                                            if(value_path == "result"):
                                                self.result = value
                                                self.result.value_namespace = name_space
                                                self.result.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sent"):
                                                self.sent = value
                                                self.sent.value_namespace = name_space
                                                self.sent.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sent-at"):
                                                self.sent_at = value
                                                self.sent_at.value_namespace = name_space
                                                self.sent_at.value_namespace_prefix = name_space_prefix
                                            if(value_path == "timed-out"):
                                                self.timed_out = value
                                                self.timed_out.value_namespace = name_space
                                                self.timed_out.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.sample:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.sample:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unaggregated" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/contents/%s" % self.get_segment_path()
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "sample"):
                                            for c in self.sample:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.sample.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "sample"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.bucket_type.is_set or
                                        (self.aggregated is not None and self.aggregated.has_data()) or
                                        (self.unaggregated is not None and self.unaggregated.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bucket_type.yfilter != YFilter.not_set or
                                        (self.aggregated is not None and self.aggregated.has_operation()) or
                                        (self.unaggregated is not None and self.unaggregated.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "contents" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/%s" % self.get_segment_path()
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bucket_type.is_set or self.bucket_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "aggregated"):
                                        if (self.aggregated is None):
                                            self.aggregated = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated()
                                            self.aggregated.parent = self
                                            self._children_name_map["aggregated"] = "aggregated"
                                        return self.aggregated

                                    if (child_yang_name == "unaggregated"):
                                        if (self.unaggregated is None):
                                            self.unaggregated = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated()
                                            self.unaggregated.parent = self
                                            self._children_name_map["unaggregated"] = "unaggregated"
                                        return self.unaggregated

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "aggregated" or name == "unaggregated" or name == "bucket-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bucket-type"):
                                        self.bucket_type = value
                                        self.bucket_type.value_namespace = name_space
                                        self.bucket_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.average.is_set or
                                    self.corrupt.is_set or
                                    self.data_lost_count.is_set or
                                    self.data_sent_count.is_set or
                                    self.duplicates.is_set or
                                    self.duration.is_set or
                                    self.lost.is_set or
                                    self.maximum.is_set or
                                    self.minimum.is_set or
                                    self.out_of_order.is_set or
                                    self.overall_flr.is_set or
                                    self.premature_reason.is_set or
                                    self.premature_reason_string.is_set or
                                    self.result_count.is_set or
                                    self.sent.is_set or
                                    self.standard_deviation.is_set or
                                    self.start_at.is_set or
                                    self.suspect_cleared_mid_bucket.is_set or
                                    self.suspect_clock_drift.is_set or
                                    self.suspect_flr_low_packet_count.is_set or
                                    self.suspect_management_latency.is_set or
                                    self.suspect_memory_allocation_failed.is_set or
                                    self.suspect_misordering.is_set or
                                    self.suspect_multiple_buckets.is_set or
                                    self.suspect_premature_end.is_set or
                                    self.suspect_probe_restarted.is_set or
                                    self.suspect_schedule_latency.is_set or
                                    self.suspect_send_fail.is_set or
                                    self.suspect_start_mid_bucket.is_set or
                                    self.time_of_maximum.is_set or
                                    self.time_of_minimum.is_set or
                                    (self.contents is not None and self.contents.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.average.yfilter != YFilter.not_set or
                                    self.corrupt.yfilter != YFilter.not_set or
                                    self.data_lost_count.yfilter != YFilter.not_set or
                                    self.data_sent_count.yfilter != YFilter.not_set or
                                    self.duplicates.yfilter != YFilter.not_set or
                                    self.duration.yfilter != YFilter.not_set or
                                    self.lost.yfilter != YFilter.not_set or
                                    self.maximum.yfilter != YFilter.not_set or
                                    self.minimum.yfilter != YFilter.not_set or
                                    self.out_of_order.yfilter != YFilter.not_set or
                                    self.overall_flr.yfilter != YFilter.not_set or
                                    self.premature_reason.yfilter != YFilter.not_set or
                                    self.premature_reason_string.yfilter != YFilter.not_set or
                                    self.result_count.yfilter != YFilter.not_set or
                                    self.sent.yfilter != YFilter.not_set or
                                    self.standard_deviation.yfilter != YFilter.not_set or
                                    self.start_at.yfilter != YFilter.not_set or
                                    self.suspect_cleared_mid_bucket.yfilter != YFilter.not_set or
                                    self.suspect_clock_drift.yfilter != YFilter.not_set or
                                    self.suspect_flr_low_packet_count.yfilter != YFilter.not_set or
                                    self.suspect_management_latency.yfilter != YFilter.not_set or
                                    self.suspect_memory_allocation_failed.yfilter != YFilter.not_set or
                                    self.suspect_misordering.yfilter != YFilter.not_set or
                                    self.suspect_multiple_buckets.yfilter != YFilter.not_set or
                                    self.suspect_premature_end.yfilter != YFilter.not_set or
                                    self.suspect_probe_restarted.yfilter != YFilter.not_set or
                                    self.suspect_schedule_latency.yfilter != YFilter.not_set or
                                    self.suspect_send_fail.yfilter != YFilter.not_set or
                                    self.suspect_start_mid_bucket.yfilter != YFilter.not_set or
                                    self.time_of_maximum.yfilter != YFilter.not_set or
                                    self.time_of_minimum.yfilter != YFilter.not_set or
                                    (self.contents is not None and self.contents.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bucket" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.average.is_set or self.average.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.average.get_name_leafdata())
                                if (self.corrupt.is_set or self.corrupt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.corrupt.get_name_leafdata())
                                if (self.data_lost_count.is_set or self.data_lost_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_lost_count.get_name_leafdata())
                                if (self.data_sent_count.is_set or self.data_sent_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_sent_count.get_name_leafdata())
                                if (self.duplicates.is_set or self.duplicates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duplicates.get_name_leafdata())
                                if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duration.get_name_leafdata())
                                if (self.lost.is_set or self.lost.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lost.get_name_leafdata())
                                if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.maximum.get_name_leafdata())
                                if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.minimum.get_name_leafdata())
                                if (self.out_of_order.is_set or self.out_of_order.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_of_order.get_name_leafdata())
                                if (self.overall_flr.is_set or self.overall_flr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.overall_flr.get_name_leafdata())
                                if (self.premature_reason.is_set or self.premature_reason.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.premature_reason.get_name_leafdata())
                                if (self.premature_reason_string.is_set or self.premature_reason_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.premature_reason_string.get_name_leafdata())
                                if (self.result_count.is_set or self.result_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.result_count.get_name_leafdata())
                                if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sent.get_name_leafdata())
                                if (self.standard_deviation.is_set or self.standard_deviation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.standard_deviation.get_name_leafdata())
                                if (self.start_at.is_set or self.start_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_at.get_name_leafdata())
                                if (self.suspect_cleared_mid_bucket.is_set or self.suspect_cleared_mid_bucket.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_cleared_mid_bucket.get_name_leafdata())
                                if (self.suspect_clock_drift.is_set or self.suspect_clock_drift.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_clock_drift.get_name_leafdata())
                                if (self.suspect_flr_low_packet_count.is_set or self.suspect_flr_low_packet_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_flr_low_packet_count.get_name_leafdata())
                                if (self.suspect_management_latency.is_set or self.suspect_management_latency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_management_latency.get_name_leafdata())
                                if (self.suspect_memory_allocation_failed.is_set or self.suspect_memory_allocation_failed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_memory_allocation_failed.get_name_leafdata())
                                if (self.suspect_misordering.is_set or self.suspect_misordering.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_misordering.get_name_leafdata())
                                if (self.suspect_multiple_buckets.is_set or self.suspect_multiple_buckets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_multiple_buckets.get_name_leafdata())
                                if (self.suspect_premature_end.is_set or self.suspect_premature_end.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_premature_end.get_name_leafdata())
                                if (self.suspect_probe_restarted.is_set or self.suspect_probe_restarted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_probe_restarted.get_name_leafdata())
                                if (self.suspect_schedule_latency.is_set or self.suspect_schedule_latency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_schedule_latency.get_name_leafdata())
                                if (self.suspect_send_fail.is_set or self.suspect_send_fail.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_send_fail.get_name_leafdata())
                                if (self.suspect_start_mid_bucket.is_set or self.suspect_start_mid_bucket.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_start_mid_bucket.get_name_leafdata())
                                if (self.time_of_maximum.is_set or self.time_of_maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_of_maximum.get_name_leafdata())
                                if (self.time_of_minimum.is_set or self.time_of_minimum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_of_minimum.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "contents"):
                                    if (self.contents is None):
                                        self.contents = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents()
                                        self.contents.parent = self
                                        self._children_name_map["contents"] = "contents"
                                    return self.contents

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "contents" or name == "average" or name == "corrupt" or name == "data-lost-count" or name == "data-sent-count" or name == "duplicates" or name == "duration" or name == "lost" or name == "maximum" or name == "minimum" or name == "out-of-order" or name == "overall-flr" or name == "premature-reason" or name == "premature-reason-string" or name == "result-count" or name == "sent" or name == "standard-deviation" or name == "start-at" or name == "suspect-cleared-mid-bucket" or name == "suspect-clock-drift" or name == "suspect-flr-low-packet-count" or name == "suspect-management-latency" or name == "suspect-memory-allocation-failed" or name == "suspect-misordering" or name == "suspect-multiple-buckets" or name == "suspect-premature-end" or name == "suspect-probe-restarted" or name == "suspect-schedule-latency" or name == "suspect-send-fail" or name == "suspect-start-mid-bucket" or name == "time-of-maximum" or name == "time-of-minimum"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "average"):
                                    self.average = value
                                    self.average.value_namespace = name_space
                                    self.average.value_namespace_prefix = name_space_prefix
                                if(value_path == "corrupt"):
                                    self.corrupt = value
                                    self.corrupt.value_namespace = name_space
                                    self.corrupt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-lost-count"):
                                    self.data_lost_count = value
                                    self.data_lost_count.value_namespace = name_space
                                    self.data_lost_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-sent-count"):
                                    self.data_sent_count = value
                                    self.data_sent_count.value_namespace = name_space
                                    self.data_sent_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "duplicates"):
                                    self.duplicates = value
                                    self.duplicates.value_namespace = name_space
                                    self.duplicates.value_namespace_prefix = name_space_prefix
                                if(value_path == "duration"):
                                    self.duration = value
                                    self.duration.value_namespace = name_space
                                    self.duration.value_namespace_prefix = name_space_prefix
                                if(value_path == "lost"):
                                    self.lost = value
                                    self.lost.value_namespace = name_space
                                    self.lost.value_namespace_prefix = name_space_prefix
                                if(value_path == "maximum"):
                                    self.maximum = value
                                    self.maximum.value_namespace = name_space
                                    self.maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "minimum"):
                                    self.minimum = value
                                    self.minimum.value_namespace = name_space
                                    self.minimum.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-of-order"):
                                    self.out_of_order = value
                                    self.out_of_order.value_namespace = name_space
                                    self.out_of_order.value_namespace_prefix = name_space_prefix
                                if(value_path == "overall-flr"):
                                    self.overall_flr = value
                                    self.overall_flr.value_namespace = name_space
                                    self.overall_flr.value_namespace_prefix = name_space_prefix
                                if(value_path == "premature-reason"):
                                    self.premature_reason = value
                                    self.premature_reason.value_namespace = name_space
                                    self.premature_reason.value_namespace_prefix = name_space_prefix
                                if(value_path == "premature-reason-string"):
                                    self.premature_reason_string = value
                                    self.premature_reason_string.value_namespace = name_space
                                    self.premature_reason_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "result-count"):
                                    self.result_count = value
                                    self.result_count.value_namespace = name_space
                                    self.result_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "sent"):
                                    self.sent = value
                                    self.sent.value_namespace = name_space
                                    self.sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "standard-deviation"):
                                    self.standard_deviation = value
                                    self.standard_deviation.value_namespace = name_space
                                    self.standard_deviation.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-at"):
                                    self.start_at = value
                                    self.start_at.value_namespace = name_space
                                    self.start_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-cleared-mid-bucket"):
                                    self.suspect_cleared_mid_bucket = value
                                    self.suspect_cleared_mid_bucket.value_namespace = name_space
                                    self.suspect_cleared_mid_bucket.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-clock-drift"):
                                    self.suspect_clock_drift = value
                                    self.suspect_clock_drift.value_namespace = name_space
                                    self.suspect_clock_drift.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-flr-low-packet-count"):
                                    self.suspect_flr_low_packet_count = value
                                    self.suspect_flr_low_packet_count.value_namespace = name_space
                                    self.suspect_flr_low_packet_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-management-latency"):
                                    self.suspect_management_latency = value
                                    self.suspect_management_latency.value_namespace = name_space
                                    self.suspect_management_latency.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-memory-allocation-failed"):
                                    self.suspect_memory_allocation_failed = value
                                    self.suspect_memory_allocation_failed.value_namespace = name_space
                                    self.suspect_memory_allocation_failed.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-misordering"):
                                    self.suspect_misordering = value
                                    self.suspect_misordering.value_namespace = name_space
                                    self.suspect_misordering.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-multiple-buckets"):
                                    self.suspect_multiple_buckets = value
                                    self.suspect_multiple_buckets.value_namespace = name_space
                                    self.suspect_multiple_buckets.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-premature-end"):
                                    self.suspect_premature_end = value
                                    self.suspect_premature_end.value_namespace = name_space
                                    self.suspect_premature_end.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-probe-restarted"):
                                    self.suspect_probe_restarted = value
                                    self.suspect_probe_restarted.value_namespace = name_space
                                    self.suspect_probe_restarted.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-schedule-latency"):
                                    self.suspect_schedule_latency = value
                                    self.suspect_schedule_latency.value_namespace = name_space
                                    self.suspect_schedule_latency.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-send-fail"):
                                    self.suspect_send_fail = value
                                    self.suspect_send_fail.value_namespace = name_space
                                    self.suspect_send_fail.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-start-mid-bucket"):
                                    self.suspect_start_mid_bucket = value
                                    self.suspect_start_mid_bucket.value_namespace = name_space
                                    self.suspect_start_mid_bucket.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-of-maximum"):
                                    self.time_of_maximum = value
                                    self.time_of_maximum.value_namespace = name_space
                                    self.time_of_maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-of-minimum"):
                                    self.time_of_minimum = value
                                    self.time_of_minimum.value_namespace = name_space
                                    self.time_of_minimum.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.bucket:
                                if (c.has_data()):
                                    return True
                            return (self.config is not None and self.config.has_data())

                        def has_operation(self):
                            for c in self.bucket:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operation-metric" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "bucket"):
                                for c in self.bucket:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.bucket.append(c)
                                return c

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bucket" or name == "config"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        for c in self.operation_metric:
                            if (c.has_data()):
                                return True
                        return (
                            self.display_long.is_set or
                            self.display_short.is_set or
                            self.domain_name.is_set or
                            self.flr_calculation_interval.is_set or
                            self.interface_name.is_set or
                            self.mac_address.is_set or
                            self.mep_id.is_set or
                            self.probe_type.is_set or
                            self.profile_name.is_set or
                            (self.operation_schedule is not None and self.operation_schedule.has_data()) or
                            (self.specific_options is not None and self.specific_options.has_data()))

                    def has_operation(self):
                        for c in self.operation_metric:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.display_long.yfilter != YFilter.not_set or
                            self.display_short.yfilter != YFilter.not_set or
                            self.domain_name.yfilter != YFilter.not_set or
                            self.flr_calculation_interval.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.mep_id.yfilter != YFilter.not_set or
                            self.probe_type.yfilter != YFilter.not_set or
                            self.profile_name.yfilter != YFilter.not_set or
                            (self.operation_schedule is not None and self.operation_schedule.has_operation()) or
                            (self.specific_options is not None and self.specific_options.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics-historical" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.display_long.is_set or self.display_long.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_long.get_name_leafdata())
                        if (self.display_short.is_set or self.display_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_short.get_name_leafdata())
                        if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_name.get_name_leafdata())
                        if (self.flr_calculation_interval.is_set or self.flr_calculation_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flr_calculation_interval.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.mep_id.is_set or self.mep_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mep_id.get_name_leafdata())
                        if (self.probe_type.is_set or self.probe_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.probe_type.get_name_leafdata())
                        if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.profile_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "operation-metric"):
                            for c in self.operation_metric:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.operation_metric.append(c)
                            return c

                        if (child_yang_name == "operation-schedule"):
                            if (self.operation_schedule is None):
                                self.operation_schedule = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule()
                                self.operation_schedule.parent = self
                                self._children_name_map["operation_schedule"] = "operation-schedule"
                            return self.operation_schedule

                        if (child_yang_name == "specific-options"):
                            if (self.specific_options is None):
                                self.specific_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions()
                                self.specific_options.parent = self
                                self._children_name_map["specific_options"] = "specific-options"
                            return self.specific_options

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "operation-metric" or name == "operation-schedule" or name == "specific-options" or name == "display-long" or name == "display-short" or name == "domain-name" or name == "flr-calculation-interval" or name == "interface-name" or name == "mac-address" or name == "mep-id" or name == "probe-type" or name == "profile-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "display-long"):
                            self.display_long = value
                            self.display_long.value_namespace = name_space
                            self.display_long.value_namespace_prefix = name_space_prefix
                        if(value_path == "display-short"):
                            self.display_short = value
                            self.display_short.value_namespace = name_space
                            self.display_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-name"):
                            self.domain_name = value
                            self.domain_name.value_namespace = name_space
                            self.domain_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "flr-calculation-interval"):
                            self.flr_calculation_interval = value
                            self.flr_calculation_interval.value_namespace = name_space
                            self.flr_calculation_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mep-id"):
                            self.mep_id = value
                            self.mep_id.value_namespace = name_space
                            self.mep_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "probe-type"):
                            self.probe_type = value
                            self.probe_type.value_namespace = name_space
                            self.probe_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "profile-name"):
                            self.profile_name = value
                            self.profile_name.value_namespace = name_space
                            self.profile_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.statistics_historical:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.statistics_historical:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics-historicals" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "statistics-historical"):
                        for c in self.statistics_historical:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.statistics_historical.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statistics-historical"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class StatisticsOnDemandHistoricals(Entity):
                """
                Table of historical statistics for SLA
                on\-demand operations
                
                .. attribute:: statistics_on_demand_historical
                
                	Historical statistics data for an SLA on\-demand  operation
                	**type**\: list of    :py:class:`StatisticsOnDemandHistorical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals, self).__init__()

                    self.yang_name = "statistics-on-demand-historicals"
                    self.yang_parent_name = "ethernet"

                    self.statistics_on_demand_historical = YList(self)

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
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals, self).__setattr__(name, value)


                class StatisticsOnDemandHistorical(Entity):
                    """
                    Historical statistics data for an SLA
                    on\-demand  operation
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: flr_calculation_interval
                    
                    	Interval between FLR calculations for SLM, in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\:  int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: operation_id
                    
                    	Operation ID
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: operation_metric
                    
                    	Metrics gathered for the operation
                    	**type**\: list of    :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric>`
                    
                    .. attribute:: operation_schedule
                    
                    	Operation schedule
                    	**type**\:   :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule>`
                    
                    .. attribute:: probe_type
                    
                    	Type of probe used by the operation
                    	**type**\:  str
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:   :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical, self).__init__()

                        self.yang_name = "statistics-on-demand-historical"
                        self.yang_parent_name = "statistics-on-demand-historicals"

                        self.display_long = YLeaf(YType.str, "display-long")

                        self.display_short = YLeaf(YType.str, "display-short")

                        self.domain_name = YLeaf(YType.str, "domain-name")

                        self.flr_calculation_interval = YLeaf(YType.uint32, "flr-calculation-interval")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.mep_id = YLeaf(YType.uint32, "mep-id")

                        self.operation_id = YLeaf(YType.uint32, "operation-id")

                        self.probe_type = YLeaf(YType.str, "probe-type")

                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule()
                        self.operation_schedule.parent = self
                        self._children_name_map["operation_schedule"] = "operation-schedule"
                        self._children_yang_names.add("operation-schedule")

                        self.specific_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"
                        self._children_yang_names.add("specific-options")

                        self.operation_metric = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("display_long",
                                        "display_short",
                                        "domain_name",
                                        "flr_calculation_interval",
                                        "interface_name",
                                        "mac_address",
                                        "mep_id",
                                        "operation_id",
                                        "probe_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical, self).__setattr__(name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:   :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:   :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:   :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "statistics-on-demand-historical"

                            self.oper_type = YLeaf(YType.enumeration, "oper-type")

                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"
                            self._children_yang_names.add("configured-operation-options")

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._children_yang_names.add("ondemand-operation-options")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("oper_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions, self).__setattr__(name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.profile_name = YLeaf(YType.str, "profile-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "configured-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.ondemand_operation_id = YLeaf(YType.uint32, "ondemand-operation-id")

                                self.probe_count = YLeaf(YType.uint8, "probe-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ondemand_operation_id",
                                                "probe_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ondemand_operation_id.is_set or
                                    self.probe_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ondemand_operation_id.yfilter != YFilter.not_set or
                                    self.probe_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ondemand-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ondemand_operation_id.is_set or self.ondemand_operation_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ondemand_operation_id.get_name_leafdata())
                                if (self.probe_count.is_set or self.probe_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.probe_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ondemand-operation-id" or name == "probe-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ondemand-operation-id"):
                                    self.ondemand_operation_id = value
                                    self.ondemand_operation_id.value_namespace = name_space
                                    self.ondemand_operation_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "probe-count"):
                                    self.probe_count = value
                                    self.probe_count.value_namespace = name_space
                                    self.probe_count.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.oper_type.is_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_data()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.oper_type.yfilter != YFilter.not_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_operation()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "specific-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.oper_type.is_set or self.oper_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oper_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "configured-operation-options"):
                                if (self.configured_operation_options is None):
                                    self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions()
                                    self.configured_operation_options.parent = self
                                    self._children_name_map["configured_operation_options"] = "configured-operation-options"
                                return self.configured_operation_options

                            if (child_yang_name == "ondemand-operation-options"):
                                if (self.ondemand_operation_options is None):
                                    self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions()
                                    self.ondemand_operation_options.parent = self
                                    self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                                return self.ondemand_operation_options

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "configured-operation-options" or name == "ondemand-operation-options" or name == "oper-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "oper-type"):
                                self.oper_type = value
                                self.oper_type.value_namespace = name_space
                                self.oper_type.value_namespace_prefix = name_space_prefix


                    class OperationSchedule(Entity):
                        """
                        Operation schedule
                        
                        .. attribute:: schedule_duration
                        
                        	Duration of a probe for the operation in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: schedule_interval
                        
                        	Interval between the start times of consecutive probes,  in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time
                        
                        	Start time of the first probe, in seconds since the Unix Epoch
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time_configured
                        
                        	Whether or not the operation start time was explicitly configured
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule, self).__init__()

                            self.yang_name = "operation-schedule"
                            self.yang_parent_name = "statistics-on-demand-historical"

                            self.schedule_duration = YLeaf(YType.uint32, "schedule-duration")

                            self.schedule_interval = YLeaf(YType.uint32, "schedule-interval")

                            self.start_time = YLeaf(YType.uint32, "start-time")

                            self.start_time_configured = YLeaf(YType.boolean, "start-time-configured")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("schedule_duration",
                                            "schedule_interval",
                                            "start_time",
                                            "start_time_configured") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.schedule_duration.is_set or
                                self.schedule_interval.is_set or
                                self.start_time.is_set or
                                self.start_time_configured.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.schedule_duration.yfilter != YFilter.not_set or
                                self.schedule_interval.yfilter != YFilter.not_set or
                                self.start_time.yfilter != YFilter.not_set or
                                self.start_time_configured.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operation-schedule" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.schedule_duration.is_set or self.schedule_duration.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.schedule_duration.get_name_leafdata())
                            if (self.schedule_interval.is_set or self.schedule_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.schedule_interval.get_name_leafdata())
                            if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time.get_name_leafdata())
                            if (self.start_time_configured.is_set or self.start_time_configured.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time_configured.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "schedule-duration" or name == "schedule-interval" or name == "start-time" or name == "start-time-configured"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "schedule-duration"):
                                self.schedule_duration = value
                                self.schedule_duration.value_namespace = name_space
                                self.schedule_duration.value_namespace_prefix = name_space_prefix
                            if(value_path == "schedule-interval"):
                                self.schedule_interval = value
                                self.schedule_interval.value_namespace = name_space
                                self.schedule_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time"):
                                self.start_time = value
                                self.start_time.value_namespace = name_space
                                self.start_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time-configured"):
                                self.start_time_configured = value
                                self.start_time_configured.value_namespace = name_space
                                self.start_time_configured.value_namespace_prefix = name_space_prefix


                    class OperationMetric(Entity):
                        """
                        Metrics gathered for the operation
                        
                        .. attribute:: bucket
                        
                        	Buckets stored for the metric
                        	**type**\: list of    :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket>`
                        
                        .. attribute:: config
                        
                        	Configuration of the metric
                        	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric, self).__init__()

                            self.yang_name = "operation-metric"
                            self.yang_parent_name = "statistics-on-demand-historical"

                            self.config = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.bucket = YList(self)

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
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric, self).__setattr__(name, value)


                        class Config(Entity):
                            """
                            Configuration of the metric
                            
                            .. attribute:: bins_count
                            
                            	Total number of bins into which to aggregate. 0 if no aggregation
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bins_width
                            
                            	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bucket_size
                            
                            	Size of buckets into which measurements are collected
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: bucket_size_unit
                            
                            	Whether bucket size is 'per\-probe' or 'probes'
                            	**type**\:   :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:   :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "operation-metric"

                                self.bins_count = YLeaf(YType.uint16, "bins-count")

                                self.bins_width = YLeaf(YType.uint16, "bins-width")

                                self.bucket_size = YLeaf(YType.uint8, "bucket-size")

                                self.bucket_size_unit = YLeaf(YType.enumeration, "bucket-size-unit")

                                self.buckets_archive = YLeaf(YType.uint32, "buckets-archive")

                                self.metric_type = YLeaf(YType.enumeration, "metric-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bins_count",
                                                "bins_width",
                                                "bucket_size",
                                                "bucket_size_unit",
                                                "buckets_archive",
                                                "metric_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bins_count.is_set or
                                    self.bins_width.is_set or
                                    self.bucket_size.is_set or
                                    self.bucket_size_unit.is_set or
                                    self.buckets_archive.is_set or
                                    self.metric_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bins_count.yfilter != YFilter.not_set or
                                    self.bins_width.yfilter != YFilter.not_set or
                                    self.bucket_size.yfilter != YFilter.not_set or
                                    self.bucket_size_unit.yfilter != YFilter.not_set or
                                    self.buckets_archive.yfilter != YFilter.not_set or
                                    self.metric_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "config" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bins_count.is_set or self.bins_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bins_count.get_name_leafdata())
                                if (self.bins_width.is_set or self.bins_width.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bins_width.get_name_leafdata())
                                if (self.bucket_size.is_set or self.bucket_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bucket_size.get_name_leafdata())
                                if (self.bucket_size_unit.is_set or self.bucket_size_unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bucket_size_unit.get_name_leafdata())
                                if (self.buckets_archive.is_set or self.buckets_archive.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.buckets_archive.get_name_leafdata())
                                if (self.metric_type.is_set or self.metric_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.metric_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bins-count" or name == "bins-width" or name == "bucket-size" or name == "bucket-size-unit" or name == "buckets-archive" or name == "metric-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bins-count"):
                                    self.bins_count = value
                                    self.bins_count.value_namespace = name_space
                                    self.bins_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "bins-width"):
                                    self.bins_width = value
                                    self.bins_width.value_namespace = name_space
                                    self.bins_width.value_namespace_prefix = name_space_prefix
                                if(value_path == "bucket-size"):
                                    self.bucket_size = value
                                    self.bucket_size.value_namespace = name_space
                                    self.bucket_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "bucket-size-unit"):
                                    self.bucket_size_unit = value
                                    self.bucket_size_unit.value_namespace = name_space
                                    self.bucket_size_unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "buckets-archive"):
                                    self.buckets_archive = value
                                    self.buckets_archive.value_namespace = name_space
                                    self.buckets_archive.value_namespace_prefix = name_space_prefix
                                if(value_path == "metric-type"):
                                    self.metric_type = value
                                    self.metric_type.value_namespace = name_space
                                    self.metric_type.value_namespace_prefix = name_space_prefix


                        class Bucket(Entity):
                            """
                            Buckets stored for the metric
                            
                            .. attribute:: average
                            
                            	Mean of the results in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: contents
                            
                            	The contents of the bucket; bins or samples
                            	**type**\:   :py:class:`Contents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents>`
                            
                            .. attribute:: corrupt
                            
                            	Number of corrupt packets in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_lost_count
                            
                            	The number of data packets lost across the bucket, used in the calculation of overall FLR
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_sent_count
                            
                            	The number of data packets sent across the bucket, used in the calculation of overall FLR
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplicates
                            
                            	Number of duplicate packets received in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duration
                            
                            	Length of time for which the bucket is being filled in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: lost
                            
                            	Number of lost packets in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: minimum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: out_of_order
                            
                            	Number of packets recieved out\-of\-order in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: overall_flr
                            
                            	Frame Loss Ratio across the whole bucket, in millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: percentage
                            
                            .. attribute:: premature_reason
                            
                            	If the probe ended prematurely, the error that caused a probe to end
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: premature_reason_string
                            
                            	Description of the error code that caused the probe to end prematurely. For informational purposes only
                            	**type**\:  str
                            
                            .. attribute:: result_count
                            
                            	The count of samples collected in the bucket
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sent
                            
                            	Number of packets sent in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: standard_deviation
                            
                            	Standard deviation of the results in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: start_at
                            
                            	Absolute time that the bucket started being filled at
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suspect_cleared_mid_bucket
                            
                            	Results suspect as bucket was cleared mid\-way through being filled
                            	**type**\:  bool
                            
                            .. attribute:: suspect_clock_drift
                            
                            	Results suspect as more than 10 seconds time drift detected
                            	**type**\:  bool
                            
                            .. attribute:: suspect_flr_low_packet_count
                            
                            	Results suspect as FLR calculated based on a low packet count
                            	**type**\:  bool
                            
                            .. attribute:: suspect_management_latency
                            
                            	Results suspect as processing of results has been delayed
                            	**type**\:  bool
                            
                            .. attribute:: suspect_memory_allocation_failed
                            
                            	Results suspect due to a memory allocation failure
                            	**type**\:  bool
                            
                            .. attribute:: suspect_misordering
                            
                            	Results suspect as misordering has been detected , affecting results
                            	**type**\:  bool
                            
                            .. attribute:: suspect_multiple_buckets
                            
                            	Results suspect as the probe has been configured across multiple buckets
                            	**type**\:  bool
                            
                            .. attribute:: suspect_premature_end
                            
                            	Results suspect due to a probe ending prematurely
                            	**type**\:  bool
                            
                            .. attribute:: suspect_probe_restarted
                            
                            	Results suspect as probe restarted mid\-way through the bucket
                            	**type**\:  bool
                            
                            .. attribute:: suspect_schedule_latency
                            
                            	Results suspect due to scheduling latency causing one or more packets to not be sent
                            	**type**\:  bool
                            
                            .. attribute:: suspect_send_fail
                            
                            	Results suspect due to failure to send one or more packets
                            	**type**\:  bool
                            
                            .. attribute:: suspect_start_mid_bucket
                            
                            	Results suspect due to a probe starting mid\-way through a bucket
                            	**type**\:  bool
                            
                            .. attribute:: time_of_maximum
                            
                            	Absolute time that the maximum value was recorded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_of_minimum
                            
                            	Absolute time that the minimum value was recorded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket, self).__init__()

                                self.yang_name = "bucket"
                                self.yang_parent_name = "operation-metric"

                                self.average = YLeaf(YType.int32, "average")

                                self.corrupt = YLeaf(YType.uint32, "corrupt")

                                self.data_lost_count = YLeaf(YType.uint32, "data-lost-count")

                                self.data_sent_count = YLeaf(YType.uint32, "data-sent-count")

                                self.duplicates = YLeaf(YType.uint32, "duplicates")

                                self.duration = YLeaf(YType.uint32, "duration")

                                self.lost = YLeaf(YType.uint32, "lost")

                                self.maximum = YLeaf(YType.int32, "maximum")

                                self.minimum = YLeaf(YType.int32, "minimum")

                                self.out_of_order = YLeaf(YType.uint32, "out-of-order")

                                self.overall_flr = YLeaf(YType.int32, "overall-flr")

                                self.premature_reason = YLeaf(YType.uint32, "premature-reason")

                                self.premature_reason_string = YLeaf(YType.str, "premature-reason-string")

                                self.result_count = YLeaf(YType.uint32, "result-count")

                                self.sent = YLeaf(YType.uint32, "sent")

                                self.standard_deviation = YLeaf(YType.int32, "standard-deviation")

                                self.start_at = YLeaf(YType.uint32, "start-at")

                                self.suspect_cleared_mid_bucket = YLeaf(YType.boolean, "suspect-cleared-mid-bucket")

                                self.suspect_clock_drift = YLeaf(YType.boolean, "suspect-clock-drift")

                                self.suspect_flr_low_packet_count = YLeaf(YType.boolean, "suspect-flr-low-packet-count")

                                self.suspect_management_latency = YLeaf(YType.boolean, "suspect-management-latency")

                                self.suspect_memory_allocation_failed = YLeaf(YType.boolean, "suspect-memory-allocation-failed")

                                self.suspect_misordering = YLeaf(YType.boolean, "suspect-misordering")

                                self.suspect_multiple_buckets = YLeaf(YType.boolean, "suspect-multiple-buckets")

                                self.suspect_premature_end = YLeaf(YType.boolean, "suspect-premature-end")

                                self.suspect_probe_restarted = YLeaf(YType.boolean, "suspect-probe-restarted")

                                self.suspect_schedule_latency = YLeaf(YType.boolean, "suspect-schedule-latency")

                                self.suspect_send_fail = YLeaf(YType.boolean, "suspect-send-fail")

                                self.suspect_start_mid_bucket = YLeaf(YType.boolean, "suspect-start-mid-bucket")

                                self.time_of_maximum = YLeaf(YType.uint32, "time-of-maximum")

                                self.time_of_minimum = YLeaf(YType.uint32, "time-of-minimum")

                                self.contents = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self._children_name_map["contents"] = "contents"
                                self._children_yang_names.add("contents")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("average",
                                                "corrupt",
                                                "data_lost_count",
                                                "data_sent_count",
                                                "duplicates",
                                                "duration",
                                                "lost",
                                                "maximum",
                                                "minimum",
                                                "out_of_order",
                                                "overall_flr",
                                                "premature_reason",
                                                "premature_reason_string",
                                                "result_count",
                                                "sent",
                                                "standard_deviation",
                                                "start_at",
                                                "suspect_cleared_mid_bucket",
                                                "suspect_clock_drift",
                                                "suspect_flr_low_packet_count",
                                                "suspect_management_latency",
                                                "suspect_memory_allocation_failed",
                                                "suspect_misordering",
                                                "suspect_multiple_buckets",
                                                "suspect_premature_end",
                                                "suspect_probe_restarted",
                                                "suspect_schedule_latency",
                                                "suspect_send_fail",
                                                "suspect_start_mid_bucket",
                                                "time_of_maximum",
                                                "time_of_minimum") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket, self).__setattr__(name, value)


                            class Contents(Entity):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:   :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:   :py:class:`SlaOperBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucket>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:   :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents, self).__init__()

                                    self.yang_name = "contents"
                                    self.yang_parent_name = "bucket"

                                    self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self._children_name_map["aggregated"] = "aggregated"
                                    self._children_yang_names.add("aggregated")

                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self
                                    self._children_name_map["unaggregated"] = "unaggregated"
                                    self._children_yang_names.add("unaggregated")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bucket_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents, self).__setattr__(name, value)


                                class Aggregated(Entity):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated, self).__init__()

                                        self.yang_name = "aggregated"
                                        self.yang_parent_name = "contents"

                                        self.bins = YList(self)

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
                                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated, self).__setattr__(name, value)


                                    class Bins(Entity):
                                        """
                                        The bins of an SLA metric bucket
                                        
                                        .. attribute:: count
                                        
                                        	The total number of results in the bin
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lower_bound
                                        
                                        	Lower bound (inclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: lower_bound_tenths
                                        
                                        	Lower bound (inclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: sum
                                        
                                        	The sum of the results in the bin, in microseconds or millionths of a percent
                                        	**type**\:  int
                                        
                                        	**range:** \-9223372036854775808..9223372036854775807
                                        
                                        .. attribute:: upper_bound
                                        
                                        	Upper bound (exclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: upper_bound_tenths
                                        
                                        	Upper bound (exclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__init__()

                                            self.yang_name = "bins"
                                            self.yang_parent_name = "aggregated"

                                            self.count = YLeaf(YType.uint32, "count")

                                            self.lower_bound = YLeaf(YType.int32, "lower-bound")

                                            self.lower_bound_tenths = YLeaf(YType.int32, "lower-bound-tenths")

                                            self.sum = YLeaf(YType.int64, "sum")

                                            self.upper_bound = YLeaf(YType.int32, "upper-bound")

                                            self.upper_bound_tenths = YLeaf(YType.int32, "upper-bound-tenths")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("count",
                                                            "lower_bound",
                                                            "lower_bound_tenths",
                                                            "sum",
                                                            "upper_bound",
                                                            "upper_bound_tenths") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.count.is_set or
                                                self.lower_bound.is_set or
                                                self.lower_bound_tenths.is_set or
                                                self.sum.is_set or
                                                self.upper_bound.is_set or
                                                self.upper_bound_tenths.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.count.yfilter != YFilter.not_set or
                                                self.lower_bound.yfilter != YFilter.not_set or
                                                self.lower_bound_tenths.yfilter != YFilter.not_set or
                                                self.sum.yfilter != YFilter.not_set or
                                                self.upper_bound.yfilter != YFilter.not_set or
                                                self.upper_bound_tenths.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "bins" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/contents/aggregated/%s" % self.get_segment_path()
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.count.get_name_leafdata())
                                            if (self.lower_bound.is_set or self.lower_bound.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.lower_bound.get_name_leafdata())
                                            if (self.lower_bound_tenths.is_set or self.lower_bound_tenths.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.lower_bound_tenths.get_name_leafdata())
                                            if (self.sum.is_set or self.sum.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sum.get_name_leafdata())
                                            if (self.upper_bound.is_set or self.upper_bound.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.upper_bound.get_name_leafdata())
                                            if (self.upper_bound_tenths.is_set or self.upper_bound_tenths.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.upper_bound_tenths.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "count" or name == "lower-bound" or name == "lower-bound-tenths" or name == "sum" or name == "upper-bound" or name == "upper-bound-tenths"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "count"):
                                                self.count = value
                                                self.count.value_namespace = name_space
                                                self.count.value_namespace_prefix = name_space_prefix
                                            if(value_path == "lower-bound"):
                                                self.lower_bound = value
                                                self.lower_bound.value_namespace = name_space
                                                self.lower_bound.value_namespace_prefix = name_space_prefix
                                            if(value_path == "lower-bound-tenths"):
                                                self.lower_bound_tenths = value
                                                self.lower_bound_tenths.value_namespace = name_space
                                                self.lower_bound_tenths.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sum"):
                                                self.sum = value
                                                self.sum.value_namespace = name_space
                                                self.sum.value_namespace_prefix = name_space_prefix
                                            if(value_path == "upper-bound"):
                                                self.upper_bound = value
                                                self.upper_bound.value_namespace = name_space
                                                self.upper_bound.value_namespace_prefix = name_space_prefix
                                            if(value_path == "upper-bound-tenths"):
                                                self.upper_bound_tenths = value
                                                self.upper_bound_tenths.value_namespace = name_space
                                                self.upper_bound_tenths.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.bins:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.bins:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "aggregated" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/contents/%s" % self.get_segment_path()
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "bins"):
                                            for c in self.bins:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.bins.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "bins"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class Unaggregated(Entity):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated, self).__init__()

                                        self.yang_name = "unaggregated"
                                        self.yang_parent_name = "contents"

                                        self.sample = YList(self)

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
                                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated, self).__setattr__(name, value)


                                    class Sample(Entity):
                                        """
                                        The samples of an SLA metric bucket
                                        
                                        .. attribute:: corrupt
                                        
                                        	Whether the sample packet was corrupt
                                        	**type**\:  bool
                                        
                                        .. attribute:: frames_lost
                                        
                                        	For FLR measurements, the number of frames lost, if available
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: frames_sent
                                        
                                        	For FLR measurements, the number of frames sent, if available
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: no_data_packets
                                        
                                        	Whether a measurement could not be made because no data packets were sent in the sample period. Only applicable for LMM measurements
                                        	**type**\:  bool
                                        
                                        .. attribute:: out_of_order
                                        
                                        	Whether the sample packet was received out\-of\-order
                                        	**type**\:  bool
                                        
                                        .. attribute:: result
                                        
                                        	The result (in microseconds or millionths of a percent) of the sample, if available
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: sent
                                        
                                        	Whether the sample packet was sucessfully sent
                                        	**type**\:  bool
                                        
                                        .. attribute:: sent_at
                                        
                                        	The time (in milliseconds relative to the start time of the bucket) that the sample was sent at
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: timed_out
                                        
                                        	Whether the sample packet timed out
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__init__()

                                            self.yang_name = "sample"
                                            self.yang_parent_name = "unaggregated"

                                            self.corrupt = YLeaf(YType.boolean, "corrupt")

                                            self.frames_lost = YLeaf(YType.uint32, "frames-lost")

                                            self.frames_sent = YLeaf(YType.uint32, "frames-sent")

                                            self.no_data_packets = YLeaf(YType.boolean, "no-data-packets")

                                            self.out_of_order = YLeaf(YType.boolean, "out-of-order")

                                            self.result = YLeaf(YType.int32, "result")

                                            self.sent = YLeaf(YType.boolean, "sent")

                                            self.sent_at = YLeaf(YType.uint32, "sent-at")

                                            self.timed_out = YLeaf(YType.boolean, "timed-out")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("corrupt",
                                                            "frames_lost",
                                                            "frames_sent",
                                                            "no_data_packets",
                                                            "out_of_order",
                                                            "result",
                                                            "sent",
                                                            "sent_at",
                                                            "timed_out") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.corrupt.is_set or
                                                self.frames_lost.is_set or
                                                self.frames_sent.is_set or
                                                self.no_data_packets.is_set or
                                                self.out_of_order.is_set or
                                                self.result.is_set or
                                                self.sent.is_set or
                                                self.sent_at.is_set or
                                                self.timed_out.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.corrupt.yfilter != YFilter.not_set or
                                                self.frames_lost.yfilter != YFilter.not_set or
                                                self.frames_sent.yfilter != YFilter.not_set or
                                                self.no_data_packets.yfilter != YFilter.not_set or
                                                self.out_of_order.yfilter != YFilter.not_set or
                                                self.result.yfilter != YFilter.not_set or
                                                self.sent.yfilter != YFilter.not_set or
                                                self.sent_at.yfilter != YFilter.not_set or
                                                self.timed_out.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "sample" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/contents/unaggregated/%s" % self.get_segment_path()
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.corrupt.is_set or self.corrupt.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.corrupt.get_name_leafdata())
                                            if (self.frames_lost.is_set or self.frames_lost.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.frames_lost.get_name_leafdata())
                                            if (self.frames_sent.is_set or self.frames_sent.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.frames_sent.get_name_leafdata())
                                            if (self.no_data_packets.is_set or self.no_data_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.no_data_packets.get_name_leafdata())
                                            if (self.out_of_order.is_set or self.out_of_order.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.out_of_order.get_name_leafdata())
                                            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.result.get_name_leafdata())
                                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sent.get_name_leafdata())
                                            if (self.sent_at.is_set or self.sent_at.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sent_at.get_name_leafdata())
                                            if (self.timed_out.is_set or self.timed_out.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.timed_out.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "corrupt" or name == "frames-lost" or name == "frames-sent" or name == "no-data-packets" or name == "out-of-order" or name == "result" or name == "sent" or name == "sent-at" or name == "timed-out"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "corrupt"):
                                                self.corrupt = value
                                                self.corrupt.value_namespace = name_space
                                                self.corrupt.value_namespace_prefix = name_space_prefix
                                            if(value_path == "frames-lost"):
                                                self.frames_lost = value
                                                self.frames_lost.value_namespace = name_space
                                                self.frames_lost.value_namespace_prefix = name_space_prefix
                                            if(value_path == "frames-sent"):
                                                self.frames_sent = value
                                                self.frames_sent.value_namespace = name_space
                                                self.frames_sent.value_namespace_prefix = name_space_prefix
                                            if(value_path == "no-data-packets"):
                                                self.no_data_packets = value
                                                self.no_data_packets.value_namespace = name_space
                                                self.no_data_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "out-of-order"):
                                                self.out_of_order = value
                                                self.out_of_order.value_namespace = name_space
                                                self.out_of_order.value_namespace_prefix = name_space_prefix
                                            if(value_path == "result"):
                                                self.result = value
                                                self.result.value_namespace = name_space
                                                self.result.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sent"):
                                                self.sent = value
                                                self.sent.value_namespace = name_space
                                                self.sent.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sent-at"):
                                                self.sent_at = value
                                                self.sent_at.value_namespace = name_space
                                                self.sent_at.value_namespace_prefix = name_space_prefix
                                            if(value_path == "timed-out"):
                                                self.timed_out = value
                                                self.timed_out.value_namespace = name_space
                                                self.timed_out.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.sample:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.sample:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unaggregated" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/contents/%s" % self.get_segment_path()
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "sample"):
                                            for c in self.sample:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.sample.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "sample"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.bucket_type.is_set or
                                        (self.aggregated is not None and self.aggregated.has_data()) or
                                        (self.unaggregated is not None and self.unaggregated.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bucket_type.yfilter != YFilter.not_set or
                                        (self.aggregated is not None and self.aggregated.has_operation()) or
                                        (self.unaggregated is not None and self.unaggregated.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "contents" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/%s" % self.get_segment_path()
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bucket_type.is_set or self.bucket_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "aggregated"):
                                        if (self.aggregated is None):
                                            self.aggregated = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated()
                                            self.aggregated.parent = self
                                            self._children_name_map["aggregated"] = "aggregated"
                                        return self.aggregated

                                    if (child_yang_name == "unaggregated"):
                                        if (self.unaggregated is None):
                                            self.unaggregated = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated()
                                            self.unaggregated.parent = self
                                            self._children_name_map["unaggregated"] = "unaggregated"
                                        return self.unaggregated

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "aggregated" or name == "unaggregated" or name == "bucket-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bucket-type"):
                                        self.bucket_type = value
                                        self.bucket_type.value_namespace = name_space
                                        self.bucket_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.average.is_set or
                                    self.corrupt.is_set or
                                    self.data_lost_count.is_set or
                                    self.data_sent_count.is_set or
                                    self.duplicates.is_set or
                                    self.duration.is_set or
                                    self.lost.is_set or
                                    self.maximum.is_set or
                                    self.minimum.is_set or
                                    self.out_of_order.is_set or
                                    self.overall_flr.is_set or
                                    self.premature_reason.is_set or
                                    self.premature_reason_string.is_set or
                                    self.result_count.is_set or
                                    self.sent.is_set or
                                    self.standard_deviation.is_set or
                                    self.start_at.is_set or
                                    self.suspect_cleared_mid_bucket.is_set or
                                    self.suspect_clock_drift.is_set or
                                    self.suspect_flr_low_packet_count.is_set or
                                    self.suspect_management_latency.is_set or
                                    self.suspect_memory_allocation_failed.is_set or
                                    self.suspect_misordering.is_set or
                                    self.suspect_multiple_buckets.is_set or
                                    self.suspect_premature_end.is_set or
                                    self.suspect_probe_restarted.is_set or
                                    self.suspect_schedule_latency.is_set or
                                    self.suspect_send_fail.is_set or
                                    self.suspect_start_mid_bucket.is_set or
                                    self.time_of_maximum.is_set or
                                    self.time_of_minimum.is_set or
                                    (self.contents is not None and self.contents.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.average.yfilter != YFilter.not_set or
                                    self.corrupt.yfilter != YFilter.not_set or
                                    self.data_lost_count.yfilter != YFilter.not_set or
                                    self.data_sent_count.yfilter != YFilter.not_set or
                                    self.duplicates.yfilter != YFilter.not_set or
                                    self.duration.yfilter != YFilter.not_set or
                                    self.lost.yfilter != YFilter.not_set or
                                    self.maximum.yfilter != YFilter.not_set or
                                    self.minimum.yfilter != YFilter.not_set or
                                    self.out_of_order.yfilter != YFilter.not_set or
                                    self.overall_flr.yfilter != YFilter.not_set or
                                    self.premature_reason.yfilter != YFilter.not_set or
                                    self.premature_reason_string.yfilter != YFilter.not_set or
                                    self.result_count.yfilter != YFilter.not_set or
                                    self.sent.yfilter != YFilter.not_set or
                                    self.standard_deviation.yfilter != YFilter.not_set or
                                    self.start_at.yfilter != YFilter.not_set or
                                    self.suspect_cleared_mid_bucket.yfilter != YFilter.not_set or
                                    self.suspect_clock_drift.yfilter != YFilter.not_set or
                                    self.suspect_flr_low_packet_count.yfilter != YFilter.not_set or
                                    self.suspect_management_latency.yfilter != YFilter.not_set or
                                    self.suspect_memory_allocation_failed.yfilter != YFilter.not_set or
                                    self.suspect_misordering.yfilter != YFilter.not_set or
                                    self.suspect_multiple_buckets.yfilter != YFilter.not_set or
                                    self.suspect_premature_end.yfilter != YFilter.not_set or
                                    self.suspect_probe_restarted.yfilter != YFilter.not_set or
                                    self.suspect_schedule_latency.yfilter != YFilter.not_set or
                                    self.suspect_send_fail.yfilter != YFilter.not_set or
                                    self.suspect_start_mid_bucket.yfilter != YFilter.not_set or
                                    self.time_of_maximum.yfilter != YFilter.not_set or
                                    self.time_of_minimum.yfilter != YFilter.not_set or
                                    (self.contents is not None and self.contents.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bucket" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.average.is_set or self.average.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.average.get_name_leafdata())
                                if (self.corrupt.is_set or self.corrupt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.corrupt.get_name_leafdata())
                                if (self.data_lost_count.is_set or self.data_lost_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_lost_count.get_name_leafdata())
                                if (self.data_sent_count.is_set or self.data_sent_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_sent_count.get_name_leafdata())
                                if (self.duplicates.is_set or self.duplicates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duplicates.get_name_leafdata())
                                if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duration.get_name_leafdata())
                                if (self.lost.is_set or self.lost.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lost.get_name_leafdata())
                                if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.maximum.get_name_leafdata())
                                if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.minimum.get_name_leafdata())
                                if (self.out_of_order.is_set or self.out_of_order.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_of_order.get_name_leafdata())
                                if (self.overall_flr.is_set or self.overall_flr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.overall_flr.get_name_leafdata())
                                if (self.premature_reason.is_set or self.premature_reason.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.premature_reason.get_name_leafdata())
                                if (self.premature_reason_string.is_set or self.premature_reason_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.premature_reason_string.get_name_leafdata())
                                if (self.result_count.is_set or self.result_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.result_count.get_name_leafdata())
                                if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sent.get_name_leafdata())
                                if (self.standard_deviation.is_set or self.standard_deviation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.standard_deviation.get_name_leafdata())
                                if (self.start_at.is_set or self.start_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_at.get_name_leafdata())
                                if (self.suspect_cleared_mid_bucket.is_set or self.suspect_cleared_mid_bucket.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_cleared_mid_bucket.get_name_leafdata())
                                if (self.suspect_clock_drift.is_set or self.suspect_clock_drift.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_clock_drift.get_name_leafdata())
                                if (self.suspect_flr_low_packet_count.is_set or self.suspect_flr_low_packet_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_flr_low_packet_count.get_name_leafdata())
                                if (self.suspect_management_latency.is_set or self.suspect_management_latency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_management_latency.get_name_leafdata())
                                if (self.suspect_memory_allocation_failed.is_set or self.suspect_memory_allocation_failed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_memory_allocation_failed.get_name_leafdata())
                                if (self.suspect_misordering.is_set or self.suspect_misordering.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_misordering.get_name_leafdata())
                                if (self.suspect_multiple_buckets.is_set or self.suspect_multiple_buckets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_multiple_buckets.get_name_leafdata())
                                if (self.suspect_premature_end.is_set or self.suspect_premature_end.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_premature_end.get_name_leafdata())
                                if (self.suspect_probe_restarted.is_set or self.suspect_probe_restarted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_probe_restarted.get_name_leafdata())
                                if (self.suspect_schedule_latency.is_set or self.suspect_schedule_latency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_schedule_latency.get_name_leafdata())
                                if (self.suspect_send_fail.is_set or self.suspect_send_fail.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_send_fail.get_name_leafdata())
                                if (self.suspect_start_mid_bucket.is_set or self.suspect_start_mid_bucket.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_start_mid_bucket.get_name_leafdata())
                                if (self.time_of_maximum.is_set or self.time_of_maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_of_maximum.get_name_leafdata())
                                if (self.time_of_minimum.is_set or self.time_of_minimum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_of_minimum.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "contents"):
                                    if (self.contents is None):
                                        self.contents = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents()
                                        self.contents.parent = self
                                        self._children_name_map["contents"] = "contents"
                                    return self.contents

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "contents" or name == "average" or name == "corrupt" or name == "data-lost-count" or name == "data-sent-count" or name == "duplicates" or name == "duration" or name == "lost" or name == "maximum" or name == "minimum" or name == "out-of-order" or name == "overall-flr" or name == "premature-reason" or name == "premature-reason-string" or name == "result-count" or name == "sent" or name == "standard-deviation" or name == "start-at" or name == "suspect-cleared-mid-bucket" or name == "suspect-clock-drift" or name == "suspect-flr-low-packet-count" or name == "suspect-management-latency" or name == "suspect-memory-allocation-failed" or name == "suspect-misordering" or name == "suspect-multiple-buckets" or name == "suspect-premature-end" or name == "suspect-probe-restarted" or name == "suspect-schedule-latency" or name == "suspect-send-fail" or name == "suspect-start-mid-bucket" or name == "time-of-maximum" or name == "time-of-minimum"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "average"):
                                    self.average = value
                                    self.average.value_namespace = name_space
                                    self.average.value_namespace_prefix = name_space_prefix
                                if(value_path == "corrupt"):
                                    self.corrupt = value
                                    self.corrupt.value_namespace = name_space
                                    self.corrupt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-lost-count"):
                                    self.data_lost_count = value
                                    self.data_lost_count.value_namespace = name_space
                                    self.data_lost_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-sent-count"):
                                    self.data_sent_count = value
                                    self.data_sent_count.value_namespace = name_space
                                    self.data_sent_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "duplicates"):
                                    self.duplicates = value
                                    self.duplicates.value_namespace = name_space
                                    self.duplicates.value_namespace_prefix = name_space_prefix
                                if(value_path == "duration"):
                                    self.duration = value
                                    self.duration.value_namespace = name_space
                                    self.duration.value_namespace_prefix = name_space_prefix
                                if(value_path == "lost"):
                                    self.lost = value
                                    self.lost.value_namespace = name_space
                                    self.lost.value_namespace_prefix = name_space_prefix
                                if(value_path == "maximum"):
                                    self.maximum = value
                                    self.maximum.value_namespace = name_space
                                    self.maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "minimum"):
                                    self.minimum = value
                                    self.minimum.value_namespace = name_space
                                    self.minimum.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-of-order"):
                                    self.out_of_order = value
                                    self.out_of_order.value_namespace = name_space
                                    self.out_of_order.value_namespace_prefix = name_space_prefix
                                if(value_path == "overall-flr"):
                                    self.overall_flr = value
                                    self.overall_flr.value_namespace = name_space
                                    self.overall_flr.value_namespace_prefix = name_space_prefix
                                if(value_path == "premature-reason"):
                                    self.premature_reason = value
                                    self.premature_reason.value_namespace = name_space
                                    self.premature_reason.value_namespace_prefix = name_space_prefix
                                if(value_path == "premature-reason-string"):
                                    self.premature_reason_string = value
                                    self.premature_reason_string.value_namespace = name_space
                                    self.premature_reason_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "result-count"):
                                    self.result_count = value
                                    self.result_count.value_namespace = name_space
                                    self.result_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "sent"):
                                    self.sent = value
                                    self.sent.value_namespace = name_space
                                    self.sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "standard-deviation"):
                                    self.standard_deviation = value
                                    self.standard_deviation.value_namespace = name_space
                                    self.standard_deviation.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-at"):
                                    self.start_at = value
                                    self.start_at.value_namespace = name_space
                                    self.start_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-cleared-mid-bucket"):
                                    self.suspect_cleared_mid_bucket = value
                                    self.suspect_cleared_mid_bucket.value_namespace = name_space
                                    self.suspect_cleared_mid_bucket.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-clock-drift"):
                                    self.suspect_clock_drift = value
                                    self.suspect_clock_drift.value_namespace = name_space
                                    self.suspect_clock_drift.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-flr-low-packet-count"):
                                    self.suspect_flr_low_packet_count = value
                                    self.suspect_flr_low_packet_count.value_namespace = name_space
                                    self.suspect_flr_low_packet_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-management-latency"):
                                    self.suspect_management_latency = value
                                    self.suspect_management_latency.value_namespace = name_space
                                    self.suspect_management_latency.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-memory-allocation-failed"):
                                    self.suspect_memory_allocation_failed = value
                                    self.suspect_memory_allocation_failed.value_namespace = name_space
                                    self.suspect_memory_allocation_failed.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-misordering"):
                                    self.suspect_misordering = value
                                    self.suspect_misordering.value_namespace = name_space
                                    self.suspect_misordering.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-multiple-buckets"):
                                    self.suspect_multiple_buckets = value
                                    self.suspect_multiple_buckets.value_namespace = name_space
                                    self.suspect_multiple_buckets.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-premature-end"):
                                    self.suspect_premature_end = value
                                    self.suspect_premature_end.value_namespace = name_space
                                    self.suspect_premature_end.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-probe-restarted"):
                                    self.suspect_probe_restarted = value
                                    self.suspect_probe_restarted.value_namespace = name_space
                                    self.suspect_probe_restarted.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-schedule-latency"):
                                    self.suspect_schedule_latency = value
                                    self.suspect_schedule_latency.value_namespace = name_space
                                    self.suspect_schedule_latency.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-send-fail"):
                                    self.suspect_send_fail = value
                                    self.suspect_send_fail.value_namespace = name_space
                                    self.suspect_send_fail.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-start-mid-bucket"):
                                    self.suspect_start_mid_bucket = value
                                    self.suspect_start_mid_bucket.value_namespace = name_space
                                    self.suspect_start_mid_bucket.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-of-maximum"):
                                    self.time_of_maximum = value
                                    self.time_of_maximum.value_namespace = name_space
                                    self.time_of_maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-of-minimum"):
                                    self.time_of_minimum = value
                                    self.time_of_minimum.value_namespace = name_space
                                    self.time_of_minimum.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.bucket:
                                if (c.has_data()):
                                    return True
                            return (self.config is not None and self.config.has_data())

                        def has_operation(self):
                            for c in self.bucket:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operation-metric" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "bucket"):
                                for c in self.bucket:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.bucket.append(c)
                                return c

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bucket" or name == "config"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        for c in self.operation_metric:
                            if (c.has_data()):
                                return True
                        return (
                            self.display_long.is_set or
                            self.display_short.is_set or
                            self.domain_name.is_set or
                            self.flr_calculation_interval.is_set or
                            self.interface_name.is_set or
                            self.mac_address.is_set or
                            self.mep_id.is_set or
                            self.operation_id.is_set or
                            self.probe_type.is_set or
                            (self.operation_schedule is not None and self.operation_schedule.has_data()) or
                            (self.specific_options is not None and self.specific_options.has_data()))

                    def has_operation(self):
                        for c in self.operation_metric:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.display_long.yfilter != YFilter.not_set or
                            self.display_short.yfilter != YFilter.not_set or
                            self.domain_name.yfilter != YFilter.not_set or
                            self.flr_calculation_interval.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.mep_id.yfilter != YFilter.not_set or
                            self.operation_id.yfilter != YFilter.not_set or
                            self.probe_type.yfilter != YFilter.not_set or
                            (self.operation_schedule is not None and self.operation_schedule.has_operation()) or
                            (self.specific_options is not None and self.specific_options.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics-on-demand-historical" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.display_long.is_set or self.display_long.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_long.get_name_leafdata())
                        if (self.display_short.is_set or self.display_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_short.get_name_leafdata())
                        if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_name.get_name_leafdata())
                        if (self.flr_calculation_interval.is_set or self.flr_calculation_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flr_calculation_interval.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.mep_id.is_set or self.mep_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mep_id.get_name_leafdata())
                        if (self.operation_id.is_set or self.operation_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.operation_id.get_name_leafdata())
                        if (self.probe_type.is_set or self.probe_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.probe_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "operation-metric"):
                            for c in self.operation_metric:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.operation_metric.append(c)
                            return c

                        if (child_yang_name == "operation-schedule"):
                            if (self.operation_schedule is None):
                                self.operation_schedule = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule()
                                self.operation_schedule.parent = self
                                self._children_name_map["operation_schedule"] = "operation-schedule"
                            return self.operation_schedule

                        if (child_yang_name == "specific-options"):
                            if (self.specific_options is None):
                                self.specific_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions()
                                self.specific_options.parent = self
                                self._children_name_map["specific_options"] = "specific-options"
                            return self.specific_options

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "operation-metric" or name == "operation-schedule" or name == "specific-options" or name == "display-long" or name == "display-short" or name == "domain-name" or name == "flr-calculation-interval" or name == "interface-name" or name == "mac-address" or name == "mep-id" or name == "operation-id" or name == "probe-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "display-long"):
                            self.display_long = value
                            self.display_long.value_namespace = name_space
                            self.display_long.value_namespace_prefix = name_space_prefix
                        if(value_path == "display-short"):
                            self.display_short = value
                            self.display_short.value_namespace = name_space
                            self.display_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-name"):
                            self.domain_name = value
                            self.domain_name.value_namespace = name_space
                            self.domain_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "flr-calculation-interval"):
                            self.flr_calculation_interval = value
                            self.flr_calculation_interval.value_namespace = name_space
                            self.flr_calculation_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mep-id"):
                            self.mep_id = value
                            self.mep_id.value_namespace = name_space
                            self.mep_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "operation-id"):
                            self.operation_id = value
                            self.operation_id.value_namespace = name_space
                            self.operation_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "probe-type"):
                            self.probe_type = value
                            self.probe_type.value_namespace = name_space
                            self.probe_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.statistics_on_demand_historical:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.statistics_on_demand_historical:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics-on-demand-historicals" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "statistics-on-demand-historical"):
                        for c in self.statistics_on_demand_historical:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.statistics_on_demand_historical.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statistics-on-demand-historical"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ConfigErrors(Entity):
                """
                Table of SLA configuration errors on configured
                operations
                
                .. attribute:: config_error
                
                	SLA operation to get configuration errors data for
                	**type**\: list of    :py:class:`ConfigError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.ConfigErrors.ConfigError>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.ConfigErrors, self).__init__()

                    self.yang_name = "config-errors"
                    self.yang_parent_name = "ethernet"

                    self.config_error = YList(self)

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
                                super(Sla.Protocols.Ethernet.ConfigErrors, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sla.Protocols.Ethernet.ConfigErrors, self).__setattr__(name, value)


                class ConfigError(Entity):
                    """
                    SLA operation to get configuration errors data
                    for
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: error_string
                    
                    	Displays other issues not indicated from the flags above, for example MIB incompatibility issues
                    	**type**\:  list of str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191
                    	**type**\:  int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: min_packet_interval_inconsistent
                    
                    	Is the profile configured to send packets more frequently than the protocol allows?
                    	**type**\:  bool
                    
                    .. attribute:: ow_delay_ds_inconsistent
                    
                    	Is the profile configured to collect OW Delay (DS) but the packet type doesn't support it?
                    	**type**\:  bool
                    
                    .. attribute:: ow_delay_sd_inconsistent
                    
                    	Is the profile configured to collect OW Delay (SD) but the packet type doesn't support it?
                    	**type**\:  bool
                    
                    .. attribute:: ow_jitter_ds_inconsistent
                    
                    	Is the profile configured to collect OW Delay (DS) but the packet type doesn't support it?
                    	**type**\:  bool
                    
                    .. attribute:: ow_jitter_sd_inconsistent
                    
                    	Is the profile configured to collect OW Jitter (SD) but the packet type doesn't support it?
                    	**type**\:  bool
                    
                    .. attribute:: ow_loss_ds_inconsistent
                    
                    	Is the profile configured to collect OW Frame Loss (DS) but the packet type doesn't support it ?
                    	**type**\:  bool
                    
                    .. attribute:: ow_loss_sd_inconsistent
                    
                    	Is the profile configured to collect OW Frame Loss (SD) but the packet type doesn't support it ?
                    	**type**\:  bool
                    
                    .. attribute:: packet_pad_inconsistent
                    
                    	Is the profile configured to pad packets but the packet type doesn't support it?
                    	**type**\:  bool
                    
                    .. attribute:: packet_rand_pad_inconsistent
                    
                    	Is the profile configured to pad packets with a pseudo\-random string but the packet type doesn't support it?
                    	**type**\:  bool
                    
                    .. attribute:: packet_type_inconsistent
                    
                    	Is the profile configured to use a packet type that isn't supported by any protocols?
                    	**type**\:  bool
                    
                    .. attribute:: priority_inconsistent
                    
                    	Is the profile configured to use a packet priority scheme that the protocol does not support?
                    	**type**\:  bool
                    
                    .. attribute:: probe_too_big
                    
                    	The profile is configured to use a packet type which does not allow more than 72000 packets per probe and greater than 72000 packets per probe have been configured
                    	**type**\:  bool
                    
                    .. attribute:: profile_doesnt_exist
                    
                    	Is the operation configured to use a profile that is not currently defined for the protocol?
                    	**type**\:  bool
                    
                    .. attribute:: profile_name
                    
                    	Profile Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: profile_name_xr
                    
                    	The name of the operation profile
                    	**type**\:  str
                    
                    .. attribute:: rt_delay_inconsistent
                    
                    	Is the profile configured to collect RT Delay but the packet type doesn't support it?
                    	**type**\:  bool
                    
                    .. attribute:: rt_jitter_inconsistent
                    
                    	Is the profile configured to collect RT Jitter but the packet type doesn't support it?
                    	**type**\:  bool
                    
                    .. attribute:: synthetic_loss_not_supported
                    
                    	The profile is configured to use a packet type which doesn't support synthetic loss measurement and the number of packets per FLR calculation has been configured
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.ConfigErrors.ConfigError, self).__init__()

                        self.yang_name = "config-error"
                        self.yang_parent_name = "config-errors"

                        self.display_short = YLeaf(YType.str, "display-short")

                        self.domain_name = YLeaf(YType.str, "domain-name")

                        self.error_string = YLeafList(YType.str, "error-string")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.mep_id = YLeaf(YType.uint32, "mep-id")

                        self.min_packet_interval_inconsistent = YLeaf(YType.boolean, "min-packet-interval-inconsistent")

                        self.ow_delay_ds_inconsistent = YLeaf(YType.boolean, "ow-delay-ds-inconsistent")

                        self.ow_delay_sd_inconsistent = YLeaf(YType.boolean, "ow-delay-sd-inconsistent")

                        self.ow_jitter_ds_inconsistent = YLeaf(YType.boolean, "ow-jitter-ds-inconsistent")

                        self.ow_jitter_sd_inconsistent = YLeaf(YType.boolean, "ow-jitter-sd-inconsistent")

                        self.ow_loss_ds_inconsistent = YLeaf(YType.boolean, "ow-loss-ds-inconsistent")

                        self.ow_loss_sd_inconsistent = YLeaf(YType.boolean, "ow-loss-sd-inconsistent")

                        self.packet_pad_inconsistent = YLeaf(YType.boolean, "packet-pad-inconsistent")

                        self.packet_rand_pad_inconsistent = YLeaf(YType.boolean, "packet-rand-pad-inconsistent")

                        self.packet_type_inconsistent = YLeaf(YType.boolean, "packet-type-inconsistent")

                        self.priority_inconsistent = YLeaf(YType.boolean, "priority-inconsistent")

                        self.probe_too_big = YLeaf(YType.boolean, "probe-too-big")

                        self.profile_doesnt_exist = YLeaf(YType.boolean, "profile-doesnt-exist")

                        self.profile_name = YLeaf(YType.str, "profile-name")

                        self.profile_name_xr = YLeaf(YType.str, "profile-name-xr")

                        self.rt_delay_inconsistent = YLeaf(YType.boolean, "rt-delay-inconsistent")

                        self.rt_jitter_inconsistent = YLeaf(YType.boolean, "rt-jitter-inconsistent")

                        self.synthetic_loss_not_supported = YLeaf(YType.boolean, "synthetic-loss-not-supported")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("display_short",
                                        "domain_name",
                                        "error_string",
                                        "interface_name",
                                        "mac_address",
                                        "mep_id",
                                        "min_packet_interval_inconsistent",
                                        "ow_delay_ds_inconsistent",
                                        "ow_delay_sd_inconsistent",
                                        "ow_jitter_ds_inconsistent",
                                        "ow_jitter_sd_inconsistent",
                                        "ow_loss_ds_inconsistent",
                                        "ow_loss_sd_inconsistent",
                                        "packet_pad_inconsistent",
                                        "packet_rand_pad_inconsistent",
                                        "packet_type_inconsistent",
                                        "priority_inconsistent",
                                        "probe_too_big",
                                        "profile_doesnt_exist",
                                        "profile_name",
                                        "profile_name_xr",
                                        "rt_delay_inconsistent",
                                        "rt_jitter_inconsistent",
                                        "synthetic_loss_not_supported") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sla.Protocols.Ethernet.ConfigErrors.ConfigError, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sla.Protocols.Ethernet.ConfigErrors.ConfigError, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.error_string.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.display_short.is_set or
                            self.domain_name.is_set or
                            self.interface_name.is_set or
                            self.mac_address.is_set or
                            self.mep_id.is_set or
                            self.min_packet_interval_inconsistent.is_set or
                            self.ow_delay_ds_inconsistent.is_set or
                            self.ow_delay_sd_inconsistent.is_set or
                            self.ow_jitter_ds_inconsistent.is_set or
                            self.ow_jitter_sd_inconsistent.is_set or
                            self.ow_loss_ds_inconsistent.is_set or
                            self.ow_loss_sd_inconsistent.is_set or
                            self.packet_pad_inconsistent.is_set or
                            self.packet_rand_pad_inconsistent.is_set or
                            self.packet_type_inconsistent.is_set or
                            self.priority_inconsistent.is_set or
                            self.probe_too_big.is_set or
                            self.profile_doesnt_exist.is_set or
                            self.profile_name.is_set or
                            self.profile_name_xr.is_set or
                            self.rt_delay_inconsistent.is_set or
                            self.rt_jitter_inconsistent.is_set or
                            self.synthetic_loss_not_supported.is_set)

                    def has_operation(self):
                        for leaf in self.error_string.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.display_short.yfilter != YFilter.not_set or
                            self.domain_name.yfilter != YFilter.not_set or
                            self.error_string.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.mep_id.yfilter != YFilter.not_set or
                            self.min_packet_interval_inconsistent.yfilter != YFilter.not_set or
                            self.ow_delay_ds_inconsistent.yfilter != YFilter.not_set or
                            self.ow_delay_sd_inconsistent.yfilter != YFilter.not_set or
                            self.ow_jitter_ds_inconsistent.yfilter != YFilter.not_set or
                            self.ow_jitter_sd_inconsistent.yfilter != YFilter.not_set or
                            self.ow_loss_ds_inconsistent.yfilter != YFilter.not_set or
                            self.ow_loss_sd_inconsistent.yfilter != YFilter.not_set or
                            self.packet_pad_inconsistent.yfilter != YFilter.not_set or
                            self.packet_rand_pad_inconsistent.yfilter != YFilter.not_set or
                            self.packet_type_inconsistent.yfilter != YFilter.not_set or
                            self.priority_inconsistent.yfilter != YFilter.not_set or
                            self.probe_too_big.yfilter != YFilter.not_set or
                            self.profile_doesnt_exist.yfilter != YFilter.not_set or
                            self.profile_name.yfilter != YFilter.not_set or
                            self.profile_name_xr.yfilter != YFilter.not_set or
                            self.rt_delay_inconsistent.yfilter != YFilter.not_set or
                            self.rt_jitter_inconsistent.yfilter != YFilter.not_set or
                            self.synthetic_loss_not_supported.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "config-error" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/config-errors/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.display_short.is_set or self.display_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_short.get_name_leafdata())
                        if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_name.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.mep_id.is_set or self.mep_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mep_id.get_name_leafdata())
                        if (self.min_packet_interval_inconsistent.is_set or self.min_packet_interval_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min_packet_interval_inconsistent.get_name_leafdata())
                        if (self.ow_delay_ds_inconsistent.is_set or self.ow_delay_ds_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ow_delay_ds_inconsistent.get_name_leafdata())
                        if (self.ow_delay_sd_inconsistent.is_set or self.ow_delay_sd_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ow_delay_sd_inconsistent.get_name_leafdata())
                        if (self.ow_jitter_ds_inconsistent.is_set or self.ow_jitter_ds_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ow_jitter_ds_inconsistent.get_name_leafdata())
                        if (self.ow_jitter_sd_inconsistent.is_set or self.ow_jitter_sd_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ow_jitter_sd_inconsistent.get_name_leafdata())
                        if (self.ow_loss_ds_inconsistent.is_set or self.ow_loss_ds_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ow_loss_ds_inconsistent.get_name_leafdata())
                        if (self.ow_loss_sd_inconsistent.is_set or self.ow_loss_sd_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ow_loss_sd_inconsistent.get_name_leafdata())
                        if (self.packet_pad_inconsistent.is_set or self.packet_pad_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packet_pad_inconsistent.get_name_leafdata())
                        if (self.packet_rand_pad_inconsistent.is_set or self.packet_rand_pad_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packet_rand_pad_inconsistent.get_name_leafdata())
                        if (self.packet_type_inconsistent.is_set or self.packet_type_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packet_type_inconsistent.get_name_leafdata())
                        if (self.priority_inconsistent.is_set or self.priority_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.priority_inconsistent.get_name_leafdata())
                        if (self.probe_too_big.is_set or self.probe_too_big.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.probe_too_big.get_name_leafdata())
                        if (self.profile_doesnt_exist.is_set or self.profile_doesnt_exist.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.profile_doesnt_exist.get_name_leafdata())
                        if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.profile_name.get_name_leafdata())
                        if (self.profile_name_xr.is_set or self.profile_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.profile_name_xr.get_name_leafdata())
                        if (self.rt_delay_inconsistent.is_set or self.rt_delay_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rt_delay_inconsistent.get_name_leafdata())
                        if (self.rt_jitter_inconsistent.is_set or self.rt_jitter_inconsistent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rt_jitter_inconsistent.get_name_leafdata())
                        if (self.synthetic_loss_not_supported.is_set or self.synthetic_loss_not_supported.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.synthetic_loss_not_supported.get_name_leafdata())

                        leaf_name_data.extend(self.error_string.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "display-short" or name == "domain-name" or name == "error-string" or name == "interface-name" or name == "mac-address" or name == "mep-id" or name == "min-packet-interval-inconsistent" or name == "ow-delay-ds-inconsistent" or name == "ow-delay-sd-inconsistent" or name == "ow-jitter-ds-inconsistent" or name == "ow-jitter-sd-inconsistent" or name == "ow-loss-ds-inconsistent" or name == "ow-loss-sd-inconsistent" or name == "packet-pad-inconsistent" or name == "packet-rand-pad-inconsistent" or name == "packet-type-inconsistent" or name == "priority-inconsistent" or name == "probe-too-big" or name == "profile-doesnt-exist" or name == "profile-name" or name == "profile-name-xr" or name == "rt-delay-inconsistent" or name == "rt-jitter-inconsistent" or name == "synthetic-loss-not-supported"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "display-short"):
                            self.display_short = value
                            self.display_short.value_namespace = name_space
                            self.display_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-name"):
                            self.domain_name = value
                            self.domain_name.value_namespace = name_space
                            self.domain_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "error-string"):
                            self.error_string.append(value)
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mep-id"):
                            self.mep_id = value
                            self.mep_id.value_namespace = name_space
                            self.mep_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "min-packet-interval-inconsistent"):
                            self.min_packet_interval_inconsistent = value
                            self.min_packet_interval_inconsistent.value_namespace = name_space
                            self.min_packet_interval_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "ow-delay-ds-inconsistent"):
                            self.ow_delay_ds_inconsistent = value
                            self.ow_delay_ds_inconsistent.value_namespace = name_space
                            self.ow_delay_ds_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "ow-delay-sd-inconsistent"):
                            self.ow_delay_sd_inconsistent = value
                            self.ow_delay_sd_inconsistent.value_namespace = name_space
                            self.ow_delay_sd_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "ow-jitter-ds-inconsistent"):
                            self.ow_jitter_ds_inconsistent = value
                            self.ow_jitter_ds_inconsistent.value_namespace = name_space
                            self.ow_jitter_ds_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "ow-jitter-sd-inconsistent"):
                            self.ow_jitter_sd_inconsistent = value
                            self.ow_jitter_sd_inconsistent.value_namespace = name_space
                            self.ow_jitter_sd_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "ow-loss-ds-inconsistent"):
                            self.ow_loss_ds_inconsistent = value
                            self.ow_loss_ds_inconsistent.value_namespace = name_space
                            self.ow_loss_ds_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "ow-loss-sd-inconsistent"):
                            self.ow_loss_sd_inconsistent = value
                            self.ow_loss_sd_inconsistent.value_namespace = name_space
                            self.ow_loss_sd_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "packet-pad-inconsistent"):
                            self.packet_pad_inconsistent = value
                            self.packet_pad_inconsistent.value_namespace = name_space
                            self.packet_pad_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "packet-rand-pad-inconsistent"):
                            self.packet_rand_pad_inconsistent = value
                            self.packet_rand_pad_inconsistent.value_namespace = name_space
                            self.packet_rand_pad_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "packet-type-inconsistent"):
                            self.packet_type_inconsistent = value
                            self.packet_type_inconsistent.value_namespace = name_space
                            self.packet_type_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "priority-inconsistent"):
                            self.priority_inconsistent = value
                            self.priority_inconsistent.value_namespace = name_space
                            self.priority_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "probe-too-big"):
                            self.probe_too_big = value
                            self.probe_too_big.value_namespace = name_space
                            self.probe_too_big.value_namespace_prefix = name_space_prefix
                        if(value_path == "profile-doesnt-exist"):
                            self.profile_doesnt_exist = value
                            self.profile_doesnt_exist.value_namespace = name_space
                            self.profile_doesnt_exist.value_namespace_prefix = name_space_prefix
                        if(value_path == "profile-name"):
                            self.profile_name = value
                            self.profile_name.value_namespace = name_space
                            self.profile_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "profile-name-xr"):
                            self.profile_name_xr = value
                            self.profile_name_xr.value_namespace = name_space
                            self.profile_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "rt-delay-inconsistent"):
                            self.rt_delay_inconsistent = value
                            self.rt_delay_inconsistent.value_namespace = name_space
                            self.rt_delay_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "rt-jitter-inconsistent"):
                            self.rt_jitter_inconsistent = value
                            self.rt_jitter_inconsistent.value_namespace = name_space
                            self.rt_jitter_inconsistent.value_namespace_prefix = name_space_prefix
                        if(value_path == "synthetic-loss-not-supported"):
                            self.synthetic_loss_not_supported = value
                            self.synthetic_loss_not_supported.value_namespace = name_space
                            self.synthetic_loss_not_supported.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.config_error:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.config_error:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "config-errors" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "config-error"):
                        for c in self.config_error:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sla.Protocols.Ethernet.ConfigErrors.ConfigError()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.config_error.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config-error"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class OnDemandOperations(Entity):
                """
                Table of SLA on\-demand operations
                
                .. attribute:: on_demand_operation
                
                	SLA on\-demand operation to get operation data for
                	**type**\: list of    :py:class:`OnDemandOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.OnDemandOperations, self).__init__()

                    self.yang_name = "on-demand-operations"
                    self.yang_parent_name = "ethernet"

                    self.on_demand_operation = YList(self)

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
                                super(Sla.Protocols.Ethernet.OnDemandOperations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sla.Protocols.Ethernet.OnDemandOperations, self).__setattr__(name, value)


                class OnDemandOperation(Entity):
                    """
                    SLA on\-demand operation to get operation data
                    for
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: last_run
                    
                    	Time that the last probe for the operation was run, NULL if never run
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\:  int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: operation_id
                    
                    	Operation ID
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: profile_options
                    
                    	Options that are only valid if the operation has a profile
                    	**type**\:   :py:class:`ProfileOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions>`
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:   :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation, self).__init__()

                        self.yang_name = "on-demand-operation"
                        self.yang_parent_name = "on-demand-operations"

                        self.display_long = YLeaf(YType.str, "display-long")

                        self.display_short = YLeaf(YType.str, "display-short")

                        self.domain_name = YLeaf(YType.str, "domain-name")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.last_run = YLeaf(YType.uint32, "last-run")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.mep_id = YLeaf(YType.uint32, "mep-id")

                        self.operation_id = YLeaf(YType.uint32, "operation-id")

                        self.profile_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions()
                        self.profile_options.parent = self
                        self._children_name_map["profile_options"] = "profile-options"
                        self._children_yang_names.add("profile-options")

                        self.specific_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"
                        self._children_yang_names.add("specific-options")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("display_long",
                                        "display_short",
                                        "domain_name",
                                        "interface_name",
                                        "last_run",
                                        "mac_address",
                                        "mep_id",
                                        "operation_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation, self).__setattr__(name, value)


                    class ProfileOptions(Entity):
                        """
                        Options that are only valid if the operation has
                        a profile
                        
                        .. attribute:: bursts_per_probe
                        
                        	Number of bursts sent per probe
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flr_calculation_interval
                        
                        	Interval between FLR calculations for SLM, in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: inter_burst_interval
                        
                        	Interval between bursts within a probe in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: inter_packet_interval
                        
                        	Interval between packets within a burst in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**units**\: millisecond
                        
                        .. attribute:: operation_metric
                        
                        	Array of the metrics that are measured by the operation
                        	**type**\: list of    :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric>`
                        
                        .. attribute:: operation_schedule
                        
                        	Operation schedule
                        	**type**\:   :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule>`
                        
                        .. attribute:: packet_padding
                        
                        	Configuration of the packet padding
                        	**type**\:   :py:class:`PacketPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding>`
                        
                        .. attribute:: packets_per_burst
                        
                        	Number of packets sent per burst
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: priority
                        
                        	Priority at which to send the packet, if configured
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority>`
                        
                        .. attribute:: probe_type
                        
                        	Type of probe used by the operation
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions, self).__init__()

                            self.yang_name = "profile-options"
                            self.yang_parent_name = "on-demand-operation"

                            self.bursts_per_probe = YLeaf(YType.uint32, "bursts-per-probe")

                            self.flr_calculation_interval = YLeaf(YType.uint32, "flr-calculation-interval")

                            self.inter_burst_interval = YLeaf(YType.uint32, "inter-burst-interval")

                            self.inter_packet_interval = YLeaf(YType.uint16, "inter-packet-interval")

                            self.packets_per_burst = YLeaf(YType.uint16, "packets-per-burst")

                            self.probe_type = YLeaf(YType.str, "probe-type")

                            self.operation_schedule = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule()
                            self.operation_schedule.parent = self
                            self._children_name_map["operation_schedule"] = "operation-schedule"
                            self._children_yang_names.add("operation-schedule")

                            self.packet_padding = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding()
                            self.packet_padding.parent = self
                            self._children_name_map["packet_padding"] = "packet-padding"
                            self._children_yang_names.add("packet-padding")

                            self.priority = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority()
                            self.priority.parent = self
                            self._children_name_map["priority"] = "priority"
                            self._children_yang_names.add("priority")

                            self.operation_metric = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bursts_per_probe",
                                            "flr_calculation_interval",
                                            "inter_burst_interval",
                                            "inter_packet_interval",
                                            "packets_per_burst",
                                            "probe_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions, self).__setattr__(name, value)


                        class PacketPadding(Entity):
                            """
                            Configuration of the packet padding
                            
                            .. attribute:: packet_pad_size
                            
                            	Size that packets are being padded to
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: test_pattern_pad_hex_string
                            
                            	Hex string that is used in the packet padding
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: test_pattern_pad_scheme
                            
                            	Test pattern scheme that is used in the packet padding
                            	**type**\:   :py:class:`SlaOperTestPatternScheme <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperTestPatternScheme>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding, self).__init__()

                                self.yang_name = "packet-padding"
                                self.yang_parent_name = "profile-options"

                                self.packet_pad_size = YLeaf(YType.uint16, "packet-pad-size")

                                self.test_pattern_pad_hex_string = YLeaf(YType.uint32, "test-pattern-pad-hex-string")

                                self.test_pattern_pad_scheme = YLeaf(YType.enumeration, "test-pattern-pad-scheme")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("packet_pad_size",
                                                "test_pattern_pad_hex_string",
                                                "test_pattern_pad_scheme") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.packet_pad_size.is_set or
                                    self.test_pattern_pad_hex_string.is_set or
                                    self.test_pattern_pad_scheme.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.packet_pad_size.yfilter != YFilter.not_set or
                                    self.test_pattern_pad_hex_string.yfilter != YFilter.not_set or
                                    self.test_pattern_pad_scheme.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-padding" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.packet_pad_size.is_set or self.packet_pad_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packet_pad_size.get_name_leafdata())
                                if (self.test_pattern_pad_hex_string.is_set or self.test_pattern_pad_hex_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.test_pattern_pad_hex_string.get_name_leafdata())
                                if (self.test_pattern_pad_scheme.is_set or self.test_pattern_pad_scheme.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.test_pattern_pad_scheme.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "packet-pad-size" or name == "test-pattern-pad-hex-string" or name == "test-pattern-pad-scheme"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "packet-pad-size"):
                                    self.packet_pad_size = value
                                    self.packet_pad_size.value_namespace = name_space
                                    self.packet_pad_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "test-pattern-pad-hex-string"):
                                    self.test_pattern_pad_hex_string = value
                                    self.test_pattern_pad_hex_string.value_namespace = name_space
                                    self.test_pattern_pad_hex_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "test-pattern-pad-scheme"):
                                    self.test_pattern_pad_scheme = value
                                    self.test_pattern_pad_scheme.value_namespace = name_space
                                    self.test_pattern_pad_scheme.value_namespace_prefix = name_space_prefix


                        class Priority(Entity):
                            """
                            Priority at which to send the packet, if
                            configured
                            
                            .. attribute:: cos
                            
                            	3\-bit COS priority value applied to packets
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: priority_type
                            
                            	PriorityType
                            	**type**\:   :py:class:`SlaOperPacketPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperPacketPriority>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "profile-options"

                                self.cos = YLeaf(YType.uint8, "cos")

                                self.priority_type = YLeaf(YType.enumeration, "priority-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("cos",
                                                "priority_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.cos.is_set or
                                    self.priority_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.cos.yfilter != YFilter.not_set or
                                    self.priority_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "priority" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cos.get_name_leafdata())
                                if (self.priority_type.is_set or self.priority_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "cos" or name == "priority-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "cos"):
                                    self.cos = value
                                    self.cos.value_namespace = name_space
                                    self.cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority-type"):
                                    self.priority_type = value
                                    self.priority_type.value_namespace = name_space
                                    self.priority_type.value_namespace_prefix = name_space_prefix


                        class OperationSchedule(Entity):
                            """
                            Operation schedule
                            
                            .. attribute:: schedule_duration
                            
                            	Duration of a probe for the operation in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: schedule_interval
                            
                            	Interval between the start times of consecutive probes,  in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: start_time
                            
                            	Start time of the first probe, in seconds since the Unix Epoch
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: start_time_configured
                            
                            	Whether or not the operation start time was explicitly configured
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule, self).__init__()

                                self.yang_name = "operation-schedule"
                                self.yang_parent_name = "profile-options"

                                self.schedule_duration = YLeaf(YType.uint32, "schedule-duration")

                                self.schedule_interval = YLeaf(YType.uint32, "schedule-interval")

                                self.start_time = YLeaf(YType.uint32, "start-time")

                                self.start_time_configured = YLeaf(YType.boolean, "start-time-configured")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("schedule_duration",
                                                "schedule_interval",
                                                "start_time",
                                                "start_time_configured") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.schedule_duration.is_set or
                                    self.schedule_interval.is_set or
                                    self.start_time.is_set or
                                    self.start_time_configured.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.schedule_duration.yfilter != YFilter.not_set or
                                    self.schedule_interval.yfilter != YFilter.not_set or
                                    self.start_time.yfilter != YFilter.not_set or
                                    self.start_time_configured.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operation-schedule" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.schedule_duration.is_set or self.schedule_duration.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.schedule_duration.get_name_leafdata())
                                if (self.schedule_interval.is_set or self.schedule_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.schedule_interval.get_name_leafdata())
                                if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_time.get_name_leafdata())
                                if (self.start_time_configured.is_set or self.start_time_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_time_configured.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "schedule-duration" or name == "schedule-interval" or name == "start-time" or name == "start-time-configured"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "schedule-duration"):
                                    self.schedule_duration = value
                                    self.schedule_duration.value_namespace = name_space
                                    self.schedule_duration.value_namespace_prefix = name_space_prefix
                                if(value_path == "schedule-interval"):
                                    self.schedule_interval = value
                                    self.schedule_interval.value_namespace = name_space
                                    self.schedule_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-time"):
                                    self.start_time = value
                                    self.start_time.value_namespace = name_space
                                    self.start_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-time-configured"):
                                    self.start_time_configured = value
                                    self.start_time_configured.value_namespace = name_space
                                    self.start_time_configured.value_namespace_prefix = name_space_prefix


                        class OperationMetric(Entity):
                            """
                            Array of the metrics that are measured by the
                            operation
                            
                            .. attribute:: current_buckets_archive
                            
                            	Number of valid buckets currently in the buckets archive
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_config
                            
                            	Configuration of the metric
                            	**type**\:   :py:class:`MetricConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric, self).__init__()

                                self.yang_name = "operation-metric"
                                self.yang_parent_name = "profile-options"

                                self.current_buckets_archive = YLeaf(YType.uint32, "current-buckets-archive")

                                self.metric_config = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig()
                                self.metric_config.parent = self
                                self._children_name_map["metric_config"] = "metric-config"
                                self._children_yang_names.add("metric-config")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("current_buckets_archive") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric, self).__setattr__(name, value)


                            class MetricConfig(Entity):
                                """
                                Configuration of the metric
                                
                                .. attribute:: bins_count
                                
                                	Total number of bins into which to aggregate. 0 if no aggregation
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: bins_width
                                
                                	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: bucket_size
                                
                                	Size of buckets into which measurements are collected
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: bucket_size_unit
                                
                                	Whether bucket size is 'per\-probe' or 'probes'
                                	**type**\:   :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                                
                                .. attribute:: buckets_archive
                                
                                	Maximum number of buckets to store in memory
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric_type
                                
                                	Type of metric to which this configuration applies
                                	**type**\:   :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig, self).__init__()

                                    self.yang_name = "metric-config"
                                    self.yang_parent_name = "operation-metric"

                                    self.bins_count = YLeaf(YType.uint16, "bins-count")

                                    self.bins_width = YLeaf(YType.uint16, "bins-width")

                                    self.bucket_size = YLeaf(YType.uint8, "bucket-size")

                                    self.bucket_size_unit = YLeaf(YType.enumeration, "bucket-size-unit")

                                    self.buckets_archive = YLeaf(YType.uint32, "buckets-archive")

                                    self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bins_count",
                                                    "bins_width",
                                                    "bucket_size",
                                                    "bucket_size_unit",
                                                    "buckets_archive",
                                                    "metric_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.bins_count.is_set or
                                        self.bins_width.is_set or
                                        self.bucket_size.is_set or
                                        self.bucket_size_unit.is_set or
                                        self.buckets_archive.is_set or
                                        self.metric_type.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bins_count.yfilter != YFilter.not_set or
                                        self.bins_width.yfilter != YFilter.not_set or
                                        self.bucket_size.yfilter != YFilter.not_set or
                                        self.bucket_size_unit.yfilter != YFilter.not_set or
                                        self.buckets_archive.yfilter != YFilter.not_set or
                                        self.metric_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "metric-config" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/operation-metric/%s" % self.get_segment_path()
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bins_count.is_set or self.bins_count.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bins_count.get_name_leafdata())
                                    if (self.bins_width.is_set or self.bins_width.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bins_width.get_name_leafdata())
                                    if (self.bucket_size.is_set or self.bucket_size.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_size.get_name_leafdata())
                                    if (self.bucket_size_unit.is_set or self.bucket_size_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_size_unit.get_name_leafdata())
                                    if (self.buckets_archive.is_set or self.buckets_archive.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.buckets_archive.get_name_leafdata())
                                    if (self.metric_type.is_set or self.metric_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.metric_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "bins-count" or name == "bins-width" or name == "bucket-size" or name == "bucket-size-unit" or name == "buckets-archive" or name == "metric-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bins-count"):
                                        self.bins_count = value
                                        self.bins_count.value_namespace = name_space
                                        self.bins_count.value_namespace_prefix = name_space_prefix
                                    if(value_path == "bins-width"):
                                        self.bins_width = value
                                        self.bins_width.value_namespace = name_space
                                        self.bins_width.value_namespace_prefix = name_space_prefix
                                    if(value_path == "bucket-size"):
                                        self.bucket_size = value
                                        self.bucket_size.value_namespace = name_space
                                        self.bucket_size.value_namespace_prefix = name_space_prefix
                                    if(value_path == "bucket-size-unit"):
                                        self.bucket_size_unit = value
                                        self.bucket_size_unit.value_namespace = name_space
                                        self.bucket_size_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "buckets-archive"):
                                        self.buckets_archive = value
                                        self.buckets_archive.value_namespace = name_space
                                        self.buckets_archive.value_namespace_prefix = name_space_prefix
                                    if(value_path == "metric-type"):
                                        self.metric_type = value
                                        self.metric_type.value_namespace = name_space
                                        self.metric_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.current_buckets_archive.is_set or
                                    (self.metric_config is not None and self.metric_config.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.current_buckets_archive.yfilter != YFilter.not_set or
                                    (self.metric_config is not None and self.metric_config.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operation-metric" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.current_buckets_archive.is_set or self.current_buckets_archive.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.current_buckets_archive.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "metric-config"):
                                    if (self.metric_config is None):
                                        self.metric_config = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig()
                                        self.metric_config.parent = self
                                        self._children_name_map["metric_config"] = "metric-config"
                                    return self.metric_config

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "metric-config" or name == "current-buckets-archive"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "current-buckets-archive"):
                                    self.current_buckets_archive = value
                                    self.current_buckets_archive.value_namespace = name_space
                                    self.current_buckets_archive.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.operation_metric:
                                if (c.has_data()):
                                    return True
                            return (
                                self.bursts_per_probe.is_set or
                                self.flr_calculation_interval.is_set or
                                self.inter_burst_interval.is_set or
                                self.inter_packet_interval.is_set or
                                self.packets_per_burst.is_set or
                                self.probe_type.is_set or
                                (self.operation_schedule is not None and self.operation_schedule.has_data()) or
                                (self.packet_padding is not None and self.packet_padding.has_data()) or
                                (self.priority is not None and self.priority.has_data()))

                        def has_operation(self):
                            for c in self.operation_metric:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bursts_per_probe.yfilter != YFilter.not_set or
                                self.flr_calculation_interval.yfilter != YFilter.not_set or
                                self.inter_burst_interval.yfilter != YFilter.not_set or
                                self.inter_packet_interval.yfilter != YFilter.not_set or
                                self.packets_per_burst.yfilter != YFilter.not_set or
                                self.probe_type.yfilter != YFilter.not_set or
                                (self.operation_schedule is not None and self.operation_schedule.has_operation()) or
                                (self.packet_padding is not None and self.packet_padding.has_operation()) or
                                (self.priority is not None and self.priority.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "profile-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bursts_per_probe.is_set or self.bursts_per_probe.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bursts_per_probe.get_name_leafdata())
                            if (self.flr_calculation_interval.is_set or self.flr_calculation_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flr_calculation_interval.get_name_leafdata())
                            if (self.inter_burst_interval.is_set or self.inter_burst_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.inter_burst_interval.get_name_leafdata())
                            if (self.inter_packet_interval.is_set or self.inter_packet_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.inter_packet_interval.get_name_leafdata())
                            if (self.packets_per_burst.is_set or self.packets_per_burst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_per_burst.get_name_leafdata())
                            if (self.probe_type.is_set or self.probe_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "operation-metric"):
                                for c in self.operation_metric:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.operation_metric.append(c)
                                return c

                            if (child_yang_name == "operation-schedule"):
                                if (self.operation_schedule is None):
                                    self.operation_schedule = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule()
                                    self.operation_schedule.parent = self
                                    self._children_name_map["operation_schedule"] = "operation-schedule"
                                return self.operation_schedule

                            if (child_yang_name == "packet-padding"):
                                if (self.packet_padding is None):
                                    self.packet_padding = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding()
                                    self.packet_padding.parent = self
                                    self._children_name_map["packet_padding"] = "packet-padding"
                                return self.packet_padding

                            if (child_yang_name == "priority"):
                                if (self.priority is None):
                                    self.priority = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority()
                                    self.priority.parent = self
                                    self._children_name_map["priority"] = "priority"
                                return self.priority

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "operation-metric" or name == "operation-schedule" or name == "packet-padding" or name == "priority" or name == "bursts-per-probe" or name == "flr-calculation-interval" or name == "inter-burst-interval" or name == "inter-packet-interval" or name == "packets-per-burst" or name == "probe-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bursts-per-probe"):
                                self.bursts_per_probe = value
                                self.bursts_per_probe.value_namespace = name_space
                                self.bursts_per_probe.value_namespace_prefix = name_space_prefix
                            if(value_path == "flr-calculation-interval"):
                                self.flr_calculation_interval = value
                                self.flr_calculation_interval.value_namespace = name_space
                                self.flr_calculation_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "inter-burst-interval"):
                                self.inter_burst_interval = value
                                self.inter_burst_interval.value_namespace = name_space
                                self.inter_burst_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "inter-packet-interval"):
                                self.inter_packet_interval = value
                                self.inter_packet_interval.value_namespace = name_space
                                self.inter_packet_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-per-burst"):
                                self.packets_per_burst = value
                                self.packets_per_burst.value_namespace = name_space
                                self.packets_per_burst.value_namespace_prefix = name_space_prefix
                            if(value_path == "probe-type"):
                                self.probe_type = value
                                self.probe_type.value_namespace = name_space
                                self.probe_type.value_namespace_prefix = name_space_prefix


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:   :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:   :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:   :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "on-demand-operation"

                            self.oper_type = YLeaf(YType.enumeration, "oper-type")

                            self.configured_operation_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"
                            self._children_yang_names.add("configured-operation-options")

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._children_yang_names.add("ondemand-operation-options")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("oper_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions, self).__setattr__(name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.profile_name = YLeaf(YType.str, "profile-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "configured-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.ondemand_operation_id = YLeaf(YType.uint32, "ondemand-operation-id")

                                self.probe_count = YLeaf(YType.uint8, "probe-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ondemand_operation_id",
                                                "probe_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ondemand_operation_id.is_set or
                                    self.probe_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ondemand_operation_id.yfilter != YFilter.not_set or
                                    self.probe_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ondemand-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ondemand_operation_id.is_set or self.ondemand_operation_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ondemand_operation_id.get_name_leafdata())
                                if (self.probe_count.is_set or self.probe_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.probe_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ondemand-operation-id" or name == "probe-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ondemand-operation-id"):
                                    self.ondemand_operation_id = value
                                    self.ondemand_operation_id.value_namespace = name_space
                                    self.ondemand_operation_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "probe-count"):
                                    self.probe_count = value
                                    self.probe_count.value_namespace = name_space
                                    self.probe_count.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.oper_type.is_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_data()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.oper_type.yfilter != YFilter.not_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_operation()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "specific-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.oper_type.is_set or self.oper_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oper_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "configured-operation-options"):
                                if (self.configured_operation_options is None):
                                    self.configured_operation_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions()
                                    self.configured_operation_options.parent = self
                                    self._children_name_map["configured_operation_options"] = "configured-operation-options"
                                return self.configured_operation_options

                            if (child_yang_name == "ondemand-operation-options"):
                                if (self.ondemand_operation_options is None):
                                    self.ondemand_operation_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions()
                                    self.ondemand_operation_options.parent = self
                                    self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                                return self.ondemand_operation_options

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "configured-operation-options" or name == "ondemand-operation-options" or name == "oper-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "oper-type"):
                                self.oper_type = value
                                self.oper_type.value_namespace = name_space
                                self.oper_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.display_long.is_set or
                            self.display_short.is_set or
                            self.domain_name.is_set or
                            self.interface_name.is_set or
                            self.last_run.is_set or
                            self.mac_address.is_set or
                            self.mep_id.is_set or
                            self.operation_id.is_set or
                            (self.profile_options is not None and self.profile_options.has_data()) or
                            (self.specific_options is not None and self.specific_options.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.display_long.yfilter != YFilter.not_set or
                            self.display_short.yfilter != YFilter.not_set or
                            self.domain_name.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.last_run.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.mep_id.yfilter != YFilter.not_set or
                            self.operation_id.yfilter != YFilter.not_set or
                            (self.profile_options is not None and self.profile_options.has_operation()) or
                            (self.specific_options is not None and self.specific_options.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "on-demand-operation" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.display_long.is_set or self.display_long.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_long.get_name_leafdata())
                        if (self.display_short.is_set or self.display_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_short.get_name_leafdata())
                        if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_name.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.last_run.is_set or self.last_run.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_run.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.mep_id.is_set or self.mep_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mep_id.get_name_leafdata())
                        if (self.operation_id.is_set or self.operation_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.operation_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "profile-options"):
                            if (self.profile_options is None):
                                self.profile_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions()
                                self.profile_options.parent = self
                                self._children_name_map["profile_options"] = "profile-options"
                            return self.profile_options

                        if (child_yang_name == "specific-options"):
                            if (self.specific_options is None):
                                self.specific_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions()
                                self.specific_options.parent = self
                                self._children_name_map["specific_options"] = "specific-options"
                            return self.specific_options

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "profile-options" or name == "specific-options" or name == "display-long" or name == "display-short" or name == "domain-name" or name == "interface-name" or name == "last-run" or name == "mac-address" or name == "mep-id" or name == "operation-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "display-long"):
                            self.display_long = value
                            self.display_long.value_namespace = name_space
                            self.display_long.value_namespace_prefix = name_space_prefix
                        if(value_path == "display-short"):
                            self.display_short = value
                            self.display_short.value_namespace = name_space
                            self.display_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-name"):
                            self.domain_name = value
                            self.domain_name.value_namespace = name_space
                            self.domain_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-run"):
                            self.last_run = value
                            self.last_run.value_namespace = name_space
                            self.last_run.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mep-id"):
                            self.mep_id = value
                            self.mep_id.value_namespace = name_space
                            self.mep_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "operation-id"):
                            self.operation_id = value
                            self.operation_id.value_namespace = name_space
                            self.operation_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.on_demand_operation:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.on_demand_operation:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "on-demand-operations" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "on-demand-operation"):
                        for c in self.on_demand_operation:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.on_demand_operation.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "on-demand-operation"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class StatisticsCurrents(Entity):
                """
                Table of current statistics for SLA operations
                
                .. attribute:: statistics_current
                
                	Current statistics data for an SLA configured operation
                	**type**\: list of    :py:class:`StatisticsCurrent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.StatisticsCurrents, self).__init__()

                    self.yang_name = "statistics-currents"
                    self.yang_parent_name = "ethernet"

                    self.statistics_current = YList(self)

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
                                super(Sla.Protocols.Ethernet.StatisticsCurrents, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sla.Protocols.Ethernet.StatisticsCurrents, self).__setattr__(name, value)


                class StatisticsCurrent(Entity):
                    """
                    Current statistics data for an SLA configured
                    operation
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\:  str
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: flr_calculation_interval
                    
                    	Interval between FLR calculations for SLM, in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\:  int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: operation_metric
                    
                    	Metrics gathered for the operation
                    	**type**\: list of    :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric>`
                    
                    .. attribute:: operation_schedule
                    
                    	Operation schedule
                    	**type**\:   :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule>`
                    
                    .. attribute:: probe_type
                    
                    	Type of probe used by the operation
                    	**type**\:  str
                    
                    .. attribute:: profile_name
                    
                    	Profile Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:   :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent, self).__init__()

                        self.yang_name = "statistics-current"
                        self.yang_parent_name = "statistics-currents"

                        self.display_long = YLeaf(YType.str, "display-long")

                        self.display_short = YLeaf(YType.str, "display-short")

                        self.domain_name = YLeaf(YType.str, "domain-name")

                        self.flr_calculation_interval = YLeaf(YType.uint32, "flr-calculation-interval")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.mep_id = YLeaf(YType.uint32, "mep-id")

                        self.probe_type = YLeaf(YType.str, "probe-type")

                        self.profile_name = YLeaf(YType.str, "profile-name")

                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule()
                        self.operation_schedule.parent = self
                        self._children_name_map["operation_schedule"] = "operation-schedule"
                        self._children_yang_names.add("operation-schedule")

                        self.specific_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"
                        self._children_yang_names.add("specific-options")

                        self.operation_metric = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("display_long",
                                        "display_short",
                                        "domain_name",
                                        "flr_calculation_interval",
                                        "interface_name",
                                        "mac_address",
                                        "mep_id",
                                        "probe_type",
                                        "profile_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent, self).__setattr__(name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:   :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:   :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:   :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "statistics-current"

                            self.oper_type = YLeaf(YType.enumeration, "oper-type")

                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"
                            self._children_yang_names.add("configured-operation-options")

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._children_yang_names.add("ondemand-operation-options")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("oper_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions, self).__setattr__(name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.profile_name = YLeaf(YType.str, "profile-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "configured-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"

                                self.ondemand_operation_id = YLeaf(YType.uint32, "ondemand-operation-id")

                                self.probe_count = YLeaf(YType.uint8, "probe-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ondemand_operation_id",
                                                "probe_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ondemand_operation_id.is_set or
                                    self.probe_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ondemand_operation_id.yfilter != YFilter.not_set or
                                    self.probe_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ondemand-operation-options" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/specific-options/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ondemand_operation_id.is_set or self.ondemand_operation_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ondemand_operation_id.get_name_leafdata())
                                if (self.probe_count.is_set or self.probe_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.probe_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ondemand-operation-id" or name == "probe-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ondemand-operation-id"):
                                    self.ondemand_operation_id = value
                                    self.ondemand_operation_id.value_namespace = name_space
                                    self.ondemand_operation_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "probe-count"):
                                    self.probe_count = value
                                    self.probe_count.value_namespace = name_space
                                    self.probe_count.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.oper_type.is_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_data()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.oper_type.yfilter != YFilter.not_set or
                                (self.configured_operation_options is not None and self.configured_operation_options.has_operation()) or
                                (self.ondemand_operation_options is not None and self.ondemand_operation_options.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "specific-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.oper_type.is_set or self.oper_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oper_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "configured-operation-options"):
                                if (self.configured_operation_options is None):
                                    self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions()
                                    self.configured_operation_options.parent = self
                                    self._children_name_map["configured_operation_options"] = "configured-operation-options"
                                return self.configured_operation_options

                            if (child_yang_name == "ondemand-operation-options"):
                                if (self.ondemand_operation_options is None):
                                    self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions()
                                    self.ondemand_operation_options.parent = self
                                    self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                                return self.ondemand_operation_options

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "configured-operation-options" or name == "ondemand-operation-options" or name == "oper-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "oper-type"):
                                self.oper_type = value
                                self.oper_type.value_namespace = name_space
                                self.oper_type.value_namespace_prefix = name_space_prefix


                    class OperationSchedule(Entity):
                        """
                        Operation schedule
                        
                        .. attribute:: schedule_duration
                        
                        	Duration of a probe for the operation in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: schedule_interval
                        
                        	Interval between the start times of consecutive probes,  in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time
                        
                        	Start time of the first probe, in seconds since the Unix Epoch
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time_configured
                        
                        	Whether or not the operation start time was explicitly configured
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule, self).__init__()

                            self.yang_name = "operation-schedule"
                            self.yang_parent_name = "statistics-current"

                            self.schedule_duration = YLeaf(YType.uint32, "schedule-duration")

                            self.schedule_interval = YLeaf(YType.uint32, "schedule-interval")

                            self.start_time = YLeaf(YType.uint32, "start-time")

                            self.start_time_configured = YLeaf(YType.boolean, "start-time-configured")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("schedule_duration",
                                            "schedule_interval",
                                            "start_time",
                                            "start_time_configured") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.schedule_duration.is_set or
                                self.schedule_interval.is_set or
                                self.start_time.is_set or
                                self.start_time_configured.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.schedule_duration.yfilter != YFilter.not_set or
                                self.schedule_interval.yfilter != YFilter.not_set or
                                self.start_time.yfilter != YFilter.not_set or
                                self.start_time_configured.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operation-schedule" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.schedule_duration.is_set or self.schedule_duration.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.schedule_duration.get_name_leafdata())
                            if (self.schedule_interval.is_set or self.schedule_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.schedule_interval.get_name_leafdata())
                            if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time.get_name_leafdata())
                            if (self.start_time_configured.is_set or self.start_time_configured.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time_configured.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "schedule-duration" or name == "schedule-interval" or name == "start-time" or name == "start-time-configured"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "schedule-duration"):
                                self.schedule_duration = value
                                self.schedule_duration.value_namespace = name_space
                                self.schedule_duration.value_namespace_prefix = name_space_prefix
                            if(value_path == "schedule-interval"):
                                self.schedule_interval = value
                                self.schedule_interval.value_namespace = name_space
                                self.schedule_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time"):
                                self.start_time = value
                                self.start_time.value_namespace = name_space
                                self.start_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time-configured"):
                                self.start_time_configured = value
                                self.start_time_configured.value_namespace = name_space
                                self.start_time_configured.value_namespace_prefix = name_space_prefix


                    class OperationMetric(Entity):
                        """
                        Metrics gathered for the operation
                        
                        .. attribute:: bucket
                        
                        	Buckets stored for the metric
                        	**type**\: list of    :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket>`
                        
                        .. attribute:: config
                        
                        	Configuration of the metric
                        	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric, self).__init__()

                            self.yang_name = "operation-metric"
                            self.yang_parent_name = "statistics-current"

                            self.config = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.bucket = YList(self)

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
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric, self).__setattr__(name, value)


                        class Config(Entity):
                            """
                            Configuration of the metric
                            
                            .. attribute:: bins_count
                            
                            	Total number of bins into which to aggregate. 0 if no aggregation
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bins_width
                            
                            	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bucket_size
                            
                            	Size of buckets into which measurements are collected
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: bucket_size_unit
                            
                            	Whether bucket size is 'per\-probe' or 'probes'
                            	**type**\:   :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:   :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "operation-metric"

                                self.bins_count = YLeaf(YType.uint16, "bins-count")

                                self.bins_width = YLeaf(YType.uint16, "bins-width")

                                self.bucket_size = YLeaf(YType.uint8, "bucket-size")

                                self.bucket_size_unit = YLeaf(YType.enumeration, "bucket-size-unit")

                                self.buckets_archive = YLeaf(YType.uint32, "buckets-archive")

                                self.metric_type = YLeaf(YType.enumeration, "metric-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bins_count",
                                                "bins_width",
                                                "bucket_size",
                                                "bucket_size_unit",
                                                "buckets_archive",
                                                "metric_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bins_count.is_set or
                                    self.bins_width.is_set or
                                    self.bucket_size.is_set or
                                    self.bucket_size_unit.is_set or
                                    self.buckets_archive.is_set or
                                    self.metric_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bins_count.yfilter != YFilter.not_set or
                                    self.bins_width.yfilter != YFilter.not_set or
                                    self.bucket_size.yfilter != YFilter.not_set or
                                    self.bucket_size_unit.yfilter != YFilter.not_set or
                                    self.buckets_archive.yfilter != YFilter.not_set or
                                    self.metric_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "config" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bins_count.is_set or self.bins_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bins_count.get_name_leafdata())
                                if (self.bins_width.is_set or self.bins_width.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bins_width.get_name_leafdata())
                                if (self.bucket_size.is_set or self.bucket_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bucket_size.get_name_leafdata())
                                if (self.bucket_size_unit.is_set or self.bucket_size_unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bucket_size_unit.get_name_leafdata())
                                if (self.buckets_archive.is_set or self.buckets_archive.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.buckets_archive.get_name_leafdata())
                                if (self.metric_type.is_set or self.metric_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.metric_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bins-count" or name == "bins-width" or name == "bucket-size" or name == "bucket-size-unit" or name == "buckets-archive" or name == "metric-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bins-count"):
                                    self.bins_count = value
                                    self.bins_count.value_namespace = name_space
                                    self.bins_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "bins-width"):
                                    self.bins_width = value
                                    self.bins_width.value_namespace = name_space
                                    self.bins_width.value_namespace_prefix = name_space_prefix
                                if(value_path == "bucket-size"):
                                    self.bucket_size = value
                                    self.bucket_size.value_namespace = name_space
                                    self.bucket_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "bucket-size-unit"):
                                    self.bucket_size_unit = value
                                    self.bucket_size_unit.value_namespace = name_space
                                    self.bucket_size_unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "buckets-archive"):
                                    self.buckets_archive = value
                                    self.buckets_archive.value_namespace = name_space
                                    self.buckets_archive.value_namespace_prefix = name_space_prefix
                                if(value_path == "metric-type"):
                                    self.metric_type = value
                                    self.metric_type.value_namespace = name_space
                                    self.metric_type.value_namespace_prefix = name_space_prefix


                        class Bucket(Entity):
                            """
                            Buckets stored for the metric
                            
                            .. attribute:: average
                            
                            	Mean of the results in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: contents
                            
                            	The contents of the bucket; bins or samples
                            	**type**\:   :py:class:`Contents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents>`
                            
                            .. attribute:: corrupt
                            
                            	Number of corrupt packets in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_lost_count
                            
                            	The number of data packets lost across the bucket, used in the calculation of overall FLR
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_sent_count
                            
                            	The number of data packets sent across the bucket, used in the calculation of overall FLR
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplicates
                            
                            	Number of duplicate packets received in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duration
                            
                            	Length of time for which the bucket is being filled in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: lost
                            
                            	Number of lost packets in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: minimum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: out_of_order
                            
                            	Number of packets recieved out\-of\-order in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: overall_flr
                            
                            	Frame Loss Ratio across the whole bucket, in millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: percentage
                            
                            .. attribute:: premature_reason
                            
                            	If the probe ended prematurely, the error that caused a probe to end
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: premature_reason_string
                            
                            	Description of the error code that caused the probe to end prematurely. For informational purposes only
                            	**type**\:  str
                            
                            .. attribute:: result_count
                            
                            	The count of samples collected in the bucket
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sent
                            
                            	Number of packets sent in the probe
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: standard_deviation
                            
                            	Standard deviation of the results in the probe, in microseconds or millionths of a percent
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: start_at
                            
                            	Absolute time that the bucket started being filled at
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suspect_cleared_mid_bucket
                            
                            	Results suspect as bucket was cleared mid\-way through being filled
                            	**type**\:  bool
                            
                            .. attribute:: suspect_clock_drift
                            
                            	Results suspect as more than 10 seconds time drift detected
                            	**type**\:  bool
                            
                            .. attribute:: suspect_flr_low_packet_count
                            
                            	Results suspect as FLR calculated based on a low packet count
                            	**type**\:  bool
                            
                            .. attribute:: suspect_management_latency
                            
                            	Results suspect as processing of results has been delayed
                            	**type**\:  bool
                            
                            .. attribute:: suspect_memory_allocation_failed
                            
                            	Results suspect due to a memory allocation failure
                            	**type**\:  bool
                            
                            .. attribute:: suspect_misordering
                            
                            	Results suspect as misordering has been detected , affecting results
                            	**type**\:  bool
                            
                            .. attribute:: suspect_multiple_buckets
                            
                            	Results suspect as the probe has been configured across multiple buckets
                            	**type**\:  bool
                            
                            .. attribute:: suspect_premature_end
                            
                            	Results suspect due to a probe ending prematurely
                            	**type**\:  bool
                            
                            .. attribute:: suspect_probe_restarted
                            
                            	Results suspect as probe restarted mid\-way through the bucket
                            	**type**\:  bool
                            
                            .. attribute:: suspect_schedule_latency
                            
                            	Results suspect due to scheduling latency causing one or more packets to not be sent
                            	**type**\:  bool
                            
                            .. attribute:: suspect_send_fail
                            
                            	Results suspect due to failure to send one or more packets
                            	**type**\:  bool
                            
                            .. attribute:: suspect_start_mid_bucket
                            
                            	Results suspect due to a probe starting mid\-way through a bucket
                            	**type**\:  bool
                            
                            .. attribute:: time_of_maximum
                            
                            	Absolute time that the maximum value was recorded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_of_minimum
                            
                            	Absolute time that the minimum value was recorded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket, self).__init__()

                                self.yang_name = "bucket"
                                self.yang_parent_name = "operation-metric"

                                self.average = YLeaf(YType.int32, "average")

                                self.corrupt = YLeaf(YType.uint32, "corrupt")

                                self.data_lost_count = YLeaf(YType.uint32, "data-lost-count")

                                self.data_sent_count = YLeaf(YType.uint32, "data-sent-count")

                                self.duplicates = YLeaf(YType.uint32, "duplicates")

                                self.duration = YLeaf(YType.uint32, "duration")

                                self.lost = YLeaf(YType.uint32, "lost")

                                self.maximum = YLeaf(YType.int32, "maximum")

                                self.minimum = YLeaf(YType.int32, "minimum")

                                self.out_of_order = YLeaf(YType.uint32, "out-of-order")

                                self.overall_flr = YLeaf(YType.int32, "overall-flr")

                                self.premature_reason = YLeaf(YType.uint32, "premature-reason")

                                self.premature_reason_string = YLeaf(YType.str, "premature-reason-string")

                                self.result_count = YLeaf(YType.uint32, "result-count")

                                self.sent = YLeaf(YType.uint32, "sent")

                                self.standard_deviation = YLeaf(YType.int32, "standard-deviation")

                                self.start_at = YLeaf(YType.uint32, "start-at")

                                self.suspect_cleared_mid_bucket = YLeaf(YType.boolean, "suspect-cleared-mid-bucket")

                                self.suspect_clock_drift = YLeaf(YType.boolean, "suspect-clock-drift")

                                self.suspect_flr_low_packet_count = YLeaf(YType.boolean, "suspect-flr-low-packet-count")

                                self.suspect_management_latency = YLeaf(YType.boolean, "suspect-management-latency")

                                self.suspect_memory_allocation_failed = YLeaf(YType.boolean, "suspect-memory-allocation-failed")

                                self.suspect_misordering = YLeaf(YType.boolean, "suspect-misordering")

                                self.suspect_multiple_buckets = YLeaf(YType.boolean, "suspect-multiple-buckets")

                                self.suspect_premature_end = YLeaf(YType.boolean, "suspect-premature-end")

                                self.suspect_probe_restarted = YLeaf(YType.boolean, "suspect-probe-restarted")

                                self.suspect_schedule_latency = YLeaf(YType.boolean, "suspect-schedule-latency")

                                self.suspect_send_fail = YLeaf(YType.boolean, "suspect-send-fail")

                                self.suspect_start_mid_bucket = YLeaf(YType.boolean, "suspect-start-mid-bucket")

                                self.time_of_maximum = YLeaf(YType.uint32, "time-of-maximum")

                                self.time_of_minimum = YLeaf(YType.uint32, "time-of-minimum")

                                self.contents = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self._children_name_map["contents"] = "contents"
                                self._children_yang_names.add("contents")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("average",
                                                "corrupt",
                                                "data_lost_count",
                                                "data_sent_count",
                                                "duplicates",
                                                "duration",
                                                "lost",
                                                "maximum",
                                                "minimum",
                                                "out_of_order",
                                                "overall_flr",
                                                "premature_reason",
                                                "premature_reason_string",
                                                "result_count",
                                                "sent",
                                                "standard_deviation",
                                                "start_at",
                                                "suspect_cleared_mid_bucket",
                                                "suspect_clock_drift",
                                                "suspect_flr_low_packet_count",
                                                "suspect_management_latency",
                                                "suspect_memory_allocation_failed",
                                                "suspect_misordering",
                                                "suspect_multiple_buckets",
                                                "suspect_premature_end",
                                                "suspect_probe_restarted",
                                                "suspect_schedule_latency",
                                                "suspect_send_fail",
                                                "suspect_start_mid_bucket",
                                                "time_of_maximum",
                                                "time_of_minimum") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket, self).__setattr__(name, value)


                            class Contents(Entity):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:   :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:   :py:class:`SlaOperBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucket>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:   :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents, self).__init__()

                                    self.yang_name = "contents"
                                    self.yang_parent_name = "bucket"

                                    self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self._children_name_map["aggregated"] = "aggregated"
                                    self._children_yang_names.add("aggregated")

                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self
                                    self._children_name_map["unaggregated"] = "unaggregated"
                                    self._children_yang_names.add("unaggregated")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bucket_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents, self).__setattr__(name, value)


                                class Aggregated(Entity):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated, self).__init__()

                                        self.yang_name = "aggregated"
                                        self.yang_parent_name = "contents"

                                        self.bins = YList(self)

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
                                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated, self).__setattr__(name, value)


                                    class Bins(Entity):
                                        """
                                        The bins of an SLA metric bucket
                                        
                                        .. attribute:: count
                                        
                                        	The total number of results in the bin
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lower_bound
                                        
                                        	Lower bound (inclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: lower_bound_tenths
                                        
                                        	Lower bound (inclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: sum
                                        
                                        	The sum of the results in the bin, in microseconds or millionths of a percent
                                        	**type**\:  int
                                        
                                        	**range:** \-9223372036854775808..9223372036854775807
                                        
                                        .. attribute:: upper_bound
                                        
                                        	Upper bound (exclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: upper_bound_tenths
                                        
                                        	Upper bound (exclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__init__()

                                            self.yang_name = "bins"
                                            self.yang_parent_name = "aggregated"

                                            self.count = YLeaf(YType.uint32, "count")

                                            self.lower_bound = YLeaf(YType.int32, "lower-bound")

                                            self.lower_bound_tenths = YLeaf(YType.int32, "lower-bound-tenths")

                                            self.sum = YLeaf(YType.int64, "sum")

                                            self.upper_bound = YLeaf(YType.int32, "upper-bound")

                                            self.upper_bound_tenths = YLeaf(YType.int32, "upper-bound-tenths")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("count",
                                                            "lower_bound",
                                                            "lower_bound_tenths",
                                                            "sum",
                                                            "upper_bound",
                                                            "upper_bound_tenths") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.count.is_set or
                                                self.lower_bound.is_set or
                                                self.lower_bound_tenths.is_set or
                                                self.sum.is_set or
                                                self.upper_bound.is_set or
                                                self.upper_bound_tenths.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.count.yfilter != YFilter.not_set or
                                                self.lower_bound.yfilter != YFilter.not_set or
                                                self.lower_bound_tenths.yfilter != YFilter.not_set or
                                                self.sum.yfilter != YFilter.not_set or
                                                self.upper_bound.yfilter != YFilter.not_set or
                                                self.upper_bound_tenths.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "bins" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/contents/aggregated/%s" % self.get_segment_path()
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.count.get_name_leafdata())
                                            if (self.lower_bound.is_set or self.lower_bound.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.lower_bound.get_name_leafdata())
                                            if (self.lower_bound_tenths.is_set or self.lower_bound_tenths.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.lower_bound_tenths.get_name_leafdata())
                                            if (self.sum.is_set or self.sum.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sum.get_name_leafdata())
                                            if (self.upper_bound.is_set or self.upper_bound.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.upper_bound.get_name_leafdata())
                                            if (self.upper_bound_tenths.is_set or self.upper_bound_tenths.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.upper_bound_tenths.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "count" or name == "lower-bound" or name == "lower-bound-tenths" or name == "sum" or name == "upper-bound" or name == "upper-bound-tenths"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "count"):
                                                self.count = value
                                                self.count.value_namespace = name_space
                                                self.count.value_namespace_prefix = name_space_prefix
                                            if(value_path == "lower-bound"):
                                                self.lower_bound = value
                                                self.lower_bound.value_namespace = name_space
                                                self.lower_bound.value_namespace_prefix = name_space_prefix
                                            if(value_path == "lower-bound-tenths"):
                                                self.lower_bound_tenths = value
                                                self.lower_bound_tenths.value_namespace = name_space
                                                self.lower_bound_tenths.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sum"):
                                                self.sum = value
                                                self.sum.value_namespace = name_space
                                                self.sum.value_namespace_prefix = name_space_prefix
                                            if(value_path == "upper-bound"):
                                                self.upper_bound = value
                                                self.upper_bound.value_namespace = name_space
                                                self.upper_bound.value_namespace_prefix = name_space_prefix
                                            if(value_path == "upper-bound-tenths"):
                                                self.upper_bound_tenths = value
                                                self.upper_bound_tenths.value_namespace = name_space
                                                self.upper_bound_tenths.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.bins:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.bins:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "aggregated" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/contents/%s" % self.get_segment_path()
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "bins"):
                                            for c in self.bins:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.bins.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "bins"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class Unaggregated(Entity):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated, self).__init__()

                                        self.yang_name = "unaggregated"
                                        self.yang_parent_name = "contents"

                                        self.sample = YList(self)

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
                                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated, self).__setattr__(name, value)


                                    class Sample(Entity):
                                        """
                                        The samples of an SLA metric bucket
                                        
                                        .. attribute:: corrupt
                                        
                                        	Whether the sample packet was corrupt
                                        	**type**\:  bool
                                        
                                        .. attribute:: frames_lost
                                        
                                        	For FLR measurements, the number of frames lost, if available
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: frames_sent
                                        
                                        	For FLR measurements, the number of frames sent, if available
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: no_data_packets
                                        
                                        	Whether a measurement could not be made because no data packets were sent in the sample period. Only applicable for LMM measurements
                                        	**type**\:  bool
                                        
                                        .. attribute:: out_of_order
                                        
                                        	Whether the sample packet was received out\-of\-order
                                        	**type**\:  bool
                                        
                                        .. attribute:: result
                                        
                                        	The result (in microseconds or millionths of a percent) of the sample, if available
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: sent
                                        
                                        	Whether the sample packet was sucessfully sent
                                        	**type**\:  bool
                                        
                                        .. attribute:: sent_at
                                        
                                        	The time (in milliseconds relative to the start time of the bucket) that the sample was sent at
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: timed_out
                                        
                                        	Whether the sample packet timed out
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__init__()

                                            self.yang_name = "sample"
                                            self.yang_parent_name = "unaggregated"

                                            self.corrupt = YLeaf(YType.boolean, "corrupt")

                                            self.frames_lost = YLeaf(YType.uint32, "frames-lost")

                                            self.frames_sent = YLeaf(YType.uint32, "frames-sent")

                                            self.no_data_packets = YLeaf(YType.boolean, "no-data-packets")

                                            self.out_of_order = YLeaf(YType.boolean, "out-of-order")

                                            self.result = YLeaf(YType.int32, "result")

                                            self.sent = YLeaf(YType.boolean, "sent")

                                            self.sent_at = YLeaf(YType.uint32, "sent-at")

                                            self.timed_out = YLeaf(YType.boolean, "timed-out")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("corrupt",
                                                            "frames_lost",
                                                            "frames_sent",
                                                            "no_data_packets",
                                                            "out_of_order",
                                                            "result",
                                                            "sent",
                                                            "sent_at",
                                                            "timed_out") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.corrupt.is_set or
                                                self.frames_lost.is_set or
                                                self.frames_sent.is_set or
                                                self.no_data_packets.is_set or
                                                self.out_of_order.is_set or
                                                self.result.is_set or
                                                self.sent.is_set or
                                                self.sent_at.is_set or
                                                self.timed_out.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.corrupt.yfilter != YFilter.not_set or
                                                self.frames_lost.yfilter != YFilter.not_set or
                                                self.frames_sent.yfilter != YFilter.not_set or
                                                self.no_data_packets.yfilter != YFilter.not_set or
                                                self.out_of_order.yfilter != YFilter.not_set or
                                                self.result.yfilter != YFilter.not_set or
                                                self.sent.yfilter != YFilter.not_set or
                                                self.sent_at.yfilter != YFilter.not_set or
                                                self.timed_out.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "sample" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/contents/unaggregated/%s" % self.get_segment_path()
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.corrupt.is_set or self.corrupt.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.corrupt.get_name_leafdata())
                                            if (self.frames_lost.is_set or self.frames_lost.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.frames_lost.get_name_leafdata())
                                            if (self.frames_sent.is_set or self.frames_sent.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.frames_sent.get_name_leafdata())
                                            if (self.no_data_packets.is_set or self.no_data_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.no_data_packets.get_name_leafdata())
                                            if (self.out_of_order.is_set or self.out_of_order.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.out_of_order.get_name_leafdata())
                                            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.result.get_name_leafdata())
                                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sent.get_name_leafdata())
                                            if (self.sent_at.is_set or self.sent_at.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.sent_at.get_name_leafdata())
                                            if (self.timed_out.is_set or self.timed_out.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.timed_out.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "corrupt" or name == "frames-lost" or name == "frames-sent" or name == "no-data-packets" or name == "out-of-order" or name == "result" or name == "sent" or name == "sent-at" or name == "timed-out"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "corrupt"):
                                                self.corrupt = value
                                                self.corrupt.value_namespace = name_space
                                                self.corrupt.value_namespace_prefix = name_space_prefix
                                            if(value_path == "frames-lost"):
                                                self.frames_lost = value
                                                self.frames_lost.value_namespace = name_space
                                                self.frames_lost.value_namespace_prefix = name_space_prefix
                                            if(value_path == "frames-sent"):
                                                self.frames_sent = value
                                                self.frames_sent.value_namespace = name_space
                                                self.frames_sent.value_namespace_prefix = name_space_prefix
                                            if(value_path == "no-data-packets"):
                                                self.no_data_packets = value
                                                self.no_data_packets.value_namespace = name_space
                                                self.no_data_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "out-of-order"):
                                                self.out_of_order = value
                                                self.out_of_order.value_namespace = name_space
                                                self.out_of_order.value_namespace_prefix = name_space_prefix
                                            if(value_path == "result"):
                                                self.result = value
                                                self.result.value_namespace = name_space
                                                self.result.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sent"):
                                                self.sent = value
                                                self.sent.value_namespace = name_space
                                                self.sent.value_namespace_prefix = name_space_prefix
                                            if(value_path == "sent-at"):
                                                self.sent_at = value
                                                self.sent_at.value_namespace = name_space
                                                self.sent_at.value_namespace_prefix = name_space_prefix
                                            if(value_path == "timed-out"):
                                                self.timed_out = value
                                                self.timed_out.value_namespace = name_space
                                                self.timed_out.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.sample:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.sample:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unaggregated" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/contents/%s" % self.get_segment_path()
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "sample"):
                                            for c in self.sample:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.sample.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "sample"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.bucket_type.is_set or
                                        (self.aggregated is not None and self.aggregated.has_data()) or
                                        (self.unaggregated is not None and self.unaggregated.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bucket_type.yfilter != YFilter.not_set or
                                        (self.aggregated is not None and self.aggregated.has_operation()) or
                                        (self.unaggregated is not None and self.unaggregated.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "contents" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/%s" % self.get_segment_path()
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bucket_type.is_set or self.bucket_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "aggregated"):
                                        if (self.aggregated is None):
                                            self.aggregated = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated()
                                            self.aggregated.parent = self
                                            self._children_name_map["aggregated"] = "aggregated"
                                        return self.aggregated

                                    if (child_yang_name == "unaggregated"):
                                        if (self.unaggregated is None):
                                            self.unaggregated = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated()
                                            self.unaggregated.parent = self
                                            self._children_name_map["unaggregated"] = "unaggregated"
                                        return self.unaggregated

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "aggregated" or name == "unaggregated" or name == "bucket-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bucket-type"):
                                        self.bucket_type = value
                                        self.bucket_type.value_namespace = name_space
                                        self.bucket_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.average.is_set or
                                    self.corrupt.is_set or
                                    self.data_lost_count.is_set or
                                    self.data_sent_count.is_set or
                                    self.duplicates.is_set or
                                    self.duration.is_set or
                                    self.lost.is_set or
                                    self.maximum.is_set or
                                    self.minimum.is_set or
                                    self.out_of_order.is_set or
                                    self.overall_flr.is_set or
                                    self.premature_reason.is_set or
                                    self.premature_reason_string.is_set or
                                    self.result_count.is_set or
                                    self.sent.is_set or
                                    self.standard_deviation.is_set or
                                    self.start_at.is_set or
                                    self.suspect_cleared_mid_bucket.is_set or
                                    self.suspect_clock_drift.is_set or
                                    self.suspect_flr_low_packet_count.is_set or
                                    self.suspect_management_latency.is_set or
                                    self.suspect_memory_allocation_failed.is_set or
                                    self.suspect_misordering.is_set or
                                    self.suspect_multiple_buckets.is_set or
                                    self.suspect_premature_end.is_set or
                                    self.suspect_probe_restarted.is_set or
                                    self.suspect_schedule_latency.is_set or
                                    self.suspect_send_fail.is_set or
                                    self.suspect_start_mid_bucket.is_set or
                                    self.time_of_maximum.is_set or
                                    self.time_of_minimum.is_set or
                                    (self.contents is not None and self.contents.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.average.yfilter != YFilter.not_set or
                                    self.corrupt.yfilter != YFilter.not_set or
                                    self.data_lost_count.yfilter != YFilter.not_set or
                                    self.data_sent_count.yfilter != YFilter.not_set or
                                    self.duplicates.yfilter != YFilter.not_set or
                                    self.duration.yfilter != YFilter.not_set or
                                    self.lost.yfilter != YFilter.not_set or
                                    self.maximum.yfilter != YFilter.not_set or
                                    self.minimum.yfilter != YFilter.not_set or
                                    self.out_of_order.yfilter != YFilter.not_set or
                                    self.overall_flr.yfilter != YFilter.not_set or
                                    self.premature_reason.yfilter != YFilter.not_set or
                                    self.premature_reason_string.yfilter != YFilter.not_set or
                                    self.result_count.yfilter != YFilter.not_set or
                                    self.sent.yfilter != YFilter.not_set or
                                    self.standard_deviation.yfilter != YFilter.not_set or
                                    self.start_at.yfilter != YFilter.not_set or
                                    self.suspect_cleared_mid_bucket.yfilter != YFilter.not_set or
                                    self.suspect_clock_drift.yfilter != YFilter.not_set or
                                    self.suspect_flr_low_packet_count.yfilter != YFilter.not_set or
                                    self.suspect_management_latency.yfilter != YFilter.not_set or
                                    self.suspect_memory_allocation_failed.yfilter != YFilter.not_set or
                                    self.suspect_misordering.yfilter != YFilter.not_set or
                                    self.suspect_multiple_buckets.yfilter != YFilter.not_set or
                                    self.suspect_premature_end.yfilter != YFilter.not_set or
                                    self.suspect_probe_restarted.yfilter != YFilter.not_set or
                                    self.suspect_schedule_latency.yfilter != YFilter.not_set or
                                    self.suspect_send_fail.yfilter != YFilter.not_set or
                                    self.suspect_start_mid_bucket.yfilter != YFilter.not_set or
                                    self.time_of_maximum.yfilter != YFilter.not_set or
                                    self.time_of_minimum.yfilter != YFilter.not_set or
                                    (self.contents is not None and self.contents.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bucket" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.average.is_set or self.average.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.average.get_name_leafdata())
                                if (self.corrupt.is_set or self.corrupt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.corrupt.get_name_leafdata())
                                if (self.data_lost_count.is_set or self.data_lost_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_lost_count.get_name_leafdata())
                                if (self.data_sent_count.is_set or self.data_sent_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_sent_count.get_name_leafdata())
                                if (self.duplicates.is_set or self.duplicates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duplicates.get_name_leafdata())
                                if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.duration.get_name_leafdata())
                                if (self.lost.is_set or self.lost.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lost.get_name_leafdata())
                                if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.maximum.get_name_leafdata())
                                if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.minimum.get_name_leafdata())
                                if (self.out_of_order.is_set or self.out_of_order.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_of_order.get_name_leafdata())
                                if (self.overall_flr.is_set or self.overall_flr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.overall_flr.get_name_leafdata())
                                if (self.premature_reason.is_set or self.premature_reason.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.premature_reason.get_name_leafdata())
                                if (self.premature_reason_string.is_set or self.premature_reason_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.premature_reason_string.get_name_leafdata())
                                if (self.result_count.is_set or self.result_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.result_count.get_name_leafdata())
                                if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sent.get_name_leafdata())
                                if (self.standard_deviation.is_set or self.standard_deviation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.standard_deviation.get_name_leafdata())
                                if (self.start_at.is_set or self.start_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_at.get_name_leafdata())
                                if (self.suspect_cleared_mid_bucket.is_set or self.suspect_cleared_mid_bucket.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_cleared_mid_bucket.get_name_leafdata())
                                if (self.suspect_clock_drift.is_set or self.suspect_clock_drift.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_clock_drift.get_name_leafdata())
                                if (self.suspect_flr_low_packet_count.is_set or self.suspect_flr_low_packet_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_flr_low_packet_count.get_name_leafdata())
                                if (self.suspect_management_latency.is_set or self.suspect_management_latency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_management_latency.get_name_leafdata())
                                if (self.suspect_memory_allocation_failed.is_set or self.suspect_memory_allocation_failed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_memory_allocation_failed.get_name_leafdata())
                                if (self.suspect_misordering.is_set or self.suspect_misordering.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_misordering.get_name_leafdata())
                                if (self.suspect_multiple_buckets.is_set or self.suspect_multiple_buckets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_multiple_buckets.get_name_leafdata())
                                if (self.suspect_premature_end.is_set or self.suspect_premature_end.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_premature_end.get_name_leafdata())
                                if (self.suspect_probe_restarted.is_set or self.suspect_probe_restarted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_probe_restarted.get_name_leafdata())
                                if (self.suspect_schedule_latency.is_set or self.suspect_schedule_latency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_schedule_latency.get_name_leafdata())
                                if (self.suspect_send_fail.is_set or self.suspect_send_fail.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_send_fail.get_name_leafdata())
                                if (self.suspect_start_mid_bucket.is_set or self.suspect_start_mid_bucket.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suspect_start_mid_bucket.get_name_leafdata())
                                if (self.time_of_maximum.is_set or self.time_of_maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_of_maximum.get_name_leafdata())
                                if (self.time_of_minimum.is_set or self.time_of_minimum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_of_minimum.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "contents"):
                                    if (self.contents is None):
                                        self.contents = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents()
                                        self.contents.parent = self
                                        self._children_name_map["contents"] = "contents"
                                    return self.contents

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "contents" or name == "average" or name == "corrupt" or name == "data-lost-count" or name == "data-sent-count" or name == "duplicates" or name == "duration" or name == "lost" or name == "maximum" or name == "minimum" or name == "out-of-order" or name == "overall-flr" or name == "premature-reason" or name == "premature-reason-string" or name == "result-count" or name == "sent" or name == "standard-deviation" or name == "start-at" or name == "suspect-cleared-mid-bucket" or name == "suspect-clock-drift" or name == "suspect-flr-low-packet-count" or name == "suspect-management-latency" or name == "suspect-memory-allocation-failed" or name == "suspect-misordering" or name == "suspect-multiple-buckets" or name == "suspect-premature-end" or name == "suspect-probe-restarted" or name == "suspect-schedule-latency" or name == "suspect-send-fail" or name == "suspect-start-mid-bucket" or name == "time-of-maximum" or name == "time-of-minimum"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "average"):
                                    self.average = value
                                    self.average.value_namespace = name_space
                                    self.average.value_namespace_prefix = name_space_prefix
                                if(value_path == "corrupt"):
                                    self.corrupt = value
                                    self.corrupt.value_namespace = name_space
                                    self.corrupt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-lost-count"):
                                    self.data_lost_count = value
                                    self.data_lost_count.value_namespace = name_space
                                    self.data_lost_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-sent-count"):
                                    self.data_sent_count = value
                                    self.data_sent_count.value_namespace = name_space
                                    self.data_sent_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "duplicates"):
                                    self.duplicates = value
                                    self.duplicates.value_namespace = name_space
                                    self.duplicates.value_namespace_prefix = name_space_prefix
                                if(value_path == "duration"):
                                    self.duration = value
                                    self.duration.value_namespace = name_space
                                    self.duration.value_namespace_prefix = name_space_prefix
                                if(value_path == "lost"):
                                    self.lost = value
                                    self.lost.value_namespace = name_space
                                    self.lost.value_namespace_prefix = name_space_prefix
                                if(value_path == "maximum"):
                                    self.maximum = value
                                    self.maximum.value_namespace = name_space
                                    self.maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "minimum"):
                                    self.minimum = value
                                    self.minimum.value_namespace = name_space
                                    self.minimum.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-of-order"):
                                    self.out_of_order = value
                                    self.out_of_order.value_namespace = name_space
                                    self.out_of_order.value_namespace_prefix = name_space_prefix
                                if(value_path == "overall-flr"):
                                    self.overall_flr = value
                                    self.overall_flr.value_namespace = name_space
                                    self.overall_flr.value_namespace_prefix = name_space_prefix
                                if(value_path == "premature-reason"):
                                    self.premature_reason = value
                                    self.premature_reason.value_namespace = name_space
                                    self.premature_reason.value_namespace_prefix = name_space_prefix
                                if(value_path == "premature-reason-string"):
                                    self.premature_reason_string = value
                                    self.premature_reason_string.value_namespace = name_space
                                    self.premature_reason_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "result-count"):
                                    self.result_count = value
                                    self.result_count.value_namespace = name_space
                                    self.result_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "sent"):
                                    self.sent = value
                                    self.sent.value_namespace = name_space
                                    self.sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "standard-deviation"):
                                    self.standard_deviation = value
                                    self.standard_deviation.value_namespace = name_space
                                    self.standard_deviation.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-at"):
                                    self.start_at = value
                                    self.start_at.value_namespace = name_space
                                    self.start_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-cleared-mid-bucket"):
                                    self.suspect_cleared_mid_bucket = value
                                    self.suspect_cleared_mid_bucket.value_namespace = name_space
                                    self.suspect_cleared_mid_bucket.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-clock-drift"):
                                    self.suspect_clock_drift = value
                                    self.suspect_clock_drift.value_namespace = name_space
                                    self.suspect_clock_drift.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-flr-low-packet-count"):
                                    self.suspect_flr_low_packet_count = value
                                    self.suspect_flr_low_packet_count.value_namespace = name_space
                                    self.suspect_flr_low_packet_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-management-latency"):
                                    self.suspect_management_latency = value
                                    self.suspect_management_latency.value_namespace = name_space
                                    self.suspect_management_latency.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-memory-allocation-failed"):
                                    self.suspect_memory_allocation_failed = value
                                    self.suspect_memory_allocation_failed.value_namespace = name_space
                                    self.suspect_memory_allocation_failed.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-misordering"):
                                    self.suspect_misordering = value
                                    self.suspect_misordering.value_namespace = name_space
                                    self.suspect_misordering.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-multiple-buckets"):
                                    self.suspect_multiple_buckets = value
                                    self.suspect_multiple_buckets.value_namespace = name_space
                                    self.suspect_multiple_buckets.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-premature-end"):
                                    self.suspect_premature_end = value
                                    self.suspect_premature_end.value_namespace = name_space
                                    self.suspect_premature_end.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-probe-restarted"):
                                    self.suspect_probe_restarted = value
                                    self.suspect_probe_restarted.value_namespace = name_space
                                    self.suspect_probe_restarted.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-schedule-latency"):
                                    self.suspect_schedule_latency = value
                                    self.suspect_schedule_latency.value_namespace = name_space
                                    self.suspect_schedule_latency.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-send-fail"):
                                    self.suspect_send_fail = value
                                    self.suspect_send_fail.value_namespace = name_space
                                    self.suspect_send_fail.value_namespace_prefix = name_space_prefix
                                if(value_path == "suspect-start-mid-bucket"):
                                    self.suspect_start_mid_bucket = value
                                    self.suspect_start_mid_bucket.value_namespace = name_space
                                    self.suspect_start_mid_bucket.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-of-maximum"):
                                    self.time_of_maximum = value
                                    self.time_of_maximum.value_namespace = name_space
                                    self.time_of_maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-of-minimum"):
                                    self.time_of_minimum = value
                                    self.time_of_minimum.value_namespace = name_space
                                    self.time_of_minimum.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.bucket:
                                if (c.has_data()):
                                    return True
                            return (self.config is not None and self.config.has_data())

                        def has_operation(self):
                            for c in self.bucket:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operation-metric" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "bucket"):
                                for c in self.bucket:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.bucket.append(c)
                                return c

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bucket" or name == "config"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        for c in self.operation_metric:
                            if (c.has_data()):
                                return True
                        return (
                            self.display_long.is_set or
                            self.display_short.is_set or
                            self.domain_name.is_set or
                            self.flr_calculation_interval.is_set or
                            self.interface_name.is_set or
                            self.mac_address.is_set or
                            self.mep_id.is_set or
                            self.probe_type.is_set or
                            self.profile_name.is_set or
                            (self.operation_schedule is not None and self.operation_schedule.has_data()) or
                            (self.specific_options is not None and self.specific_options.has_data()))

                    def has_operation(self):
                        for c in self.operation_metric:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.display_long.yfilter != YFilter.not_set or
                            self.display_short.yfilter != YFilter.not_set or
                            self.domain_name.yfilter != YFilter.not_set or
                            self.flr_calculation_interval.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.mep_id.yfilter != YFilter.not_set or
                            self.probe_type.yfilter != YFilter.not_set or
                            self.profile_name.yfilter != YFilter.not_set or
                            (self.operation_schedule is not None and self.operation_schedule.has_operation()) or
                            (self.specific_options is not None and self.specific_options.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics-current" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.display_long.is_set or self.display_long.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_long.get_name_leafdata())
                        if (self.display_short.is_set or self.display_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_short.get_name_leafdata())
                        if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_name.get_name_leafdata())
                        if (self.flr_calculation_interval.is_set or self.flr_calculation_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flr_calculation_interval.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.mep_id.is_set or self.mep_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mep_id.get_name_leafdata())
                        if (self.probe_type.is_set or self.probe_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.probe_type.get_name_leafdata())
                        if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.profile_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "operation-metric"):
                            for c in self.operation_metric:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.operation_metric.append(c)
                            return c

                        if (child_yang_name == "operation-schedule"):
                            if (self.operation_schedule is None):
                                self.operation_schedule = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule()
                                self.operation_schedule.parent = self
                                self._children_name_map["operation_schedule"] = "operation-schedule"
                            return self.operation_schedule

                        if (child_yang_name == "specific-options"):
                            if (self.specific_options is None):
                                self.specific_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions()
                                self.specific_options.parent = self
                                self._children_name_map["specific_options"] = "specific-options"
                            return self.specific_options

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "operation-metric" or name == "operation-schedule" or name == "specific-options" or name == "display-long" or name == "display-short" or name == "domain-name" or name == "flr-calculation-interval" or name == "interface-name" or name == "mac-address" or name == "mep-id" or name == "probe-type" or name == "profile-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "display-long"):
                            self.display_long = value
                            self.display_long.value_namespace = name_space
                            self.display_long.value_namespace_prefix = name_space_prefix
                        if(value_path == "display-short"):
                            self.display_short = value
                            self.display_short.value_namespace = name_space
                            self.display_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-name"):
                            self.domain_name = value
                            self.domain_name.value_namespace = name_space
                            self.domain_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "flr-calculation-interval"):
                            self.flr_calculation_interval = value
                            self.flr_calculation_interval.value_namespace = name_space
                            self.flr_calculation_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mep-id"):
                            self.mep_id = value
                            self.mep_id.value_namespace = name_space
                            self.mep_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "probe-type"):
                            self.probe_type = value
                            self.probe_type.value_namespace = name_space
                            self.probe_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "profile-name"):
                            self.profile_name = value
                            self.profile_name.value_namespace = name_space
                            self.profile_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.statistics_current:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.statistics_current:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics-currents" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "statistics-current"):
                        for c in self.statistics_current:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.statistics_current.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statistics-current"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.config_errors is not None and self.config_errors.has_data()) or
                    (self.on_demand_operations is not None and self.on_demand_operations.has_data()) or
                    (self.operations is not None and self.operations.has_data()) or
                    (self.statistics_currents is not None and self.statistics_currents.has_data()) or
                    (self.statistics_historicals is not None and self.statistics_historicals.has_data()) or
                    (self.statistics_on_demand_currents is not None and self.statistics_on_demand_currents.has_data()) or
                    (self.statistics_on_demand_historicals is not None and self.statistics_on_demand_historicals.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.config_errors is not None and self.config_errors.has_operation()) or
                    (self.on_demand_operations is not None and self.on_demand_operations.has_operation()) or
                    (self.operations is not None and self.operations.has_operation()) or
                    (self.statistics_currents is not None and self.statistics_currents.has_operation()) or
                    (self.statistics_historicals is not None and self.statistics_historicals.has_operation()) or
                    (self.statistics_on_demand_currents is not None and self.statistics_on_demand_currents.has_operation()) or
                    (self.statistics_on_demand_historicals is not None and self.statistics_on_demand_historicals.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-ethernet-cfm-oper:ethernet" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/protocols/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config-errors"):
                    if (self.config_errors is None):
                        self.config_errors = Sla.Protocols.Ethernet.ConfigErrors()
                        self.config_errors.parent = self
                        self._children_name_map["config_errors"] = "config-errors"
                    return self.config_errors

                if (child_yang_name == "on-demand-operations"):
                    if (self.on_demand_operations is None):
                        self.on_demand_operations = Sla.Protocols.Ethernet.OnDemandOperations()
                        self.on_demand_operations.parent = self
                        self._children_name_map["on_demand_operations"] = "on-demand-operations"
                    return self.on_demand_operations

                if (child_yang_name == "operations"):
                    if (self.operations is None):
                        self.operations = Sla.Protocols.Ethernet.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"
                    return self.operations

                if (child_yang_name == "statistics-currents"):
                    if (self.statistics_currents is None):
                        self.statistics_currents = Sla.Protocols.Ethernet.StatisticsCurrents()
                        self.statistics_currents.parent = self
                        self._children_name_map["statistics_currents"] = "statistics-currents"
                    return self.statistics_currents

                if (child_yang_name == "statistics-historicals"):
                    if (self.statistics_historicals is None):
                        self.statistics_historicals = Sla.Protocols.Ethernet.StatisticsHistoricals()
                        self.statistics_historicals.parent = self
                        self._children_name_map["statistics_historicals"] = "statistics-historicals"
                    return self.statistics_historicals

                if (child_yang_name == "statistics-on-demand-currents"):
                    if (self.statistics_on_demand_currents is None):
                        self.statistics_on_demand_currents = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents()
                        self.statistics_on_demand_currents.parent = self
                        self._children_name_map["statistics_on_demand_currents"] = "statistics-on-demand-currents"
                    return self.statistics_on_demand_currents

                if (child_yang_name == "statistics-on-demand-historicals"):
                    if (self.statistics_on_demand_historicals is None):
                        self.statistics_on_demand_historicals = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals()
                        self.statistics_on_demand_historicals.parent = self
                        self._children_name_map["statistics_on_demand_historicals"] = "statistics-on-demand-historicals"
                    return self.statistics_on_demand_historicals

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config-errors" or name == "on-demand-operations" or name == "operations" or name == "statistics-currents" or name == "statistics-historicals" or name == "statistics-on-demand-currents" or name == "statistics-on-demand-historicals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.ethernet is not None and self.ethernet.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.ethernet is not None and self.ethernet.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "protocols" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ethernet"):
                if (self.ethernet is None):
                    self.ethernet = Sla.Protocols.Ethernet()
                    self.ethernet.parent = self
                    self._children_name_map["ethernet"] = "ethernet"
                return self.ethernet

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ethernet"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.protocols is not None and self.protocols.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.protocols is not None and self.protocols.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla" + path_buffer

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

        if (child_yang_name == "protocols"):
            if (self.protocols is None):
                self.protocols = Sla.Protocols()
                self.protocols.parent = self
                self._children_name_map["protocols"] = "protocols"
            return self.protocols

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "protocols"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Sla()
        return self._top_entity

class SlaNodes(Entity):
    """
    sla nodes
    
    

    """

    _prefix = 'infra-sla-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SlaNodes, self).__init__()
        self._top_entity = None

        self.yang_name = "sla-nodes"
        self.yang_parent_name = "Cisco-IOS-XR-infra-sla-oper"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-sla-oper:sla-nodes" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SlaNodes()
        return self._top_entity

