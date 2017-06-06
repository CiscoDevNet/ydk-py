""" Cisco_IOS_XR_subscriber_accounting_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-accounting package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-accounting\: Subscriber Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SubscriberAccounting(object):
    """
    Subscriber Configuration
    
    .. attribute:: prepaid_configurations
    
    	Subscriber Prepaid Feature Configuration
    	**type**\:   :py:class:`PrepaidConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg.SubscriberAccounting.PrepaidConfigurations>`
    
    

    """

    _prefix = 'subscriber-accounting-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.prepaid_configurations = SubscriberAccounting.PrepaidConfigurations()
        self.prepaid_configurations.parent = self


    class PrepaidConfigurations(object):
        """
        Subscriber Prepaid Feature Configuration
        
        .. attribute:: prepaid_configuration
        
        	Prepaid configuration name or default
        	**type**\: list of    :py:class:`PrepaidConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg.SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration>`
        
        

        """

        _prefix = 'subscriber-accounting-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.prepaid_configuration = YList()
            self.prepaid_configuration.parent = self
            self.prepaid_configuration.name = 'prepaid_configuration'


        class PrepaidConfiguration(object):
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
                self.parent = None
                self.prepaid_config_name = None
                self.accounting_method_list = None
                self.author_method_list = None
                self.password = None
                self.time_hold = None
                self.time_threshold = None
                self.time_valid = None
                self.traffic_direction = None
                self.volume_threshold = None

            @property
            def _common_path(self):
                if self.prepaid_config_name is None:
                    raise YPYModelError('Key property prepaid_config_name is None')

                return '/Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting/Cisco-IOS-XR-subscriber-accounting-cfg:prepaid-configurations/Cisco-IOS-XR-subscriber-accounting-cfg:prepaid-configuration[Cisco-IOS-XR-subscriber-accounting-cfg:prepaid-config-name = ' + str(self.prepaid_config_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.prepaid_config_name is not None:
                    return True

                if self.accounting_method_list is not None:
                    return True

                if self.author_method_list is not None:
                    return True

                if self.password is not None:
                    return True

                if self.time_hold is not None:
                    return True

                if self.time_threshold is not None:
                    return True

                if self.time_valid is not None:
                    return True

                if self.traffic_direction is not None:
                    return True

                if self.volume_threshold is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_cfg as meta
                return meta._meta_table['SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting/Cisco-IOS-XR-subscriber-accounting-cfg:prepaid-configurations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.prepaid_configuration is not None:
                for child_ref in self.prepaid_configuration:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_cfg as meta
            return meta._meta_table['SubscriberAccounting.PrepaidConfigurations']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.prepaid_configurations is not None and self.prepaid_configurations._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_cfg as meta
        return meta._meta_table['SubscriberAccounting']['meta_info']


