""" Cisco_IOS_XR_infra_tc_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-tc package configuration.

This module contains definitions
for the following management objects\:
  traffic\-collector\: Global Traffic Collector configuration
    commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CollectIonIntervalEnum(Enum):
    """
    CollectIonIntervalEnum

    Collect ion interval

    .. data:: Y_1_minute = 1

    	Interval1minute

    .. data:: Y_2_minutes = 2

    	Interval2minutes

    .. data:: Y_3_minutes = 3

    	Interval3minutes

    .. data:: Y_4_minutes = 4

    	Interval4minutes

    .. data:: Y_5_minutes = 5

    	Interval5minutes

    .. data:: Y_6_minutes = 6

    	Interval6minutes

    .. data:: Y_10_minutes = 10

    	Interval10minutes

    .. data:: Y_12_minutes = 12

    	Interval12minutes

    .. data:: Y_15_minutes = 15

    	Interval15inutes

    .. data:: Y_20_minutes = 20

    	Interval20minutes

    .. data:: Y_30_minutes = 30

    	Interval30minutes

    .. data:: Y_60_minutes = 60

    	Interval60minutes

    """

    Y_1_minute = 1

    Y_2_minutes = 2

    Y_3_minutes = 3

    Y_4_minutes = 4

    Y_5_minutes = 5

    Y_6_minutes = 6

    Y_10_minutes = 10

    Y_12_minutes = 12

    Y_15_minutes = 15

    Y_20_minutes = 20

    Y_30_minutes = 30

    Y_60_minutes = 60


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
        return meta._meta_table['CollectIonIntervalEnum']


class HistorySizeEnum(Enum):
    """
    HistorySizeEnum

    History size

    .. data:: max = 10

    	Max history

    """

    max = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
        return meta._meta_table['HistorySizeEnum']


class HistoryTimeoutEnum(Enum):
    """
    HistoryTimeoutEnum

    History timeout

    .. data:: max = 720

    	Max timeout

    """

    max = 720


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
        return meta._meta_table['HistoryTimeoutEnum']



class TrafficCollector(object):
    """
    Global Traffic Collector configuration commands
    
    .. attribute:: enable_traffic_collector
    
    	Enable traffic collector
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: external_interfaces
    
    	Configure external interfaces
    	**type**\:   :py:class:`ExternalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.ExternalInterfaces>`
    
    .. attribute:: statistics
    
    	Configure statistics related parameters
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.Statistics>`
    
    

    """

    _prefix = 'infra-tc-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.enable_traffic_collector = None
        self.external_interfaces = TrafficCollector.ExternalInterfaces()
        self.external_interfaces.parent = self
        self.statistics = TrafficCollector.Statistics()
        self.statistics.parent = self


    class ExternalInterfaces(object):
        """
        Configure external interfaces
        
        .. attribute:: external_interface
        
        	Configure an external internface
        	**type**\: list of    :py:class:`ExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.ExternalInterfaces.ExternalInterface>`
        
        

        """

        _prefix = 'infra-tc-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.external_interface = YList()
            self.external_interface.parent = self
            self.external_interface.name = 'external_interface'


        class ExternalInterface(object):
            """
            Configure an external internface
            
            .. attribute:: interface_name  <key>
            
            	Name of interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: enable
            
            	Enable traffic collector on this interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-tc-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.enable = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-infra-tc-cfg:traffic-collector/Cisco-IOS-XR-infra-tc-cfg:external-interfaces/Cisco-IOS-XR-infra-tc-cfg:external-interface[Cisco-IOS-XR-infra-tc-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
                return meta._meta_table['TrafficCollector.ExternalInterfaces.ExternalInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-tc-cfg:traffic-collector/Cisco-IOS-XR-infra-tc-cfg:external-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.external_interface is not None:
                for child_ref in self.external_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
            return meta._meta_table['TrafficCollector.ExternalInterfaces']['meta_info']


    class Statistics(object):
        """
        Configure statistics related parameters
        
        .. attribute:: collection_interval
        
        	Configure statistics collection interval
        	**type**\:   :py:class:`CollectIonIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.CollectIonIntervalEnum>`
        
        .. attribute:: enable_traffic_collector_statistics
        
        	Enable traffic collector statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: history_size
        
        	Configure statistics history size
        	**type**\: one of the below types:
        
        	**type**\:   :py:class:`HistorySizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.HistorySizeEnum>`
        
        
        ----
        	**type**\:  int
        
        	**range:** 1..10
        
        
        ----
        .. attribute:: history_timeout
        
        	Configure statistics history timeout interval
        	**type**\: one of the below types:
        
        	**type**\:   :py:class:`HistoryTimeoutEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.HistoryTimeoutEnum>`
        
        
        ----
        	**type**\:  int
        
        	**range:** 0..720
        
        
        ----
        

        """

        _prefix = 'infra-tc-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.collection_interval = None
            self.enable_traffic_collector_statistics = None
            self.history_size = None
            self.history_timeout = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-tc-cfg:traffic-collector/Cisco-IOS-XR-infra-tc-cfg:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.collection_interval is not None:
                return True

            if self.enable_traffic_collector_statistics is not None:
                return True

            if self.history_size is not None:
                return True

            if self.history_timeout is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
            return meta._meta_table['TrafficCollector.Statistics']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-tc-cfg:traffic-collector'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.enable_traffic_collector is not None:
            return True

        if self.external_interfaces is not None and self.external_interfaces._has_data():
            return True

        if self.statistics is not None and self.statistics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
        return meta._meta_table['TrafficCollector']['meta_info']


