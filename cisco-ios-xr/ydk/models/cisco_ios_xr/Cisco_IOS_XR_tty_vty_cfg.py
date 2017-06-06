""" Cisco_IOS_XR_tty_vty_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-vty package configuration.

This module contains definitions
for the following management objects\:
  vty\: VTY Pools configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Vty(object):
    """
    VTY Pools configuration
    
    .. attribute:: vty_pools
    
    	List of VTY Pools
    	**type**\:   :py:class:`VtyPools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg.Vty.VtyPools>`
    
    

    """

    _prefix = 'tty-vty-cfg'
    _revision = '2015-09-16'

    def __init__(self):
        self.vty_pools = Vty.VtyPools()
        self.vty_pools.parent = self


    class VtyPools(object):
        """
        List of VTY Pools
        
        .. attribute:: vty_pool
        
        	VTY Pool
        	**type**\: list of    :py:class:`VtyPool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg.Vty.VtyPools.VtyPool>`
        
        

        """

        _prefix = 'tty-vty-cfg'
        _revision = '2015-09-16'

        def __init__(self):
            self.parent = None
            self.vty_pool = YList()
            self.vty_pool.parent = self
            self.vty_pool.name = 'vty_pool'


        class VtyPool(object):
            """
            VTY Pool
            
            .. attribute:: pool_name  <key>
            
            	For configuring range for default pool use 'default',For configuring range for fault\-manager pool use 'fm',For configuring range for any user defined pool use any other string
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: first_vty
            
            	First VTY number,For default VTY use 0,For user\-defined use 5,For fault\-manager use 100
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**mandatory**\: True
            
            .. attribute:: last_vty
            
            	Last VTY number,For default configure between 0\-99,For user\-defined configure between 5\-99 ,For fault\-manager configure between 100\-199
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**mandatory**\: True
            
            .. attribute:: line_template
            
            	Name of line template
            	**type**\:  str
            
            .. attribute:: none
            
            	Empty Option
            	**type**\:  str
            
            

            """

            _prefix = 'tty-vty-cfg'
            _revision = '2015-09-16'

            def __init__(self):
                self.parent = None
                self.pool_name = None
                self.first_vty = None
                self.last_vty = None
                self.line_template = None
                self.none = None

            @property
            def _common_path(self):
                if self.pool_name is None:
                    raise YPYModelError('Key property pool_name is None')

                return '/Cisco-IOS-XR-tty-vty-cfg:vty/Cisco-IOS-XR-tty-vty-cfg:vty-pools/Cisco-IOS-XR-tty-vty-cfg:vty-pool[Cisco-IOS-XR-tty-vty-cfg:pool-name = ' + str(self.pool_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.pool_name is not None:
                    return True

                if self.first_vty is not None:
                    return True

                if self.last_vty is not None:
                    return True

                if self.line_template is not None:
                    return True

                if self.none is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_vty_cfg as meta
                return meta._meta_table['Vty.VtyPools.VtyPool']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-vty-cfg:vty/Cisco-IOS-XR-tty-vty-cfg:vty-pools'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vty_pool is not None:
                for child_ref in self.vty_pool:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_vty_cfg as meta
            return meta._meta_table['Vty.VtyPools']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tty-vty-cfg:vty'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.vty_pools is not None and self.vty_pools._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_vty_cfg as meta
        return meta._meta_table['Vty']['meta_info']


