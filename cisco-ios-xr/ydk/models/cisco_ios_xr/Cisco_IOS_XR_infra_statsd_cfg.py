""" Cisco_IOS_XR_infra_statsd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-statsd package configuration.

This module contains definitions
for the following management objects\:
  statistics\: Global statistics configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Statistics(Entity):
    """
    Global statistics configuration
    
    .. attribute:: period
    
    	Collection period for statistics polling
    	**type**\:  :py:class:`Period <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg.Statistics.Period>`
    
    

    """

    _prefix = 'infra-statsd-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Statistics, self).__init__()
        self._top_entity = None

        self.yang_name = "statistics"
        self.yang_parent_name = "Cisco-IOS-XR-infra-statsd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("period", ("period", Statistics.Period))])
        self._leafs = OrderedDict()

        self.period = Statistics.Period()
        self.period.parent = self
        self._children_name_map["period"] = "period"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-statsd-cfg:statistics"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Statistics, [], name, value)


    class Period(Entity):
        """
        Collection period for statistics polling
        
        .. attribute:: service_accounting
        
        	Collection polling period for service accounting collectors
        	**type**\:  :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg.Statistics.Period.ServiceAccounting>`
        
        

        """

        _prefix = 'infra-statsd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Statistics.Period, self).__init__()

            self.yang_name = "period"
            self.yang_parent_name = "statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("service-accounting", ("service_accounting", Statistics.Period.ServiceAccounting))])
            self._leafs = OrderedDict()

            self.service_accounting = Statistics.Period.ServiceAccounting()
            self.service_accounting.parent = self
            self._children_name_map["service_accounting"] = "service-accounting"
            self._segment_path = lambda: "period"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-statsd-cfg:statistics/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Statistics.Period, [], name, value)


        class ServiceAccounting(Entity):
            """
            Collection polling period for service
            accounting collectors
            
            .. attribute:: polling_period
            
            	Collection polling period for service accounting collectors
            	**type**\: int
            
            	**range:** 30..3600
            
            .. attribute:: polling_disable
            
            	Disable periodic statistics polling for service accounting collectors
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-statsd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Statistics.Period.ServiceAccounting, self).__init__()

                self.yang_name = "service-accounting"
                self.yang_parent_name = "period"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('polling_period', (YLeaf(YType.uint32, 'polling-period'), ['int'])),
                    ('polling_disable', (YLeaf(YType.empty, 'polling-disable'), ['Empty'])),
                ])
                self.polling_period = None
                self.polling_disable = None
                self._segment_path = lambda: "service-accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-statsd-cfg:statistics/period/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Statistics.Period.ServiceAccounting, ['polling_period', 'polling_disable'], name, value)

    def clone_ptr(self):
        self._top_entity = Statistics()
        return self._top_entity

