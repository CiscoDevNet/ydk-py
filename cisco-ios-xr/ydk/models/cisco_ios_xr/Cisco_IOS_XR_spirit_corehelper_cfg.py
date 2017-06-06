""" Cisco_IOS_XR_spirit_corehelper_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR spirit\-corehelper package configuration.

This module contains definitions
for the following management objects\:
  exception\: Core dump configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Exception(object):
    """
    Core dump configuration commands
    
    .. attribute:: file
    
    	Container for the order of preference
    	**type**\:   :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg.Exception.File>`
    
    

    """

    _prefix = 'spirit-corehelper-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.file = Exception.File()
        self.file.parent = self


    class File(object):
        """
        Container for the order of preference
        
        .. attribute:: choice1
        
        	Preference of the dump location
        	**type**\:  str
        
        .. attribute:: choice2
        
        	Preference of the dump location
        	**type**\:  str
        
        .. attribute:: choice3
        
        	Preference of the dump location
        	**type**\:  str
        
        

        """

        _prefix = 'spirit-corehelper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.choice1 = None
            self.choice2 = None
            self.choice3 = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-corehelper-cfg:exception/Cisco-IOS-XR-spirit-corehelper-cfg:file'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.choice1 is not None:
                return True

            if self.choice2 is not None:
                return True

            if self.choice3 is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_corehelper_cfg as meta
            return meta._meta_table['Exception.File']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-spirit-corehelper-cfg:exception'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.file is not None and self.file._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_corehelper_cfg as meta
        return meta._meta_table['Exception']['meta_info']


