""" Cisco_IOS_XR_infra_sla_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-sla package operational data.

This module contains definitions
for the following management objects\:
  sla\: SLA oper commands
  sla\-nodes\: sla nodes

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Sla(Entity):
    """
    SLA oper commands
    
    .. attribute:: protocols
    
    	Table of all SLA protocols
    	**type**\:  :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols>`
    
    

    """

    _prefix = 'infra-sla-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sla, self).__init__()
        self._top_entity = None

        self.yang_name = "sla"
        self.yang_parent_name = "Cisco-IOS-XR-infra-sla-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("protocols", ("protocols", Sla.Protocols))])
        self._leafs = OrderedDict()

        self.protocols = Sla.Protocols()
        self.protocols.parent = self
        self._children_name_map["protocols"] = "protocols"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Sla, [], name, value)


    class Protocols(Entity):
        """
        Table of all SLA protocols
        
        .. attribute:: ethernet
        
        	The Ethernet SLA protocol
        	**type**\:  :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet>`
        
        

        """

        _prefix = 'infra-sla-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sla.Protocols, self).__init__()

            self.yang_name = "protocols"
            self.yang_parent_name = "sla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("Cisco-IOS-XR-ethernet-cfm-oper:ethernet", ("ethernet", Sla.Protocols.Ethernet))])
            self._leafs = OrderedDict()

            self.ethernet = Sla.Protocols.Ethernet()
            self.ethernet.parent = self
            self._children_name_map["ethernet"] = "Cisco-IOS-XR-ethernet-cfm-oper:ethernet"
            self._segment_path = lambda: "protocols"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sla.Protocols, [], name, value)


        class Ethernet(Entity):
            """
            The Ethernet SLA protocol
            
            .. attribute:: statistics_on_demand_currents
            
            	Table of current statistics for SLA on\-demand operations
            	**type**\:  :py:class:`StatisticsOnDemandCurrents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents>`
            
            .. attribute:: operations
            
            	Table of SLA operations
            	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations>`
            
            .. attribute:: statistics_historicals
            
            	Table of historical statistics for SLA operations
            	**type**\:  :py:class:`StatisticsHistoricals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals>`
            
            .. attribute:: statistics_on_demand_historicals
            
            	Table of historical statistics for SLA on\-demand operations
            	**type**\:  :py:class:`StatisticsOnDemandHistoricals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals>`
            
            .. attribute:: config_errors
            
            	Table of SLA configuration errors on configured operations
            	**type**\:  :py:class:`ConfigErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.ConfigErrors>`
            
            .. attribute:: on_demand_operations
            
            	Table of SLA on\-demand operations
            	**type**\:  :py:class:`OnDemandOperations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations>`
            
            .. attribute:: statistics_currents
            
            	Table of current statistics for SLA operations
            	**type**\:  :py:class:`StatisticsCurrents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Sla.Protocols.Ethernet, self).__init__()

                self.yang_name = "ethernet"
                self.yang_parent_name = "protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("statistics-on-demand-currents", ("statistics_on_demand_currents", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents)), ("operations", ("operations", Sla.Protocols.Ethernet.Operations)), ("statistics-historicals", ("statistics_historicals", Sla.Protocols.Ethernet.StatisticsHistoricals)), ("statistics-on-demand-historicals", ("statistics_on_demand_historicals", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals)), ("config-errors", ("config_errors", Sla.Protocols.Ethernet.ConfigErrors)), ("on-demand-operations", ("on_demand_operations", Sla.Protocols.Ethernet.OnDemandOperations)), ("statistics-currents", ("statistics_currents", Sla.Protocols.Ethernet.StatisticsCurrents))])
                self._leafs = OrderedDict()

                self.statistics_on_demand_currents = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents()
                self.statistics_on_demand_currents.parent = self
                self._children_name_map["statistics_on_demand_currents"] = "statistics-on-demand-currents"

                self.operations = Sla.Protocols.Ethernet.Operations()
                self.operations.parent = self
                self._children_name_map["operations"] = "operations"

                self.statistics_historicals = Sla.Protocols.Ethernet.StatisticsHistoricals()
                self.statistics_historicals.parent = self
                self._children_name_map["statistics_historicals"] = "statistics-historicals"

                self.statistics_on_demand_historicals = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals()
                self.statistics_on_demand_historicals.parent = self
                self._children_name_map["statistics_on_demand_historicals"] = "statistics-on-demand-historicals"

                self.config_errors = Sla.Protocols.Ethernet.ConfigErrors()
                self.config_errors.parent = self
                self._children_name_map["config_errors"] = "config-errors"

                self.on_demand_operations = Sla.Protocols.Ethernet.OnDemandOperations()
                self.on_demand_operations.parent = self
                self._children_name_map["on_demand_operations"] = "on-demand-operations"

                self.statistics_currents = Sla.Protocols.Ethernet.StatisticsCurrents()
                self.statistics_currents.parent = self
                self._children_name_map["statistics_currents"] = "statistics-currents"
                self._segment_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:ethernet"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sla.Protocols.Ethernet, [], name, value)


            class StatisticsOnDemandCurrents(Entity):
                """
                Table of current statistics for SLA on\-demand
                operations
                
                .. attribute:: statistics_on_demand_current
                
                	Current statistics data for an SLA on\-demand operation
                	**type**\: list of  		 :py:class:`StatisticsOnDemandCurrent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents, self).__init__()

                    self.yang_name = "statistics-on-demand-currents"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics-on-demand-current", ("statistics_on_demand_current", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent))])
                    self._leafs = OrderedDict()

                    self.statistics_on_demand_current = YList(self)
                    self._segment_path = lambda: "statistics-on-demand-currents"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents, [], name, value)


                class StatisticsOnDemandCurrent(Entity):
                    """
                    Current statistics data for an SLA on\-demand
                    operation
                    
                    .. attribute:: operation_id
                    
                    	Operation ID
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\: int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:  :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions>`
                    
                    .. attribute:: operation_schedule
                    
                    	Operation schedule
                    	**type**\:  :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule>`
                    
                    .. attribute:: probe_type
                    
                    	Type of probe used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: flr_calculation_interval
                    
                    	Interval between FLR calculations for SLM, in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: operation_metric
                    
                    	Metrics gathered for the operation
                    	**type**\: list of  		 :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent, self).__init__()

                        self.yang_name = "statistics-on-demand-current"
                        self.yang_parent_name = "statistics-on-demand-currents"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("specific-options", ("specific_options", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions)), ("operation-schedule", ("operation_schedule", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule)), ("operation-metric", ("operation_metric", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric))])
                        self._leafs = OrderedDict([
                            ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('probe_type', (YLeaf(YType.str, 'probe-type'), ['str'])),
                            ('display_short', (YLeaf(YType.str, 'display-short'), ['str'])),
                            ('display_long', (YLeaf(YType.str, 'display-long'), ['str'])),
                            ('flr_calculation_interval', (YLeaf(YType.uint32, 'flr-calculation-interval'), ['int'])),
                        ])
                        self.operation_id = None
                        self.domain_name = None
                        self.interface_name = None
                        self.mep_id = None
                        self.mac_address = None
                        self.probe_type = None
                        self.display_short = None
                        self.display_long = None
                        self.flr_calculation_interval = None

                        self.specific_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"

                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule()
                        self.operation_schedule.parent = self
                        self._children_name_map["operation_schedule"] = "operation-schedule"

                        self.operation_metric = YList(self)
                        self._segment_path = lambda: "statistics-on-demand-current"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent, ['operation_id', 'domain_name', 'interface_name', 'mep_id', 'mac_address', 'probe_type', 'display_short', 'display_long', 'flr_calculation_interval'], name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:  :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:  :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:  :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "statistics-on-demand-current"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("configured-operation-options", ("configured_operation_options", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions)), ("ondemand-operation-options", ("ondemand_operation_options", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions))])
                            self._leafs = OrderedDict([
                                ('oper_type', (YLeaf(YType.enumeration, 'oper-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation', '')])),
                            ])
                            self.oper_type = None

                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._segment_path = lambda: "specific-options"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions, ['oper_type'], name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "configured-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions, ['profile_name'], name, value)


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ondemand_operation_id', (YLeaf(YType.uint32, 'ondemand-operation-id'), ['int'])),
                                    ('probe_count', (YLeaf(YType.uint8, 'probe-count'), ['int'])),
                                ])
                                self.ondemand_operation_id = None
                                self.probe_count = None
                                self._segment_path = lambda: "ondemand-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions, ['ondemand_operation_id', 'probe_count'], name, value)


                    class OperationSchedule(Entity):
                        """
                        Operation schedule
                        
                        .. attribute:: start_time
                        
                        	Start time of the first probe, in seconds since the Unix Epoch
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time_configured
                        
                        	Whether or not the operation start time was explicitly configured
                        	**type**\: bool
                        
                        .. attribute:: schedule_duration
                        
                        	Duration of a probe for the operation in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: schedule_interval
                        
                        	Interval between the start times of consecutive probes,  in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule, self).__init__()

                            self.yang_name = "operation-schedule"
                            self.yang_parent_name = "statistics-on-demand-current"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                                ('start_time_configured', (YLeaf(YType.boolean, 'start-time-configured'), ['bool'])),
                                ('schedule_duration', (YLeaf(YType.uint32, 'schedule-duration'), ['int'])),
                                ('schedule_interval', (YLeaf(YType.uint32, 'schedule-interval'), ['int'])),
                            ])
                            self.start_time = None
                            self.start_time_configured = None
                            self.schedule_duration = None
                            self.schedule_interval = None
                            self._segment_path = lambda: "operation-schedule"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule, ['start_time', 'start_time_configured', 'schedule_duration', 'schedule_interval'], name, value)


                    class OperationMetric(Entity):
                        """
                        Metrics gathered for the operation
                        
                        .. attribute:: config
                        
                        	Configuration of the metric
                        	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config>`
                        
                        .. attribute:: bucket
                        
                        	Buckets stored for the metric
                        	**type**\: list of  		 :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric, self).__init__()

                            self.yang_name = "operation-metric"
                            self.yang_parent_name = "statistics-on-demand-current"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config)), ("bucket", ("bucket", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket))])
                            self._leafs = OrderedDict()

                            self.config = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.bucket = YList(self)
                            self._segment_path = lambda: "operation-metric"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric, [], name, value)


                        class Config(Entity):
                            """
                            Configuration of the metric
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:  :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                            
                            .. attribute:: bins_count
                            
                            	Total number of bins into which to aggregate. 0 if no aggregation
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bins_width
                            
                            	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bucket_size
                            
                            	Size of buckets into which measurements are collected
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: bucket_size_unit
                            
                            	Whether bucket size is 'per\-probe' or 'probes'
                            	**type**\:  :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "operation-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric', '')])),
                                    ('bins_count', (YLeaf(YType.uint16, 'bins-count'), ['int'])),
                                    ('bins_width', (YLeaf(YType.uint16, 'bins-width'), ['int'])),
                                    ('bucket_size', (YLeaf(YType.uint8, 'bucket-size'), ['int'])),
                                    ('bucket_size_unit', (YLeaf(YType.enumeration, 'bucket-size-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize', '')])),
                                    ('buckets_archive', (YLeaf(YType.uint32, 'buckets-archive'), ['int'])),
                                ])
                                self.metric_type = None
                                self.bins_count = None
                                self.bins_width = None
                                self.bucket_size = None
                                self.bucket_size_unit = None
                                self.buckets_archive = None
                                self._segment_path = lambda: "config"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config, ['metric_type', 'bins_count', 'bins_width', 'bucket_size', 'bucket_size_unit', 'buckets_archive'], name, value)


                        class Bucket(Entity):
                            """
                            Buckets stored for the metric
                            
                            .. attribute:: contents
                            
                            	The contents of the bucket; bins or samples
                            	**type**\:  :py:class:`Contents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents>`
                            
                            .. attribute:: start_at
                            
                            	Absolute time that the bucket started being filled at
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duration
                            
                            	Length of time for which the bucket is being filled in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: sent
                            
                            	Number of packets sent in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lost
                            
                            	Number of lost packets in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: corrupt
                            
                            	Number of corrupt packets in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_order
                            
                            	Number of packets recieved out\-of\-order in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplicates
                            
                            	Number of duplicate packets received in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: minimum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: maximum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: time_of_minimum
                            
                            	Absolute time that the minimum value was recorded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_of_maximum
                            
                            	Absolute time that the maximum value was recorded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: average
                            
                            	Mean of the results in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: standard_deviation
                            
                            	Standard deviation of the results in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: result_count
                            
                            	The count of samples collected in the bucket
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_sent_count
                            
                            	The number of data packets sent across the bucket, used in the calculation of overall FLR
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_lost_count
                            
                            	The number of data packets lost across the bucket, used in the calculation of overall FLR
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: overall_flr
                            
                            	Frame Loss Ratio across the whole bucket, in millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: percentage
                            
                            .. attribute:: suspect_start_mid_bucket
                            
                            	Results suspect due to a probe starting mid\-way through a bucket
                            	**type**\: bool
                            
                            .. attribute:: suspect_schedule_latency
                            
                            	Results suspect due to scheduling latency causing one or more packets to not be sent
                            	**type**\: bool
                            
                            .. attribute:: suspect_send_fail
                            
                            	Results suspect due to failure to send one or more packets
                            	**type**\: bool
                            
                            .. attribute:: suspect_premature_end
                            
                            	Results suspect due to a probe ending prematurely
                            	**type**\: bool
                            
                            .. attribute:: suspect_clock_drift
                            
                            	Results suspect as more than 10 seconds time drift detected
                            	**type**\: bool
                            
                            .. attribute:: suspect_memory_allocation_failed
                            
                            	Results suspect due to a memory allocation failure
                            	**type**\: bool
                            
                            .. attribute:: suspect_cleared_mid_bucket
                            
                            	Results suspect as bucket was cleared mid\-way through being filled
                            	**type**\: bool
                            
                            .. attribute:: suspect_probe_restarted
                            
                            	Results suspect as probe restarted mid\-way through the bucket
                            	**type**\: bool
                            
                            .. attribute:: suspect_management_latency
                            
                            	Results suspect as processing of results has been delayed
                            	**type**\: bool
                            
                            .. attribute:: suspect_multiple_buckets
                            
                            	Results suspect as the probe has been configured across multiple buckets
                            	**type**\: bool
                            
                            .. attribute:: suspect_misordering
                            
                            	Results suspect as misordering has been detected , affecting results
                            	**type**\: bool
                            
                            .. attribute:: suspect_flr_low_packet_count
                            
                            	Results suspect as FLR calculated based on a low packet count
                            	**type**\: bool
                            
                            .. attribute:: premature_reason
                            
                            	If the probe ended prematurely, the error that caused a probe to end
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: premature_reason_string
                            
                            	Description of the error code that caused the probe to end prematurely. For informational purposes only
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket, self).__init__()

                                self.yang_name = "bucket"
                                self.yang_parent_name = "operation-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("contents", ("contents", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents))])
                                self._leafs = OrderedDict([
                                    ('start_at', (YLeaf(YType.uint32, 'start-at'), ['int'])),
                                    ('duration', (YLeaf(YType.uint32, 'duration'), ['int'])),
                                    ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                    ('lost', (YLeaf(YType.uint32, 'lost'), ['int'])),
                                    ('corrupt', (YLeaf(YType.uint32, 'corrupt'), ['int'])),
                                    ('out_of_order', (YLeaf(YType.uint32, 'out-of-order'), ['int'])),
                                    ('duplicates', (YLeaf(YType.uint32, 'duplicates'), ['int'])),
                                    ('minimum', (YLeaf(YType.int32, 'minimum'), ['int'])),
                                    ('maximum', (YLeaf(YType.int32, 'maximum'), ['int'])),
                                    ('time_of_minimum', (YLeaf(YType.uint32, 'time-of-minimum'), ['int'])),
                                    ('time_of_maximum', (YLeaf(YType.uint32, 'time-of-maximum'), ['int'])),
                                    ('average', (YLeaf(YType.int32, 'average'), ['int'])),
                                    ('standard_deviation', (YLeaf(YType.int32, 'standard-deviation'), ['int'])),
                                    ('result_count', (YLeaf(YType.uint32, 'result-count'), ['int'])),
                                    ('data_sent_count', (YLeaf(YType.uint32, 'data-sent-count'), ['int'])),
                                    ('data_lost_count', (YLeaf(YType.uint32, 'data-lost-count'), ['int'])),
                                    ('overall_flr', (YLeaf(YType.int32, 'overall-flr'), ['int'])),
                                    ('suspect_start_mid_bucket', (YLeaf(YType.boolean, 'suspect-start-mid-bucket'), ['bool'])),
                                    ('suspect_schedule_latency', (YLeaf(YType.boolean, 'suspect-schedule-latency'), ['bool'])),
                                    ('suspect_send_fail', (YLeaf(YType.boolean, 'suspect-send-fail'), ['bool'])),
                                    ('suspect_premature_end', (YLeaf(YType.boolean, 'suspect-premature-end'), ['bool'])),
                                    ('suspect_clock_drift', (YLeaf(YType.boolean, 'suspect-clock-drift'), ['bool'])),
                                    ('suspect_memory_allocation_failed', (YLeaf(YType.boolean, 'suspect-memory-allocation-failed'), ['bool'])),
                                    ('suspect_cleared_mid_bucket', (YLeaf(YType.boolean, 'suspect-cleared-mid-bucket'), ['bool'])),
                                    ('suspect_probe_restarted', (YLeaf(YType.boolean, 'suspect-probe-restarted'), ['bool'])),
                                    ('suspect_management_latency', (YLeaf(YType.boolean, 'suspect-management-latency'), ['bool'])),
                                    ('suspect_multiple_buckets', (YLeaf(YType.boolean, 'suspect-multiple-buckets'), ['bool'])),
                                    ('suspect_misordering', (YLeaf(YType.boolean, 'suspect-misordering'), ['bool'])),
                                    ('suspect_flr_low_packet_count', (YLeaf(YType.boolean, 'suspect-flr-low-packet-count'), ['bool'])),
                                    ('premature_reason', (YLeaf(YType.uint32, 'premature-reason'), ['int'])),
                                    ('premature_reason_string', (YLeaf(YType.str, 'premature-reason-string'), ['str'])),
                                ])
                                self.start_at = None
                                self.duration = None
                                self.sent = None
                                self.lost = None
                                self.corrupt = None
                                self.out_of_order = None
                                self.duplicates = None
                                self.minimum = None
                                self.maximum = None
                                self.time_of_minimum = None
                                self.time_of_maximum = None
                                self.average = None
                                self.standard_deviation = None
                                self.result_count = None
                                self.data_sent_count = None
                                self.data_lost_count = None
                                self.overall_flr = None
                                self.suspect_start_mid_bucket = None
                                self.suspect_schedule_latency = None
                                self.suspect_send_fail = None
                                self.suspect_premature_end = None
                                self.suspect_clock_drift = None
                                self.suspect_memory_allocation_failed = None
                                self.suspect_cleared_mid_bucket = None
                                self.suspect_probe_restarted = None
                                self.suspect_management_latency = None
                                self.suspect_multiple_buckets = None
                                self.suspect_misordering = None
                                self.suspect_flr_low_packet_count = None
                                self.premature_reason = None
                                self.premature_reason_string = None

                                self.contents = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self._children_name_map["contents"] = "contents"
                                self._segment_path = lambda: "bucket"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket, ['start_at', 'duration', 'sent', 'lost', 'corrupt', 'out_of_order', 'duplicates', 'minimum', 'maximum', 'time_of_minimum', 'time_of_maximum', 'average', 'standard_deviation', 'result_count', 'data_sent_count', 'data_lost_count', 'overall_flr', 'suspect_start_mid_bucket', 'suspect_schedule_latency', 'suspect_send_fail', 'suspect_premature_end', 'suspect_clock_drift', 'suspect_memory_allocation_failed', 'suspect_cleared_mid_bucket', 'suspect_probe_restarted', 'suspect_management_latency', 'suspect_multiple_buckets', 'suspect_misordering', 'suspect_flr_low_packet_count', 'premature_reason', 'premature_reason_string'], name, value)


                            class Contents(Entity):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:  :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:  :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:  :py:class:`SlaOperBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucket>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents, self).__init__()

                                    self.yang_name = "contents"
                                    self.yang_parent_name = "bucket"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("aggregated", ("aggregated", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated)), ("unaggregated", ("unaggregated", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated))])
                                    self._leafs = OrderedDict([
                                        ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperBucket', '')])),
                                    ])
                                    self.bucket_type = None

                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self._children_name_map["aggregated"] = "aggregated"

                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self
                                    self._children_name_map["unaggregated"] = "unaggregated"
                                    self._segment_path = lambda: "contents"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents, ['bucket_type'], name, value)


                                class Aggregated(Entity):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of  		 :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated, self).__init__()

                                        self.yang_name = "aggregated"
                                        self.yang_parent_name = "contents"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("bins", ("bins", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins))])
                                        self._leafs = OrderedDict()

                                        self.bins = YList(self)
                                        self._segment_path = lambda: "aggregated"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/contents/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated, [], name, value)


                                    class Bins(Entity):
                                        """
                                        The bins of an SLA metric bucket
                                        
                                        .. attribute:: lower_bound
                                        
                                        	Lower bound (inclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: upper_bound
                                        
                                        	Upper bound (exclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: lower_bound_tenths
                                        
                                        	Lower bound (inclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: upper_bound_tenths
                                        
                                        	Upper bound (exclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: sum
                                        
                                        	The sum of the results in the bin, in microseconds or millionths of a percent
                                        	**type**\: int
                                        
                                        	**range:** \-9223372036854775808..9223372036854775807
                                        
                                        .. attribute:: count
                                        
                                        	The total number of results in the bin
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2017-10-06'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__init__()

                                            self.yang_name = "bins"
                                            self.yang_parent_name = "aggregated"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('lower_bound', (YLeaf(YType.int32, 'lower-bound'), ['int'])),
                                                ('upper_bound', (YLeaf(YType.int32, 'upper-bound'), ['int'])),
                                                ('lower_bound_tenths', (YLeaf(YType.int32, 'lower-bound-tenths'), ['int'])),
                                                ('upper_bound_tenths', (YLeaf(YType.int32, 'upper-bound-tenths'), ['int'])),
                                                ('sum', (YLeaf(YType.int64, 'sum'), ['int'])),
                                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ])
                                            self.lower_bound = None
                                            self.upper_bound = None
                                            self.lower_bound_tenths = None
                                            self.upper_bound_tenths = None
                                            self.sum = None
                                            self.count = None
                                            self._segment_path = lambda: "bins"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/contents/aggregated/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, ['lower_bound', 'upper_bound', 'lower_bound_tenths', 'upper_bound_tenths', 'sum', 'count'], name, value)


                                class Unaggregated(Entity):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated, self).__init__()

                                        self.yang_name = "unaggregated"
                                        self.yang_parent_name = "contents"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("sample", ("sample", Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample))])
                                        self._leafs = OrderedDict()

                                        self.sample = YList(self)
                                        self._segment_path = lambda: "unaggregated"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/contents/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated, [], name, value)


                                    class Sample(Entity):
                                        """
                                        The samples of an SLA metric bucket
                                        
                                        .. attribute:: sent_at
                                        
                                        	The time (in milliseconds relative to the start time of the bucket) that the sample was sent at
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: sent
                                        
                                        	Whether the sample packet was sucessfully sent
                                        	**type**\: bool
                                        
                                        .. attribute:: timed_out
                                        
                                        	Whether the sample packet timed out
                                        	**type**\: bool
                                        
                                        .. attribute:: corrupt
                                        
                                        	Whether the sample packet was corrupt
                                        	**type**\: bool
                                        
                                        .. attribute:: out_of_order
                                        
                                        	Whether the sample packet was received out\-of\-order
                                        	**type**\: bool
                                        
                                        .. attribute:: no_data_packets
                                        
                                        	Whether a measurement could not be made because no data packets were sent in the sample period. Only applicable for LMM measurements
                                        	**type**\: bool
                                        
                                        .. attribute:: result
                                        
                                        	The result (in microseconds or millionths of a percent) of the sample, if available
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: frames_sent
                                        
                                        	For FLR measurements, the number of frames sent, if available
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: frames_lost
                                        
                                        	For FLR measurements, the number of frames lost, if available
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2017-10-06'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__init__()

                                            self.yang_name = "sample"
                                            self.yang_parent_name = "unaggregated"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sent_at', (YLeaf(YType.uint32, 'sent-at'), ['int'])),
                                                ('sent', (YLeaf(YType.boolean, 'sent'), ['bool'])),
                                                ('timed_out', (YLeaf(YType.boolean, 'timed-out'), ['bool'])),
                                                ('corrupt', (YLeaf(YType.boolean, 'corrupt'), ['bool'])),
                                                ('out_of_order', (YLeaf(YType.boolean, 'out-of-order'), ['bool'])),
                                                ('no_data_packets', (YLeaf(YType.boolean, 'no-data-packets'), ['bool'])),
                                                ('result', (YLeaf(YType.int32, 'result'), ['int'])),
                                                ('frames_sent', (YLeaf(YType.uint32, 'frames-sent'), ['int'])),
                                                ('frames_lost', (YLeaf(YType.uint32, 'frames-lost'), ['int'])),
                                            ])
                                            self.sent_at = None
                                            self.sent = None
                                            self.timed_out = None
                                            self.corrupt = None
                                            self.out_of_order = None
                                            self.no_data_packets = None
                                            self.result = None
                                            self.frames_sent = None
                                            self.frames_lost = None
                                            self._segment_path = lambda: "sample"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-currents/statistics-on-demand-current/operation-metric/bucket/contents/unaggregated/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, ['sent_at', 'sent', 'timed_out', 'corrupt', 'out_of_order', 'no_data_packets', 'result', 'frames_sent', 'frames_lost'], name, value)


            class Operations(Entity):
                """
                Table of SLA operations
                
                .. attribute:: operation_
                
                	SLA operation to get operation data for
                	**type**\: list of  		 :py:class:`Operation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.Operations, self).__init__()

                    self.yang_name = "operations"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("operation", ("operation_", Sla.Protocols.Ethernet.Operations.Operation))])
                    self._leafs = OrderedDict()

                    self.operation_ = YList(self)
                    self._segment_path = lambda: "operations"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sla.Protocols.Ethernet.Operations, [], name, value)


                class Operation(Entity):
                    """
                    SLA operation to get operation data for
                    
                    .. attribute:: profile_name
                    
                    	Profile Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\: int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: profile_options
                    
                    	Options that are only valid if the operation has a profile
                    	**type**\:  :py:class:`ProfileOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions>`
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:  :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions>`
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: last_run
                    
                    	Time that the last probe for the operation was run, NULL if never run
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.Operations.Operation, self).__init__()

                        self.yang_name = "operation"
                        self.yang_parent_name = "operations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("profile-options", ("profile_options", Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions)), ("specific-options", ("specific_options", Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions))])
                        self._leafs = OrderedDict([
                            ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('display_short', (YLeaf(YType.str, 'display-short'), ['str'])),
                            ('display_long', (YLeaf(YType.str, 'display-long'), ['str'])),
                            ('last_run', (YLeaf(YType.uint32, 'last-run'), ['int'])),
                        ])
                        self.profile_name = None
                        self.domain_name = None
                        self.interface_name = None
                        self.mep_id = None
                        self.mac_address = None
                        self.display_short = None
                        self.display_long = None
                        self.last_run = None

                        self.profile_options = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions()
                        self.profile_options.parent = self
                        self._children_name_map["profile_options"] = "profile-options"

                        self.specific_options = Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"
                        self._segment_path = lambda: "operation"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation, ['profile_name', 'domain_name', 'interface_name', 'mep_id', 'mac_address', 'display_short', 'display_long', 'last_run'], name, value)


                    class ProfileOptions(Entity):
                        """
                        Options that are only valid if the operation has
                        a profile
                        
                        .. attribute:: packet_padding
                        
                        	Configuration of the packet padding
                        	**type**\:  :py:class:`PacketPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding>`
                        
                        .. attribute:: priority
                        
                        	Priority at which to send the packet, if configured
                        	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority>`
                        
                        .. attribute:: operation_schedule
                        
                        	Operation schedule
                        	**type**\:  :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule>`
                        
                        .. attribute:: probe_type
                        
                        	Type of probe used by the operation
                        	**type**\: str
                        
                        .. attribute:: packets_per_burst
                        
                        	Number of packets sent per burst
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: inter_packet_interval
                        
                        	Interval between packets within a burst in milliseconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**units**\: millisecond
                        
                        .. attribute:: bursts_per_probe
                        
                        	Number of bursts sent per probe
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inter_burst_interval
                        
                        	Interval between bursts within a probe in milliseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: flr_calculation_interval
                        
                        	Interval between FLR calculations for SLM, in milliseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: operation_metric
                        
                        	Array of the metrics that are measured by the operation
                        	**type**\: list of  		 :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions, self).__init__()

                            self.yang_name = "profile-options"
                            self.yang_parent_name = "operation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("packet-padding", ("packet_padding", Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding)), ("priority", ("priority", Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority)), ("operation-schedule", ("operation_schedule", Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule)), ("operation-metric", ("operation_metric", Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric))])
                            self._leafs = OrderedDict([
                                ('probe_type', (YLeaf(YType.str, 'probe-type'), ['str'])),
                                ('packets_per_burst', (YLeaf(YType.uint16, 'packets-per-burst'), ['int'])),
                                ('inter_packet_interval', (YLeaf(YType.uint16, 'inter-packet-interval'), ['int'])),
                                ('bursts_per_probe', (YLeaf(YType.uint32, 'bursts-per-probe'), ['int'])),
                                ('inter_burst_interval', (YLeaf(YType.uint32, 'inter-burst-interval'), ['int'])),
                                ('flr_calculation_interval', (YLeaf(YType.uint32, 'flr-calculation-interval'), ['int'])),
                            ])
                            self.probe_type = None
                            self.packets_per_burst = None
                            self.inter_packet_interval = None
                            self.bursts_per_probe = None
                            self.inter_burst_interval = None
                            self.flr_calculation_interval = None

                            self.packet_padding = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding()
                            self.packet_padding.parent = self
                            self._children_name_map["packet_padding"] = "packet-padding"

                            self.priority = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority()
                            self.priority.parent = self
                            self._children_name_map["priority"] = "priority"

                            self.operation_schedule = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule()
                            self.operation_schedule.parent = self
                            self._children_name_map["operation_schedule"] = "operation-schedule"

                            self.operation_metric = YList(self)
                            self._segment_path = lambda: "profile-options"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions, ['probe_type', 'packets_per_burst', 'inter_packet_interval', 'bursts_per_probe', 'inter_burst_interval', 'flr_calculation_interval'], name, value)


                        class PacketPadding(Entity):
                            """
                            Configuration of the packet padding
                            
                            .. attribute:: packet_pad_size
                            
                            	Size that packets are being padded to
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: test_pattern_pad_scheme
                            
                            	Test pattern scheme that is used in the packet padding
                            	**type**\:  :py:class:`SlaOperTestPatternScheme <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperTestPatternScheme>`
                            
                            .. attribute:: test_pattern_pad_hex_string
                            
                            	Hex string that is used in the packet padding
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding, self).__init__()

                                self.yang_name = "packet-padding"
                                self.yang_parent_name = "profile-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packet_pad_size', (YLeaf(YType.uint16, 'packet-pad-size'), ['int'])),
                                    ('test_pattern_pad_scheme', (YLeaf(YType.enumeration, 'test-pattern-pad-scheme'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperTestPatternScheme', '')])),
                                    ('test_pattern_pad_hex_string', (YLeaf(YType.uint32, 'test-pattern-pad-hex-string'), ['int'])),
                                ])
                                self.packet_pad_size = None
                                self.test_pattern_pad_scheme = None
                                self.test_pattern_pad_hex_string = None
                                self._segment_path = lambda: "packet-padding"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding, ['packet_pad_size', 'test_pattern_pad_scheme', 'test_pattern_pad_hex_string'], name, value)


                        class Priority(Entity):
                            """
                            Priority at which to send the packet, if
                            configured
                            
                            .. attribute:: priority_type
                            
                            	PriorityType
                            	**type**\:  :py:class:`SlaOperPacketPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperPacketPriority>`
                            
                            .. attribute:: cos
                            
                            	3\-bit COS priority value applied to packets
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "profile-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('priority_type', (YLeaf(YType.enumeration, 'priority-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperPacketPriority', '')])),
                                    ('cos', (YLeaf(YType.uint8, 'cos'), ['int'])),
                                ])
                                self.priority_type = None
                                self.cos = None
                                self._segment_path = lambda: "priority"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority, ['priority_type', 'cos'], name, value)


                        class OperationSchedule(Entity):
                            """
                            Operation schedule
                            
                            .. attribute:: start_time
                            
                            	Start time of the first probe, in seconds since the Unix Epoch
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: start_time_configured
                            
                            	Whether or not the operation start time was explicitly configured
                            	**type**\: bool
                            
                            .. attribute:: schedule_duration
                            
                            	Duration of a probe for the operation in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: schedule_interval
                            
                            	Interval between the start times of consecutive probes,  in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule, self).__init__()

                                self.yang_name = "operation-schedule"
                                self.yang_parent_name = "profile-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                                    ('start_time_configured', (YLeaf(YType.boolean, 'start-time-configured'), ['bool'])),
                                    ('schedule_duration', (YLeaf(YType.uint32, 'schedule-duration'), ['int'])),
                                    ('schedule_interval', (YLeaf(YType.uint32, 'schedule-interval'), ['int'])),
                                ])
                                self.start_time = None
                                self.start_time_configured = None
                                self.schedule_duration = None
                                self.schedule_interval = None
                                self._segment_path = lambda: "operation-schedule"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule, ['start_time', 'start_time_configured', 'schedule_duration', 'schedule_interval'], name, value)


                        class OperationMetric(Entity):
                            """
                            Array of the metrics that are measured by the
                            operation
                            
                            .. attribute:: metric_config
                            
                            	Configuration of the metric
                            	**type**\:  :py:class:`MetricConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig>`
                            
                            .. attribute:: current_buckets_archive
                            
                            	Number of valid buckets currently in the buckets archive
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric, self).__init__()

                                self.yang_name = "operation-metric"
                                self.yang_parent_name = "profile-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("metric-config", ("metric_config", Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig))])
                                self._leafs = OrderedDict([
                                    ('current_buckets_archive', (YLeaf(YType.uint32, 'current-buckets-archive'), ['int'])),
                                ])
                                self.current_buckets_archive = None

                                self.metric_config = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig()
                                self.metric_config.parent = self
                                self._children_name_map["metric_config"] = "metric-config"
                                self._segment_path = lambda: "operation-metric"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric, ['current_buckets_archive'], name, value)


                            class MetricConfig(Entity):
                                """
                                Configuration of the metric
                                
                                .. attribute:: metric_type
                                
                                	Type of metric to which this configuration applies
                                	**type**\:  :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                                
                                .. attribute:: bins_count
                                
                                	Total number of bins into which to aggregate. 0 if no aggregation
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: bins_width
                                
                                	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: bucket_size
                                
                                	Size of buckets into which measurements are collected
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: bucket_size_unit
                                
                                	Whether bucket size is 'per\-probe' or 'probes'
                                	**type**\:  :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                                
                                .. attribute:: buckets_archive
                                
                                	Maximum number of buckets to store in memory
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig, self).__init__()

                                    self.yang_name = "metric-config"
                                    self.yang_parent_name = "operation-metric"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric', '')])),
                                        ('bins_count', (YLeaf(YType.uint16, 'bins-count'), ['int'])),
                                        ('bins_width', (YLeaf(YType.uint16, 'bins-width'), ['int'])),
                                        ('bucket_size', (YLeaf(YType.uint8, 'bucket-size'), ['int'])),
                                        ('bucket_size_unit', (YLeaf(YType.enumeration, 'bucket-size-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize', '')])),
                                        ('buckets_archive', (YLeaf(YType.uint32, 'buckets-archive'), ['int'])),
                                    ])
                                    self.metric_type = None
                                    self.bins_count = None
                                    self.bins_width = None
                                    self.bucket_size = None
                                    self.bucket_size_unit = None
                                    self.buckets_archive = None
                                    self._segment_path = lambda: "metric-config"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/profile-options/operation-metric/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig, ['metric_type', 'bins_count', 'bins_width', 'bucket_size', 'bucket_size_unit', 'buckets_archive'], name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:  :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:  :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:  :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "operation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("configured-operation-options", ("configured_operation_options", Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions)), ("ondemand-operation-options", ("ondemand_operation_options", Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions))])
                            self._leafs = OrderedDict([
                                ('oper_type', (YLeaf(YType.enumeration, 'oper-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation', '')])),
                            ])
                            self.oper_type = None

                            self.configured_operation_options = Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._segment_path = lambda: "specific-options"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions, ['oper_type'], name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "configured-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions, ['profile_name'], name, value)


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ondemand_operation_id', (YLeaf(YType.uint32, 'ondemand-operation-id'), ['int'])),
                                    ('probe_count', (YLeaf(YType.uint8, 'probe-count'), ['int'])),
                                ])
                                self.ondemand_operation_id = None
                                self.probe_count = None
                                self._segment_path = lambda: "ondemand-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/operations/operation/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions, ['ondemand_operation_id', 'probe_count'], name, value)


            class StatisticsHistoricals(Entity):
                """
                Table of historical statistics for SLA
                operations
                
                .. attribute:: statistics_historical
                
                	Historical statistics data for an SLA configured operation
                	**type**\: list of  		 :py:class:`StatisticsHistorical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.StatisticsHistoricals, self).__init__()

                    self.yang_name = "statistics-historicals"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics-historical", ("statistics_historical", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical))])
                    self._leafs = OrderedDict()

                    self.statistics_historical = YList(self)
                    self._segment_path = lambda: "statistics-historicals"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals, [], name, value)


                class StatisticsHistorical(Entity):
                    """
                    Historical statistics data for an SLA
                    configured operation
                    
                    .. attribute:: profile_name
                    
                    	Profile Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\: int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:  :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions>`
                    
                    .. attribute:: operation_schedule
                    
                    	Operation schedule
                    	**type**\:  :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule>`
                    
                    .. attribute:: probe_type
                    
                    	Type of probe used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: flr_calculation_interval
                    
                    	Interval between FLR calculations for SLM, in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: operation_metric
                    
                    	Metrics gathered for the operation
                    	**type**\: list of  		 :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical, self).__init__()

                        self.yang_name = "statistics-historical"
                        self.yang_parent_name = "statistics-historicals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("specific-options", ("specific_options", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions)), ("operation-schedule", ("operation_schedule", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule)), ("operation-metric", ("operation_metric", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric))])
                        self._leafs = OrderedDict([
                            ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('probe_type', (YLeaf(YType.str, 'probe-type'), ['str'])),
                            ('display_short', (YLeaf(YType.str, 'display-short'), ['str'])),
                            ('display_long', (YLeaf(YType.str, 'display-long'), ['str'])),
                            ('flr_calculation_interval', (YLeaf(YType.uint32, 'flr-calculation-interval'), ['int'])),
                        ])
                        self.profile_name = None
                        self.domain_name = None
                        self.interface_name = None
                        self.mep_id = None
                        self.mac_address = None
                        self.probe_type = None
                        self.display_short = None
                        self.display_long = None
                        self.flr_calculation_interval = None

                        self.specific_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"

                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule()
                        self.operation_schedule.parent = self
                        self._children_name_map["operation_schedule"] = "operation-schedule"

                        self.operation_metric = YList(self)
                        self._segment_path = lambda: "statistics-historical"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical, ['profile_name', 'domain_name', 'interface_name', 'mep_id', 'mac_address', 'probe_type', 'display_short', 'display_long', 'flr_calculation_interval'], name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:  :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:  :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:  :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "statistics-historical"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("configured-operation-options", ("configured_operation_options", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions)), ("ondemand-operation-options", ("ondemand_operation_options", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions))])
                            self._leafs = OrderedDict([
                                ('oper_type', (YLeaf(YType.enumeration, 'oper-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation', '')])),
                            ])
                            self.oper_type = None

                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._segment_path = lambda: "specific-options"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions, ['oper_type'], name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "configured-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions, ['profile_name'], name, value)


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ondemand_operation_id', (YLeaf(YType.uint32, 'ondemand-operation-id'), ['int'])),
                                    ('probe_count', (YLeaf(YType.uint8, 'probe-count'), ['int'])),
                                ])
                                self.ondemand_operation_id = None
                                self.probe_count = None
                                self._segment_path = lambda: "ondemand-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions, ['ondemand_operation_id', 'probe_count'], name, value)


                    class OperationSchedule(Entity):
                        """
                        Operation schedule
                        
                        .. attribute:: start_time
                        
                        	Start time of the first probe, in seconds since the Unix Epoch
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time_configured
                        
                        	Whether or not the operation start time was explicitly configured
                        	**type**\: bool
                        
                        .. attribute:: schedule_duration
                        
                        	Duration of a probe for the operation in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: schedule_interval
                        
                        	Interval between the start times of consecutive probes,  in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule, self).__init__()

                            self.yang_name = "operation-schedule"
                            self.yang_parent_name = "statistics-historical"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                                ('start_time_configured', (YLeaf(YType.boolean, 'start-time-configured'), ['bool'])),
                                ('schedule_duration', (YLeaf(YType.uint32, 'schedule-duration'), ['int'])),
                                ('schedule_interval', (YLeaf(YType.uint32, 'schedule-interval'), ['int'])),
                            ])
                            self.start_time = None
                            self.start_time_configured = None
                            self.schedule_duration = None
                            self.schedule_interval = None
                            self._segment_path = lambda: "operation-schedule"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule, ['start_time', 'start_time_configured', 'schedule_duration', 'schedule_interval'], name, value)


                    class OperationMetric(Entity):
                        """
                        Metrics gathered for the operation
                        
                        .. attribute:: config
                        
                        	Configuration of the metric
                        	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config>`
                        
                        .. attribute:: bucket
                        
                        	Buckets stored for the metric
                        	**type**\: list of  		 :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric, self).__init__()

                            self.yang_name = "operation-metric"
                            self.yang_parent_name = "statistics-historical"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config)), ("bucket", ("bucket", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket))])
                            self._leafs = OrderedDict()

                            self.config = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.bucket = YList(self)
                            self._segment_path = lambda: "operation-metric"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric, [], name, value)


                        class Config(Entity):
                            """
                            Configuration of the metric
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:  :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                            
                            .. attribute:: bins_count
                            
                            	Total number of bins into which to aggregate. 0 if no aggregation
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bins_width
                            
                            	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bucket_size
                            
                            	Size of buckets into which measurements are collected
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: bucket_size_unit
                            
                            	Whether bucket size is 'per\-probe' or 'probes'
                            	**type**\:  :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "operation-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric', '')])),
                                    ('bins_count', (YLeaf(YType.uint16, 'bins-count'), ['int'])),
                                    ('bins_width', (YLeaf(YType.uint16, 'bins-width'), ['int'])),
                                    ('bucket_size', (YLeaf(YType.uint8, 'bucket-size'), ['int'])),
                                    ('bucket_size_unit', (YLeaf(YType.enumeration, 'bucket-size-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize', '')])),
                                    ('buckets_archive', (YLeaf(YType.uint32, 'buckets-archive'), ['int'])),
                                ])
                                self.metric_type = None
                                self.bins_count = None
                                self.bins_width = None
                                self.bucket_size = None
                                self.bucket_size_unit = None
                                self.buckets_archive = None
                                self._segment_path = lambda: "config"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config, ['metric_type', 'bins_count', 'bins_width', 'bucket_size', 'bucket_size_unit', 'buckets_archive'], name, value)


                        class Bucket(Entity):
                            """
                            Buckets stored for the metric
                            
                            .. attribute:: contents
                            
                            	The contents of the bucket; bins or samples
                            	**type**\:  :py:class:`Contents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents>`
                            
                            .. attribute:: start_at
                            
                            	Absolute time that the bucket started being filled at
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duration
                            
                            	Length of time for which the bucket is being filled in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: sent
                            
                            	Number of packets sent in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lost
                            
                            	Number of lost packets in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: corrupt
                            
                            	Number of corrupt packets in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_order
                            
                            	Number of packets recieved out\-of\-order in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplicates
                            
                            	Number of duplicate packets received in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: minimum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: maximum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: time_of_minimum
                            
                            	Absolute time that the minimum value was recorded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_of_maximum
                            
                            	Absolute time that the maximum value was recorded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: average
                            
                            	Mean of the results in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: standard_deviation
                            
                            	Standard deviation of the results in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: result_count
                            
                            	The count of samples collected in the bucket
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_sent_count
                            
                            	The number of data packets sent across the bucket, used in the calculation of overall FLR
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_lost_count
                            
                            	The number of data packets lost across the bucket, used in the calculation of overall FLR
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: overall_flr
                            
                            	Frame Loss Ratio across the whole bucket, in millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: percentage
                            
                            .. attribute:: suspect_start_mid_bucket
                            
                            	Results suspect due to a probe starting mid\-way through a bucket
                            	**type**\: bool
                            
                            .. attribute:: suspect_schedule_latency
                            
                            	Results suspect due to scheduling latency causing one or more packets to not be sent
                            	**type**\: bool
                            
                            .. attribute:: suspect_send_fail
                            
                            	Results suspect due to failure to send one or more packets
                            	**type**\: bool
                            
                            .. attribute:: suspect_premature_end
                            
                            	Results suspect due to a probe ending prematurely
                            	**type**\: bool
                            
                            .. attribute:: suspect_clock_drift
                            
                            	Results suspect as more than 10 seconds time drift detected
                            	**type**\: bool
                            
                            .. attribute:: suspect_memory_allocation_failed
                            
                            	Results suspect due to a memory allocation failure
                            	**type**\: bool
                            
                            .. attribute:: suspect_cleared_mid_bucket
                            
                            	Results suspect as bucket was cleared mid\-way through being filled
                            	**type**\: bool
                            
                            .. attribute:: suspect_probe_restarted
                            
                            	Results suspect as probe restarted mid\-way through the bucket
                            	**type**\: bool
                            
                            .. attribute:: suspect_management_latency
                            
                            	Results suspect as processing of results has been delayed
                            	**type**\: bool
                            
                            .. attribute:: suspect_multiple_buckets
                            
                            	Results suspect as the probe has been configured across multiple buckets
                            	**type**\: bool
                            
                            .. attribute:: suspect_misordering
                            
                            	Results suspect as misordering has been detected , affecting results
                            	**type**\: bool
                            
                            .. attribute:: suspect_flr_low_packet_count
                            
                            	Results suspect as FLR calculated based on a low packet count
                            	**type**\: bool
                            
                            .. attribute:: premature_reason
                            
                            	If the probe ended prematurely, the error that caused a probe to end
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: premature_reason_string
                            
                            	Description of the error code that caused the probe to end prematurely. For informational purposes only
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket, self).__init__()

                                self.yang_name = "bucket"
                                self.yang_parent_name = "operation-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("contents", ("contents", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents))])
                                self._leafs = OrderedDict([
                                    ('start_at', (YLeaf(YType.uint32, 'start-at'), ['int'])),
                                    ('duration', (YLeaf(YType.uint32, 'duration'), ['int'])),
                                    ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                    ('lost', (YLeaf(YType.uint32, 'lost'), ['int'])),
                                    ('corrupt', (YLeaf(YType.uint32, 'corrupt'), ['int'])),
                                    ('out_of_order', (YLeaf(YType.uint32, 'out-of-order'), ['int'])),
                                    ('duplicates', (YLeaf(YType.uint32, 'duplicates'), ['int'])),
                                    ('minimum', (YLeaf(YType.int32, 'minimum'), ['int'])),
                                    ('maximum', (YLeaf(YType.int32, 'maximum'), ['int'])),
                                    ('time_of_minimum', (YLeaf(YType.uint32, 'time-of-minimum'), ['int'])),
                                    ('time_of_maximum', (YLeaf(YType.uint32, 'time-of-maximum'), ['int'])),
                                    ('average', (YLeaf(YType.int32, 'average'), ['int'])),
                                    ('standard_deviation', (YLeaf(YType.int32, 'standard-deviation'), ['int'])),
                                    ('result_count', (YLeaf(YType.uint32, 'result-count'), ['int'])),
                                    ('data_sent_count', (YLeaf(YType.uint32, 'data-sent-count'), ['int'])),
                                    ('data_lost_count', (YLeaf(YType.uint32, 'data-lost-count'), ['int'])),
                                    ('overall_flr', (YLeaf(YType.int32, 'overall-flr'), ['int'])),
                                    ('suspect_start_mid_bucket', (YLeaf(YType.boolean, 'suspect-start-mid-bucket'), ['bool'])),
                                    ('suspect_schedule_latency', (YLeaf(YType.boolean, 'suspect-schedule-latency'), ['bool'])),
                                    ('suspect_send_fail', (YLeaf(YType.boolean, 'suspect-send-fail'), ['bool'])),
                                    ('suspect_premature_end', (YLeaf(YType.boolean, 'suspect-premature-end'), ['bool'])),
                                    ('suspect_clock_drift', (YLeaf(YType.boolean, 'suspect-clock-drift'), ['bool'])),
                                    ('suspect_memory_allocation_failed', (YLeaf(YType.boolean, 'suspect-memory-allocation-failed'), ['bool'])),
                                    ('suspect_cleared_mid_bucket', (YLeaf(YType.boolean, 'suspect-cleared-mid-bucket'), ['bool'])),
                                    ('suspect_probe_restarted', (YLeaf(YType.boolean, 'suspect-probe-restarted'), ['bool'])),
                                    ('suspect_management_latency', (YLeaf(YType.boolean, 'suspect-management-latency'), ['bool'])),
                                    ('suspect_multiple_buckets', (YLeaf(YType.boolean, 'suspect-multiple-buckets'), ['bool'])),
                                    ('suspect_misordering', (YLeaf(YType.boolean, 'suspect-misordering'), ['bool'])),
                                    ('suspect_flr_low_packet_count', (YLeaf(YType.boolean, 'suspect-flr-low-packet-count'), ['bool'])),
                                    ('premature_reason', (YLeaf(YType.uint32, 'premature-reason'), ['int'])),
                                    ('premature_reason_string', (YLeaf(YType.str, 'premature-reason-string'), ['str'])),
                                ])
                                self.start_at = None
                                self.duration = None
                                self.sent = None
                                self.lost = None
                                self.corrupt = None
                                self.out_of_order = None
                                self.duplicates = None
                                self.minimum = None
                                self.maximum = None
                                self.time_of_minimum = None
                                self.time_of_maximum = None
                                self.average = None
                                self.standard_deviation = None
                                self.result_count = None
                                self.data_sent_count = None
                                self.data_lost_count = None
                                self.overall_flr = None
                                self.suspect_start_mid_bucket = None
                                self.suspect_schedule_latency = None
                                self.suspect_send_fail = None
                                self.suspect_premature_end = None
                                self.suspect_clock_drift = None
                                self.suspect_memory_allocation_failed = None
                                self.suspect_cleared_mid_bucket = None
                                self.suspect_probe_restarted = None
                                self.suspect_management_latency = None
                                self.suspect_multiple_buckets = None
                                self.suspect_misordering = None
                                self.suspect_flr_low_packet_count = None
                                self.premature_reason = None
                                self.premature_reason_string = None

                                self.contents = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self._children_name_map["contents"] = "contents"
                                self._segment_path = lambda: "bucket"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket, ['start_at', 'duration', 'sent', 'lost', 'corrupt', 'out_of_order', 'duplicates', 'minimum', 'maximum', 'time_of_minimum', 'time_of_maximum', 'average', 'standard_deviation', 'result_count', 'data_sent_count', 'data_lost_count', 'overall_flr', 'suspect_start_mid_bucket', 'suspect_schedule_latency', 'suspect_send_fail', 'suspect_premature_end', 'suspect_clock_drift', 'suspect_memory_allocation_failed', 'suspect_cleared_mid_bucket', 'suspect_probe_restarted', 'suspect_management_latency', 'suspect_multiple_buckets', 'suspect_misordering', 'suspect_flr_low_packet_count', 'premature_reason', 'premature_reason_string'], name, value)


                            class Contents(Entity):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:  :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:  :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:  :py:class:`SlaOperBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucket>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents, self).__init__()

                                    self.yang_name = "contents"
                                    self.yang_parent_name = "bucket"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("aggregated", ("aggregated", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated)), ("unaggregated", ("unaggregated", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated))])
                                    self._leafs = OrderedDict([
                                        ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperBucket', '')])),
                                    ])
                                    self.bucket_type = None

                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self._children_name_map["aggregated"] = "aggregated"

                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self
                                    self._children_name_map["unaggregated"] = "unaggregated"
                                    self._segment_path = lambda: "contents"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents, ['bucket_type'], name, value)


                                class Aggregated(Entity):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of  		 :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated, self).__init__()

                                        self.yang_name = "aggregated"
                                        self.yang_parent_name = "contents"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("bins", ("bins", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins))])
                                        self._leafs = OrderedDict()

                                        self.bins = YList(self)
                                        self._segment_path = lambda: "aggregated"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/contents/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated, [], name, value)


                                    class Bins(Entity):
                                        """
                                        The bins of an SLA metric bucket
                                        
                                        .. attribute:: lower_bound
                                        
                                        	Lower bound (inclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: upper_bound
                                        
                                        	Upper bound (exclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: lower_bound_tenths
                                        
                                        	Lower bound (inclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: upper_bound_tenths
                                        
                                        	Upper bound (exclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: sum
                                        
                                        	The sum of the results in the bin, in microseconds or millionths of a percent
                                        	**type**\: int
                                        
                                        	**range:** \-9223372036854775808..9223372036854775807
                                        
                                        .. attribute:: count
                                        
                                        	The total number of results in the bin
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2017-10-06'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__init__()

                                            self.yang_name = "bins"
                                            self.yang_parent_name = "aggregated"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('lower_bound', (YLeaf(YType.int32, 'lower-bound'), ['int'])),
                                                ('upper_bound', (YLeaf(YType.int32, 'upper-bound'), ['int'])),
                                                ('lower_bound_tenths', (YLeaf(YType.int32, 'lower-bound-tenths'), ['int'])),
                                                ('upper_bound_tenths', (YLeaf(YType.int32, 'upper-bound-tenths'), ['int'])),
                                                ('sum', (YLeaf(YType.int64, 'sum'), ['int'])),
                                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ])
                                            self.lower_bound = None
                                            self.upper_bound = None
                                            self.lower_bound_tenths = None
                                            self.upper_bound_tenths = None
                                            self.sum = None
                                            self.count = None
                                            self._segment_path = lambda: "bins"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/contents/aggregated/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, ['lower_bound', 'upper_bound', 'lower_bound_tenths', 'upper_bound_tenths', 'sum', 'count'], name, value)


                                class Unaggregated(Entity):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated, self).__init__()

                                        self.yang_name = "unaggregated"
                                        self.yang_parent_name = "contents"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("sample", ("sample", Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample))])
                                        self._leafs = OrderedDict()

                                        self.sample = YList(self)
                                        self._segment_path = lambda: "unaggregated"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/contents/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated, [], name, value)


                                    class Sample(Entity):
                                        """
                                        The samples of an SLA metric bucket
                                        
                                        .. attribute:: sent_at
                                        
                                        	The time (in milliseconds relative to the start time of the bucket) that the sample was sent at
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: sent
                                        
                                        	Whether the sample packet was sucessfully sent
                                        	**type**\: bool
                                        
                                        .. attribute:: timed_out
                                        
                                        	Whether the sample packet timed out
                                        	**type**\: bool
                                        
                                        .. attribute:: corrupt
                                        
                                        	Whether the sample packet was corrupt
                                        	**type**\: bool
                                        
                                        .. attribute:: out_of_order
                                        
                                        	Whether the sample packet was received out\-of\-order
                                        	**type**\: bool
                                        
                                        .. attribute:: no_data_packets
                                        
                                        	Whether a measurement could not be made because no data packets were sent in the sample period. Only applicable for LMM measurements
                                        	**type**\: bool
                                        
                                        .. attribute:: result
                                        
                                        	The result (in microseconds or millionths of a percent) of the sample, if available
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: frames_sent
                                        
                                        	For FLR measurements, the number of frames sent, if available
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: frames_lost
                                        
                                        	For FLR measurements, the number of frames lost, if available
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2017-10-06'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__init__()

                                            self.yang_name = "sample"
                                            self.yang_parent_name = "unaggregated"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sent_at', (YLeaf(YType.uint32, 'sent-at'), ['int'])),
                                                ('sent', (YLeaf(YType.boolean, 'sent'), ['bool'])),
                                                ('timed_out', (YLeaf(YType.boolean, 'timed-out'), ['bool'])),
                                                ('corrupt', (YLeaf(YType.boolean, 'corrupt'), ['bool'])),
                                                ('out_of_order', (YLeaf(YType.boolean, 'out-of-order'), ['bool'])),
                                                ('no_data_packets', (YLeaf(YType.boolean, 'no-data-packets'), ['bool'])),
                                                ('result', (YLeaf(YType.int32, 'result'), ['int'])),
                                                ('frames_sent', (YLeaf(YType.uint32, 'frames-sent'), ['int'])),
                                                ('frames_lost', (YLeaf(YType.uint32, 'frames-lost'), ['int'])),
                                            ])
                                            self.sent_at = None
                                            self.sent = None
                                            self.timed_out = None
                                            self.corrupt = None
                                            self.out_of_order = None
                                            self.no_data_packets = None
                                            self.result = None
                                            self.frames_sent = None
                                            self.frames_lost = None
                                            self._segment_path = lambda: "sample"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-historicals/statistics-historical/operation-metric/bucket/contents/unaggregated/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, ['sent_at', 'sent', 'timed_out', 'corrupt', 'out_of_order', 'no_data_packets', 'result', 'frames_sent', 'frames_lost'], name, value)


            class StatisticsOnDemandHistoricals(Entity):
                """
                Table of historical statistics for SLA
                on\-demand operations
                
                .. attribute:: statistics_on_demand_historical
                
                	Historical statistics data for an SLA on\-demand  operation
                	**type**\: list of  		 :py:class:`StatisticsOnDemandHistorical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals, self).__init__()

                    self.yang_name = "statistics-on-demand-historicals"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics-on-demand-historical", ("statistics_on_demand_historical", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical))])
                    self._leafs = OrderedDict()

                    self.statistics_on_demand_historical = YList(self)
                    self._segment_path = lambda: "statistics-on-demand-historicals"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals, [], name, value)


                class StatisticsOnDemandHistorical(Entity):
                    """
                    Historical statistics data for an SLA
                    on\-demand  operation
                    
                    .. attribute:: operation_id
                    
                    	Operation ID
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\: int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:  :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions>`
                    
                    .. attribute:: operation_schedule
                    
                    	Operation schedule
                    	**type**\:  :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule>`
                    
                    .. attribute:: probe_type
                    
                    	Type of probe used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: flr_calculation_interval
                    
                    	Interval between FLR calculations for SLM, in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: operation_metric
                    
                    	Metrics gathered for the operation
                    	**type**\: list of  		 :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical, self).__init__()

                        self.yang_name = "statistics-on-demand-historical"
                        self.yang_parent_name = "statistics-on-demand-historicals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("specific-options", ("specific_options", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions)), ("operation-schedule", ("operation_schedule", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule)), ("operation-metric", ("operation_metric", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric))])
                        self._leafs = OrderedDict([
                            ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('probe_type', (YLeaf(YType.str, 'probe-type'), ['str'])),
                            ('display_short', (YLeaf(YType.str, 'display-short'), ['str'])),
                            ('display_long', (YLeaf(YType.str, 'display-long'), ['str'])),
                            ('flr_calculation_interval', (YLeaf(YType.uint32, 'flr-calculation-interval'), ['int'])),
                        ])
                        self.operation_id = None
                        self.domain_name = None
                        self.interface_name = None
                        self.mep_id = None
                        self.mac_address = None
                        self.probe_type = None
                        self.display_short = None
                        self.display_long = None
                        self.flr_calculation_interval = None

                        self.specific_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"

                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule()
                        self.operation_schedule.parent = self
                        self._children_name_map["operation_schedule"] = "operation-schedule"

                        self.operation_metric = YList(self)
                        self._segment_path = lambda: "statistics-on-demand-historical"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical, ['operation_id', 'domain_name', 'interface_name', 'mep_id', 'mac_address', 'probe_type', 'display_short', 'display_long', 'flr_calculation_interval'], name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:  :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:  :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:  :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "statistics-on-demand-historical"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("configured-operation-options", ("configured_operation_options", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions)), ("ondemand-operation-options", ("ondemand_operation_options", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions))])
                            self._leafs = OrderedDict([
                                ('oper_type', (YLeaf(YType.enumeration, 'oper-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation', '')])),
                            ])
                            self.oper_type = None

                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._segment_path = lambda: "specific-options"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions, ['oper_type'], name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "configured-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions, ['profile_name'], name, value)


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ondemand_operation_id', (YLeaf(YType.uint32, 'ondemand-operation-id'), ['int'])),
                                    ('probe_count', (YLeaf(YType.uint8, 'probe-count'), ['int'])),
                                ])
                                self.ondemand_operation_id = None
                                self.probe_count = None
                                self._segment_path = lambda: "ondemand-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions, ['ondemand_operation_id', 'probe_count'], name, value)


                    class OperationSchedule(Entity):
                        """
                        Operation schedule
                        
                        .. attribute:: start_time
                        
                        	Start time of the first probe, in seconds since the Unix Epoch
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time_configured
                        
                        	Whether or not the operation start time was explicitly configured
                        	**type**\: bool
                        
                        .. attribute:: schedule_duration
                        
                        	Duration of a probe for the operation in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: schedule_interval
                        
                        	Interval between the start times of consecutive probes,  in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule, self).__init__()

                            self.yang_name = "operation-schedule"
                            self.yang_parent_name = "statistics-on-demand-historical"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                                ('start_time_configured', (YLeaf(YType.boolean, 'start-time-configured'), ['bool'])),
                                ('schedule_duration', (YLeaf(YType.uint32, 'schedule-duration'), ['int'])),
                                ('schedule_interval', (YLeaf(YType.uint32, 'schedule-interval'), ['int'])),
                            ])
                            self.start_time = None
                            self.start_time_configured = None
                            self.schedule_duration = None
                            self.schedule_interval = None
                            self._segment_path = lambda: "operation-schedule"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule, ['start_time', 'start_time_configured', 'schedule_duration', 'schedule_interval'], name, value)


                    class OperationMetric(Entity):
                        """
                        Metrics gathered for the operation
                        
                        .. attribute:: config
                        
                        	Configuration of the metric
                        	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config>`
                        
                        .. attribute:: bucket
                        
                        	Buckets stored for the metric
                        	**type**\: list of  		 :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric, self).__init__()

                            self.yang_name = "operation-metric"
                            self.yang_parent_name = "statistics-on-demand-historical"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config)), ("bucket", ("bucket", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket))])
                            self._leafs = OrderedDict()

                            self.config = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.bucket = YList(self)
                            self._segment_path = lambda: "operation-metric"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric, [], name, value)


                        class Config(Entity):
                            """
                            Configuration of the metric
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:  :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                            
                            .. attribute:: bins_count
                            
                            	Total number of bins into which to aggregate. 0 if no aggregation
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bins_width
                            
                            	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bucket_size
                            
                            	Size of buckets into which measurements are collected
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: bucket_size_unit
                            
                            	Whether bucket size is 'per\-probe' or 'probes'
                            	**type**\:  :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "operation-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric', '')])),
                                    ('bins_count', (YLeaf(YType.uint16, 'bins-count'), ['int'])),
                                    ('bins_width', (YLeaf(YType.uint16, 'bins-width'), ['int'])),
                                    ('bucket_size', (YLeaf(YType.uint8, 'bucket-size'), ['int'])),
                                    ('bucket_size_unit', (YLeaf(YType.enumeration, 'bucket-size-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize', '')])),
                                    ('buckets_archive', (YLeaf(YType.uint32, 'buckets-archive'), ['int'])),
                                ])
                                self.metric_type = None
                                self.bins_count = None
                                self.bins_width = None
                                self.bucket_size = None
                                self.bucket_size_unit = None
                                self.buckets_archive = None
                                self._segment_path = lambda: "config"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config, ['metric_type', 'bins_count', 'bins_width', 'bucket_size', 'bucket_size_unit', 'buckets_archive'], name, value)


                        class Bucket(Entity):
                            """
                            Buckets stored for the metric
                            
                            .. attribute:: contents
                            
                            	The contents of the bucket; bins or samples
                            	**type**\:  :py:class:`Contents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents>`
                            
                            .. attribute:: start_at
                            
                            	Absolute time that the bucket started being filled at
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duration
                            
                            	Length of time for which the bucket is being filled in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: sent
                            
                            	Number of packets sent in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lost
                            
                            	Number of lost packets in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: corrupt
                            
                            	Number of corrupt packets in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_order
                            
                            	Number of packets recieved out\-of\-order in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplicates
                            
                            	Number of duplicate packets received in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: minimum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: maximum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: time_of_minimum
                            
                            	Absolute time that the minimum value was recorded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_of_maximum
                            
                            	Absolute time that the maximum value was recorded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: average
                            
                            	Mean of the results in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: standard_deviation
                            
                            	Standard deviation of the results in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: result_count
                            
                            	The count of samples collected in the bucket
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_sent_count
                            
                            	The number of data packets sent across the bucket, used in the calculation of overall FLR
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_lost_count
                            
                            	The number of data packets lost across the bucket, used in the calculation of overall FLR
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: overall_flr
                            
                            	Frame Loss Ratio across the whole bucket, in millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: percentage
                            
                            .. attribute:: suspect_start_mid_bucket
                            
                            	Results suspect due to a probe starting mid\-way through a bucket
                            	**type**\: bool
                            
                            .. attribute:: suspect_schedule_latency
                            
                            	Results suspect due to scheduling latency causing one or more packets to not be sent
                            	**type**\: bool
                            
                            .. attribute:: suspect_send_fail
                            
                            	Results suspect due to failure to send one or more packets
                            	**type**\: bool
                            
                            .. attribute:: suspect_premature_end
                            
                            	Results suspect due to a probe ending prematurely
                            	**type**\: bool
                            
                            .. attribute:: suspect_clock_drift
                            
                            	Results suspect as more than 10 seconds time drift detected
                            	**type**\: bool
                            
                            .. attribute:: suspect_memory_allocation_failed
                            
                            	Results suspect due to a memory allocation failure
                            	**type**\: bool
                            
                            .. attribute:: suspect_cleared_mid_bucket
                            
                            	Results suspect as bucket was cleared mid\-way through being filled
                            	**type**\: bool
                            
                            .. attribute:: suspect_probe_restarted
                            
                            	Results suspect as probe restarted mid\-way through the bucket
                            	**type**\: bool
                            
                            .. attribute:: suspect_management_latency
                            
                            	Results suspect as processing of results has been delayed
                            	**type**\: bool
                            
                            .. attribute:: suspect_multiple_buckets
                            
                            	Results suspect as the probe has been configured across multiple buckets
                            	**type**\: bool
                            
                            .. attribute:: suspect_misordering
                            
                            	Results suspect as misordering has been detected , affecting results
                            	**type**\: bool
                            
                            .. attribute:: suspect_flr_low_packet_count
                            
                            	Results suspect as FLR calculated based on a low packet count
                            	**type**\: bool
                            
                            .. attribute:: premature_reason
                            
                            	If the probe ended prematurely, the error that caused a probe to end
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: premature_reason_string
                            
                            	Description of the error code that caused the probe to end prematurely. For informational purposes only
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket, self).__init__()

                                self.yang_name = "bucket"
                                self.yang_parent_name = "operation-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("contents", ("contents", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents))])
                                self._leafs = OrderedDict([
                                    ('start_at', (YLeaf(YType.uint32, 'start-at'), ['int'])),
                                    ('duration', (YLeaf(YType.uint32, 'duration'), ['int'])),
                                    ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                    ('lost', (YLeaf(YType.uint32, 'lost'), ['int'])),
                                    ('corrupt', (YLeaf(YType.uint32, 'corrupt'), ['int'])),
                                    ('out_of_order', (YLeaf(YType.uint32, 'out-of-order'), ['int'])),
                                    ('duplicates', (YLeaf(YType.uint32, 'duplicates'), ['int'])),
                                    ('minimum', (YLeaf(YType.int32, 'minimum'), ['int'])),
                                    ('maximum', (YLeaf(YType.int32, 'maximum'), ['int'])),
                                    ('time_of_minimum', (YLeaf(YType.uint32, 'time-of-minimum'), ['int'])),
                                    ('time_of_maximum', (YLeaf(YType.uint32, 'time-of-maximum'), ['int'])),
                                    ('average', (YLeaf(YType.int32, 'average'), ['int'])),
                                    ('standard_deviation', (YLeaf(YType.int32, 'standard-deviation'), ['int'])),
                                    ('result_count', (YLeaf(YType.uint32, 'result-count'), ['int'])),
                                    ('data_sent_count', (YLeaf(YType.uint32, 'data-sent-count'), ['int'])),
                                    ('data_lost_count', (YLeaf(YType.uint32, 'data-lost-count'), ['int'])),
                                    ('overall_flr', (YLeaf(YType.int32, 'overall-flr'), ['int'])),
                                    ('suspect_start_mid_bucket', (YLeaf(YType.boolean, 'suspect-start-mid-bucket'), ['bool'])),
                                    ('suspect_schedule_latency', (YLeaf(YType.boolean, 'suspect-schedule-latency'), ['bool'])),
                                    ('suspect_send_fail', (YLeaf(YType.boolean, 'suspect-send-fail'), ['bool'])),
                                    ('suspect_premature_end', (YLeaf(YType.boolean, 'suspect-premature-end'), ['bool'])),
                                    ('suspect_clock_drift', (YLeaf(YType.boolean, 'suspect-clock-drift'), ['bool'])),
                                    ('suspect_memory_allocation_failed', (YLeaf(YType.boolean, 'suspect-memory-allocation-failed'), ['bool'])),
                                    ('suspect_cleared_mid_bucket', (YLeaf(YType.boolean, 'suspect-cleared-mid-bucket'), ['bool'])),
                                    ('suspect_probe_restarted', (YLeaf(YType.boolean, 'suspect-probe-restarted'), ['bool'])),
                                    ('suspect_management_latency', (YLeaf(YType.boolean, 'suspect-management-latency'), ['bool'])),
                                    ('suspect_multiple_buckets', (YLeaf(YType.boolean, 'suspect-multiple-buckets'), ['bool'])),
                                    ('suspect_misordering', (YLeaf(YType.boolean, 'suspect-misordering'), ['bool'])),
                                    ('suspect_flr_low_packet_count', (YLeaf(YType.boolean, 'suspect-flr-low-packet-count'), ['bool'])),
                                    ('premature_reason', (YLeaf(YType.uint32, 'premature-reason'), ['int'])),
                                    ('premature_reason_string', (YLeaf(YType.str, 'premature-reason-string'), ['str'])),
                                ])
                                self.start_at = None
                                self.duration = None
                                self.sent = None
                                self.lost = None
                                self.corrupt = None
                                self.out_of_order = None
                                self.duplicates = None
                                self.minimum = None
                                self.maximum = None
                                self.time_of_minimum = None
                                self.time_of_maximum = None
                                self.average = None
                                self.standard_deviation = None
                                self.result_count = None
                                self.data_sent_count = None
                                self.data_lost_count = None
                                self.overall_flr = None
                                self.suspect_start_mid_bucket = None
                                self.suspect_schedule_latency = None
                                self.suspect_send_fail = None
                                self.suspect_premature_end = None
                                self.suspect_clock_drift = None
                                self.suspect_memory_allocation_failed = None
                                self.suspect_cleared_mid_bucket = None
                                self.suspect_probe_restarted = None
                                self.suspect_management_latency = None
                                self.suspect_multiple_buckets = None
                                self.suspect_misordering = None
                                self.suspect_flr_low_packet_count = None
                                self.premature_reason = None
                                self.premature_reason_string = None

                                self.contents = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self._children_name_map["contents"] = "contents"
                                self._segment_path = lambda: "bucket"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket, ['start_at', 'duration', 'sent', 'lost', 'corrupt', 'out_of_order', 'duplicates', 'minimum', 'maximum', 'time_of_minimum', 'time_of_maximum', 'average', 'standard_deviation', 'result_count', 'data_sent_count', 'data_lost_count', 'overall_flr', 'suspect_start_mid_bucket', 'suspect_schedule_latency', 'suspect_send_fail', 'suspect_premature_end', 'suspect_clock_drift', 'suspect_memory_allocation_failed', 'suspect_cleared_mid_bucket', 'suspect_probe_restarted', 'suspect_management_latency', 'suspect_multiple_buckets', 'suspect_misordering', 'suspect_flr_low_packet_count', 'premature_reason', 'premature_reason_string'], name, value)


                            class Contents(Entity):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:  :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:  :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:  :py:class:`SlaOperBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucket>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents, self).__init__()

                                    self.yang_name = "contents"
                                    self.yang_parent_name = "bucket"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("aggregated", ("aggregated", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated)), ("unaggregated", ("unaggregated", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated))])
                                    self._leafs = OrderedDict([
                                        ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperBucket', '')])),
                                    ])
                                    self.bucket_type = None

                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self._children_name_map["aggregated"] = "aggregated"

                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self
                                    self._children_name_map["unaggregated"] = "unaggregated"
                                    self._segment_path = lambda: "contents"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents, ['bucket_type'], name, value)


                                class Aggregated(Entity):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of  		 :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated, self).__init__()

                                        self.yang_name = "aggregated"
                                        self.yang_parent_name = "contents"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("bins", ("bins", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins))])
                                        self._leafs = OrderedDict()

                                        self.bins = YList(self)
                                        self._segment_path = lambda: "aggregated"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/contents/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated, [], name, value)


                                    class Bins(Entity):
                                        """
                                        The bins of an SLA metric bucket
                                        
                                        .. attribute:: lower_bound
                                        
                                        	Lower bound (inclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: upper_bound
                                        
                                        	Upper bound (exclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: lower_bound_tenths
                                        
                                        	Lower bound (inclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: upper_bound_tenths
                                        
                                        	Upper bound (exclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: sum
                                        
                                        	The sum of the results in the bin, in microseconds or millionths of a percent
                                        	**type**\: int
                                        
                                        	**range:** \-9223372036854775808..9223372036854775807
                                        
                                        .. attribute:: count
                                        
                                        	The total number of results in the bin
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2017-10-06'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__init__()

                                            self.yang_name = "bins"
                                            self.yang_parent_name = "aggregated"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('lower_bound', (YLeaf(YType.int32, 'lower-bound'), ['int'])),
                                                ('upper_bound', (YLeaf(YType.int32, 'upper-bound'), ['int'])),
                                                ('lower_bound_tenths', (YLeaf(YType.int32, 'lower-bound-tenths'), ['int'])),
                                                ('upper_bound_tenths', (YLeaf(YType.int32, 'upper-bound-tenths'), ['int'])),
                                                ('sum', (YLeaf(YType.int64, 'sum'), ['int'])),
                                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ])
                                            self.lower_bound = None
                                            self.upper_bound = None
                                            self.lower_bound_tenths = None
                                            self.upper_bound_tenths = None
                                            self.sum = None
                                            self.count = None
                                            self._segment_path = lambda: "bins"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/contents/aggregated/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins, ['lower_bound', 'upper_bound', 'lower_bound_tenths', 'upper_bound_tenths', 'sum', 'count'], name, value)


                                class Unaggregated(Entity):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated, self).__init__()

                                        self.yang_name = "unaggregated"
                                        self.yang_parent_name = "contents"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("sample", ("sample", Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample))])
                                        self._leafs = OrderedDict()

                                        self.sample = YList(self)
                                        self._segment_path = lambda: "unaggregated"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/contents/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated, [], name, value)


                                    class Sample(Entity):
                                        """
                                        The samples of an SLA metric bucket
                                        
                                        .. attribute:: sent_at
                                        
                                        	The time (in milliseconds relative to the start time of the bucket) that the sample was sent at
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: sent
                                        
                                        	Whether the sample packet was sucessfully sent
                                        	**type**\: bool
                                        
                                        .. attribute:: timed_out
                                        
                                        	Whether the sample packet timed out
                                        	**type**\: bool
                                        
                                        .. attribute:: corrupt
                                        
                                        	Whether the sample packet was corrupt
                                        	**type**\: bool
                                        
                                        .. attribute:: out_of_order
                                        
                                        	Whether the sample packet was received out\-of\-order
                                        	**type**\: bool
                                        
                                        .. attribute:: no_data_packets
                                        
                                        	Whether a measurement could not be made because no data packets were sent in the sample period. Only applicable for LMM measurements
                                        	**type**\: bool
                                        
                                        .. attribute:: result
                                        
                                        	The result (in microseconds or millionths of a percent) of the sample, if available
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: frames_sent
                                        
                                        	For FLR measurements, the number of frames sent, if available
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: frames_lost
                                        
                                        	For FLR measurements, the number of frames lost, if available
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2017-10-06'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__init__()

                                            self.yang_name = "sample"
                                            self.yang_parent_name = "unaggregated"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sent_at', (YLeaf(YType.uint32, 'sent-at'), ['int'])),
                                                ('sent', (YLeaf(YType.boolean, 'sent'), ['bool'])),
                                                ('timed_out', (YLeaf(YType.boolean, 'timed-out'), ['bool'])),
                                                ('corrupt', (YLeaf(YType.boolean, 'corrupt'), ['bool'])),
                                                ('out_of_order', (YLeaf(YType.boolean, 'out-of-order'), ['bool'])),
                                                ('no_data_packets', (YLeaf(YType.boolean, 'no-data-packets'), ['bool'])),
                                                ('result', (YLeaf(YType.int32, 'result'), ['int'])),
                                                ('frames_sent', (YLeaf(YType.uint32, 'frames-sent'), ['int'])),
                                                ('frames_lost', (YLeaf(YType.uint32, 'frames-lost'), ['int'])),
                                            ])
                                            self.sent_at = None
                                            self.sent = None
                                            self.timed_out = None
                                            self.corrupt = None
                                            self.out_of_order = None
                                            self.no_data_packets = None
                                            self.result = None
                                            self.frames_sent = None
                                            self.frames_lost = None
                                            self._segment_path = lambda: "sample"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-on-demand-historicals/statistics-on-demand-historical/operation-metric/bucket/contents/unaggregated/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample, ['sent_at', 'sent', 'timed_out', 'corrupt', 'out_of_order', 'no_data_packets', 'result', 'frames_sent', 'frames_lost'], name, value)


            class ConfigErrors(Entity):
                """
                Table of SLA configuration errors on configured
                operations
                
                .. attribute:: config_error
                
                	SLA operation to get configuration errors data for
                	**type**\: list of  		 :py:class:`ConfigError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.ConfigErrors.ConfigError>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.ConfigErrors, self).__init__()

                    self.yang_name = "config-errors"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config-error", ("config_error", Sla.Protocols.Ethernet.ConfigErrors.ConfigError))])
                    self._leafs = OrderedDict()

                    self.config_error = YList(self)
                    self._segment_path = lambda: "config-errors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sla.Protocols.Ethernet.ConfigErrors, [], name, value)


                class ConfigError(Entity):
                    """
                    SLA operation to get configuration errors data
                    for
                    
                    .. attribute:: profile_name
                    
                    	Profile Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191
                    	**type**\: int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: profile_name_xr
                    
                    	The name of the operation profile
                    	**type**\: str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: rt_delay_inconsistent
                    
                    	Is the profile configured to collect RT Delay but the packet type doesn't support it?
                    	**type**\: bool
                    
                    .. attribute:: ow_delay_sd_inconsistent
                    
                    	Is the profile configured to collect OW Delay (SD) but the packet type doesn't support it?
                    	**type**\: bool
                    
                    .. attribute:: ow_delay_ds_inconsistent
                    
                    	Is the profile configured to collect OW Delay (DS) but the packet type doesn't support it?
                    	**type**\: bool
                    
                    .. attribute:: rt_jitter_inconsistent
                    
                    	Is the profile configured to collect RT Jitter but the packet type doesn't support it?
                    	**type**\: bool
                    
                    .. attribute:: ow_jitter_sd_inconsistent
                    
                    	Is the profile configured to collect OW Jitter (SD) but the packet type doesn't support it?
                    	**type**\: bool
                    
                    .. attribute:: ow_jitter_ds_inconsistent
                    
                    	Is the profile configured to collect OW Delay (DS) but the packet type doesn't support it?
                    	**type**\: bool
                    
                    .. attribute:: ow_loss_sd_inconsistent
                    
                    	Is the profile configured to collect OW Frame Loss (SD) but the packet type doesn't support it ?
                    	**type**\: bool
                    
                    .. attribute:: ow_loss_ds_inconsistent
                    
                    	Is the profile configured to collect OW Frame Loss (DS) but the packet type doesn't support it ?
                    	**type**\: bool
                    
                    .. attribute:: packet_pad_inconsistent
                    
                    	Is the profile configured to pad packets but the packet type doesn't support it?
                    	**type**\: bool
                    
                    .. attribute:: packet_rand_pad_inconsistent
                    
                    	Is the profile configured to pad packets with a pseudo\-random string but the packet type doesn't support it?
                    	**type**\: bool
                    
                    .. attribute:: min_packet_interval_inconsistent
                    
                    	Is the profile configured to send packets more frequently than the protocol allows?
                    	**type**\: bool
                    
                    .. attribute:: priority_inconsistent
                    
                    	Is the profile configured to use a packet priority scheme that the protocol does not support?
                    	**type**\: bool
                    
                    .. attribute:: packet_type_inconsistent
                    
                    	Is the profile configured to use a packet type that isn't supported by any protocols?
                    	**type**\: bool
                    
                    .. attribute:: profile_doesnt_exist
                    
                    	Is the operation configured to use a profile that is not currently defined for the protocol?
                    	**type**\: bool
                    
                    .. attribute:: synthetic_loss_not_supported
                    
                    	The profile is configured to use a packet type which doesn't support synthetic loss measurement and the number of packets per FLR calculation has been configured
                    	**type**\: bool
                    
                    .. attribute:: probe_too_big
                    
                    	The profile is configured to use a packet type which does not allow more than 72000 packets per probe and greater than 72000 packets per probe have been configured
                    	**type**\: bool
                    
                    .. attribute:: error_string
                    
                    	Displays other issues not indicated from the flags above, for example MIB incompatibility issues
                    	**type**\: list of str
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.ConfigErrors.ConfigError, self).__init__()

                        self.yang_name = "config-error"
                        self.yang_parent_name = "config-errors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('profile_name_xr', (YLeaf(YType.str, 'profile-name-xr'), ['str'])),
                            ('display_short', (YLeaf(YType.str, 'display-short'), ['str'])),
                            ('rt_delay_inconsistent', (YLeaf(YType.boolean, 'rt-delay-inconsistent'), ['bool'])),
                            ('ow_delay_sd_inconsistent', (YLeaf(YType.boolean, 'ow-delay-sd-inconsistent'), ['bool'])),
                            ('ow_delay_ds_inconsistent', (YLeaf(YType.boolean, 'ow-delay-ds-inconsistent'), ['bool'])),
                            ('rt_jitter_inconsistent', (YLeaf(YType.boolean, 'rt-jitter-inconsistent'), ['bool'])),
                            ('ow_jitter_sd_inconsistent', (YLeaf(YType.boolean, 'ow-jitter-sd-inconsistent'), ['bool'])),
                            ('ow_jitter_ds_inconsistent', (YLeaf(YType.boolean, 'ow-jitter-ds-inconsistent'), ['bool'])),
                            ('ow_loss_sd_inconsistent', (YLeaf(YType.boolean, 'ow-loss-sd-inconsistent'), ['bool'])),
                            ('ow_loss_ds_inconsistent', (YLeaf(YType.boolean, 'ow-loss-ds-inconsistent'), ['bool'])),
                            ('packet_pad_inconsistent', (YLeaf(YType.boolean, 'packet-pad-inconsistent'), ['bool'])),
                            ('packet_rand_pad_inconsistent', (YLeaf(YType.boolean, 'packet-rand-pad-inconsistent'), ['bool'])),
                            ('min_packet_interval_inconsistent', (YLeaf(YType.boolean, 'min-packet-interval-inconsistent'), ['bool'])),
                            ('priority_inconsistent', (YLeaf(YType.boolean, 'priority-inconsistent'), ['bool'])),
                            ('packet_type_inconsistent', (YLeaf(YType.boolean, 'packet-type-inconsistent'), ['bool'])),
                            ('profile_doesnt_exist', (YLeaf(YType.boolean, 'profile-doesnt-exist'), ['bool'])),
                            ('synthetic_loss_not_supported', (YLeaf(YType.boolean, 'synthetic-loss-not-supported'), ['bool'])),
                            ('probe_too_big', (YLeaf(YType.boolean, 'probe-too-big'), ['bool'])),
                            ('error_string', (YLeafList(YType.str, 'error-string'), ['str'])),
                        ])
                        self.profile_name = None
                        self.domain_name = None
                        self.interface_name = None
                        self.mep_id = None
                        self.mac_address = None
                        self.profile_name_xr = None
                        self.display_short = None
                        self.rt_delay_inconsistent = None
                        self.ow_delay_sd_inconsistent = None
                        self.ow_delay_ds_inconsistent = None
                        self.rt_jitter_inconsistent = None
                        self.ow_jitter_sd_inconsistent = None
                        self.ow_jitter_ds_inconsistent = None
                        self.ow_loss_sd_inconsistent = None
                        self.ow_loss_ds_inconsistent = None
                        self.packet_pad_inconsistent = None
                        self.packet_rand_pad_inconsistent = None
                        self.min_packet_interval_inconsistent = None
                        self.priority_inconsistent = None
                        self.packet_type_inconsistent = None
                        self.profile_doesnt_exist = None
                        self.synthetic_loss_not_supported = None
                        self.probe_too_big = None
                        self.error_string = []
                        self._segment_path = lambda: "config-error"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/config-errors/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sla.Protocols.Ethernet.ConfigErrors.ConfigError, ['profile_name', 'domain_name', 'interface_name', 'mep_id', 'mac_address', 'profile_name_xr', 'display_short', 'rt_delay_inconsistent', 'ow_delay_sd_inconsistent', 'ow_delay_ds_inconsistent', 'rt_jitter_inconsistent', 'ow_jitter_sd_inconsistent', 'ow_jitter_ds_inconsistent', 'ow_loss_sd_inconsistent', 'ow_loss_ds_inconsistent', 'packet_pad_inconsistent', 'packet_rand_pad_inconsistent', 'min_packet_interval_inconsistent', 'priority_inconsistent', 'packet_type_inconsistent', 'profile_doesnt_exist', 'synthetic_loss_not_supported', 'probe_too_big', 'error_string'], name, value)


            class OnDemandOperations(Entity):
                """
                Table of SLA on\-demand operations
                
                .. attribute:: on_demand_operation
                
                	SLA on\-demand operation to get operation data for
                	**type**\: list of  		 :py:class:`OnDemandOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.OnDemandOperations, self).__init__()

                    self.yang_name = "on-demand-operations"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("on-demand-operation", ("on_demand_operation", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation))])
                    self._leafs = OrderedDict()

                    self.on_demand_operation = YList(self)
                    self._segment_path = lambda: "on-demand-operations"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations, [], name, value)


                class OnDemandOperation(Entity):
                    """
                    SLA on\-demand operation to get operation data
                    for
                    
                    .. attribute:: operation_id
                    
                    	Operation ID
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\: int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: profile_options
                    
                    	Options that are only valid if the operation has a profile
                    	**type**\:  :py:class:`ProfileOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions>`
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:  :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions>`
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: last_run
                    
                    	Time that the last probe for the operation was run, NULL if never run
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation, self).__init__()

                        self.yang_name = "on-demand-operation"
                        self.yang_parent_name = "on-demand-operations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("profile-options", ("profile_options", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions)), ("specific-options", ("specific_options", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions))])
                        self._leafs = OrderedDict([
                            ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('display_short', (YLeaf(YType.str, 'display-short'), ['str'])),
                            ('display_long', (YLeaf(YType.str, 'display-long'), ['str'])),
                            ('last_run', (YLeaf(YType.uint32, 'last-run'), ['int'])),
                        ])
                        self.operation_id = None
                        self.domain_name = None
                        self.interface_name = None
                        self.mep_id = None
                        self.mac_address = None
                        self.display_short = None
                        self.display_long = None
                        self.last_run = None

                        self.profile_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions()
                        self.profile_options.parent = self
                        self._children_name_map["profile_options"] = "profile-options"

                        self.specific_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"
                        self._segment_path = lambda: "on-demand-operation"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation, ['operation_id', 'domain_name', 'interface_name', 'mep_id', 'mac_address', 'display_short', 'display_long', 'last_run'], name, value)


                    class ProfileOptions(Entity):
                        """
                        Options that are only valid if the operation has
                        a profile
                        
                        .. attribute:: packet_padding
                        
                        	Configuration of the packet padding
                        	**type**\:  :py:class:`PacketPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding>`
                        
                        .. attribute:: priority
                        
                        	Priority at which to send the packet, if configured
                        	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority>`
                        
                        .. attribute:: operation_schedule
                        
                        	Operation schedule
                        	**type**\:  :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule>`
                        
                        .. attribute:: probe_type
                        
                        	Type of probe used by the operation
                        	**type**\: str
                        
                        .. attribute:: packets_per_burst
                        
                        	Number of packets sent per burst
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: inter_packet_interval
                        
                        	Interval between packets within a burst in milliseconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**units**\: millisecond
                        
                        .. attribute:: bursts_per_probe
                        
                        	Number of bursts sent per probe
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inter_burst_interval
                        
                        	Interval between bursts within a probe in milliseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: flr_calculation_interval
                        
                        	Interval between FLR calculations for SLM, in milliseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: operation_metric
                        
                        	Array of the metrics that are measured by the operation
                        	**type**\: list of  		 :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions, self).__init__()

                            self.yang_name = "profile-options"
                            self.yang_parent_name = "on-demand-operation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("packet-padding", ("packet_padding", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding)), ("priority", ("priority", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority)), ("operation-schedule", ("operation_schedule", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule)), ("operation-metric", ("operation_metric", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric))])
                            self._leafs = OrderedDict([
                                ('probe_type', (YLeaf(YType.str, 'probe-type'), ['str'])),
                                ('packets_per_burst', (YLeaf(YType.uint16, 'packets-per-burst'), ['int'])),
                                ('inter_packet_interval', (YLeaf(YType.uint16, 'inter-packet-interval'), ['int'])),
                                ('bursts_per_probe', (YLeaf(YType.uint32, 'bursts-per-probe'), ['int'])),
                                ('inter_burst_interval', (YLeaf(YType.uint32, 'inter-burst-interval'), ['int'])),
                                ('flr_calculation_interval', (YLeaf(YType.uint32, 'flr-calculation-interval'), ['int'])),
                            ])
                            self.probe_type = None
                            self.packets_per_burst = None
                            self.inter_packet_interval = None
                            self.bursts_per_probe = None
                            self.inter_burst_interval = None
                            self.flr_calculation_interval = None

                            self.packet_padding = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding()
                            self.packet_padding.parent = self
                            self._children_name_map["packet_padding"] = "packet-padding"

                            self.priority = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority()
                            self.priority.parent = self
                            self._children_name_map["priority"] = "priority"

                            self.operation_schedule = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule()
                            self.operation_schedule.parent = self
                            self._children_name_map["operation_schedule"] = "operation-schedule"

                            self.operation_metric = YList(self)
                            self._segment_path = lambda: "profile-options"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions, ['probe_type', 'packets_per_burst', 'inter_packet_interval', 'bursts_per_probe', 'inter_burst_interval', 'flr_calculation_interval'], name, value)


                        class PacketPadding(Entity):
                            """
                            Configuration of the packet padding
                            
                            .. attribute:: packet_pad_size
                            
                            	Size that packets are being padded to
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: test_pattern_pad_scheme
                            
                            	Test pattern scheme that is used in the packet padding
                            	**type**\:  :py:class:`SlaOperTestPatternScheme <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperTestPatternScheme>`
                            
                            .. attribute:: test_pattern_pad_hex_string
                            
                            	Hex string that is used in the packet padding
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding, self).__init__()

                                self.yang_name = "packet-padding"
                                self.yang_parent_name = "profile-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packet_pad_size', (YLeaf(YType.uint16, 'packet-pad-size'), ['int'])),
                                    ('test_pattern_pad_scheme', (YLeaf(YType.enumeration, 'test-pattern-pad-scheme'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperTestPatternScheme', '')])),
                                    ('test_pattern_pad_hex_string', (YLeaf(YType.uint32, 'test-pattern-pad-hex-string'), ['int'])),
                                ])
                                self.packet_pad_size = None
                                self.test_pattern_pad_scheme = None
                                self.test_pattern_pad_hex_string = None
                                self._segment_path = lambda: "packet-padding"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding, ['packet_pad_size', 'test_pattern_pad_scheme', 'test_pattern_pad_hex_string'], name, value)


                        class Priority(Entity):
                            """
                            Priority at which to send the packet, if
                            configured
                            
                            .. attribute:: priority_type
                            
                            	PriorityType
                            	**type**\:  :py:class:`SlaOperPacketPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperPacketPriority>`
                            
                            .. attribute:: cos
                            
                            	3\-bit COS priority value applied to packets
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "profile-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('priority_type', (YLeaf(YType.enumeration, 'priority-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperPacketPriority', '')])),
                                    ('cos', (YLeaf(YType.uint8, 'cos'), ['int'])),
                                ])
                                self.priority_type = None
                                self.cos = None
                                self._segment_path = lambda: "priority"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority, ['priority_type', 'cos'], name, value)


                        class OperationSchedule(Entity):
                            """
                            Operation schedule
                            
                            .. attribute:: start_time
                            
                            	Start time of the first probe, in seconds since the Unix Epoch
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: start_time_configured
                            
                            	Whether or not the operation start time was explicitly configured
                            	**type**\: bool
                            
                            .. attribute:: schedule_duration
                            
                            	Duration of a probe for the operation in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: schedule_interval
                            
                            	Interval between the start times of consecutive probes,  in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule, self).__init__()

                                self.yang_name = "operation-schedule"
                                self.yang_parent_name = "profile-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                                    ('start_time_configured', (YLeaf(YType.boolean, 'start-time-configured'), ['bool'])),
                                    ('schedule_duration', (YLeaf(YType.uint32, 'schedule-duration'), ['int'])),
                                    ('schedule_interval', (YLeaf(YType.uint32, 'schedule-interval'), ['int'])),
                                ])
                                self.start_time = None
                                self.start_time_configured = None
                                self.schedule_duration = None
                                self.schedule_interval = None
                                self._segment_path = lambda: "operation-schedule"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule, ['start_time', 'start_time_configured', 'schedule_duration', 'schedule_interval'], name, value)


                        class OperationMetric(Entity):
                            """
                            Array of the metrics that are measured by the
                            operation
                            
                            .. attribute:: metric_config
                            
                            	Configuration of the metric
                            	**type**\:  :py:class:`MetricConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig>`
                            
                            .. attribute:: current_buckets_archive
                            
                            	Number of valid buckets currently in the buckets archive
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric, self).__init__()

                                self.yang_name = "operation-metric"
                                self.yang_parent_name = "profile-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("metric-config", ("metric_config", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig))])
                                self._leafs = OrderedDict([
                                    ('current_buckets_archive', (YLeaf(YType.uint32, 'current-buckets-archive'), ['int'])),
                                ])
                                self.current_buckets_archive = None

                                self.metric_config = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig()
                                self.metric_config.parent = self
                                self._children_name_map["metric_config"] = "metric-config"
                                self._segment_path = lambda: "operation-metric"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric, ['current_buckets_archive'], name, value)


                            class MetricConfig(Entity):
                                """
                                Configuration of the metric
                                
                                .. attribute:: metric_type
                                
                                	Type of metric to which this configuration applies
                                	**type**\:  :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                                
                                .. attribute:: bins_count
                                
                                	Total number of bins into which to aggregate. 0 if no aggregation
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: bins_width
                                
                                	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: bucket_size
                                
                                	Size of buckets into which measurements are collected
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: bucket_size_unit
                                
                                	Whether bucket size is 'per\-probe' or 'probes'
                                	**type**\:  :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                                
                                .. attribute:: buckets_archive
                                
                                	Maximum number of buckets to store in memory
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig, self).__init__()

                                    self.yang_name = "metric-config"
                                    self.yang_parent_name = "operation-metric"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric', '')])),
                                        ('bins_count', (YLeaf(YType.uint16, 'bins-count'), ['int'])),
                                        ('bins_width', (YLeaf(YType.uint16, 'bins-width'), ['int'])),
                                        ('bucket_size', (YLeaf(YType.uint8, 'bucket-size'), ['int'])),
                                        ('bucket_size_unit', (YLeaf(YType.enumeration, 'bucket-size-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize', '')])),
                                        ('buckets_archive', (YLeaf(YType.uint32, 'buckets-archive'), ['int'])),
                                    ])
                                    self.metric_type = None
                                    self.bins_count = None
                                    self.bins_width = None
                                    self.bucket_size = None
                                    self.bucket_size_unit = None
                                    self.buckets_archive = None
                                    self._segment_path = lambda: "metric-config"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/profile-options/operation-metric/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig, ['metric_type', 'bins_count', 'bins_width', 'bucket_size', 'bucket_size_unit', 'buckets_archive'], name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:  :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:  :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:  :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "on-demand-operation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("configured-operation-options", ("configured_operation_options", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions)), ("ondemand-operation-options", ("ondemand_operation_options", Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions))])
                            self._leafs = OrderedDict([
                                ('oper_type', (YLeaf(YType.enumeration, 'oper-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation', '')])),
                            ])
                            self.oper_type = None

                            self.configured_operation_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._segment_path = lambda: "specific-options"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions, ['oper_type'], name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "configured-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions, ['profile_name'], name, value)


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ondemand_operation_id', (YLeaf(YType.uint32, 'ondemand-operation-id'), ['int'])),
                                    ('probe_count', (YLeaf(YType.uint8, 'probe-count'), ['int'])),
                                ])
                                self.ondemand_operation_id = None
                                self.probe_count = None
                                self._segment_path = lambda: "ondemand-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/on-demand-operations/on-demand-operation/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions, ['ondemand_operation_id', 'probe_count'], name, value)


            class StatisticsCurrents(Entity):
                """
                Table of current statistics for SLA operations
                
                .. attribute:: statistics_current
                
                	Current statistics data for an SLA configured operation
                	**type**\: list of  		 :py:class:`StatisticsCurrent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.StatisticsCurrents, self).__init__()

                    self.yang_name = "statistics-currents"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics-current", ("statistics_current", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent))])
                    self._leafs = OrderedDict()

                    self.statistics_current = YList(self)
                    self._segment_path = lambda: "statistics-currents"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents, [], name, value)


                class StatisticsCurrent(Entity):
                    """
                    Current statistics data for an SLA configured
                    operation
                    
                    .. attribute:: profile_name
                    
                    	Profile Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mep_id
                    
                    	MEP ID in the range 1 to 8191. Either MEP ID or MAC address must be specified
                    	**type**\: int
                    
                    	**range:** 1..8191
                    
                    .. attribute:: mac_address
                    
                    	Unicast MAC Address in xxxx.xxxx.xxxx format. Either MEP ID or MAC address must be specified
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:  :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions>`
                    
                    .. attribute:: operation_schedule
                    
                    	Operation schedule
                    	**type**\:  :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule>`
                    
                    .. attribute:: probe_type
                    
                    	Type of probe used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_short
                    
                    	Short display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: display_long
                    
                    	Long display name used by the operation
                    	**type**\: str
                    
                    .. attribute:: flr_calculation_interval
                    
                    	Interval between FLR calculations for SLM, in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: operation_metric
                    
                    	Metrics gathered for the operation
                    	**type**\: list of  		 :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent, self).__init__()

                        self.yang_name = "statistics-current"
                        self.yang_parent_name = "statistics-currents"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("specific-options", ("specific_options", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions)), ("operation-schedule", ("operation_schedule", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule)), ("operation-metric", ("operation_metric", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric))])
                        self._leafs = OrderedDict([
                            ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('probe_type', (YLeaf(YType.str, 'probe-type'), ['str'])),
                            ('display_short', (YLeaf(YType.str, 'display-short'), ['str'])),
                            ('display_long', (YLeaf(YType.str, 'display-long'), ['str'])),
                            ('flr_calculation_interval', (YLeaf(YType.uint32, 'flr-calculation-interval'), ['int'])),
                        ])
                        self.profile_name = None
                        self.domain_name = None
                        self.interface_name = None
                        self.mep_id = None
                        self.mac_address = None
                        self.probe_type = None
                        self.display_short = None
                        self.display_long = None
                        self.flr_calculation_interval = None

                        self.specific_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions()
                        self.specific_options.parent = self
                        self._children_name_map["specific_options"] = "specific-options"

                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule()
                        self.operation_schedule.parent = self
                        self._children_name_map["operation_schedule"] = "operation-schedule"

                        self.operation_metric = YList(self)
                        self._segment_path = lambda: "statistics-current"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent, ['profile_name', 'domain_name', 'interface_name', 'mep_id', 'mac_address', 'probe_type', 'display_short', 'display_long', 'flr_calculation_interval'], name, value)


                    class SpecificOptions(Entity):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:  :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:  :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:  :py:class:`SlaOperOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperation>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions, self).__init__()

                            self.yang_name = "specific-options"
                            self.yang_parent_name = "statistics-current"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("configured-operation-options", ("configured_operation_options", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions)), ("ondemand-operation-options", ("ondemand_operation_options", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions))])
                            self._leafs = OrderedDict([
                                ('oper_type', (YLeaf(YType.enumeration, 'oper-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation', '')])),
                            ])
                            self.oper_type = None

                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self._children_name_map["configured_operation_options"] = "configured-operation-options"

                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self._children_name_map["ondemand_operation_options"] = "ondemand-operation-options"
                            self._segment_path = lambda: "specific-options"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions, ['oper_type'], name, value)


                        class ConfiguredOperationOptions(Entity):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions, self).__init__()

                                self.yang_name = "configured-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "configured-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions, ['profile_name'], name, value)


                        class OndemandOperationOptions(Entity):
                            """
                            Parameters for an ondemand operation
                            
                            .. attribute:: ondemand_operation_id
                            
                            	ID of the ondemand operation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: probe_count
                            
                            	Total number of probes sent during the operation
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions, self).__init__()

                                self.yang_name = "ondemand-operation-options"
                                self.yang_parent_name = "specific-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ondemand_operation_id', (YLeaf(YType.uint32, 'ondemand-operation-id'), ['int'])),
                                    ('probe_count', (YLeaf(YType.uint8, 'probe-count'), ['int'])),
                                ])
                                self.ondemand_operation_id = None
                                self.probe_count = None
                                self._segment_path = lambda: "ondemand-operation-options"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/specific-options/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions, ['ondemand_operation_id', 'probe_count'], name, value)


                    class OperationSchedule(Entity):
                        """
                        Operation schedule
                        
                        .. attribute:: start_time
                        
                        	Start time of the first probe, in seconds since the Unix Epoch
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: start_time_configured
                        
                        	Whether or not the operation start time was explicitly configured
                        	**type**\: bool
                        
                        .. attribute:: schedule_duration
                        
                        	Duration of a probe for the operation in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: schedule_interval
                        
                        	Interval between the start times of consecutive probes,  in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule, self).__init__()

                            self.yang_name = "operation-schedule"
                            self.yang_parent_name = "statistics-current"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                                ('start_time_configured', (YLeaf(YType.boolean, 'start-time-configured'), ['bool'])),
                                ('schedule_duration', (YLeaf(YType.uint32, 'schedule-duration'), ['int'])),
                                ('schedule_interval', (YLeaf(YType.uint32, 'schedule-interval'), ['int'])),
                            ])
                            self.start_time = None
                            self.start_time_configured = None
                            self.schedule_duration = None
                            self.schedule_interval = None
                            self._segment_path = lambda: "operation-schedule"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule, ['start_time', 'start_time_configured', 'schedule_duration', 'schedule_interval'], name, value)


                    class OperationMetric(Entity):
                        """
                        Metrics gathered for the operation
                        
                        .. attribute:: config
                        
                        	Configuration of the metric
                        	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config>`
                        
                        .. attribute:: bucket
                        
                        	Buckets stored for the metric
                        	**type**\: list of  		 :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric, self).__init__()

                            self.yang_name = "operation-metric"
                            self.yang_parent_name = "statistics-current"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config)), ("bucket", ("bucket", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket))])
                            self._leafs = OrderedDict()

                            self.config = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.bucket = YList(self)
                            self._segment_path = lambda: "operation-metric"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric, [], name, value)


                        class Config(Entity):
                            """
                            Configuration of the metric
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:  :py:class:`SlaRecordableMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetric>`
                            
                            .. attribute:: bins_count
                            
                            	Total number of bins into which to aggregate. 0 if no aggregation
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bins_width
                            
                            	Width of each bin into which to aggregate. 0 if no aggregation. For SLM, the units of this value are in single units of percent; for LMM they are in tenths of percent; for other measurements they are in milliseconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: bucket_size
                            
                            	Size of buckets into which measurements are collected
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: bucket_size_unit
                            
                            	Whether bucket size is 'per\-probe' or 'probes'
                            	**type**\:  :py:class:`SlaBucketSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSize>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "operation-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric', '')])),
                                    ('bins_count', (YLeaf(YType.uint16, 'bins-count'), ['int'])),
                                    ('bins_width', (YLeaf(YType.uint16, 'bins-width'), ['int'])),
                                    ('bucket_size', (YLeaf(YType.uint8, 'bucket-size'), ['int'])),
                                    ('bucket_size_unit', (YLeaf(YType.enumeration, 'bucket-size-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize', '')])),
                                    ('buckets_archive', (YLeaf(YType.uint32, 'buckets-archive'), ['int'])),
                                ])
                                self.metric_type = None
                                self.bins_count = None
                                self.bins_width = None
                                self.bucket_size = None
                                self.bucket_size_unit = None
                                self.buckets_archive = None
                                self._segment_path = lambda: "config"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config, ['metric_type', 'bins_count', 'bins_width', 'bucket_size', 'bucket_size_unit', 'buckets_archive'], name, value)


                        class Bucket(Entity):
                            """
                            Buckets stored for the metric
                            
                            .. attribute:: contents
                            
                            	The contents of the bucket; bins or samples
                            	**type**\:  :py:class:`Contents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents>`
                            
                            .. attribute:: start_at
                            
                            	Absolute time that the bucket started being filled at
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duration
                            
                            	Length of time for which the bucket is being filled in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: sent
                            
                            	Number of packets sent in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lost
                            
                            	Number of lost packets in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: corrupt
                            
                            	Number of corrupt packets in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_order
                            
                            	Number of packets recieved out\-of\-order in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplicates
                            
                            	Number of duplicate packets received in the probe
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: minimum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: maximum
                            
                            	Overall minimum result in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: time_of_minimum
                            
                            	Absolute time that the minimum value was recorded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_of_maximum
                            
                            	Absolute time that the maximum value was recorded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: average
                            
                            	Mean of the results in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: standard_deviation
                            
                            	Standard deviation of the results in the probe, in microseconds or millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: result_count
                            
                            	The count of samples collected in the bucket
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_sent_count
                            
                            	The number of data packets sent across the bucket, used in the calculation of overall FLR
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_lost_count
                            
                            	The number of data packets lost across the bucket, used in the calculation of overall FLR
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: overall_flr
                            
                            	Frame Loss Ratio across the whole bucket, in millionths of a percent
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: percentage
                            
                            .. attribute:: suspect_start_mid_bucket
                            
                            	Results suspect due to a probe starting mid\-way through a bucket
                            	**type**\: bool
                            
                            .. attribute:: suspect_schedule_latency
                            
                            	Results suspect due to scheduling latency causing one or more packets to not be sent
                            	**type**\: bool
                            
                            .. attribute:: suspect_send_fail
                            
                            	Results suspect due to failure to send one or more packets
                            	**type**\: bool
                            
                            .. attribute:: suspect_premature_end
                            
                            	Results suspect due to a probe ending prematurely
                            	**type**\: bool
                            
                            .. attribute:: suspect_clock_drift
                            
                            	Results suspect as more than 10 seconds time drift detected
                            	**type**\: bool
                            
                            .. attribute:: suspect_memory_allocation_failed
                            
                            	Results suspect due to a memory allocation failure
                            	**type**\: bool
                            
                            .. attribute:: suspect_cleared_mid_bucket
                            
                            	Results suspect as bucket was cleared mid\-way through being filled
                            	**type**\: bool
                            
                            .. attribute:: suspect_probe_restarted
                            
                            	Results suspect as probe restarted mid\-way through the bucket
                            	**type**\: bool
                            
                            .. attribute:: suspect_management_latency
                            
                            	Results suspect as processing of results has been delayed
                            	**type**\: bool
                            
                            .. attribute:: suspect_multiple_buckets
                            
                            	Results suspect as the probe has been configured across multiple buckets
                            	**type**\: bool
                            
                            .. attribute:: suspect_misordering
                            
                            	Results suspect as misordering has been detected , affecting results
                            	**type**\: bool
                            
                            .. attribute:: suspect_flr_low_packet_count
                            
                            	Results suspect as FLR calculated based on a low packet count
                            	**type**\: bool
                            
                            .. attribute:: premature_reason
                            
                            	If the probe ended prematurely, the error that caused a probe to end
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: premature_reason_string
                            
                            	Description of the error code that caused the probe to end prematurely. For informational purposes only
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket, self).__init__()

                                self.yang_name = "bucket"
                                self.yang_parent_name = "operation-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("contents", ("contents", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents))])
                                self._leafs = OrderedDict([
                                    ('start_at', (YLeaf(YType.uint32, 'start-at'), ['int'])),
                                    ('duration', (YLeaf(YType.uint32, 'duration'), ['int'])),
                                    ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                    ('lost', (YLeaf(YType.uint32, 'lost'), ['int'])),
                                    ('corrupt', (YLeaf(YType.uint32, 'corrupt'), ['int'])),
                                    ('out_of_order', (YLeaf(YType.uint32, 'out-of-order'), ['int'])),
                                    ('duplicates', (YLeaf(YType.uint32, 'duplicates'), ['int'])),
                                    ('minimum', (YLeaf(YType.int32, 'minimum'), ['int'])),
                                    ('maximum', (YLeaf(YType.int32, 'maximum'), ['int'])),
                                    ('time_of_minimum', (YLeaf(YType.uint32, 'time-of-minimum'), ['int'])),
                                    ('time_of_maximum', (YLeaf(YType.uint32, 'time-of-maximum'), ['int'])),
                                    ('average', (YLeaf(YType.int32, 'average'), ['int'])),
                                    ('standard_deviation', (YLeaf(YType.int32, 'standard-deviation'), ['int'])),
                                    ('result_count', (YLeaf(YType.uint32, 'result-count'), ['int'])),
                                    ('data_sent_count', (YLeaf(YType.uint32, 'data-sent-count'), ['int'])),
                                    ('data_lost_count', (YLeaf(YType.uint32, 'data-lost-count'), ['int'])),
                                    ('overall_flr', (YLeaf(YType.int32, 'overall-flr'), ['int'])),
                                    ('suspect_start_mid_bucket', (YLeaf(YType.boolean, 'suspect-start-mid-bucket'), ['bool'])),
                                    ('suspect_schedule_latency', (YLeaf(YType.boolean, 'suspect-schedule-latency'), ['bool'])),
                                    ('suspect_send_fail', (YLeaf(YType.boolean, 'suspect-send-fail'), ['bool'])),
                                    ('suspect_premature_end', (YLeaf(YType.boolean, 'suspect-premature-end'), ['bool'])),
                                    ('suspect_clock_drift', (YLeaf(YType.boolean, 'suspect-clock-drift'), ['bool'])),
                                    ('suspect_memory_allocation_failed', (YLeaf(YType.boolean, 'suspect-memory-allocation-failed'), ['bool'])),
                                    ('suspect_cleared_mid_bucket', (YLeaf(YType.boolean, 'suspect-cleared-mid-bucket'), ['bool'])),
                                    ('suspect_probe_restarted', (YLeaf(YType.boolean, 'suspect-probe-restarted'), ['bool'])),
                                    ('suspect_management_latency', (YLeaf(YType.boolean, 'suspect-management-latency'), ['bool'])),
                                    ('suspect_multiple_buckets', (YLeaf(YType.boolean, 'suspect-multiple-buckets'), ['bool'])),
                                    ('suspect_misordering', (YLeaf(YType.boolean, 'suspect-misordering'), ['bool'])),
                                    ('suspect_flr_low_packet_count', (YLeaf(YType.boolean, 'suspect-flr-low-packet-count'), ['bool'])),
                                    ('premature_reason', (YLeaf(YType.uint32, 'premature-reason'), ['int'])),
                                    ('premature_reason_string', (YLeaf(YType.str, 'premature-reason-string'), ['str'])),
                                ])
                                self.start_at = None
                                self.duration = None
                                self.sent = None
                                self.lost = None
                                self.corrupt = None
                                self.out_of_order = None
                                self.duplicates = None
                                self.minimum = None
                                self.maximum = None
                                self.time_of_minimum = None
                                self.time_of_maximum = None
                                self.average = None
                                self.standard_deviation = None
                                self.result_count = None
                                self.data_sent_count = None
                                self.data_lost_count = None
                                self.overall_flr = None
                                self.suspect_start_mid_bucket = None
                                self.suspect_schedule_latency = None
                                self.suspect_send_fail = None
                                self.suspect_premature_end = None
                                self.suspect_clock_drift = None
                                self.suspect_memory_allocation_failed = None
                                self.suspect_cleared_mid_bucket = None
                                self.suspect_probe_restarted = None
                                self.suspect_management_latency = None
                                self.suspect_multiple_buckets = None
                                self.suspect_misordering = None
                                self.suspect_flr_low_packet_count = None
                                self.premature_reason = None
                                self.premature_reason_string = None

                                self.contents = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self._children_name_map["contents"] = "contents"
                                self._segment_path = lambda: "bucket"
                                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket, ['start_at', 'duration', 'sent', 'lost', 'corrupt', 'out_of_order', 'duplicates', 'minimum', 'maximum', 'time_of_minimum', 'time_of_maximum', 'average', 'standard_deviation', 'result_count', 'data_sent_count', 'data_lost_count', 'overall_flr', 'suspect_start_mid_bucket', 'suspect_schedule_latency', 'suspect_send_fail', 'suspect_premature_end', 'suspect_clock_drift', 'suspect_memory_allocation_failed', 'suspect_cleared_mid_bucket', 'suspect_probe_restarted', 'suspect_management_latency', 'suspect_multiple_buckets', 'suspect_misordering', 'suspect_flr_low_packet_count', 'premature_reason', 'premature_reason_string'], name, value)


                            class Contents(Entity):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:  :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:  :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:  :py:class:`SlaOperBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucket>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents, self).__init__()

                                    self.yang_name = "contents"
                                    self.yang_parent_name = "bucket"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("aggregated", ("aggregated", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated)), ("unaggregated", ("unaggregated", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated))])
                                    self._leafs = OrderedDict([
                                        ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperBucket', '')])),
                                    ])
                                    self.bucket_type = None

                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self._children_name_map["aggregated"] = "aggregated"

                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self
                                    self._children_name_map["unaggregated"] = "unaggregated"
                                    self._segment_path = lambda: "contents"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents, ['bucket_type'], name, value)


                                class Aggregated(Entity):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of  		 :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated, self).__init__()

                                        self.yang_name = "aggregated"
                                        self.yang_parent_name = "contents"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("bins", ("bins", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins))])
                                        self._leafs = OrderedDict()

                                        self.bins = YList(self)
                                        self._segment_path = lambda: "aggregated"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/contents/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated, [], name, value)


                                    class Bins(Entity):
                                        """
                                        The bins of an SLA metric bucket
                                        
                                        .. attribute:: lower_bound
                                        
                                        	Lower bound (inclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: upper_bound
                                        
                                        	Upper bound (exclusive) of the bin, in milliseconds or single units of percent. This field is not used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: lower_bound_tenths
                                        
                                        	Lower bound (inclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: upper_bound_tenths
                                        
                                        	Upper bound (exclusive) of the bin, in tenths of percent. This field is only used for LMM measurements
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: percentage
                                        
                                        .. attribute:: sum
                                        
                                        	The sum of the results in the bin, in microseconds or millionths of a percent
                                        	**type**\: int
                                        
                                        	**range:** \-9223372036854775808..9223372036854775807
                                        
                                        .. attribute:: count
                                        
                                        	The total number of results in the bin
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2017-10-06'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, self).__init__()

                                            self.yang_name = "bins"
                                            self.yang_parent_name = "aggregated"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('lower_bound', (YLeaf(YType.int32, 'lower-bound'), ['int'])),
                                                ('upper_bound', (YLeaf(YType.int32, 'upper-bound'), ['int'])),
                                                ('lower_bound_tenths', (YLeaf(YType.int32, 'lower-bound-tenths'), ['int'])),
                                                ('upper_bound_tenths', (YLeaf(YType.int32, 'upper-bound-tenths'), ['int'])),
                                                ('sum', (YLeaf(YType.int64, 'sum'), ['int'])),
                                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ])
                                            self.lower_bound = None
                                            self.upper_bound = None
                                            self.lower_bound_tenths = None
                                            self.upper_bound_tenths = None
                                            self.sum = None
                                            self.count = None
                                            self._segment_path = lambda: "bins"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/contents/aggregated/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins, ['lower_bound', 'upper_bound', 'lower_bound_tenths', 'upper_bound_tenths', 'sum', 'count'], name, value)


                                class Unaggregated(Entity):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated, self).__init__()

                                        self.yang_name = "unaggregated"
                                        self.yang_parent_name = "contents"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("sample", ("sample", Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample))])
                                        self._leafs = OrderedDict()

                                        self.sample = YList(self)
                                        self._segment_path = lambda: "unaggregated"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/contents/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated, [], name, value)


                                    class Sample(Entity):
                                        """
                                        The samples of an SLA metric bucket
                                        
                                        .. attribute:: sent_at
                                        
                                        	The time (in milliseconds relative to the start time of the bucket) that the sample was sent at
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: sent
                                        
                                        	Whether the sample packet was sucessfully sent
                                        	**type**\: bool
                                        
                                        .. attribute:: timed_out
                                        
                                        	Whether the sample packet timed out
                                        	**type**\: bool
                                        
                                        .. attribute:: corrupt
                                        
                                        	Whether the sample packet was corrupt
                                        	**type**\: bool
                                        
                                        .. attribute:: out_of_order
                                        
                                        	Whether the sample packet was received out\-of\-order
                                        	**type**\: bool
                                        
                                        .. attribute:: no_data_packets
                                        
                                        	Whether a measurement could not be made because no data packets were sent in the sample period. Only applicable for LMM measurements
                                        	**type**\: bool
                                        
                                        .. attribute:: result
                                        
                                        	The result (in microseconds or millionths of a percent) of the sample, if available
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: frames_sent
                                        
                                        	For FLR measurements, the number of frames sent, if available
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: frames_lost
                                        
                                        	For FLR measurements, the number of frames lost, if available
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-cfm-oper'
                                        _revision = '2017-10-06'

                                        def __init__(self):
                                            super(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, self).__init__()

                                            self.yang_name = "sample"
                                            self.yang_parent_name = "unaggregated"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sent_at', (YLeaf(YType.uint32, 'sent-at'), ['int'])),
                                                ('sent', (YLeaf(YType.boolean, 'sent'), ['bool'])),
                                                ('timed_out', (YLeaf(YType.boolean, 'timed-out'), ['bool'])),
                                                ('corrupt', (YLeaf(YType.boolean, 'corrupt'), ['bool'])),
                                                ('out_of_order', (YLeaf(YType.boolean, 'out-of-order'), ['bool'])),
                                                ('no_data_packets', (YLeaf(YType.boolean, 'no-data-packets'), ['bool'])),
                                                ('result', (YLeaf(YType.int32, 'result'), ['int'])),
                                                ('frames_sent', (YLeaf(YType.uint32, 'frames-sent'), ['int'])),
                                                ('frames_lost', (YLeaf(YType.uint32, 'frames-lost'), ['int'])),
                                            ])
                                            self.sent_at = None
                                            self.sent = None
                                            self.timed_out = None
                                            self.corrupt = None
                                            self.out_of_order = None
                                            self.no_data_packets = None
                                            self.result = None
                                            self.frames_sent = None
                                            self.frames_lost = None
                                            self._segment_path = lambda: "sample"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla/protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/statistics-currents/statistics-current/operation-metric/bucket/contents/unaggregated/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample, ['sent_at', 'sent', 'timed_out', 'corrupt', 'out_of_order', 'no_data_packets', 'result', 'frames_sent', 'frames_lost'], name, value)

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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-infra-sla-oper:sla-nodes"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = SlaNodes()
        return self._top_entity

