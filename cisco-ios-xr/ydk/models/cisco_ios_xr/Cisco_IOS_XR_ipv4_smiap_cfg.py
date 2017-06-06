""" Cisco_IOS_XR_ipv4_smiap_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-smiap package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-virtual\: IPv4 virtual address for management interfaces

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ipv4Virtual(object):
    """
    IPv4 virtual address for management interfaces
    
    .. attribute:: use_as_source_address
    
    	Enable use as default source address on sourced packets
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: vrfs
    
    	VRFs for the virtual IPv4 addresses
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs>`
    
    

    """

    _prefix = 'ipv4-smiap-cfg'
    _revision = '2016-07-04'

    def __init__(self):
        self.use_as_source_address = None
        self.vrfs = Ipv4Virtual.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRFs for the virtual IPv4 addresses
        
        .. attribute:: vrf
        
        	A VRF for a virtual IPv4 address.  Specify 'default' for VRF default
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-smiap-cfg'
        _revision = '2016-07-04'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            A VRF for a virtual IPv4 address.  Specify
            'default' for VRF default
            
            .. attribute:: vrf_name  <key>
            
            	Name of VRF
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: address
            
            	IPv4 sddress and mask
            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs.Vrf.Address>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-smiap-cfg'
            _revision = '2016-07-04'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.address = None


            class Address(object):
                """
                IPv4 sddress and mask
                
                .. attribute:: address
                
                	IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                .. attribute:: netmask
                
                	IPv4 address mask
                	**type**\:  int
                
                	**range:** 0..32
                
                	**mandatory**\: True
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-smiap-cfg'
                _revision = '2016-07-04'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.address = None
                    self.netmask = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-smiap-cfg:address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.address is not None:
                        return True

                    if self.netmask is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_smiap_cfg as meta
                    return meta._meta_table['Ipv4Virtual.Vrfs.Vrf.Address']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual/Cisco-IOS-XR-ipv4-smiap-cfg:vrfs/Cisco-IOS-XR-ipv4-smiap-cfg:vrf[Cisco-IOS-XR-ipv4-smiap-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.address is not None and self.address._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_smiap_cfg as meta
                return meta._meta_table['Ipv4Virtual.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual/Cisco-IOS-XR-ipv4-smiap-cfg:vrfs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_smiap_cfg as meta
            return meta._meta_table['Ipv4Virtual.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.use_as_source_address is not None:
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_smiap_cfg as meta
        return meta._meta_table['Ipv4Virtual']['meta_info']


