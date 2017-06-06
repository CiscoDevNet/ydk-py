""" Cisco_IOS_XR_ip_rib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rib package configuration.

This module contains definitions
for the following management objects\:
  rib\: RIB configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-infra\-rsi\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Rib(object):
    """
    RIB configuration.
    
    .. attribute:: af
    
    	RIB address family configuration
    	**type**\:   :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af>`
    
    .. attribute:: max_recursion_depth
    
    	Set maximum depth for route recursion check
    	**type**\:  int
    
    	**range:** 5..16
    
    

    """

    _prefix = 'ip-rib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.af = Rib.Af()
        self.af.parent = self
        self.max_recursion_depth = None


    class Af(object):
        """
        RIB address family configuration
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6>`
        
        

        """

        _prefix = 'ip-rib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ipv4 = Rib.Af.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = Rib.Af.Ipv6()
            self.ipv6.parent = self


        class Ipv4(object):
            """
            IPv4 configuration
            
            .. attribute:: next_hop_dampening_disable
            
            	Disable next\-hop dampening
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redistribution_history
            
            	Redistribution history related configs
            	**type**\:   :py:class:`RedistributionHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4.RedistributionHistory>`
            
            

            """

            _prefix = 'ip-rib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.next_hop_dampening_disable = None
                self.redistribution_history = Rib.Af.Ipv4.RedistributionHistory()
                self.redistribution_history.parent = self


            class RedistributionHistory(object):
                """
                Redistribution history related configs
                
                .. attribute:: bcdl_client
                
                	Maximum BCDL redistribution history size
                	**type**\:  int
                
                	**range:** 10..2000000
                
                .. attribute:: keep
                
                	Retain redistribution history after disconnect
                	**type**\:   :py:class:`Keep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4.RedistributionHistory.Keep>`
                
                .. attribute:: protocol_client
                
                	Maximum protocol redistribution history size
                	**type**\:  int
                
                	**range:** 10..250000
                
                

                """

                _prefix = 'ip-rib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bcdl_client = None
                    self.keep = Rib.Af.Ipv4.RedistributionHistory.Keep()
                    self.keep.parent = self
                    self.protocol_client = None


                class Keep(object):
                    """
                    Retain redistribution history after disconnect.
                    
                    .. attribute:: bcdl
                    
                    	Enable retain BCDL history
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bcdl = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ip-rib-cfg:rib/Cisco-IOS-XR-ip-rib-cfg:af/Cisco-IOS-XR-ip-rib-cfg:ipv4/Cisco-IOS-XR-ip-rib-cfg:redistribution-history/Cisco-IOS-XR-ip-rib-cfg:keep'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bcdl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rib_cfg as meta
                        return meta._meta_table['Rib.Af.Ipv4.RedistributionHistory.Keep']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rib-cfg:rib/Cisco-IOS-XR-ip-rib-cfg:af/Cisco-IOS-XR-ip-rib-cfg:ipv4/Cisco-IOS-XR-ip-rib-cfg:redistribution-history'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bcdl_client is not None:
                        return True

                    if self.keep is not None and self.keep._has_data():
                        return True

                    if self.protocol_client is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rib_cfg as meta
                    return meta._meta_table['Rib.Af.Ipv4.RedistributionHistory']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rib-cfg:rib/Cisco-IOS-XR-ip-rib-cfg:af/Cisco-IOS-XR-ip-rib-cfg:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.next_hop_dampening_disable is not None:
                    return True

                if self.redistribution_history is not None and self.redistribution_history._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rib_cfg as meta
                return meta._meta_table['Rib.Af.Ipv4']['meta_info']


        class Ipv6(object):
            """
            IPv6 configuration
            
            .. attribute:: next_hop_dampening_disable
            
            	Disable next\-hop dampening
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redistribution_history
            
            	Redistribution history related configs
            	**type**\:   :py:class:`RedistributionHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6.RedistributionHistory>`
            
            

            """

            _prefix = 'ip-rib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.next_hop_dampening_disable = None
                self.redistribution_history = Rib.Af.Ipv6.RedistributionHistory()
                self.redistribution_history.parent = self


            class RedistributionHistory(object):
                """
                Redistribution history related configs
                
                .. attribute:: bcdl_client
                
                	Maximum BCDL redistribution history size
                	**type**\:  int
                
                	**range:** 10..2000000
                
                .. attribute:: keep
                
                	Retain redistribution history after disconnect
                	**type**\:   :py:class:`Keep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6.RedistributionHistory.Keep>`
                
                .. attribute:: protocol_client
                
                	Maximum protocol redistribution history size
                	**type**\:  int
                
                	**range:** 10..250000
                
                

                """

                _prefix = 'ip-rib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bcdl_client = None
                    self.keep = Rib.Af.Ipv6.RedistributionHistory.Keep()
                    self.keep.parent = self
                    self.protocol_client = None


                class Keep(object):
                    """
                    Retain redistribution history after disconnect.
                    
                    .. attribute:: bcdl
                    
                    	Enable retain BCDL history
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bcdl = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ip-rib-cfg:rib/Cisco-IOS-XR-ip-rib-cfg:af/Cisco-IOS-XR-ip-rib-cfg:ipv6/Cisco-IOS-XR-ip-rib-cfg:redistribution-history/Cisco-IOS-XR-ip-rib-cfg:keep'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bcdl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rib_cfg as meta
                        return meta._meta_table['Rib.Af.Ipv6.RedistributionHistory.Keep']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rib-cfg:rib/Cisco-IOS-XR-ip-rib-cfg:af/Cisco-IOS-XR-ip-rib-cfg:ipv6/Cisco-IOS-XR-ip-rib-cfg:redistribution-history'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bcdl_client is not None:
                        return True

                    if self.keep is not None and self.keep._has_data():
                        return True

                    if self.protocol_client is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rib_cfg as meta
                    return meta._meta_table['Rib.Af.Ipv6.RedistributionHistory']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rib-cfg:rib/Cisco-IOS-XR-ip-rib-cfg:af/Cisco-IOS-XR-ip-rib-cfg:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.next_hop_dampening_disable is not None:
                    return True

                if self.redistribution_history is not None and self.redistribution_history._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rib_cfg as meta
                return meta._meta_table['Rib.Af.Ipv6']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rib-cfg:rib/Cisco-IOS-XR-ip-rib-cfg:af'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rib_cfg as meta
            return meta._meta_table['Rib.Af']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-rib-cfg:rib'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.af is not None and self.af._has_data():
            return True

        if self.max_recursion_depth is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rib_cfg as meta
        return meta._meta_table['Rib']['meta_info']


