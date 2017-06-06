""" Cisco_IOS_XR_infra_dumper_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-dumper package configuration.

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
    
    .. attribute:: choice1
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice1>`
    
    	**presence node**\: True
    
    .. attribute:: choice2
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice2>`
    
    	**presence node**\: True
    
    .. attribute:: choice3
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice3>`
    
    	**presence node**\: True
    
    .. attribute:: kernel_debugger
    
    	Enable kernel debugger
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: packet_memory
    
    	Specify 'true' to dump packet memory for all process, 'false' to disable dump of packet memory
    	**type**\:  bool
    
    .. attribute:: sparse
    
    	Specify 'true' to enable sparse core dump, 'false' to disable sparse core dump
    	**type**\:  bool
    
    .. attribute:: sparse_size
    
    	Switch to sparse core dump at this size
    	**type**\:  int
    
    	**range:** 1..4095
    
    

    """

    _prefix = 'infra-dumper-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.choice1 = None
        self.choice2 = None
        self.choice3 = None
        self.kernel_debugger = None
        self.packet_memory = None
        self.sparse = None
        self.sparse_size = None


    class Choice1(object):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.compress = None
            self.file_path = None
            self.filename = None
            self.higher_limit = None
            self.lower_limit = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-dumper-cfg:exception/Cisco-IOS-XR-infra-dumper-cfg:choice1'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.compress is not None:
                return True

            if self.file_path is not None:
                return True

            if self.filename is not None:
                return True

            if self.higher_limit is not None:
                return True

            if self.lower_limit is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_dumper_cfg as meta
            return meta._meta_table['Exception.Choice1']['meta_info']


    class Choice3(object):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.compress = None
            self.file_path = None
            self.filename = None
            self.higher_limit = None
            self.lower_limit = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-dumper-cfg:exception/Cisco-IOS-XR-infra-dumper-cfg:choice3'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.compress is not None:
                return True

            if self.file_path is not None:
                return True

            if self.filename is not None:
                return True

            if self.higher_limit is not None:
                return True

            if self.lower_limit is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_dumper_cfg as meta
            return meta._meta_table['Exception.Choice3']['meta_info']


    class Choice2(object):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.compress = None
            self.file_path = None
            self.filename = None
            self.higher_limit = None
            self.lower_limit = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-dumper-cfg:exception/Cisco-IOS-XR-infra-dumper-cfg:choice2'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.compress is not None:
                return True

            if self.file_path is not None:
                return True

            if self.filename is not None:
                return True

            if self.higher_limit is not None:
                return True

            if self.lower_limit is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_dumper_cfg as meta
            return meta._meta_table['Exception.Choice2']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-dumper-cfg:exception'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.choice1 is not None and self.choice1._has_data():
            return True

        if self.choice2 is not None and self.choice2._has_data():
            return True

        if self.choice3 is not None and self.choice3._has_data():
            return True

        if self.kernel_debugger is not None:
            return True

        if self.packet_memory is not None:
            return True

        if self.sparse is not None:
            return True

        if self.sparse_size is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_dumper_cfg as meta
        return meta._meta_table['Exception']['meta_info']


