""" Cisco_IOS_XR_infra_tc_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-tc package configuration.

This module contains definitions
for the following management objects\:
  traffic\-collector\: Global Traffic Collector configuration
    commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CollectIonInterval(Enum):
    """
    CollectIonInterval (Enum Class)

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

    Y_1_minute = Enum.YLeaf(1, "1-minute")

    Y_2_minutes = Enum.YLeaf(2, "2-minutes")

    Y_3_minutes = Enum.YLeaf(3, "3-minutes")

    Y_4_minutes = Enum.YLeaf(4, "4-minutes")

    Y_5_minutes = Enum.YLeaf(5, "5-minutes")

    Y_6_minutes = Enum.YLeaf(6, "6-minutes")

    Y_10_minutes = Enum.YLeaf(10, "10-minutes")

    Y_12_minutes = Enum.YLeaf(12, "12-minutes")

    Y_15_minutes = Enum.YLeaf(15, "15-minutes")

    Y_20_minutes = Enum.YLeaf(20, "20-minutes")

    Y_30_minutes = Enum.YLeaf(30, "30-minutes")

    Y_60_minutes = Enum.YLeaf(60, "60-minutes")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
        return meta._meta_table['CollectIonInterval']


class HistorySize(Enum):
    """
    HistorySize (Enum Class)

    History size

    .. data:: max = 10

    	Max history

    """

    max = Enum.YLeaf(10, "max")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
        return meta._meta_table['HistorySize']


class HistoryTimeout(Enum):
    """
    HistoryTimeout (Enum Class)

    History timeout

    .. data:: max = 720

    	Max timeout

    """

    max = Enum.YLeaf(720, "max")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
        return meta._meta_table['HistoryTimeout']



class TrafficCollector(_Entity_):
    """
    Global Traffic Collector configuration commands
    
    .. attribute:: external_interfaces
    
    	Configure external interfaces
    	**type**\:  :py:class:`ExternalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.ExternalInterfaces>`
    
    .. attribute:: statistics
    
    	Configure statistics related parameters
    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.Statistics>`
    
    .. attribute:: enable_traffic_collector
    
    	Enable traffic collector
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'infra-tc-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(TrafficCollector, self).__init__()
        self._top_entity = None

        self.yang_name = "traffic-collector"
        self.yang_parent_name = "Cisco-IOS-XR-infra-tc-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("external-interfaces", ("external_interfaces", TrafficCollector.ExternalInterfaces)), ("statistics", ("statistics", TrafficCollector.Statistics))])
        self._leafs = OrderedDict([
            ('enable_traffic_collector', (YLeaf(YType.empty, 'enable-traffic-collector'), ['Empty'])),
        ])
        self.enable_traffic_collector = None

        self.external_interfaces = TrafficCollector.ExternalInterfaces()
        self.external_interfaces.parent = self
        self._children_name_map["external_interfaces"] = "external-interfaces"

        self.statistics = TrafficCollector.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-tc-cfg:traffic-collector"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TrafficCollector, ['enable_traffic_collector'], name, value)


    class ExternalInterfaces(_Entity_):
        """
        Configure external interfaces
        
        .. attribute:: external_interface
        
        	Configure an external internface
        	**type**\: list of  		 :py:class:`ExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.ExternalInterfaces.ExternalInterface>`
        
        

        """

        _prefix = 'infra-tc-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TrafficCollector.ExternalInterfaces, self).__init__()

            self.yang_name = "external-interfaces"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("external-interface", ("external_interface", TrafficCollector.ExternalInterfaces.ExternalInterface))])
            self._leafs = OrderedDict()

            self.external_interface = YList(self)
            self._segment_path = lambda: "external-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-cfg:traffic-collector/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.ExternalInterfaces, [], name, value)


        class ExternalInterface(_Entity_):
            """
            Configure an external internface
            
            .. attribute:: interface_name  (key)
            
            	Name of interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: enable
            
            	Enable traffic collector on this interface
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-tc-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(TrafficCollector.ExternalInterfaces.ExternalInterface, self).__init__()

                self.yang_name = "external-interface"
                self.yang_parent_name = "external-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.interface_name = None
                self.enable = None
                self._segment_path = lambda: "external-interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-cfg:traffic-collector/external-interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.ExternalInterfaces.ExternalInterface, ['interface_name', 'enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
                return meta._meta_table['TrafficCollector.ExternalInterfaces.ExternalInterface']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
            return meta._meta_table['TrafficCollector.ExternalInterfaces']['meta_info']


    class Statistics(_Entity_):
        """
        Configure statistics related parameters
        
        .. attribute:: history_size
        
        	Configure statistics history size
        	**type**\: union of the below types:
        
        		**type**\:  :py:class:`HistorySize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.HistorySize>`
        
        		**type**\: int
        
        			**range:** 1..10
        
        .. attribute:: collection_interval
        
        	Configure statistics collection interval
        	**type**\:  :py:class:`CollectIonInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.CollectIonInterval>`
        
        .. attribute:: enable_traffic_collector_statistics
        
        	Enable traffic collector statistics
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: history_timeout
        
        	Configure statistics history timeout interval
        	**type**\: union of the below types:
        
        		**type**\:  :py:class:`HistoryTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.HistoryTimeout>`
        
        		**type**\: int
        
        			**range:** 0..720
        
        

        """

        _prefix = 'infra-tc-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TrafficCollector.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('history_size', (YLeaf(YType.str, 'history-size'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'HistorySize', ''),'int'])),
                ('collection_interval', (YLeaf(YType.enumeration, 'collection-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'CollectIonInterval', '')])),
                ('enable_traffic_collector_statistics', (YLeaf(YType.empty, 'enable-traffic-collector-statistics'), ['Empty'])),
                ('history_timeout', (YLeaf(YType.str, 'history-timeout'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'HistoryTimeout', ''),'int'])),
            ])
            self.history_size = None
            self.collection_interval = None
            self.enable_traffic_collector_statistics = None
            self.history_timeout = None
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-cfg:traffic-collector/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.Statistics, ['history_size', 'collection_interval', 'enable_traffic_collector_statistics', 'history_timeout'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
            return meta._meta_table['TrafficCollector.Statistics']['meta_info']

    def clone_ptr(self):
        self._top_entity = TrafficCollector()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_cfg as meta
        return meta._meta_table['TrafficCollector']['meta_info']


