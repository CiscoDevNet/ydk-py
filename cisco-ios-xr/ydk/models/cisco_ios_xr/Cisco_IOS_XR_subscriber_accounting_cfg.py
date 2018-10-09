""" Cisco_IOS_XR_subscriber_accounting_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-accounting package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-accounting\: Subscriber Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SubscriberAccounting(Entity):
    """
    Subscriber Configuration
    
    .. attribute:: prepaid_configurations
    
    	Subscriber Prepaid Feature Configuration
    	**type**\:  :py:class:`PrepaidConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg.SubscriberAccounting.PrepaidConfigurations>`
    
    

    """

    _prefix = 'subscriber-accounting-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(SubscriberAccounting, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-accounting"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-accounting-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("prepaid-configurations", ("prepaid_configurations", SubscriberAccounting.PrepaidConfigurations))])
        self._leafs = OrderedDict()

        self.prepaid_configurations = SubscriberAccounting.PrepaidConfigurations()
        self.prepaid_configurations.parent = self
        self._children_name_map["prepaid_configurations"] = "prepaid-configurations"
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SubscriberAccounting, [], name, value)


    class PrepaidConfigurations(Entity):
        """
        Subscriber Prepaid Feature Configuration
        
        .. attribute:: prepaid_configuration
        
        	Prepaid configuration name or default
        	**type**\: list of  		 :py:class:`PrepaidConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg.SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration>`
        
        

        """

        _prefix = 'subscriber-accounting-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(SubscriberAccounting.PrepaidConfigurations, self).__init__()

            self.yang_name = "prepaid-configurations"
            self.yang_parent_name = "subscriber-accounting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prepaid-configuration", ("prepaid_configuration", SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration))])
            self._leafs = OrderedDict()

            self.prepaid_configuration = YList(self)
            self._segment_path = lambda: "prepaid-configurations"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberAccounting.PrepaidConfigurations, [], name, value)


        class PrepaidConfiguration(Entity):
            """
            Prepaid configuration name or default
            
            .. attribute:: prepaid_config_name  (key)
            
            	Prepaid configuration name or default
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: password
            
            	Password to be used when placing prepaid (re)authorization requests
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: volume_threshold
            
            	Threshold at which to send prepaid volume quota request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_method_list
            
            	Method list to be used when placing prepaid accounting requests
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: time_hold
            
            	Idle Threshold for which prepaid quota is valid
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: author_method_list
            
            	Method list to be used when placing prepaid (re)authorization requests
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: traffic_direction
            
            	Prepaid quota traffic direction
            	**type**\: str
            
            .. attribute:: time_threshold
            
            	Threshold at which to send prepaid time quota request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: time_valid
            
            	Threshold for which prepaid quota is valid
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'subscriber-accounting-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration, self).__init__()

                self.yang_name = "prepaid-configuration"
                self.yang_parent_name = "prepaid-configurations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['prepaid_config_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('prepaid_config_name', (YLeaf(YType.str, 'prepaid-config-name'), ['str'])),
                    ('password', (YLeaf(YType.str, 'password'), ['str'])),
                    ('volume_threshold', (YLeaf(YType.uint32, 'volume-threshold'), ['int'])),
                    ('accounting_method_list', (YLeaf(YType.str, 'accounting-method-list'), ['str'])),
                    ('time_hold', (YLeaf(YType.uint32, 'time-hold'), ['int'])),
                    ('author_method_list', (YLeaf(YType.str, 'author-method-list'), ['str'])),
                    ('traffic_direction', (YLeaf(YType.str, 'traffic-direction'), ['str'])),
                    ('time_threshold', (YLeaf(YType.uint32, 'time-threshold'), ['int'])),
                    ('time_valid', (YLeaf(YType.uint32, 'time-valid'), ['int'])),
                ])
                self.prepaid_config_name = None
                self.password = None
                self.volume_threshold = None
                self.accounting_method_list = None
                self.time_hold = None
                self.author_method_list = None
                self.traffic_direction = None
                self.time_threshold = None
                self.time_valid = None
                self._segment_path = lambda: "prepaid-configuration" + "[prepaid-config-name='" + str(self.prepaid_config_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting/prepaid-configurations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration, ['prepaid_config_name', 'password', 'volume_threshold', 'accounting_method_list', 'time_hold', 'author_method_list', 'traffic_direction', 'time_threshold', 'time_valid'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberAccounting()
        return self._top_entity

