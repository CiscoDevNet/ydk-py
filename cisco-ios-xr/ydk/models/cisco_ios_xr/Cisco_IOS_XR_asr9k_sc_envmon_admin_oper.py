""" Cisco_IOS_XR_asr9k_sc_envmon_admin_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-envmon package
admin\-plane operational data.

This module contains definitions
for the following management objects\:
  environmental\-monitoring\: Admin Environmental Monitoring
    Operational data space

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class EnvironmentalMonitoring(object):
    """
    Admin Environmental Monitoring Operational data
    space
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks>`
    
    

    """

    _prefix = 'asr9k-sc-envmon-admin-oper'
    _revision = '2017-01-19'

    def __init__(self):
        self.racks = EnvironmentalMonitoring.Racks()
        self.racks.parent = self


    class Racks(object):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Number
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack>`
        
        

        """

        _prefix = 'asr9k-sc-envmon-admin-oper'
        _revision = '2017-01-19'

        def __init__(self):
            self.parent = None
            self.rack = YList()
            self.rack.parent = self
            self.rack.name = 'rack'


        class Rack(object):
            """
            Number
            
            .. attribute:: rack  <key>
            
            	Rack number
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'asr9k-sc-envmon-admin-oper'
            _revision = '2017-01-19'

            def __init__(self):
                self.parent = None
                self.rack = None
                self.slots = EnvironmentalMonitoring.Racks.Rack.Slots()
                self.slots.parent = self


            class Slots(object):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Name
                	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'asr9k-sc-envmon-admin-oper'
                _revision = '2017-01-19'

                def __init__(self):
                    self.parent = None
                    self.slot = YList()
                    self.slot.parent = self
                    self.slot.name = 'slot'


                class Slot(object):
                    """
                    Name
                    
                    .. attribute:: slot  <key>
                    
                    	Slot name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: modules
                    
                    	Table of modules
                    	**type**\:   :py:class:`Modules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-envmon-admin-oper'
                    _revision = '2017-01-19'

                    def __init__(self):
                        self.parent = None
                        self.slot = None
                        self.modules = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules()
                        self.modules.parent = self


                    class Modules(object):
                        """
                        Table of modules
                        
                        .. attribute:: module
                        
                        	Name
                        	**type**\: list of    :py:class:`Module <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-envmon-admin-oper'
                        _revision = '2017-01-19'

                        def __init__(self):
                            self.parent = None
                            self.module = YList()
                            self.module.parent = self
                            self.module.name = 'module'


                        class Module(object):
                            """
                            Name
                            
                            .. attribute:: module  <key>
                            
                            	Module name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: power
                            
                            	Module Power Draw
                            	**type**\:   :py:class:`Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power>`
                            
                            .. attribute:: sensor_types
                            
                            	Table of sensor types
                            	**type**\:   :py:class:`SensorTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-envmon-admin-oper'
                            _revision = '2017-01-19'

                            def __init__(self):
                                self.parent = None
                                self.module = None
                                self.power = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power()
                                self.power.parent = self
                                self.sensor_types = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes()
                                self.sensor_types.parent = self


                            class SensorTypes(object):
                                """
                                Table of sensor types
                                
                                .. attribute:: sensor_type
                                
                                	Type of sensor
                                	**type**\: list of    :py:class:`SensorType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-envmon-admin-oper'
                                _revision = '2017-01-19'

                                def __init__(self):
                                    self.parent = None
                                    self.sensor_type = YList()
                                    self.sensor_type.parent = self
                                    self.sensor_type.name = 'sensor_type'


                                class SensorType(object):
                                    """
                                    Type of sensor
                                    
                                    .. attribute:: type  <key>
                                    
                                    	Sensor type
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: sensor_names
                                    
                                    	Table of sensors
                                    	**type**\:   :py:class:`SensorNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-envmon-admin-oper'
                                    _revision = '2017-01-19'

                                    def __init__(self):
                                        self.parent = None
                                        self.type = None
                                        self.sensor_names = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames()
                                        self.sensor_names.parent = self


                                    class SensorNames(object):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor_name
                                        
                                        	Name of sensor
                                        	**type**\: list of    :py:class:`SensorName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-envmon-admin-oper'
                                        _revision = '2017-01-19'

                                        def __init__(self):
                                            self.parent = None
                                            self.sensor_name = YList()
                                            self.sensor_name.parent = self
                                            self.sensor_name.name = 'sensor_name'


                                        class SensorName(object):
                                            """
                                            Name of sensor
                                            
                                            .. attribute:: name  <key>
                                            
                                            	Sensor name
                                            	**type**\:  str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: thresholds
                                            
                                            	The threshold information
                                            	**type**\:   :py:class:`Thresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds>`
                                            
                                            .. attribute:: value_brief
                                            
                                            	The sensor value
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: value_detailed
                                            
                                            	Detailed sensor information including the sensor value
                                            	**type**\:   :py:class:`ValueDetailed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-envmon-admin-oper'
                                            _revision = '2017-01-19'

                                            def __init__(self):
                                                self.parent = None
                                                self.name = None
                                                self.thresholds = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds()
                                                self.thresholds.parent = self
                                                self.value_brief = None
                                                self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed()
                                                self.value_detailed.parent = self


                                            class Thresholds(object):
                                                """
                                                The threshold information
                                                
                                                .. attribute:: threshold
                                                
                                                	Types of thresholds
                                                	**type**\: list of    :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold>`
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-envmon-admin-oper'
                                                _revision = '2017-01-19'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.threshold = YList()
                                                    self.threshold.parent = self
                                                    self.threshold.name = 'threshold'


                                                class Threshold(object):
                                                    """
                                                    Types of thresholds
                                                    
                                                    .. attribute:: type  <key>
                                                    
                                                    	Threshold type
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    .. attribute:: trap
                                                    
                                                    	Threshold trap enable flag true\-ENABLE, false\-DISABLE
                                                    	**type**\:  bool
                                                    
                                                    .. attribute:: value_brief
                                                    
                                                    	Threshold value for the sensor
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: value_detailed
                                                    
                                                    	Detailed sensor threshold information
                                                    	**type**\:   :py:class:`ValueDetailed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-envmon-admin-oper'
                                                    _revision = '2017-01-19'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.type = None
                                                        self.trap = None
                                                        self.value_brief = None
                                                        self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed()
                                                        self.value_detailed.parent = self


                                                    class ValueDetailed(object):
                                                        """
                                                        Detailed sensor threshold
                                                        information
                                                        
                                                        .. attribute:: threshold_evaluation
                                                        
                                                        	Indicates the result of the most recent evaluation of the thresholD
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: threshold_notification_enabled
                                                        
                                                        	Indicates whether or not a notification should result, in case of threshold violation
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: threshold_relation
                                                        
                                                        	Indicates relation between sensor value and threshold
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: threshold_severity
                                                        
                                                        	Indicates minor, major, critical severities
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: threshold_value
                                                        
                                                        	Value of the configured threshold
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-envmon-admin-oper'
                                                        _revision = '2017-01-19'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.threshold_evaluation = None
                                                            self.threshold_notification_enabled = None
                                                            self.threshold_relation = None
                                                            self.threshold_severity = None
                                                            self.threshold_value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:value-detailed'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.threshold_evaluation is not None:
                                                                return True

                                                            if self.threshold_notification_enabled is not None:
                                                                return True

                                                            if self.threshold_relation is not None:
                                                                return True

                                                            if self.threshold_severity is not None:
                                                                return True

                                                            if self.threshold_value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                                            return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.type is None:
                                                            raise YPYModelError('Key property type is None')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:threshold[Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:type = ' + str(self.type) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.type is not None:
                                                            return True

                                                        if self.trap is not None:
                                                            return True

                                                        if self.value_brief is not None:
                                                            return True

                                                        if self.value_detailed is not None and self.value_detailed._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                                        return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:thresholds'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.threshold is not None:
                                                        for child_ref in self.threshold:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds']['meta_info']


                                            class ValueDetailed(object):
                                                """
                                                Detailed sensor information including
                                                the sensor value
                                                
                                                .. attribute:: age_time_stamp
                                                
                                                	Age of the sensor value; set to the current time if directly access the value from sensor
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: alarm_type
                                                
                                                	Indicates threshold violation
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: data_type
                                                
                                                	Sensor data type enums
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: device_description
                                                
                                                	Device Name
                                                	**type**\:  str
                                                
                                                	**length:** 0..50
                                                
                                                .. attribute:: device_id
                                                
                                                	Identifier for this device
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: field_validity_bitmap
                                                
                                                	Sensor valid bitmap
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: precision
                                                
                                                	Sensor precision range
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: scale
                                                
                                                	Sensor scale enums
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: status
                                                
                                                	Sensor operation state enums
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: units
                                                
                                                	Units of variable being read
                                                	**type**\:  str
                                                
                                                	**length:** 0..50
                                                
                                                .. attribute:: update_rate
                                                
                                                	Sensor value update rate;set to 0 if sensor value is updated and evaluated immediately
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: value
                                                
                                                	Current reading of sensor
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-envmon-admin-oper'
                                                _revision = '2017-01-19'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.age_time_stamp = None
                                                    self.alarm_type = None
                                                    self.data_type = None
                                                    self.device_description = None
                                                    self.device_id = None
                                                    self.field_validity_bitmap = None
                                                    self.precision = None
                                                    self.scale = None
                                                    self.status = None
                                                    self.units = None
                                                    self.update_rate = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:value-detailed'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.age_time_stamp is not None:
                                                        return True

                                                    if self.alarm_type is not None:
                                                        return True

                                                    if self.data_type is not None:
                                                        return True

                                                    if self.device_description is not None:
                                                        return True

                                                    if self.device_id is not None:
                                                        return True

                                                    if self.field_validity_bitmap is not None:
                                                        return True

                                                    if self.precision is not None:
                                                        return True

                                                    if self.scale is not None:
                                                        return True

                                                    if self.status is not None:
                                                        return True

                                                    if self.units is not None:
                                                        return True

                                                    if self.update_rate is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.name is None:
                                                    raise YPYModelError('Key property name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:sensor-name[Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:name = ' + str(self.name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.name is not None:
                                                    return True

                                                if self.thresholds is not None and self.thresholds._has_data():
                                                    return True

                                                if self.value_brief is not None:
                                                    return True

                                                if self.value_detailed is not None and self.value_detailed._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                                return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:sensor-names'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.sensor_name is not None:
                                                for child_ref in self.sensor_name:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                            return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.type is None:
                                            raise YPYModelError('Key property type is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:sensor-type[Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:type = ' + str(self.type) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.type is not None:
                                            return True

                                        if self.sensor_names is not None and self.sensor_names._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                        return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:sensor-types'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.sensor_type is not None:
                                        for child_ref in self.sensor_type:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes']['meta_info']


                            class Power(object):
                                """
                                Module Power Draw
                                
                                .. attribute:: power_bag
                                
                                	Detailed power bag information
                                	**type**\:   :py:class:`PowerBag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-envmon-admin-oper'
                                _revision = '2017-01-19'

                                def __init__(self):
                                    self.parent = None
                                    self.power_bag = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag()
                                    self.power_bag.parent = self


                                class PowerBag(object):
                                    """
                                    Detailed power bag information
                                    
                                    .. attribute:: power_accuracy
                                    
                                    	Accuracy of the Power Value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_admin_state
                                    
                                    	Admin Status of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_current_type
                                    
                                    	Current Type of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_max_value
                                    
                                    	Max Power Value of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: power_measure_caliber
                                    
                                    	Measure Caliber
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_oper_state
                                    
                                    	Oper Status of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_origin
                                    
                                    	The Power Origin of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_state_enter_reason
                                    
                                    	Enter Reason for the State
                                    	**type**\:  str
                                    
                                    	**length:** 0..50
                                    
                                    .. attribute:: power_unit_multiplier
                                    
                                    	Unit Multiplier of Power
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_value
                                    
                                    	Current Power Value of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-envmon-admin-oper'
                                    _revision = '2017-01-19'

                                    def __init__(self):
                                        self.parent = None
                                        self.power_accuracy = None
                                        self.power_admin_state = None
                                        self.power_current_type = None
                                        self.power_max_value = None
                                        self.power_measure_caliber = None
                                        self.power_oper_state = None
                                        self.power_origin = None
                                        self.power_state_enter_reason = None
                                        self.power_unit_multiplier = None
                                        self.power_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:power-bag'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.power_accuracy is not None:
                                            return True

                                        if self.power_admin_state is not None:
                                            return True

                                        if self.power_current_type is not None:
                                            return True

                                        if self.power_max_value is not None:
                                            return True

                                        if self.power_measure_caliber is not None:
                                            return True

                                        if self.power_oper_state is not None:
                                            return True

                                        if self.power_origin is not None:
                                            return True

                                        if self.power_state_enter_reason is not None:
                                            return True

                                        if self.power_unit_multiplier is not None:
                                            return True

                                        if self.power_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                        return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:power'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.power_bag is not None and self.power_bag._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.module is None:
                                    raise YPYModelError('Key property module is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:module[Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:module = ' + str(self.module) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.module is not None:
                                    return True

                                if self.power is not None and self.power._has_data():
                                    return True

                                if self.sensor_types is not None and self.sensor_types._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                                return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:modules'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.module is not None:
                                for child_ref in self.module:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                            return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.slot is None:
                            raise YPYModelError('Key property slot is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:slot[Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:slot = ' + str(self.slot) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.slot is not None:
                            return True

                        if self.modules is not None and self.modules._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                        return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:slots'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.slot is not None:
                        for child_ref in self.slot:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots']['meta_info']

            @property
            def _common_path(self):
                if self.rack is None:
                    raise YPYModelError('Key property rack is None')

                return '/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:environmental-monitoring/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:racks/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:rack[Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:rack = ' + str(self.rack) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rack is not None:
                    return True

                if self.slots is not None and self.slots._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
                return meta._meta_table['EnvironmentalMonitoring.Racks.Rack']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:environmental-monitoring/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:racks'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rack is not None:
                for child_ref in self.rack:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
            return meta._meta_table['EnvironmentalMonitoring.Racks']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-sc-envmon-admin-oper:environmental-monitoring'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.racks is not None and self.racks._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_admin_oper as meta
        return meta._meta_table['EnvironmentalMonitoring']['meta_info']


