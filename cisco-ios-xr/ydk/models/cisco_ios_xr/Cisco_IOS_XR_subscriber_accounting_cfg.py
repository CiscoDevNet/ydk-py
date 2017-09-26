""" Cisco_IOS_XR_subscriber_accounting_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-accounting package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-accounting\: Subscriber Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SubscriberAccounting(Entity):
    """
    Subscriber Configuration
    
    .. attribute:: prepaid_configurations
    
    	Subscriber Prepaid Feature Configuration
    	**type**\:   :py:class:`PrepaidConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg.SubscriberAccounting.PrepaidConfigurations>`
    
    

    """

    _prefix = 'subscriber-accounting-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberAccounting, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-accounting"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-accounting-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"prepaid-configurations" : ("prepaid_configurations", SubscriberAccounting.PrepaidConfigurations)}
        self._child_list_classes = {}

        self.prepaid_configurations = SubscriberAccounting.PrepaidConfigurations()
        self.prepaid_configurations.parent = self
        self._children_name_map["prepaid_configurations"] = "prepaid-configurations"
        self._children_yang_names.add("prepaid-configurations")
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting"


    class PrepaidConfigurations(Entity):
        """
        Subscriber Prepaid Feature Configuration
        
        .. attribute:: prepaid_configuration
        
        	Prepaid configuration name or default
        	**type**\: list of    :py:class:`PrepaidConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg.SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration>`
        
        

        """

        _prefix = 'subscriber-accounting-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberAccounting.PrepaidConfigurations, self).__init__()

            self.yang_name = "prepaid-configurations"
            self.yang_parent_name = "subscriber-accounting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"prepaid-configuration" : ("prepaid_configuration", SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration)}

            self.prepaid_configuration = YList(self)
            self._segment_path = lambda: "prepaid-configurations"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberAccounting.PrepaidConfigurations, [], name, value)


        class PrepaidConfiguration(Entity):
            """
            Prepaid configuration name or default
            
            .. attribute:: prepaid_config_name  <key>
            
            	Prepaid configuration name or default
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: accounting_method_list
            
            	Method list to be used when placing prepaid accounting requests
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: author_method_list
            
            	Method list to be used when placing prepaid (re)authorization requests
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: password
            
            	Password to be used when placing prepaid (re)authorization requests
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: time_hold
            
            	Idle Threshold for which prepaid quota is valid
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: time_threshold
            
            	Threshold at which to send prepaid time quota request
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: time_valid
            
            	Threshold for which prepaid quota is valid
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: traffic_direction
            
            	Prepaid quota traffic direction
            	**type**\:  str
            
            .. attribute:: volume_threshold
            
            	Threshold at which to send prepaid volume quota request
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'subscriber-accounting-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration, self).__init__()

                self.yang_name = "prepaid-configuration"
                self.yang_parent_name = "prepaid-configurations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.prepaid_config_name = YLeaf(YType.str, "prepaid-config-name")

                self.accounting_method_list = YLeaf(YType.str, "accounting-method-list")

                self.author_method_list = YLeaf(YType.str, "author-method-list")

                self.password = YLeaf(YType.str, "password")

                self.time_hold = YLeaf(YType.int32, "time-hold")

                self.time_threshold = YLeaf(YType.int32, "time-threshold")

                self.time_valid = YLeaf(YType.int32, "time-valid")

                self.traffic_direction = YLeaf(YType.str, "traffic-direction")

                self.volume_threshold = YLeaf(YType.int32, "volume-threshold")
                self._segment_path = lambda: "prepaid-configuration" + "[prepaid-config-name='" + self.prepaid_config_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting/prepaid-configurations/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration, ['prepaid_config_name', 'accounting_method_list', 'author_method_list', 'password', 'time_hold', 'time_threshold', 'time_valid', 'traffic_direction', 'volume_threshold'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberAccounting()
        return self._top_entity

