""" Cisco_IOS_XR_fib_common_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fib\-common package configuration.

This module contains definitions
for the following management objects\:
  fib\: CEF configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class FibPbtsFallbackEnum(Enum):
    """
    FibPbtsFallbackEnum

    Fib pbts fallback

    .. data:: list = 1

    	Fallback to class number list

    .. data:: any = 2

    	Fallback to any class

    .. data:: drop = 3

    	Fallback to drop

    """

    list = 1

    any = 2

    drop = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fib_common_cfg as meta
        return meta._meta_table['FibPbtsFallbackEnum']


class FibPbtsForwardClassEnum(Enum):
    """
    FibPbtsForwardClassEnum

    Fib pbts forward class

    .. data:: any = 8

    	Any class

    """

    any = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fib_common_cfg as meta
        return meta._meta_table['FibPbtsForwardClassEnum']



class Fib(object):
    """
    CEF configuration
    
    .. attribute:: pbts_forward_class_fallbacks
    
    	PBTS class configuration
    	**type**\:   :py:class:`PbtsForwardClassFallbacks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.PbtsForwardClassFallbacks>`
    
    .. attribute:: platform
    
    	FIB platform parameters
    	**type**\:   :py:class:`Platform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.Platform>`
    
    .. attribute:: prefer_aib_routes
    
    	Set options for adjacency routes overriding RIB routes
    	**type**\:  bool
    
    

    """

    _prefix = 'fib-common-cfg'
    _revision = '2017-01-20'

    def __init__(self):
        self.pbts_forward_class_fallbacks = Fib.PbtsForwardClassFallbacks()
        self.pbts_forward_class_fallbacks.parent = self
        self.platform = Fib.Platform()
        self.platform.parent = self
        self.prefer_aib_routes = None


    class PbtsForwardClassFallbacks(object):
        """
        PBTS class configuration
        
        .. attribute:: pbts_forward_class_fallback
        
        	Set PBTS class for fallback
        	**type**\: list of    :py:class:`PbtsForwardClassFallback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback>`
        
        

        """

        _prefix = 'fib-common-cfg'
        _revision = '2017-01-20'

        def __init__(self):
            self.parent = None
            self.pbts_forward_class_fallback = YList()
            self.pbts_forward_class_fallback.parent = self
            self.pbts_forward_class_fallback.name = 'pbts_forward_class_fallback'


        class PbtsForwardClassFallback(object):
            """
            Set PBTS class for fallback
            
            .. attribute:: forward_class_number  <key>
            
            	PBTS forward class number
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`FibPbtsForwardClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.FibPbtsForwardClassEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..8
            
            
            ----
            .. attribute:: fallback_class_number_array
            
            	Set PBTS fallback class number array
            	**type**\:  list of int
            
            	**range:** 0..7
            
            .. attribute:: fallback_type
            
            	Set PBTS fallback type
            	**type**\:   :py:class:`FibPbtsFallbackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.FibPbtsFallbackEnum>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'fib-common-cfg'
            _revision = '2017-01-20'

            def __init__(self):
                self.parent = None
                self.forward_class_number = None
                self.fallback_class_number_array = YLeafList()
                self.fallback_class_number_array.parent = self
                self.fallback_class_number_array.name = 'fallback_class_number_array'
                self.fallback_type = None

            @property
            def _common_path(self):
                if self.forward_class_number is None:
                    raise YPYModelError('Key property forward_class_number is None')

                return '/Cisco-IOS-XR-fib-common-cfg:fib/Cisco-IOS-XR-fib-common-cfg:pbts-forward-class-fallbacks/Cisco-IOS-XR-fib-common-cfg:pbts-forward-class-fallback[Cisco-IOS-XR-fib-common-cfg:forward-class-number = ' + str(self.forward_class_number) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.forward_class_number is not None:
                    return True

                if self.fallback_class_number_array is not None:
                    for child in self.fallback_class_number_array:
                        if child is not None:
                            return True

                if self.fallback_type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fib_common_cfg as meta
                return meta._meta_table['Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fib-common-cfg:fib/Cisco-IOS-XR-fib-common-cfg:pbts-forward-class-fallbacks'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.pbts_forward_class_fallback is not None:
                for child_ref in self.pbts_forward_class_fallback:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fib_common_cfg as meta
            return meta._meta_table['Fib.PbtsForwardClassFallbacks']['meta_info']


    class Platform(object):
        """
        FIB platform parameters
        
        .. attribute:: label_switched_multicast
        
        	Options for label\-switched\-multicast parameters
        	**type**\:   :py:class:`LabelSwitchedMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.Platform.LabelSwitchedMulticast>`
        
        

        """

        _prefix = 'fib-common-cfg'
        _revision = '2017-01-20'

        def __init__(self):
            self.parent = None
            self.label_switched_multicast = Fib.Platform.LabelSwitchedMulticast()
            self.label_switched_multicast.parent = self


        class LabelSwitchedMulticast(object):
            """
            Options for label\-switched\-multicast parameters
            
            .. attribute:: frr_holdtime
            
            	Set time to keep FRR slots programmed post FRR
            	**type**\:  int
            
            	**range:** 3..180
            
            	**units**\: second
            
            

            """

            _prefix = 'fib-common-cfg'
            _revision = '2017-01-20'

            def __init__(self):
                self.parent = None
                self.frr_holdtime = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-fib-common-cfg:fib/Cisco-IOS-XR-fib-common-cfg:platform/Cisco-IOS-XR-fib-common-cfg:label-switched-multicast'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.frr_holdtime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fib_common_cfg as meta
                return meta._meta_table['Fib.Platform.LabelSwitchedMulticast']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fib-common-cfg:fib/Cisco-IOS-XR-fib-common-cfg:platform'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.label_switched_multicast is not None and self.label_switched_multicast._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fib_common_cfg as meta
            return meta._meta_table['Fib.Platform']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-fib-common-cfg:fib'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.pbts_forward_class_fallbacks is not None and self.pbts_forward_class_fallbacks._has_data():
            return True

        if self.platform is not None and self.platform._has_data():
            return True

        if self.prefer_aib_routes is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fib_common_cfg as meta
        return meta._meta_table['Fib']['meta_info']


