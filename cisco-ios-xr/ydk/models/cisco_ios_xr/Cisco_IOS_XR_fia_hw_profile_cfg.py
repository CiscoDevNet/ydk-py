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
    	**type**\:   :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile>`
    
    

    """

    _prefix = 'fia-hw-profile-cfg'
    _revision = '2016-06-22'

    def __init__(self):
        self.profile = HwModuleProfileConfig.Profile()
        self.profile.parent = self


    class Profile(object):
        """
        Configure profile.
        
        .. attribute:: tcam_table
        
        	Configure profile for TCAM LC cards
        	**type**\:   :py:class:`TcamTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            self.parent = None
            self.tcam_table = HwModuleProfileConfig.Profile.TcamTable()
            self.tcam_table.parent = self


        class TcamTable(object):
            """
            Configure profile for TCAM LC cards
            
            .. attribute:: fib_table
            
            	FIB table for TCAM LC cards
            	**type**\:   :py:class:`FibTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                self.parent = None
                self.fib_table = HwModuleProfileConfig.Profile.TcamTable.FibTable()
                self.fib_table.parent = self


            class FibTable(object):
                """
                FIB table for TCAM LC cards
                
                .. attribute:: ipv4_address
                
                	IPv4 table for TCAM LC cards
                	**type**\:   :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address>`
                
                .. attribute:: ipv6_address
                
                	IPv6 table for TCAM LC cards
                	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    self.parent = None
                    self.ipv4_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address()
                    self.ipv4_address.parent = self
                    self.ipv6_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address()
                    self.ipv6_address.parent = self


                class Ipv4Address(object):
                    """
                    IPv4 table for TCAM LC cards
                    
                    .. attribute:: ipv4_unicast
                    
                    	Unicast table for TCAM LC cards
                    	**type**\:   :py:class:`Ipv4Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast()
                        self.ipv4_unicast.parent = self


                    class Ipv4Unicast(object):
                        """
                        Unicast table for TCAM LC cards
                        
                        .. attribute:: ipv4_unicast_percent
                        
                        	curve out percentage of TCAM table entries
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        	**units**\: percentage
                        
                        .. attribute:: ipv4_unicast_prefix_lengths
                        
                        	IPv4 Unicast prefix 
                        	**type**\:   :py:class:`Ipv4UnicastPrefixLengths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths>`
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            self.parent = None
                            self.ipv4_unicast_percent = None
                            self.ipv4_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths()
                            self.ipv4_unicast_prefix_lengths.parent = self


                        class Ipv4UnicastPrefixLengths(object):
                            """
                            IPv4 Unicast prefix 
                            
                            .. attribute:: ipv4_unicast_prefix_length
                            
                            	IPv4 Unicast prefix length
                            	**type**\: list of    :py:class:`Ipv4UnicastPrefixLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength>`
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_unicast_prefix_length = YList()
                                self.ipv4_unicast_prefix_length.parent = self
                                self.ipv4_unicast_prefix_length.name = 'ipv4_unicast_prefix_length'


                            class Ipv4UnicastPrefixLength(object):
                                """
                                IPv4 Unicast prefix length
                                
                                .. attribute:: prefix_length  <key>
                                
                                	prefix length
                                	**type**\:  int
                                
                                	**range:** 0..32
                                
                                .. attribute:: ipv4_unicast_prefix_percent
                                
                                	curve out percentage of TCAM table entries
                                	**type**\:  str
                                
                                	**units**\: percentage
                                
                                

                                """

                                _prefix = 'fia-hw-profile-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    self.parent = None
                                    self.prefix_length = None
                                    self.ipv4_unicast_prefix_percent = None

                                @property
                                def _common_path(self):
                                    if self.prefix_length is None:
                                        raise YPYModelError('Key property prefix_length is None')

                                    return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-address/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-unicast/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-unicast-prefix-lengths/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-unicast-prefix-length[Cisco-IOS-XR-fia-hw-profile-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.prefix_length is not None:
                                        return True

                                    if self.ipv4_unicast_prefix_percent is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                                    return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-address/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-unicast/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-unicast-prefix-lengths'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ipv4_unicast_prefix_length is not None:
                                    for child_ref in self.ipv4_unicast_prefix_length:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                                return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-address/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ipv4_unicast_percent is not None:
                                return True

                            if self.ipv4_unicast_prefix_lengths is not None and self.ipv4_unicast_prefix_lengths._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                            return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table/Cisco-IOS-XR-fia-hw-profile-cfg:ipv4-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv4_unicast is not None and self.ipv4_unicast._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                        return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address']['meta_info']


                class Ipv6Address(object):
                    """
                    IPv6 table for TCAM LC cards
                    
                    .. attribute:: ipv6_unicast
                    
                    	Unicast table for TCAM LC cards
                    	**type**\:   :py:class:`Ipv6Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast()
                        self.ipv6_unicast.parent = self


                    class Ipv6Unicast(object):
                        """
                        Unicast table for TCAM LC cards
                        
                        .. attribute:: ipv6_unicast_percent
                        
                        	curve out percentage of TCAM table entries
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        	**units**\: percentage
                        
                        .. attribute:: ipv6_unicast_prefix_lengths
                        
                        	IPv6 Unicast prefix 
                        	**type**\:   :py:class:`Ipv6UnicastPrefixLengths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths>`
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            self.parent = None
                            self.ipv6_unicast_percent = None
                            self.ipv6_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths()
                            self.ipv6_unicast_prefix_lengths.parent = self


                        class Ipv6UnicastPrefixLengths(object):
                            """
                            IPv6 Unicast prefix 
                            
                            .. attribute:: ipv6_unicast_prefix_length
                            
                            	IPv6 Unicast prefix length
                            	**type**\: list of    :py:class:`Ipv6UnicastPrefixLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength>`
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                self.parent = None
                                self.ipv6_unicast_prefix_length = YList()
                                self.ipv6_unicast_prefix_length.parent = self
                                self.ipv6_unicast_prefix_length.name = 'ipv6_unicast_prefix_length'


                            class Ipv6UnicastPrefixLength(object):
                                """
                                IPv6 Unicast prefix length
                                
                                .. attribute:: prefix_length  <key>
                                
                                	prefix length
                                	**type**\:  int
                                
                                	**range:** 0..128
                                
                                .. attribute:: ipv6_unicast_prefix_percent
                                
                                	curve out percentage of TCAM table entries
                                	**type**\:  str
                                
                                	**units**\: percentage
                                
                                

                                """

                                _prefix = 'fia-hw-profile-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    self.parent = None
                                    self.prefix_length = None
                                    self.ipv6_unicast_prefix_percent = None

                                @property
                                def _common_path(self):
                                    if self.prefix_length is None:
                                        raise YPYModelError('Key property prefix_length is None')

                                    return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-address/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-unicast/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-unicast-prefix-lengths/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-unicast-prefix-length[Cisco-IOS-XR-fia-hw-profile-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.prefix_length is not None:
                                        return True

                                    if self.ipv6_unicast_prefix_percent is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                                    return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-address/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-unicast/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-unicast-prefix-lengths'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ipv6_unicast_prefix_length is not None:
                                    for child_ref in self.ipv6_unicast_prefix_length:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                                return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-address/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ipv6_unicast_percent is not None:
                                return True

                            if self.ipv6_unicast_prefix_lengths is not None and self.ipv6_unicast_prefix_lengths._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                            return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table/Cisco-IOS-XR-fia-hw-profile-cfg:ipv6-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv6_unicast is not None and self.ipv6_unicast._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                        return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table/Cisco-IOS-XR-fia-hw-profile-cfg:fib-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipv4_address is not None and self.ipv4_address._has_data():
                        return True

                    if self.ipv6_address is not None and self.ipv6_address._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                    return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile/Cisco-IOS-XR-fia-hw-profile-cfg:tcam-table'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.fib_table is not None and self.fib_table._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
                return meta._meta_table['HwModuleProfileConfig.Profile.TcamTable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/Cisco-IOS-XR-fia-hw-profile-cfg:profile'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.tcam_table is not None and self.tcam_table._has_data():
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
        if self.profile is not None and self.profile._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_hw_profile_cfg as meta
        return meta._meta_table['HwModuleProfileConfig']['meta_info']


