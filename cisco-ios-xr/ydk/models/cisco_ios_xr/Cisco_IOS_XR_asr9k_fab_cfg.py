""" Cisco_IOS_XR_asr9k_fab_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-fab package configuration.

This module contains definitions
for the following management objects\:
  fab\-vqi\-config\: Configure Fabric

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class FabVqiConfig(object):
    """
    Configure Fabric
    
    .. attribute:: operates
    
    	none
    	**type**\:   :py:class:`Operates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg.FabVqiConfig.Operates>`
    
    

    """

    _prefix = 'asr9k-fab-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.operates = FabVqiConfig.Operates()
        self.operates.parent = self


    class Operates(object):
        """
        none
        
        .. attribute:: operate
        
        	none
        	**type**\: list of    :py:class:`Operate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg.FabVqiConfig.Operates.Operate>`
        
        

        """

        _prefix = 'asr9k-fab-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.operate = YList()
            self.operate.parent = self
            self.operate.name = 'operate'


        class Operate(object):
            """
            none
            
            .. attribute:: id1  <key>
            
            	none
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: id1_xr
            
            	none
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: id2
            
            	none
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'asr9k-fab-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.id1 = None
                self.id1_xr = None
                self.id2 = None

            @property
            def _common_path(self):
                if self.id1 is None:
                    raise YPYModelError('Key property id1 is None')

                return '/Cisco-IOS-XR-asr9k-fab-cfg:fab-vqi-config/Cisco-IOS-XR-asr9k-fab-cfg:operates/Cisco-IOS-XR-asr9k-fab-cfg:operate[Cisco-IOS-XR-asr9k-fab-cfg:id1 = ' + str(self.id1) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.id1 is not None:
                    return True

                if self.id1_xr is not None:
                    return True

                if self.id2 is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fab_cfg as meta
                return meta._meta_table['FabVqiConfig.Operates.Operate']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-fab-cfg:fab-vqi-config/Cisco-IOS-XR-asr9k-fab-cfg:operates'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.operate is not None:
                for child_ref in self.operate:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fab_cfg as meta
            return meta._meta_table['FabVqiConfig.Operates']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-fab-cfg:fab-vqi-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.operates is not None and self.operates._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fab_cfg as meta
        return meta._meta_table['FabVqiConfig']['meta_info']


