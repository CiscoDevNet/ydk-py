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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Sla(object):
    """
    SLA oper commands
    
    .. attribute:: protocols
    
    	Table of all SLA protocols
    	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols>`
    
    

    """

    _prefix = 'infra-sla-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.protocols = Sla.Protocols()
        self.protocols.parent = self


    class Protocols(object):
        """
        Table of all SLA protocols
        
        .. attribute:: ethernet
        
        	The Ethernet SLA protocol
        	**type**\:   :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet>`
        
        

        """

        _prefix = 'infra-sla-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ethernet = Sla.Protocols.Ethernet()
            self.ethernet.parent = self


        class Ethernet(object):
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
                self.parent = None
                self.config_errors = Sla.Protocols.Ethernet.ConfigErrors()
                self.config_errors.parent = self
                self.on_demand_operations = Sla.Protocols.Ethernet.OnDemandOperations()
                self.on_demand_operations.parent = self
                self.operations = Sla.Protocols.Ethernet.Operations()
                self.operations.parent = self
                self.statistics_currents = Sla.Protocols.Ethernet.StatisticsCurrents()
                self.statistics_currents.parent = self
                self.statistics_historicals = Sla.Protocols.Ethernet.StatisticsHistoricals()
                self.statistics_historicals.parent = self
                self.statistics_on_demand_currents = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents()
                self.statistics_on_demand_currents.parent = self
                self.statistics_on_demand_historicals = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals()
                self.statistics_on_demand_historicals.parent = self


            class StatisticsOnDemandCurrents(object):
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
                    self.parent = None
                    self.statistics_on_demand_current = YList()
                    self.statistics_on_demand_current.parent = self
                    self.statistics_on_demand_current.name = 'statistics_on_demand_current'


                class StatisticsOnDemandCurrent(object):
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
                        self.parent = None
                        self.display_long = None
                        self.display_short = None
                        self.domain_name = None
                        self.flr_calculation_interval = None
                        self.interface_name = None
                        self.mac_address = None
                        self.mep_id = None
                        self.operation_id = None
                        self.operation_metric = YList()
                        self.operation_metric.parent = self
                        self.operation_metric.name = 'operation_metric'
                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule()
                        self.operation_schedule.parent = self
                        self.probe_type = None
                        self.specific_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions()
                        self.specific_options.parent = self


                    class SpecificOptions(object):
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
                        	**type**\:   :py:class:`SlaOperOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperationEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self.oper_type = None


                        class ConfiguredOperationOptions(object):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:configured-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions']['meta_info']


                        class OndemandOperationOptions(object):
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
                                self.parent = None
                                self.ondemand_operation_id = None
                                self.probe_count = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:ondemand-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ondemand_operation_id is not None:
                                    return True

                                if self.probe_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:specific-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.configured_operation_options is not None and self.configured_operation_options._has_data():
                                return True

                            if self.ondemand_operation_options is not None and self.ondemand_operation_options._has_data():
                                return True

                            if self.oper_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions']['meta_info']


                    class OperationSchedule(object):
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
                            self.parent = None
                            self.schedule_duration = None
                            self.schedule_interval = None
                            self.start_time = None
                            self.start_time_configured = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-schedule'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.schedule_duration is not None:
                                return True

                            if self.schedule_interval is not None:
                                return True

                            if self.start_time is not None:
                                return True

                            if self.start_time_configured is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule']['meta_info']


                    class OperationMetric(object):
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
                            self.parent = None
                            self.bucket = YList()
                            self.bucket.parent = self
                            self.bucket.name = 'bucket'
                            self.config = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config()
                            self.config.parent = self


                        class Config(object):
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
                            	**type**\:   :py:class:`SlaBucketSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSizeEnum>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:   :py:class:`SlaRecordableMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetricEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bins_count = None
                                self.bins_width = None
                                self.bucket_size = None
                                self.bucket_size_unit = None
                                self.buckets_archive = None
                                self.metric_type = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bins_count is not None:
                                    return True

                                if self.bins_width is not None:
                                    return True

                                if self.bucket_size is not None:
                                    return True

                                if self.bucket_size_unit is not None:
                                    return True

                                if self.buckets_archive is not None:
                                    return True

                                if self.metric_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config']['meta_info']


                        class Bucket(object):
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
                                self.parent = None
                                self.average = None
                                self.contents = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self.corrupt = None
                                self.data_lost_count = None
                                self.data_sent_count = None
                                self.duplicates = None
                                self.duration = None
                                self.lost = None
                                self.maximum = None
                                self.minimum = None
                                self.out_of_order = None
                                self.overall_flr = None
                                self.premature_reason = None
                                self.premature_reason_string = None
                                self.result_count = None
                                self.sent = None
                                self.standard_deviation = None
                                self.start_at = None
                                self.suspect_cleared_mid_bucket = None
                                self.suspect_clock_drift = None
                                self.suspect_flr_low_packet_count = None
                                self.suspect_management_latency = None
                                self.suspect_memory_allocation_failed = None
                                self.suspect_misordering = None
                                self.suspect_multiple_buckets = None
                                self.suspect_premature_end = None
                                self.suspect_probe_restarted = None
                                self.suspect_schedule_latency = None
                                self.suspect_send_fail = None
                                self.suspect_start_mid_bucket = None
                                self.time_of_maximum = None
                                self.time_of_minimum = None


                            class Contents(object):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:   :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:   :py:class:`SlaOperBucketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucketEnum>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:   :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self.bucket_type = None
                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self


                                class Aggregated(object):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bins = YList()
                                        self.bins.parent = self
                                        self.bins.name = 'bins'


                                    class Bins(object):
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
                                            self.parent = None
                                            self.count = None
                                            self.lower_bound = None
                                            self.lower_bound_tenths = None
                                            self.sum = None
                                            self.upper_bound = None
                                            self.upper_bound_tenths = None

                                        @property
                                        def _common_path(self):

                                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:aggregated/Cisco-IOS-XR-ethernet-cfm-oper:bins'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.count is not None:
                                                return True

                                            if self.lower_bound is not None:
                                                return True

                                            if self.lower_bound_tenths is not None:
                                                return True

                                            if self.sum is not None:
                                                return True

                                            if self.upper_bound is not None:
                                                return True

                                            if self.upper_bound_tenths is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins']['meta_info']

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:aggregated'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.bins is not None:
                                            for child_ref in self.bins:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated']['meta_info']


                                class Unaggregated(object):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.sample = YList()
                                        self.sample.parent = self
                                        self.sample.name = 'sample'


                                    class Sample(object):
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
                                            self.parent = None
                                            self.corrupt = None
                                            self.frames_lost = None
                                            self.frames_sent = None
                                            self.no_data_packets = None
                                            self.out_of_order = None
                                            self.result = None
                                            self.sent = None
                                            self.sent_at = None
                                            self.timed_out = None

                                        @property
                                        def _common_path(self):

                                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:unaggregated/Cisco-IOS-XR-ethernet-cfm-oper:sample'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.corrupt is not None:
                                                return True

                                            if self.frames_lost is not None:
                                                return True

                                            if self.frames_sent is not None:
                                                return True

                                            if self.no_data_packets is not None:
                                                return True

                                            if self.out_of_order is not None:
                                                return True

                                            if self.result is not None:
                                                return True

                                            if self.sent is not None:
                                                return True

                                            if self.sent_at is not None:
                                                return True

                                            if self.timed_out is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample']['meta_info']

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:unaggregated'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.sample is not None:
                                            for child_ref in self.sample:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aggregated is not None and self.aggregated._has_data():
                                        return True

                                    if self.bucket_type is not None:
                                        return True

                                    if self.unaggregated is not None and self.unaggregated._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.average is not None:
                                    return True

                                if self.contents is not None and self.contents._has_data():
                                    return True

                                if self.corrupt is not None:
                                    return True

                                if self.data_lost_count is not None:
                                    return True

                                if self.data_sent_count is not None:
                                    return True

                                if self.duplicates is not None:
                                    return True

                                if self.duration is not None:
                                    return True

                                if self.lost is not None:
                                    return True

                                if self.maximum is not None:
                                    return True

                                if self.minimum is not None:
                                    return True

                                if self.out_of_order is not None:
                                    return True

                                if self.overall_flr is not None:
                                    return True

                                if self.premature_reason is not None:
                                    return True

                                if self.premature_reason_string is not None:
                                    return True

                                if self.result_count is not None:
                                    return True

                                if self.sent is not None:
                                    return True

                                if self.standard_deviation is not None:
                                    return True

                                if self.start_at is not None:
                                    return True

                                if self.suspect_cleared_mid_bucket is not None:
                                    return True

                                if self.suspect_clock_drift is not None:
                                    return True

                                if self.suspect_flr_low_packet_count is not None:
                                    return True

                                if self.suspect_management_latency is not None:
                                    return True

                                if self.suspect_memory_allocation_failed is not None:
                                    return True

                                if self.suspect_misordering is not None:
                                    return True

                                if self.suspect_multiple_buckets is not None:
                                    return True

                                if self.suspect_premature_end is not None:
                                    return True

                                if self.suspect_probe_restarted is not None:
                                    return True

                                if self.suspect_schedule_latency is not None:
                                    return True

                                if self.suspect_send_fail is not None:
                                    return True

                                if self.suspect_start_mid_bucket is not None:
                                    return True

                                if self.time_of_maximum is not None:
                                    return True

                                if self.time_of_minimum is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bucket is not None:
                                for child_ref in self.bucket:
                                    if child_ref._has_data():
                                        return True

                            if self.config is not None and self.config._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-current'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.display_long is not None:
                            return True

                        if self.display_short is not None:
                            return True

                        if self.domain_name is not None:
                            return True

                        if self.flr_calculation_interval is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.operation_id is not None:
                            return True

                        if self.operation_metric is not None:
                            for child_ref in self.operation_metric:
                                if child_ref._has_data():
                                    return True

                        if self.operation_schedule is not None and self.operation_schedule._has_data():
                            return True

                        if self.probe_type is not None:
                            return True

                        if self.specific_options is not None and self.specific_options._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-currents'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.statistics_on_demand_current is not None:
                        for child_ref in self.statistics_on_demand_current:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents']['meta_info']


            class Operations(object):
                """
                Table of SLA operations
                
                .. attribute:: operation
                
                	SLA operation to get operation data for
                	**type**\: list of    :py:class:`Operation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.operation = YList()
                    self.operation.parent = self
                    self.operation.name = 'operation'


                class Operation(object):
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
                    	**type**\:   :py:class:`ProfileOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions>`
                    
                    .. attribute:: specific_options
                    
                    	Options specific to the type of operation
                    	**type**\:   :py:class:`SpecificOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.display_long = None
                        self.display_short = None
                        self.domain_name = None
                        self.interface_name = None
                        self.last_run = None
                        self.mac_address = None
                        self.mep_id = None
                        self.profile_name = None
                        self.profile_options = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions()
                        self.profile_options.parent = self
                        self.specific_options = Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions()
                        self.specific_options.parent = self


                    class ProfileOptions(object):
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
                        	**type**\: list of    :py:class:`OperationMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric>`
                        
                        .. attribute:: operation_schedule
                        
                        	Operation schedule
                        	**type**\:   :py:class:`OperationSchedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule>`
                        
                        .. attribute:: packet_padding
                        
                        	Configuration of the packet padding
                        	**type**\:   :py:class:`PacketPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding>`
                        
                        .. attribute:: packets_per_burst
                        
                        	Number of packets sent per burst
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: priority
                        
                        	Priority at which to send the packet, if configured
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority>`
                        
                        .. attribute:: probe_type
                        
                        	Type of probe used by the operation
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bursts_per_probe = None
                            self.flr_calculation_interval = None
                            self.inter_burst_interval = None
                            self.inter_packet_interval = None
                            self.operation_metric = YList()
                            self.operation_metric.parent = self
                            self.operation_metric.name = 'operation_metric'
                            self.operation_schedule = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule()
                            self.operation_schedule.parent = self
                            self.packet_padding = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding()
                            self.packet_padding.parent = self
                            self.packets_per_burst = None
                            self.priority = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority()
                            self.priority.parent = self
                            self.probe_type = None


                        class PacketPadding(object):
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
                            	**type**\:   :py:class:`SlaOperTestPatternSchemeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperTestPatternSchemeEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.packet_pad_size = None
                                self.test_pattern_pad_hex_string = None
                                self.test_pattern_pad_scheme = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:packet-padding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.packet_pad_size is not None:
                                    return True

                                if self.test_pattern_pad_hex_string is not None:
                                    return True

                                if self.test_pattern_pad_scheme is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding']['meta_info']


                        class Priority(object):
                            """
                            Priority at which to send the packet, if
                            configured
                            
                            .. attribute:: cos
                            
                            	3\-bit COS priority value applied to packets
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: priority_type
                            
                            	PriorityType
                            	**type**\:   :py:class:`SlaOperPacketPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperPacketPriorityEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.cos = None
                                self.priority_type = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:priority'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.cos is not None:
                                    return True

                                if self.priority_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority']['meta_info']


                        class OperationSchedule(object):
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
                                self.parent = None
                                self.schedule_duration = None
                                self.schedule_interval = None
                                self.start_time = None
                                self.start_time_configured = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:operation-schedule'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.schedule_duration is not None:
                                    return True

                                if self.schedule_interval is not None:
                                    return True

                                if self.start_time is not None:
                                    return True

                                if self.start_time_configured is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule']['meta_info']


                        class OperationMetric(object):
                            """
                            Array of the metrics that are measured by the
                            operation
                            
                            .. attribute:: current_buckets_archive
                            
                            	Number of valid buckets currently in the buckets archive
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_config
                            
                            	Configuration of the metric
                            	**type**\:   :py:class:`MetricConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.current_buckets_archive = None
                                self.metric_config = Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig()
                                self.metric_config.parent = self


                            class MetricConfig(object):
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
                                	**type**\:   :py:class:`SlaBucketSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSizeEnum>`
                                
                                .. attribute:: buckets_archive
                                
                                	Maximum number of buckets to store in memory
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric_type
                                
                                	Type of metric to which this configuration applies
                                	**type**\:   :py:class:`SlaRecordableMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetricEnum>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bins_count = None
                                    self.bins_width = None
                                    self.bucket_size = None
                                    self.bucket_size_unit = None
                                    self.buckets_archive = None
                                    self.metric_type = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:metric-config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bins_count is not None:
                                        return True

                                    if self.bins_width is not None:
                                        return True

                                    if self.bucket_size is not None:
                                        return True

                                    if self.bucket_size_unit is not None:
                                        return True

                                    if self.buckets_archive is not None:
                                        return True

                                    if self.metric_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.current_buckets_archive is not None:
                                    return True

                                if self.metric_config is not None and self.metric_config._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bursts_per_probe is not None:
                                return True

                            if self.flr_calculation_interval is not None:
                                return True

                            if self.inter_burst_interval is not None:
                                return True

                            if self.inter_packet_interval is not None:
                                return True

                            if self.operation_metric is not None:
                                for child_ref in self.operation_metric:
                                    if child_ref._has_data():
                                        return True

                            if self.operation_schedule is not None and self.operation_schedule._has_data():
                                return True

                            if self.packet_padding is not None and self.packet_padding._has_data():
                                return True

                            if self.packets_per_burst is not None:
                                return True

                            if self.priority is not None and self.priority._has_data():
                                return True

                            if self.probe_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions']['meta_info']


                    class SpecificOptions(object):
                        """
                        Options specific to the type of operation
                        
                        .. attribute:: configured_operation_options
                        
                        	Parameters for a configured operation
                        	**type**\:   :py:class:`ConfiguredOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions>`
                        
                        .. attribute:: ondemand_operation_options
                        
                        	Parameters for an ondemand operation
                        	**type**\:   :py:class:`OndemandOperationOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions>`
                        
                        .. attribute:: oper_type
                        
                        	OperType
                        	**type**\:   :py:class:`SlaOperOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperationEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.configured_operation_options = Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self.ondemand_operation_options = Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self.oper_type = None


                        class ConfiguredOperationOptions(object):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:configured-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions']['meta_info']


                        class OndemandOperationOptions(object):
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
                                self.parent = None
                                self.ondemand_operation_id = None
                                self.probe_count = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:ondemand-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ondemand_operation_id is not None:
                                    return True

                                if self.probe_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation/Cisco-IOS-XR-ethernet-cfm-oper:specific-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.configured_operation_options is not None and self.configured_operation_options._has_data():
                                return True

                            if self.ondemand_operation_options is not None and self.ondemand_operation_options._has_data():
                                return True

                            if self.oper_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations/Cisco-IOS-XR-ethernet-cfm-oper:operation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.display_long is not None:
                            return True

                        if self.display_short is not None:
                            return True

                        if self.domain_name is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.last_run is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.profile_name is not None:
                            return True

                        if self.profile_options is not None and self.profile_options._has_data():
                            return True

                        if self.specific_options is not None and self.specific_options._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.Operations.Operation']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:operations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.operation is not None:
                        for child_ref in self.operation:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.Operations']['meta_info']


            class StatisticsHistoricals(object):
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
                    self.parent = None
                    self.statistics_historical = YList()
                    self.statistics_historical.parent = self
                    self.statistics_historical.name = 'statistics_historical'


                class StatisticsHistorical(object):
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
                        self.parent = None
                        self.display_long = None
                        self.display_short = None
                        self.domain_name = None
                        self.flr_calculation_interval = None
                        self.interface_name = None
                        self.mac_address = None
                        self.mep_id = None
                        self.operation_metric = YList()
                        self.operation_metric.parent = self
                        self.operation_metric.name = 'operation_metric'
                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule()
                        self.operation_schedule.parent = self
                        self.probe_type = None
                        self.profile_name = None
                        self.specific_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions()
                        self.specific_options.parent = self


                    class SpecificOptions(object):
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
                        	**type**\:   :py:class:`SlaOperOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperationEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self.oper_type = None


                        class ConfiguredOperationOptions(object):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:configured-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions']['meta_info']


                        class OndemandOperationOptions(object):
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
                                self.parent = None
                                self.ondemand_operation_id = None
                                self.probe_count = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:ondemand-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ondemand_operation_id is not None:
                                    return True

                                if self.probe_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:specific-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.configured_operation_options is not None and self.configured_operation_options._has_data():
                                return True

                            if self.ondemand_operation_options is not None and self.ondemand_operation_options._has_data():
                                return True

                            if self.oper_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions']['meta_info']


                    class OperationSchedule(object):
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
                            self.parent = None
                            self.schedule_duration = None
                            self.schedule_interval = None
                            self.start_time = None
                            self.start_time_configured = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-schedule'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.schedule_duration is not None:
                                return True

                            if self.schedule_interval is not None:
                                return True

                            if self.start_time is not None:
                                return True

                            if self.start_time_configured is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule']['meta_info']


                    class OperationMetric(object):
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
                            self.parent = None
                            self.bucket = YList()
                            self.bucket.parent = self
                            self.bucket.name = 'bucket'
                            self.config = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config()
                            self.config.parent = self


                        class Config(object):
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
                            	**type**\:   :py:class:`SlaBucketSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSizeEnum>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:   :py:class:`SlaRecordableMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetricEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bins_count = None
                                self.bins_width = None
                                self.bucket_size = None
                                self.bucket_size_unit = None
                                self.buckets_archive = None
                                self.metric_type = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bins_count is not None:
                                    return True

                                if self.bins_width is not None:
                                    return True

                                if self.bucket_size is not None:
                                    return True

                                if self.bucket_size_unit is not None:
                                    return True

                                if self.buckets_archive is not None:
                                    return True

                                if self.metric_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config']['meta_info']


                        class Bucket(object):
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
                                self.parent = None
                                self.average = None
                                self.contents = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self.corrupt = None
                                self.data_lost_count = None
                                self.data_sent_count = None
                                self.duplicates = None
                                self.duration = None
                                self.lost = None
                                self.maximum = None
                                self.minimum = None
                                self.out_of_order = None
                                self.overall_flr = None
                                self.premature_reason = None
                                self.premature_reason_string = None
                                self.result_count = None
                                self.sent = None
                                self.standard_deviation = None
                                self.start_at = None
                                self.suspect_cleared_mid_bucket = None
                                self.suspect_clock_drift = None
                                self.suspect_flr_low_packet_count = None
                                self.suspect_management_latency = None
                                self.suspect_memory_allocation_failed = None
                                self.suspect_misordering = None
                                self.suspect_multiple_buckets = None
                                self.suspect_premature_end = None
                                self.suspect_probe_restarted = None
                                self.suspect_schedule_latency = None
                                self.suspect_send_fail = None
                                self.suspect_start_mid_bucket = None
                                self.time_of_maximum = None
                                self.time_of_minimum = None


                            class Contents(object):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:   :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:   :py:class:`SlaOperBucketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucketEnum>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:   :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self.bucket_type = None
                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self


                                class Aggregated(object):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bins = YList()
                                        self.bins.parent = self
                                        self.bins.name = 'bins'


                                    class Bins(object):
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
                                            self.parent = None
                                            self.count = None
                                            self.lower_bound = None
                                            self.lower_bound_tenths = None
                                            self.sum = None
                                            self.upper_bound = None
                                            self.upper_bound_tenths = None

                                        @property
                                        def _common_path(self):

                                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:aggregated/Cisco-IOS-XR-ethernet-cfm-oper:bins'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.count is not None:
                                                return True

                                            if self.lower_bound is not None:
                                                return True

                                            if self.lower_bound_tenths is not None:
                                                return True

                                            if self.sum is not None:
                                                return True

                                            if self.upper_bound is not None:
                                                return True

                                            if self.upper_bound_tenths is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins']['meta_info']

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:aggregated'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.bins is not None:
                                            for child_ref in self.bins:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated']['meta_info']


                                class Unaggregated(object):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.sample = YList()
                                        self.sample.parent = self
                                        self.sample.name = 'sample'


                                    class Sample(object):
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
                                            self.parent = None
                                            self.corrupt = None
                                            self.frames_lost = None
                                            self.frames_sent = None
                                            self.no_data_packets = None
                                            self.out_of_order = None
                                            self.result = None
                                            self.sent = None
                                            self.sent_at = None
                                            self.timed_out = None

                                        @property
                                        def _common_path(self):

                                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:unaggregated/Cisco-IOS-XR-ethernet-cfm-oper:sample'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.corrupt is not None:
                                                return True

                                            if self.frames_lost is not None:
                                                return True

                                            if self.frames_sent is not None:
                                                return True

                                            if self.no_data_packets is not None:
                                                return True

                                            if self.out_of_order is not None:
                                                return True

                                            if self.result is not None:
                                                return True

                                            if self.sent is not None:
                                                return True

                                            if self.sent_at is not None:
                                                return True

                                            if self.timed_out is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample']['meta_info']

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:unaggregated'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.sample is not None:
                                            for child_ref in self.sample:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aggregated is not None and self.aggregated._has_data():
                                        return True

                                    if self.bucket_type is not None:
                                        return True

                                    if self.unaggregated is not None and self.unaggregated._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.average is not None:
                                    return True

                                if self.contents is not None and self.contents._has_data():
                                    return True

                                if self.corrupt is not None:
                                    return True

                                if self.data_lost_count is not None:
                                    return True

                                if self.data_sent_count is not None:
                                    return True

                                if self.duplicates is not None:
                                    return True

                                if self.duration is not None:
                                    return True

                                if self.lost is not None:
                                    return True

                                if self.maximum is not None:
                                    return True

                                if self.minimum is not None:
                                    return True

                                if self.out_of_order is not None:
                                    return True

                                if self.overall_flr is not None:
                                    return True

                                if self.premature_reason is not None:
                                    return True

                                if self.premature_reason_string is not None:
                                    return True

                                if self.result_count is not None:
                                    return True

                                if self.sent is not None:
                                    return True

                                if self.standard_deviation is not None:
                                    return True

                                if self.start_at is not None:
                                    return True

                                if self.suspect_cleared_mid_bucket is not None:
                                    return True

                                if self.suspect_clock_drift is not None:
                                    return True

                                if self.suspect_flr_low_packet_count is not None:
                                    return True

                                if self.suspect_management_latency is not None:
                                    return True

                                if self.suspect_memory_allocation_failed is not None:
                                    return True

                                if self.suspect_misordering is not None:
                                    return True

                                if self.suspect_multiple_buckets is not None:
                                    return True

                                if self.suspect_premature_end is not None:
                                    return True

                                if self.suspect_probe_restarted is not None:
                                    return True

                                if self.suspect_schedule_latency is not None:
                                    return True

                                if self.suspect_send_fail is not None:
                                    return True

                                if self.suspect_start_mid_bucket is not None:
                                    return True

                                if self.time_of_maximum is not None:
                                    return True

                                if self.time_of_minimum is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bucket is not None:
                                for child_ref in self.bucket:
                                    if child_ref._has_data():
                                        return True

                            if self.config is not None and self.config._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historical'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.display_long is not None:
                            return True

                        if self.display_short is not None:
                            return True

                        if self.domain_name is not None:
                            return True

                        if self.flr_calculation_interval is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.operation_metric is not None:
                            for child_ref in self.operation_metric:
                                if child_ref._has_data():
                                    return True

                        if self.operation_schedule is not None and self.operation_schedule._has_data():
                            return True

                        if self.probe_type is not None:
                            return True

                        if self.profile_name is not None:
                            return True

                        if self.specific_options is not None and self.specific_options._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-historicals'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.statistics_historical is not None:
                        for child_ref in self.statistics_historical:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals']['meta_info']


            class StatisticsOnDemandHistoricals(object):
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
                    self.parent = None
                    self.statistics_on_demand_historical = YList()
                    self.statistics_on_demand_historical.parent = self
                    self.statistics_on_demand_historical.name = 'statistics_on_demand_historical'


                class StatisticsOnDemandHistorical(object):
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
                        self.parent = None
                        self.display_long = None
                        self.display_short = None
                        self.domain_name = None
                        self.flr_calculation_interval = None
                        self.interface_name = None
                        self.mac_address = None
                        self.mep_id = None
                        self.operation_id = None
                        self.operation_metric = YList()
                        self.operation_metric.parent = self
                        self.operation_metric.name = 'operation_metric'
                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule()
                        self.operation_schedule.parent = self
                        self.probe_type = None
                        self.specific_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions()
                        self.specific_options.parent = self


                    class SpecificOptions(object):
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
                        	**type**\:   :py:class:`SlaOperOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperationEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self.oper_type = None


                        class ConfiguredOperationOptions(object):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:configured-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions']['meta_info']


                        class OndemandOperationOptions(object):
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
                                self.parent = None
                                self.ondemand_operation_id = None
                                self.probe_count = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:ondemand-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ondemand_operation_id is not None:
                                    return True

                                if self.probe_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:specific-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.configured_operation_options is not None and self.configured_operation_options._has_data():
                                return True

                            if self.ondemand_operation_options is not None and self.ondemand_operation_options._has_data():
                                return True

                            if self.oper_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions']['meta_info']


                    class OperationSchedule(object):
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
                            self.parent = None
                            self.schedule_duration = None
                            self.schedule_interval = None
                            self.start_time = None
                            self.start_time_configured = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-schedule'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.schedule_duration is not None:
                                return True

                            if self.schedule_interval is not None:
                                return True

                            if self.start_time is not None:
                                return True

                            if self.start_time_configured is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule']['meta_info']


                    class OperationMetric(object):
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
                            self.parent = None
                            self.bucket = YList()
                            self.bucket.parent = self
                            self.bucket.name = 'bucket'
                            self.config = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config()
                            self.config.parent = self


                        class Config(object):
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
                            	**type**\:   :py:class:`SlaBucketSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSizeEnum>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:   :py:class:`SlaRecordableMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetricEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bins_count = None
                                self.bins_width = None
                                self.bucket_size = None
                                self.bucket_size_unit = None
                                self.buckets_archive = None
                                self.metric_type = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bins_count is not None:
                                    return True

                                if self.bins_width is not None:
                                    return True

                                if self.bucket_size is not None:
                                    return True

                                if self.bucket_size_unit is not None:
                                    return True

                                if self.buckets_archive is not None:
                                    return True

                                if self.metric_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config']['meta_info']


                        class Bucket(object):
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
                                self.parent = None
                                self.average = None
                                self.contents = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self.corrupt = None
                                self.data_lost_count = None
                                self.data_sent_count = None
                                self.duplicates = None
                                self.duration = None
                                self.lost = None
                                self.maximum = None
                                self.minimum = None
                                self.out_of_order = None
                                self.overall_flr = None
                                self.premature_reason = None
                                self.premature_reason_string = None
                                self.result_count = None
                                self.sent = None
                                self.standard_deviation = None
                                self.start_at = None
                                self.suspect_cleared_mid_bucket = None
                                self.suspect_clock_drift = None
                                self.suspect_flr_low_packet_count = None
                                self.suspect_management_latency = None
                                self.suspect_memory_allocation_failed = None
                                self.suspect_misordering = None
                                self.suspect_multiple_buckets = None
                                self.suspect_premature_end = None
                                self.suspect_probe_restarted = None
                                self.suspect_schedule_latency = None
                                self.suspect_send_fail = None
                                self.suspect_start_mid_bucket = None
                                self.time_of_maximum = None
                                self.time_of_minimum = None


                            class Contents(object):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:   :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:   :py:class:`SlaOperBucketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucketEnum>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:   :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self.bucket_type = None
                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self


                                class Aggregated(object):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bins = YList()
                                        self.bins.parent = self
                                        self.bins.name = 'bins'


                                    class Bins(object):
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
                                            self.parent = None
                                            self.count = None
                                            self.lower_bound = None
                                            self.lower_bound_tenths = None
                                            self.sum = None
                                            self.upper_bound = None
                                            self.upper_bound_tenths = None

                                        @property
                                        def _common_path(self):

                                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:aggregated/Cisco-IOS-XR-ethernet-cfm-oper:bins'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.count is not None:
                                                return True

                                            if self.lower_bound is not None:
                                                return True

                                            if self.lower_bound_tenths is not None:
                                                return True

                                            if self.sum is not None:
                                                return True

                                            if self.upper_bound is not None:
                                                return True

                                            if self.upper_bound_tenths is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins']['meta_info']

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:aggregated'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.bins is not None:
                                            for child_ref in self.bins:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated']['meta_info']


                                class Unaggregated(object):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.sample = YList()
                                        self.sample.parent = self
                                        self.sample.name = 'sample'


                                    class Sample(object):
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
                                            self.parent = None
                                            self.corrupt = None
                                            self.frames_lost = None
                                            self.frames_sent = None
                                            self.no_data_packets = None
                                            self.out_of_order = None
                                            self.result = None
                                            self.sent = None
                                            self.sent_at = None
                                            self.timed_out = None

                                        @property
                                        def _common_path(self):

                                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:unaggregated/Cisco-IOS-XR-ethernet-cfm-oper:sample'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.corrupt is not None:
                                                return True

                                            if self.frames_lost is not None:
                                                return True

                                            if self.frames_sent is not None:
                                                return True

                                            if self.no_data_packets is not None:
                                                return True

                                            if self.out_of_order is not None:
                                                return True

                                            if self.result is not None:
                                                return True

                                            if self.sent is not None:
                                                return True

                                            if self.sent_at is not None:
                                                return True

                                            if self.timed_out is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample']['meta_info']

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:unaggregated'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.sample is not None:
                                            for child_ref in self.sample:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aggregated is not None and self.aggregated._has_data():
                                        return True

                                    if self.bucket_type is not None:
                                        return True

                                    if self.unaggregated is not None and self.unaggregated._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.average is not None:
                                    return True

                                if self.contents is not None and self.contents._has_data():
                                    return True

                                if self.corrupt is not None:
                                    return True

                                if self.data_lost_count is not None:
                                    return True

                                if self.data_sent_count is not None:
                                    return True

                                if self.duplicates is not None:
                                    return True

                                if self.duration is not None:
                                    return True

                                if self.lost is not None:
                                    return True

                                if self.maximum is not None:
                                    return True

                                if self.minimum is not None:
                                    return True

                                if self.out_of_order is not None:
                                    return True

                                if self.overall_flr is not None:
                                    return True

                                if self.premature_reason is not None:
                                    return True

                                if self.premature_reason_string is not None:
                                    return True

                                if self.result_count is not None:
                                    return True

                                if self.sent is not None:
                                    return True

                                if self.standard_deviation is not None:
                                    return True

                                if self.start_at is not None:
                                    return True

                                if self.suspect_cleared_mid_bucket is not None:
                                    return True

                                if self.suspect_clock_drift is not None:
                                    return True

                                if self.suspect_flr_low_packet_count is not None:
                                    return True

                                if self.suspect_management_latency is not None:
                                    return True

                                if self.suspect_memory_allocation_failed is not None:
                                    return True

                                if self.suspect_misordering is not None:
                                    return True

                                if self.suspect_multiple_buckets is not None:
                                    return True

                                if self.suspect_premature_end is not None:
                                    return True

                                if self.suspect_probe_restarted is not None:
                                    return True

                                if self.suspect_schedule_latency is not None:
                                    return True

                                if self.suspect_send_fail is not None:
                                    return True

                                if self.suspect_start_mid_bucket is not None:
                                    return True

                                if self.time_of_maximum is not None:
                                    return True

                                if self.time_of_minimum is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bucket is not None:
                                for child_ref in self.bucket:
                                    if child_ref._has_data():
                                        return True

                            if self.config is not None and self.config._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historical'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.display_long is not None:
                            return True

                        if self.display_short is not None:
                            return True

                        if self.domain_name is not None:
                            return True

                        if self.flr_calculation_interval is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.operation_id is not None:
                            return True

                        if self.operation_metric is not None:
                            for child_ref in self.operation_metric:
                                if child_ref._has_data():
                                    return True

                        if self.operation_schedule is not None and self.operation_schedule._has_data():
                            return True

                        if self.probe_type is not None:
                            return True

                        if self.specific_options is not None and self.specific_options._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-on-demand-historicals'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.statistics_on_demand_historical is not None:
                        for child_ref in self.statistics_on_demand_historical:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals']['meta_info']


            class ConfigErrors(object):
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
                    self.parent = None
                    self.config_error = YList()
                    self.config_error.parent = self
                    self.config_error.name = 'config_error'


                class ConfigError(object):
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
                        self.parent = None
                        self.display_short = None
                        self.domain_name = None
                        self.error_string = YLeafList()
                        self.error_string.parent = self
                        self.error_string.name = 'error_string'
                        self.interface_name = None
                        self.mac_address = None
                        self.mep_id = None
                        self.min_packet_interval_inconsistent = None
                        self.ow_delay_ds_inconsistent = None
                        self.ow_delay_sd_inconsistent = None
                        self.ow_jitter_ds_inconsistent = None
                        self.ow_jitter_sd_inconsistent = None
                        self.ow_loss_ds_inconsistent = None
                        self.ow_loss_sd_inconsistent = None
                        self.packet_pad_inconsistent = None
                        self.packet_rand_pad_inconsistent = None
                        self.packet_type_inconsistent = None
                        self.priority_inconsistent = None
                        self.probe_too_big = None
                        self.profile_doesnt_exist = None
                        self.profile_name = None
                        self.profile_name_xr = None
                        self.rt_delay_inconsistent = None
                        self.rt_jitter_inconsistent = None
                        self.synthetic_loss_not_supported = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:config-errors/Cisco-IOS-XR-ethernet-cfm-oper:config-error'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.display_short is not None:
                            return True

                        if self.domain_name is not None:
                            return True

                        if self.error_string is not None:
                            for child in self.error_string:
                                if child is not None:
                                    return True

                        if self.interface_name is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.min_packet_interval_inconsistent is not None:
                            return True

                        if self.ow_delay_ds_inconsistent is not None:
                            return True

                        if self.ow_delay_sd_inconsistent is not None:
                            return True

                        if self.ow_jitter_ds_inconsistent is not None:
                            return True

                        if self.ow_jitter_sd_inconsistent is not None:
                            return True

                        if self.ow_loss_ds_inconsistent is not None:
                            return True

                        if self.ow_loss_sd_inconsistent is not None:
                            return True

                        if self.packet_pad_inconsistent is not None:
                            return True

                        if self.packet_rand_pad_inconsistent is not None:
                            return True

                        if self.packet_type_inconsistent is not None:
                            return True

                        if self.priority_inconsistent is not None:
                            return True

                        if self.probe_too_big is not None:
                            return True

                        if self.profile_doesnt_exist is not None:
                            return True

                        if self.profile_name is not None:
                            return True

                        if self.profile_name_xr is not None:
                            return True

                        if self.rt_delay_inconsistent is not None:
                            return True

                        if self.rt_jitter_inconsistent is not None:
                            return True

                        if self.synthetic_loss_not_supported is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.ConfigErrors.ConfigError']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:config-errors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.config_error is not None:
                        for child_ref in self.config_error:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.ConfigErrors']['meta_info']


            class OnDemandOperations(object):
                """
                Table of SLA on\-demand operations
                
                .. attribute:: on_demand_operation
                
                	SLA on\-demand operation to get operation data for
                	**type**\: list of    :py:class:`OnDemandOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.on_demand_operation = YList()
                    self.on_demand_operation.parent = self
                    self.on_demand_operation.name = 'on_demand_operation'


                class OnDemandOperation(object):
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
                        self.parent = None
                        self.display_long = None
                        self.display_short = None
                        self.domain_name = None
                        self.interface_name = None
                        self.last_run = None
                        self.mac_address = None
                        self.mep_id = None
                        self.operation_id = None
                        self.profile_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions()
                        self.profile_options.parent = self
                        self.specific_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions()
                        self.specific_options.parent = self


                    class ProfileOptions(object):
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
                            self.parent = None
                            self.bursts_per_probe = None
                            self.flr_calculation_interval = None
                            self.inter_burst_interval = None
                            self.inter_packet_interval = None
                            self.operation_metric = YList()
                            self.operation_metric.parent = self
                            self.operation_metric.name = 'operation_metric'
                            self.operation_schedule = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule()
                            self.operation_schedule.parent = self
                            self.packet_padding = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding()
                            self.packet_padding.parent = self
                            self.packets_per_burst = None
                            self.priority = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority()
                            self.priority.parent = self
                            self.probe_type = None


                        class PacketPadding(object):
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
                            	**type**\:   :py:class:`SlaOperTestPatternSchemeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperTestPatternSchemeEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.packet_pad_size = None
                                self.test_pattern_pad_hex_string = None
                                self.test_pattern_pad_scheme = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:packet-padding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.packet_pad_size is not None:
                                    return True

                                if self.test_pattern_pad_hex_string is not None:
                                    return True

                                if self.test_pattern_pad_scheme is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding']['meta_info']


                        class Priority(object):
                            """
                            Priority at which to send the packet, if
                            configured
                            
                            .. attribute:: cos
                            
                            	3\-bit COS priority value applied to packets
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: priority_type
                            
                            	PriorityType
                            	**type**\:   :py:class:`SlaOperPacketPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperPacketPriorityEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.cos = None
                                self.priority_type = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:priority'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.cos is not None:
                                    return True

                                if self.priority_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority']['meta_info']


                        class OperationSchedule(object):
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
                                self.parent = None
                                self.schedule_duration = None
                                self.schedule_interval = None
                                self.start_time = None
                                self.start_time_configured = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:operation-schedule'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.schedule_duration is not None:
                                    return True

                                if self.schedule_interval is not None:
                                    return True

                                if self.start_time is not None:
                                    return True

                                if self.start_time_configured is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule']['meta_info']


                        class OperationMetric(object):
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
                                self.parent = None
                                self.current_buckets_archive = None
                                self.metric_config = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig()
                                self.metric_config.parent = self


                            class MetricConfig(object):
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
                                	**type**\:   :py:class:`SlaBucketSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSizeEnum>`
                                
                                .. attribute:: buckets_archive
                                
                                	Maximum number of buckets to store in memory
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric_type
                                
                                	Type of metric to which this configuration applies
                                	**type**\:   :py:class:`SlaRecordableMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetricEnum>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bins_count = None
                                    self.bins_width = None
                                    self.bucket_size = None
                                    self.bucket_size_unit = None
                                    self.buckets_archive = None
                                    self.metric_type = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:metric-config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bins_count is not None:
                                        return True

                                    if self.bins_width is not None:
                                        return True

                                    if self.bucket_size is not None:
                                        return True

                                    if self.bucket_size_unit is not None:
                                        return True

                                    if self.buckets_archive is not None:
                                        return True

                                    if self.metric_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.current_buckets_archive is not None:
                                    return True

                                if self.metric_config is not None and self.metric_config._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:profile-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bursts_per_probe is not None:
                                return True

                            if self.flr_calculation_interval is not None:
                                return True

                            if self.inter_burst_interval is not None:
                                return True

                            if self.inter_packet_interval is not None:
                                return True

                            if self.operation_metric is not None:
                                for child_ref in self.operation_metric:
                                    if child_ref._has_data():
                                        return True

                            if self.operation_schedule is not None and self.operation_schedule._has_data():
                                return True

                            if self.packet_padding is not None and self.packet_padding._has_data():
                                return True

                            if self.packets_per_burst is not None:
                                return True

                            if self.priority is not None and self.priority._has_data():
                                return True

                            if self.probe_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions']['meta_info']


                    class SpecificOptions(object):
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
                        	**type**\:   :py:class:`SlaOperOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperationEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.configured_operation_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self.ondemand_operation_options = Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self.oper_type = None


                        class ConfiguredOperationOptions(object):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:configured-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions']['meta_info']


                        class OndemandOperationOptions(object):
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
                                self.parent = None
                                self.ondemand_operation_id = None
                                self.probe_count = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:ondemand-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ondemand_operation_id is not None:
                                    return True

                                if self.probe_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation/Cisco-IOS-XR-ethernet-cfm-oper:specific-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.configured_operation_options is not None and self.configured_operation_options._has_data():
                                return True

                            if self.ondemand_operation_options is not None and self.ondemand_operation_options._has_data():
                                return True

                            if self.oper_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.display_long is not None:
                            return True

                        if self.display_short is not None:
                            return True

                        if self.domain_name is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.last_run is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.operation_id is not None:
                            return True

                        if self.profile_options is not None and self.profile_options._has_data():
                            return True

                        if self.specific_options is not None and self.specific_options._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:on-demand-operations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.on_demand_operation is not None:
                        for child_ref in self.on_demand_operation:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.OnDemandOperations']['meta_info']


            class StatisticsCurrents(object):
                """
                Table of current statistics for SLA operations
                
                .. attribute:: statistics_current
                
                	Current statistics data for an SLA configured operation
                	**type**\: list of    :py:class:`StatisticsCurrent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.statistics_current = YList()
                    self.statistics_current.parent = self
                    self.statistics_current.name = 'statistics_current'


                class StatisticsCurrent(object):
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
                        self.parent = None
                        self.display_long = None
                        self.display_short = None
                        self.domain_name = None
                        self.flr_calculation_interval = None
                        self.interface_name = None
                        self.mac_address = None
                        self.mep_id = None
                        self.operation_metric = YList()
                        self.operation_metric.parent = self
                        self.operation_metric.name = 'operation_metric'
                        self.operation_schedule = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule()
                        self.operation_schedule.parent = self
                        self.probe_type = None
                        self.profile_name = None
                        self.specific_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions()
                        self.specific_options.parent = self


                    class SpecificOptions(object):
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
                        	**type**\:   :py:class:`SlaOperOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperOperationEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.configured_operation_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions()
                            self.configured_operation_options.parent = self
                            self.ondemand_operation_options = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions()
                            self.ondemand_operation_options.parent = self
                            self.oper_type = None


                        class ConfiguredOperationOptions(object):
                            """
                            Parameters for a configured operation
                            
                            .. attribute:: profile_name
                            
                            	Name of the profile used by the operation
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:configured-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions']['meta_info']


                        class OndemandOperationOptions(object):
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
                                self.parent = None
                                self.ondemand_operation_id = None
                                self.probe_count = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:specific-options/Cisco-IOS-XR-ethernet-cfm-oper:ondemand-operation-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ondemand_operation_id is not None:
                                    return True

                                if self.probe_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:specific-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.configured_operation_options is not None and self.configured_operation_options._has_data():
                                return True

                            if self.ondemand_operation_options is not None and self.ondemand_operation_options._has_data():
                                return True

                            if self.oper_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions']['meta_info']


                    class OperationSchedule(object):
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
                            self.parent = None
                            self.schedule_duration = None
                            self.schedule_interval = None
                            self.start_time = None
                            self.start_time_configured = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-schedule'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.schedule_duration is not None:
                                return True

                            if self.schedule_interval is not None:
                                return True

                            if self.start_time is not None:
                                return True

                            if self.start_time_configured is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule']['meta_info']


                    class OperationMetric(object):
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
                            self.parent = None
                            self.bucket = YList()
                            self.bucket.parent = self
                            self.bucket.name = 'bucket'
                            self.config = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config()
                            self.config.parent = self


                        class Config(object):
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
                            	**type**\:   :py:class:`SlaBucketSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaBucketSizeEnum>`
                            
                            .. attribute:: buckets_archive
                            
                            	Maximum number of buckets to store in memory
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric_type
                            
                            	Type of metric to which this configuration applies
                            	**type**\:   :py:class:`SlaRecordableMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaRecordableMetricEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bins_count = None
                                self.bins_width = None
                                self.bucket_size = None
                                self.bucket_size_unit = None
                                self.buckets_archive = None
                                self.metric_type = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bins_count is not None:
                                    return True

                                if self.bins_width is not None:
                                    return True

                                if self.bucket_size is not None:
                                    return True

                                if self.bucket_size_unit is not None:
                                    return True

                                if self.buckets_archive is not None:
                                    return True

                                if self.metric_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config']['meta_info']


                        class Bucket(object):
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
                                self.parent = None
                                self.average = None
                                self.contents = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents()
                                self.contents.parent = self
                                self.corrupt = None
                                self.data_lost_count = None
                                self.data_sent_count = None
                                self.duplicates = None
                                self.duration = None
                                self.lost = None
                                self.maximum = None
                                self.minimum = None
                                self.out_of_order = None
                                self.overall_flr = None
                                self.premature_reason = None
                                self.premature_reason_string = None
                                self.result_count = None
                                self.sent = None
                                self.standard_deviation = None
                                self.start_at = None
                                self.suspect_cleared_mid_bucket = None
                                self.suspect_clock_drift = None
                                self.suspect_flr_low_packet_count = None
                                self.suspect_management_latency = None
                                self.suspect_memory_allocation_failed = None
                                self.suspect_misordering = None
                                self.suspect_multiple_buckets = None
                                self.suspect_premature_end = None
                                self.suspect_probe_restarted = None
                                self.suspect_schedule_latency = None
                                self.suspect_send_fail = None
                                self.suspect_start_mid_bucket = None
                                self.time_of_maximum = None
                                self.time_of_minimum = None


                            class Contents(object):
                                """
                                The contents of the bucket; bins or samples
                                
                                .. attribute:: aggregated
                                
                                	Result bins in an SLA metric bucket
                                	**type**\:   :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated>`
                                
                                .. attribute:: bucket_type
                                
                                	BucketType
                                	**type**\:   :py:class:`SlaOperBucketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.SlaOperBucketEnum>`
                                
                                .. attribute:: unaggregated
                                
                                	Result samples in an SLA metric bucket
                                	**type**\:   :py:class:`Unaggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aggregated = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated()
                                    self.aggregated.parent = self
                                    self.bucket_type = None
                                    self.unaggregated = Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated()
                                    self.unaggregated.parent = self


                                class Aggregated(object):
                                    """
                                    Result bins in an SLA metric bucket
                                    
                                    .. attribute:: bins
                                    
                                    	The bins of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Bins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bins = YList()
                                        self.bins.parent = self
                                        self.bins.name = 'bins'


                                    class Bins(object):
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
                                            self.parent = None
                                            self.count = None
                                            self.lower_bound = None
                                            self.lower_bound_tenths = None
                                            self.sum = None
                                            self.upper_bound = None
                                            self.upper_bound_tenths = None

                                        @property
                                        def _common_path(self):

                                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:aggregated/Cisco-IOS-XR-ethernet-cfm-oper:bins'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.count is not None:
                                                return True

                                            if self.lower_bound is not None:
                                                return True

                                            if self.lower_bound_tenths is not None:
                                                return True

                                            if self.sum is not None:
                                                return True

                                            if self.upper_bound is not None:
                                                return True

                                            if self.upper_bound_tenths is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins']['meta_info']

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:aggregated'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.bins is not None:
                                            for child_ref in self.bins:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated']['meta_info']


                                class Unaggregated(object):
                                    """
                                    Result samples in an SLA metric bucket
                                    
                                    .. attribute:: sample
                                    
                                    	The samples of an SLA metric bucket
                                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper.Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.sample = YList()
                                        self.sample.parent = self
                                        self.sample.name = 'sample'


                                    class Sample(object):
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
                                            self.parent = None
                                            self.corrupt = None
                                            self.frames_lost = None
                                            self.frames_sent = None
                                            self.no_data_packets = None
                                            self.out_of_order = None
                                            self.result = None
                                            self.sent = None
                                            self.sent_at = None
                                            self.timed_out = None

                                        @property
                                        def _common_path(self):

                                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:unaggregated/Cisco-IOS-XR-ethernet-cfm-oper:sample'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.corrupt is not None:
                                                return True

                                            if self.frames_lost is not None:
                                                return True

                                            if self.frames_sent is not None:
                                                return True

                                            if self.no_data_packets is not None:
                                                return True

                                            if self.out_of_order is not None:
                                                return True

                                            if self.result is not None:
                                                return True

                                            if self.sent is not None:
                                                return True

                                            if self.sent_at is not None:
                                                return True

                                            if self.timed_out is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample']['meta_info']

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents/Cisco-IOS-XR-ethernet-cfm-oper:unaggregated'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.sample is not None:
                                            for child_ref in self.sample:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket/Cisco-IOS-XR-ethernet-cfm-oper:contents'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aggregated is not None and self.aggregated._has_data():
                                        return True

                                    if self.bucket_type is not None:
                                        return True

                                    if self.unaggregated is not None and self.unaggregated._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric/Cisco-IOS-XR-ethernet-cfm-oper:bucket'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.average is not None:
                                    return True

                                if self.contents is not None and self.contents._has_data():
                                    return True

                                if self.corrupt is not None:
                                    return True

                                if self.data_lost_count is not None:
                                    return True

                                if self.data_sent_count is not None:
                                    return True

                                if self.duplicates is not None:
                                    return True

                                if self.duration is not None:
                                    return True

                                if self.lost is not None:
                                    return True

                                if self.maximum is not None:
                                    return True

                                if self.minimum is not None:
                                    return True

                                if self.out_of_order is not None:
                                    return True

                                if self.overall_flr is not None:
                                    return True

                                if self.premature_reason is not None:
                                    return True

                                if self.premature_reason_string is not None:
                                    return True

                                if self.result_count is not None:
                                    return True

                                if self.sent is not None:
                                    return True

                                if self.standard_deviation is not None:
                                    return True

                                if self.start_at is not None:
                                    return True

                                if self.suspect_cleared_mid_bucket is not None:
                                    return True

                                if self.suspect_clock_drift is not None:
                                    return True

                                if self.suspect_flr_low_packet_count is not None:
                                    return True

                                if self.suspect_management_latency is not None:
                                    return True

                                if self.suspect_memory_allocation_failed is not None:
                                    return True

                                if self.suspect_misordering is not None:
                                    return True

                                if self.suspect_multiple_buckets is not None:
                                    return True

                                if self.suspect_premature_end is not None:
                                    return True

                                if self.suspect_probe_restarted is not None:
                                    return True

                                if self.suspect_schedule_latency is not None:
                                    return True

                                if self.suspect_send_fail is not None:
                                    return True

                                if self.suspect_start_mid_bucket is not None:
                                    return True

                                if self.time_of_maximum is not None:
                                    return True

                                if self.time_of_minimum is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current/Cisco-IOS-XR-ethernet-cfm-oper:operation-metric'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bucket is not None:
                                for child_ref in self.bucket:
                                    if child_ref._has_data():
                                        return True

                            if self.config is not None and self.config._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents/Cisco-IOS-XR-ethernet-cfm-oper:statistics-current'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.display_long is not None:
                            return True

                        if self.display_short is not None:
                            return True

                        if self.domain_name is not None:
                            return True

                        if self.flr_calculation_interval is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.operation_metric is not None:
                            for child_ref in self.operation_metric:
                                if child_ref._has_data():
                                    return True

                        if self.operation_schedule is not None and self.operation_schedule._has_data():
                            return True

                        if self.probe_type is not None:
                            return True

                        if self.profile_name is not None:
                            return True

                        if self.specific_options is not None and self.specific_options._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet/Cisco-IOS-XR-ethernet-cfm-oper:statistics-currents'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.statistics_current is not None:
                        for child_ref in self.statistics_current:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.StatisticsCurrents']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols/Cisco-IOS-XR-ethernet-cfm-oper:ethernet'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.config_errors is not None and self.config_errors._has_data():
                    return True

                if self.on_demand_operations is not None and self.on_demand_operations._has_data():
                    return True

                if self.operations is not None and self.operations._has_data():
                    return True

                if self.statistics_currents is not None and self.statistics_currents._has_data():
                    return True

                if self.statistics_historicals is not None and self.statistics_historicals._has_data():
                    return True

                if self.statistics_on_demand_currents is not None and self.statistics_on_demand_currents._has_data():
                    return True

                if self.statistics_on_demand_historicals is not None and self.statistics_on_demand_historicals._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
                return meta._meta_table['Sla.Protocols.Ethernet']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-sla-oper:sla/Cisco-IOS-XR-infra-sla-oper:protocols'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ethernet is not None and self.ethernet._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
            return meta._meta_table['Sla.Protocols']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-sla-oper:sla'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.protocols is not None and self.protocols._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
        return meta._meta_table['Sla']['meta_info']


class SlaNodes(object):
    """
    sla nodes
    
    

    """

    _prefix = 'infra-sla-oper'
    _revision = '2015-11-09'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-sla-oper:sla-nodes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_oper as meta
        return meta._meta_table['SlaNodes']['meta_info']


