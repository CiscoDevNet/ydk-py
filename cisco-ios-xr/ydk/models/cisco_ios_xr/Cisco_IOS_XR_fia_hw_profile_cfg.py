""" Cisco_IOS_XR_fia_hw_profile_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fia\-hw\-profile package configuration.

This module contains definitions
for the following management objects\:
  hw\-module\-profile\-config\: none

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class HwModuleProfileConfig(object):
    """
    none
    
    .. attribute:: profile
    
    	Configure profile
    	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile>`
    
    

    """

    _prefix = 'fia-hw-profile-cfg'
    _revision = '2016-06-22'

    def __init__(self):
        self.profile = HwModuleProfileConfig.Profile()
        self.profile.parent = self


    class Profile(object):
        """
        Configure profile.
        
        .. attribute:: tcams
        
        	Configure profile for TCAM LC cards
        	**type**\:  :py:class:`Tcams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Tcams>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            self.parent = None
            self.tcams = HwModuleProfileConfig.Profile.Tcams()
            self.tcams.parent = self


        class Tcams(object):
            """
            Configure profile for TCAM LC cards
            
            .. attribute:: tcam
            
            	In the tcam fib table, denotes the address type ipv4 or ipv6 and whether unicast or multicast
            	**type**\: list of  :py:class:`Tcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Tcams.Tcam>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                self.parent = None
                self.tcam = YList()
                self.tcam.parent = self
                self.tcam.name = 'tcam'


            class Tcam(object):
                """
                In the tcam fib table, denotes the address
                type ipv4 or ipv6 and whether unicast or
                multicast
                
                .. attribute:: address_type  <key>
                
                	none
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: communication_type  <key>
                
                	none
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: table_type  <key>
                
                	none
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: percent
                
                	curve out percentage of TCAM table entries
                	**type**\:  int
                
                	**range:** 0..100
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    self.parent = None
                    self.address_type = None
                    self.communication_type = None
                    self.table_type = None
                    self.percent = None

                @property
                def _common_path(self):
                    if self.address_type is None:
                        raise YPYModelError('Key property address_type is None')
                    if self.communication_type is None:
                        raise YPYModelError('Key property communication_type is None')
                    if self.table_type is None:
                        raise YPYModelError('Key property table_type is None')

                    return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcams/Cisco-IOS-XR-fia-hw-profile-cfg:tcam[Cisco-IOS-XR-fia-hw-profile-cfg:address-type = ' + str(self.address_type) + '][Cisco-IOS-XR-fia-hw-profile-cfg:communication-type = ' + str(self.communication_type) + '][Cisco-IOS-XR-fia-hw-profile-cfg:table-type = ' + str(self.table_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address_type is not None:
                        return True

                    if self.communication_type is not None:
                        return True

                    if self.table_type is not None:
                        return True

                    if self.percent is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                    return meta._meta_table['HwModuleProfileConfig.Profile.Tcams.Tcam']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcams'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.tcam is not None:
                    for child_ref in self.tcam:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                return meta._meta_table['HwModuleProfileConfig.Profile.Tcams']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.tcams is not None and self.tcams._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
            return meta._meta_table['HwModuleProfileConfig.Profile']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.profile is not None and self.profile._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
        return meta._meta_table['HwModuleProfileConfig']['meta_info']


