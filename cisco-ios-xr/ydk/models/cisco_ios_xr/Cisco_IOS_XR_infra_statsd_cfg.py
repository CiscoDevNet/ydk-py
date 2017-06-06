""" Cisco_IOS_XR_infra_statsd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-statsd package configuration.

This module contains definitions
for the following management objects\:
  statistics\: Global statistics configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Statistics(object):
    """
    Global statistics configuration
    
    .. attribute:: period
    
    	Collection period for statistics polling
    	**type**\:   :py:class:`Period <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg.Statistics.Period>`
    
    

    """

    _prefix = 'infra-statsd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.period = Statistics.Period()
        self.period.parent = self


    class Period(object):
        """
        Collection period for statistics polling
        
        .. attribute:: service_accounting
        
        	Collection polling period for service accounting collectors
        	**type**\:   :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg.Statistics.Period.ServiceAccounting>`
        
        

        """

        _prefix = 'infra-statsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.service_accounting = Statistics.Period.ServiceAccounting()
            self.service_accounting.parent = self


        class ServiceAccounting(object):
            """
            Collection polling period for service
            accounting collectors
            
            .. attribute:: polling_disable
            
            	Disable periodic statistics polling for service accounting collectors
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: polling_period
            
            	Collection polling period for service accounting collectors
            	**type**\:  int
            
            	**range:** 30..3600
            
            	**default value**\: 900
            
            

            """

            _prefix = 'infra-statsd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.polling_disable = None
                self.polling_period = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-statsd-cfg:statistics/Cisco-IOS-XR-infra-statsd-cfg:period/Cisco-IOS-XR-infra-statsd-cfg:service-accounting'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.polling_disable is not None:
                    return True

                if self.polling_period is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_cfg as meta
                return meta._meta_table['Statistics.Period.ServiceAccounting']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-statsd-cfg:statistics/Cisco-IOS-XR-infra-statsd-cfg:period'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.service_accounting is not None and self.service_accounting._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_cfg as meta
            return meta._meta_table['Statistics.Period']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-statsd-cfg:statistics'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.period is not None and self.period._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_cfg as meta
        return meta._meta_table['Statistics']['meta_info']


