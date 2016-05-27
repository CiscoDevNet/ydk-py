""" Cisco_IOS_XR_segment_routing_ms_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package configuration.

This module contains definitions
for the following management objects\:
  sr\: Segment Routing

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SrmsMiFlagEnum(Enum):
    """
    SrmsMiFlagEnum

    Srms mi flag

    .. data:: DISABLE = 0

    	Disable flag

    .. data:: ENABLE = 1

    	Enable flag

    """

    DISABLE = 0

    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.segment._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
        return meta._meta_table['SrmsMiFlagEnum']



class Sr(object):
    """
    Segment Routing
    
    .. attribute:: global_block
    
    	Global Block Segment Routing
    	**type**\: :py:class:`GlobalBlock <ydk.models.segment.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.GlobalBlock>`
    
    .. attribute:: mappings
    
    	Mapping Server
    	**type**\: :py:class:`Mappings <ydk.models.segment.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Mappings>`
    
    .. attribute:: enable
    
    	enable SR
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    

    """

    _prefix = 'segment-routing-ms-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.global_block = None
        self.mappings = Sr.Mappings()
        self.mappings.parent = self
        self.enable = None


    class GlobalBlock(object):
        """
        Global Block Segment Routing
        
        .. attribute:: lower_bound
        
        	SRGB Lower Bound
        	**type**\: int
        
        	**range:** 16000..1048574
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        .. attribute:: upper_bound
        
        	SRGB Upper Bound
        	**type**\: int
        
        	**range:** 16001..1048575
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.lower_bound = None
            self.upper_bound = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-ms-cfg:global-block'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.lower_bound is not None:
                return True

            if self.upper_bound is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.segment._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
            return meta._meta_table['Sr.GlobalBlock']['meta_info']


    class Mappings(object):
        """
        Mapping Server
        
        .. attribute:: mapping
        
        	IP prefix to SID mapping
        	**type**\: list of :py:class:`Mapping <ydk.models.segment.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Mappings.Mapping>`
        
        

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.mapping = YList()
            self.mapping.parent = self
            self.mapping.name = 'mapping'


        class Mapping(object):
            """
            IP prefix to SID mapping
            
            .. attribute:: af  <key>
            
            	Address Family
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ip  <key>
            
            	IP prefix
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: mask  <key>
            
            	Mask
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sid_start
            
            	Start of SID index range
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: sid_range
            
            	Range (number of SIDs)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: flag_attached
            
            	Enable/Disable Attached flag
            	**type**\: :py:class:`SrmsMiFlagEnum <ydk.models.segment.Cisco_IOS_XR_segment_routing_ms_cfg.SrmsMiFlagEnum>`
            
            

            """

            _prefix = 'segment-routing-ms-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.af = None
                self.ip = None
                self.mask = None
                self.sid_start = None
                self.sid_range = None
                self.flag_attached = None

            @property
            def _common_path(self):
                if self.af is None:
                    raise YPYDataValidationError('Key property af is None')
                if self.ip is None:
                    raise YPYDataValidationError('Key property ip is None')
                if self.mask is None:
                    raise YPYDataValidationError('Key property mask is None')

                return '/Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-ms-cfg:mappings/Cisco-IOS-XR-segment-routing-ms-cfg:mapping[Cisco-IOS-XR-segment-routing-ms-cfg:af = ' + str(self.af) + '][Cisco-IOS-XR-segment-routing-ms-cfg:ip = ' + str(self.ip) + '][Cisco-IOS-XR-segment-routing-ms-cfg:mask = ' + str(self.mask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.af is not None:
                    return True

                if self.ip is not None:
                    return True

                if self.mask is not None:
                    return True

                if self.sid_start is not None:
                    return True

                if self.sid_range is not None:
                    return True

                if self.flag_attached is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.segment._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.Mappings.Mapping']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-ms-cfg:mappings'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.mapping is not None:
                for child_ref in self.mapping:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.segment._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
            return meta._meta_table['Sr.Mappings']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-segment-routing-ms-cfg:sr'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.global_block is not None and self.global_block._has_data():
            return True

        if self.mappings is not None and self.mappings._has_data():
            return True

        if self.enable is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.segment._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
        return meta._meta_table['Sr']['meta_info']


