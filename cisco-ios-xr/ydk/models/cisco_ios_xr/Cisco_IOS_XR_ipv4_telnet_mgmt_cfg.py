""" Cisco_IOS_XR_ipv4_telnet_mgmt_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-telnet\-mgmt package configuration.

This module contains definitions
for the following management objects\:
  telnet\: Global Telnet configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Telnet(object):
    """
    Global Telnet configuration commands
    
    .. attribute:: vrfs
    
    	VRF name for telnet service
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg.Telnet.Vrfs>`
    
    

    """

    _prefix = 'ipv4-telnet-mgmt-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.vrfs = Telnet.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF name for telnet service
        
        .. attribute:: vrf
        
        	VRF name for telnet service
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg.Telnet.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-telnet-mgmt-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF name for telnet service
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4
            
            	IPv4 configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg.Telnet.Vrfs.Vrf.Ipv4>`
            
            

            """

            _prefix = 'ipv4-telnet-mgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.ipv4 = Telnet.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self


            class Ipv4(object):
                """
                IPv4 configuration
                
                .. attribute:: dscp
                
                	Specify the DSCP value
                	**type**\:  int
                
                	**range:** 0..63
                
                

                """

                _prefix = 'ipv4-telnet-mgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dscp = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.dscp is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_telnet_mgmt_cfg as meta
                    return meta._meta_table['Telnet.Vrfs.Vrf.Ipv4']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:telnet/Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:vrfs/Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:vrf[Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_telnet_mgmt_cfg as meta
                return meta._meta_table['Telnet.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:telnet/Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_telnet_mgmt_cfg as meta
            return meta._meta_table['Telnet.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:telnet'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_telnet_mgmt_cfg as meta
        return meta._meta_table['Telnet']['meta_info']


