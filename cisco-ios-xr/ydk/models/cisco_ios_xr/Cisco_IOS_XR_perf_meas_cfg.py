""" Cisco_IOS_XR_perf_meas_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR perf\-meas package configuration.

This module contains definitions
for the following management objects\:
  performance\-measurement\: The root of performance\-measurement
    configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class PerformanceMeasurement(Entity):
    """
    The root of performance\-measurement configuration
    
    .. attribute:: delay_profile_interface
    
    	PM Delay Profile
    	**type**\:  :py:class:`DelayProfileInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.DelayProfileInterface>`
    
    .. attribute:: interfaces
    
    	Configure performance\-measurement interfaces
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.Interfaces>`
    
    .. attribute:: enable_performance_measurement
    
    	Enable the performance measurement feature
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'perf-meas-cfg'
    _revision = '2017-10-17'

    def __init__(self):
        super(PerformanceMeasurement, self).__init__()
        self._top_entity = None

        self.yang_name = "performance-measurement"
        self.yang_parent_name = "Cisco-IOS-XR-perf-meas-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("delay-profile-interface", ("delay_profile_interface", PerformanceMeasurement.DelayProfileInterface)), ("interfaces", ("interfaces", PerformanceMeasurement.Interfaces))])
        self._leafs = OrderedDict([
            ('enable_performance_measurement', (YLeaf(YType.empty, 'enable-performance-measurement'), ['Empty'])),
        ])
        self.enable_performance_measurement = None

        self.delay_profile_interface = PerformanceMeasurement.DelayProfileInterface()
        self.delay_profile_interface.parent = self
        self._children_name_map["delay_profile_interface"] = "delay-profile-interface"

        self.interfaces = PerformanceMeasurement.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PerformanceMeasurement, ['enable_performance_measurement'], name, value)


    class DelayProfileInterface(Entity):
        """
        PM Delay Profile
        
        .. attribute:: advertisement
        
        	Advertisement Profile
        	**type**\:  :py:class:`Advertisement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.DelayProfileInterface.Advertisement>`
        
        .. attribute:: probe
        
        	PM Delay Profile Probe
        	**type**\:  :py:class:`Probe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.DelayProfileInterface.Probe>`
        
        

        """

        _prefix = 'perf-meas-cfg'
        _revision = '2017-10-17'

        def __init__(self):
            super(PerformanceMeasurement.DelayProfileInterface, self).__init__()

            self.yang_name = "delay-profile-interface"
            self.yang_parent_name = "performance-measurement"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("advertisement", ("advertisement", PerformanceMeasurement.DelayProfileInterface.Advertisement)), ("probe", ("probe", PerformanceMeasurement.DelayProfileInterface.Probe))])
            self._leafs = OrderedDict()

            self.advertisement = PerformanceMeasurement.DelayProfileInterface.Advertisement()
            self.advertisement.parent = self
            self._children_name_map["advertisement"] = "advertisement"

            self.probe = PerformanceMeasurement.DelayProfileInterface.Probe()
            self.probe.parent = self
            self._children_name_map["probe"] = "probe"
            self._segment_path = lambda: "delay-profile-interface"
            self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerformanceMeasurement.DelayProfileInterface, [], name, value)


        class Advertisement(Entity):
            """
            Advertisement Profile
            
            .. attribute:: accelerated
            
            	Accelerated Advertisement Profile
            	**type**\:  :py:class:`Accelerated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated>`
            
            .. attribute:: periodic
            
            	Periodic Advertisement Profile
            	**type**\:  :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic>`
            
            

            """

            _prefix = 'perf-meas-cfg'
            _revision = '2017-10-17'

            def __init__(self):
                super(PerformanceMeasurement.DelayProfileInterface.Advertisement, self).__init__()

                self.yang_name = "advertisement"
                self.yang_parent_name = "delay-profile-interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("accelerated", ("accelerated", PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated)), ("periodic", ("periodic", PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic))])
                self._leafs = OrderedDict()

                self.accelerated = PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated()
                self.accelerated.parent = self
                self._children_name_map["accelerated"] = "accelerated"

                self.periodic = PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic()
                self.periodic.parent = self
                self._children_name_map["periodic"] = "periodic"
                self._segment_path = lambda: "advertisement"
                self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement/delay-profile-interface/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerformanceMeasurement.DelayProfileInterface.Advertisement, [], name, value)


            class Accelerated(Entity):
                """
                Accelerated Advertisement Profile
                
                .. attribute:: threshold
                
                	Accelerated advertisement threshold percentage
                	**type**\: int
                
                	**range:** 0..100
                
                	**units**\: percentage
                
                	**default value**\: 20
                
                .. attribute:: minimum_change
                
                	Accelerated advertisement minimum value in uSec
                	**type**\: int
                
                	**range:** 0..100000
                
                	**default value**\: 500
                
                .. attribute:: enable
                
                	Enable Accelerated Advertisement
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'perf-meas-cfg'
                _revision = '2017-10-17'

                def __init__(self):
                    super(PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated, self).__init__()

                    self.yang_name = "accelerated"
                    self.yang_parent_name = "advertisement"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ('minimum_change', (YLeaf(YType.uint32, 'minimum-change'), ['int'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.threshold = None
                    self.minimum_change = None
                    self.enable = None
                    self._segment_path = lambda: "accelerated"
                    self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement/delay-profile-interface/advertisement/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated, ['threshold', 'minimum_change', 'enable'], name, value)


            class Periodic(Entity):
                """
                Periodic Advertisement Profile
                
                .. attribute:: interval
                
                	Periodic advertisement interval in seconds
                	**type**\: int
                
                	**range:** 30..3600
                
                	**units**\: second
                
                	**default value**\: 120
                
                .. attribute:: threshold
                
                	Periodic advertisement threshold percentage
                	**type**\: int
                
                	**range:** 0..100
                
                	**units**\: percentage
                
                	**default value**\: 10
                
                .. attribute:: minimum_change
                
                	Periodic advertisement minimum value in uSec
                	**type**\: int
                
                	**range:** 0..100000
                
                	**default value**\: 500
                
                .. attribute:: disable
                
                	Enable Performance Measurement Periodic Advertisement
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'perf-meas-cfg'
                _revision = '2017-10-17'

                def __init__(self):
                    super(PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic, self).__init__()

                    self.yang_name = "periodic"
                    self.yang_parent_name = "advertisement"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ('minimum_change', (YLeaf(YType.uint32, 'minimum-change'), ['int'])),
                        ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                    ])
                    self.interval = None
                    self.threshold = None
                    self.minimum_change = None
                    self.disable = None
                    self._segment_path = lambda: "periodic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement/delay-profile-interface/advertisement/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic, ['interval', 'threshold', 'minimum_change', 'disable'], name, value)


        class Probe(Entity):
            """
            PM Delay Profile Probe
            
            .. attribute:: burst
            
            	PM Delay Profile Probe Burst
            	**type**\:  :py:class:`Burst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.DelayProfileInterface.Probe.Burst>`
            
            .. attribute:: one_way_measurement
            
            	Enable one\-way measurement
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interval
            
            	The value for delay profile probe interval in seconds
            	**type**\: int
            
            	**range:** 30..3600
            
            	**units**\: second
            
            	**default value**\: 30
            
            

            """

            _prefix = 'perf-meas-cfg'
            _revision = '2017-10-17'

            def __init__(self):
                super(PerformanceMeasurement.DelayProfileInterface.Probe, self).__init__()

                self.yang_name = "probe"
                self.yang_parent_name = "delay-profile-interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("burst", ("burst", PerformanceMeasurement.DelayProfileInterface.Probe.Burst))])
                self._leafs = OrderedDict([
                    ('one_way_measurement', (YLeaf(YType.empty, 'one-way-measurement'), ['Empty'])),
                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                ])
                self.one_way_measurement = None
                self.interval = None

                self.burst = PerformanceMeasurement.DelayProfileInterface.Probe.Burst()
                self.burst.parent = self
                self._children_name_map["burst"] = "burst"
                self._segment_path = lambda: "probe"
                self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement/delay-profile-interface/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerformanceMeasurement.DelayProfileInterface.Probe, ['one_way_measurement', 'interval'], name, value)


            class Burst(Entity):
                """
                PM Delay Profile Probe Burst
                
                .. attribute:: count
                
                	The value for delay profile probe burst count
                	**type**\: int
                
                	**range:** 1..30
                
                	**default value**\: 10
                
                .. attribute:: interval
                
                	The value for delay profile probe burst interval
                	**type**\: int
                
                	**range:** 30..15000
                
                	**default value**\: 3000
                
                

                """

                _prefix = 'perf-meas-cfg'
                _revision = '2017-10-17'

                def __init__(self):
                    super(PerformanceMeasurement.DelayProfileInterface.Probe.Burst, self).__init__()

                    self.yang_name = "burst"
                    self.yang_parent_name = "probe"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                    ])
                    self.count = None
                    self.interval = None
                    self._segment_path = lambda: "burst"
                    self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement/delay-profile-interface/probe/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerformanceMeasurement.DelayProfileInterface.Probe.Burst, ['count', 'interval'], name, value)


    class Interfaces(Entity):
        """
        Configure performance\-measurement interfaces
        
        .. attribute:: interface
        
        	Configure a performance\-measurement interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.Interfaces.Interface>`
        
        

        """

        _prefix = 'perf-meas-cfg'
        _revision = '2017-10-17'

        def __init__(self):
            super(PerformanceMeasurement.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "performance-measurement"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", PerformanceMeasurement.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerformanceMeasurement.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Configure a performance\-measurement interface
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: delay_measurement
            
            	Interface delay measurement
            	**type**\:  :py:class:`DelayMeasurement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg.PerformanceMeasurement.Interfaces.Interface.DelayMeasurement>`
            
            .. attribute:: enable_interface
            
            	Enable interface submode
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'perf-meas-cfg'
            _revision = '2017-10-17'

            def __init__(self):
                super(PerformanceMeasurement.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("delay-measurement", ("delay_measurement", PerformanceMeasurement.Interfaces.Interface.DelayMeasurement))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('enable_interface', (YLeaf(YType.empty, 'enable-interface'), ['Empty'])),
                ])
                self.interface_name = None
                self.enable_interface = None

                self.delay_measurement = PerformanceMeasurement.Interfaces.Interface.DelayMeasurement()
                self.delay_measurement.parent = self
                self._children_name_map["delay_measurement"] = "delay-measurement"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-cfg:performance-measurement/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerformanceMeasurement.Interfaces.Interface, ['interface_name', 'enable_interface'], name, value)


            class DelayMeasurement(Entity):
                """
                Interface delay measurement
                
                .. attribute:: enable_delay_measurement
                
                	Enable interface delay measurement
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: advertise_delay
                
                	The value for interface delay measurement advertisement delay in uSec
                	**type**\: int
                
                	**range:** 0..16777215
                
                

                """

                _prefix = 'perf-meas-cfg'
                _revision = '2017-10-17'

                def __init__(self):
                    super(PerformanceMeasurement.Interfaces.Interface.DelayMeasurement, self).__init__()

                    self.yang_name = "delay-measurement"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable_delay_measurement', (YLeaf(YType.empty, 'enable-delay-measurement'), ['Empty'])),
                        ('advertise_delay', (YLeaf(YType.uint32, 'advertise-delay'), ['int'])),
                    ])
                    self.enable_delay_measurement = None
                    self.advertise_delay = None
                    self._segment_path = lambda: "delay-measurement"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerformanceMeasurement.Interfaces.Interface.DelayMeasurement, ['enable_delay_measurement', 'advertise_delay'], name, value)

    def clone_ptr(self):
        self._top_entity = PerformanceMeasurement()
        return self._top_entity

