""" CISCO_UBE_MIB 

This MIB describes objects used for managing Cisco
Unified Border Element (CUBE).

The Cisco Unified Border Element (CUBE) is a Cisco 
IOS Session Border Controller (SBC) that interconnects
independent voice over IP (VoIP) and video over IP 
networks for data, voice, and video transport

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoUbeMib(object):
    """
    
    
    .. attribute:: ciscoubemibobjects
    
    	
    	**type**\:   :py:class:`Ciscoubemibobjects <ydk.models.cisco_ios_xe.CISCO_UBE_MIB.CiscoUbeMib.Ciscoubemibobjects>`
    
    

    """

    _prefix = 'CISCO-UBE-MIB'
    _revision = '2010-11-29'

    def __init__(self):
        self.ciscoubemibobjects = CiscoUbeMib.Ciscoubemibobjects()
        self.ciscoubemibobjects.parent = self


    class Ciscoubemibobjects(object):
        """
        
        
        .. attribute:: cubeenabled
        
        	This object represents, whether the Cisco Unified Border Element (CUBE) is enabled  on the device or not.  The value 'true' means that the CUBE feature  is enabled on the device.  The value 'false' means that the CUBE feature  is disabled
        	**type**\:  bool
        
        .. attribute:: cubetotalsessionallowed
        
        	This object provides the total number of CUBE session allowed on the device. The value zero  means no sessions are allowed with CUBE
        	**type**\:  int
        
        	**range:** 0..999999
        
        	**units**\: session
        
        .. attribute:: cubeversion
        
        	This object represents the version of Cisco Unified Border Element on the device
        	**type**\:  str
        
        

        """

        _prefix = 'CISCO-UBE-MIB'
        _revision = '2010-11-29'

        def __init__(self):
            self.parent = None
            self.cubeenabled = None
            self.cubetotalsessionallowed = None
            self.cubeversion = None

        @property
        def _common_path(self):

            return '/CISCO-UBE-MIB:CISCO-UBE-MIB/CISCO-UBE-MIB:ciscoUbeMIBObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cubeenabled is not None:
                return True

            if self.cubetotalsessionallowed is not None:
                return True

            if self.cubeversion is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_UBE_MIB as meta
            return meta._meta_table['CiscoUbeMib.Ciscoubemibobjects']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-UBE-MIB:CISCO-UBE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ciscoubemibobjects is not None and self.ciscoubemibobjects._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_UBE_MIB as meta
        return meta._meta_table['CiscoUbeMib']['meta_info']


