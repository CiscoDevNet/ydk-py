""" Cisco_IOS_XR_ncs5500_coherent_portmode_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-coherent\-portmode package operational data.

This module contains definitions
for the following management objects\:
  controller\-port\-mode\: Coherent PortMode  operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ControllerPortMode(object):
    """
    Coherent PortMode  operational data
    
    .. attribute:: optics_name
    
    	Name of optics controller
    	**type**\: list of    :py:class:`OpticsName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper.ControllerPortMode.OpticsName>`
    
    

    """

    _prefix = 'ncs5500-coherent-portmode-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.optics_name = YList()
        self.optics_name.parent = self
        self.optics_name.name = 'optics_name'


    class OpticsName(object):
        """
        Name of optics controller
        
        .. attribute:: interface_name  <key>
        
        	Interface Name
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: port_mode_info
        
        	PortMode  operational data
        	**type**\:   :py:class:`PortModeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper.ControllerPortMode.OpticsName.PortModeInfo>`
        
        

        """

        _prefix = 'ncs5500-coherent-portmode-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface_name = None
            self.port_mode_info = ControllerPortMode.OpticsName.PortModeInfo()
            self.port_mode_info.parent = self


        class PortModeInfo(object):
            """
            PortMode  operational data
            
            .. attribute:: diff
            
            	Optics diff
            	**type**\:  str
            
            .. attribute:: fec
            
            	Optics fec
            	**type**\:  str
            
            .. attribute:: intf_name
            
            	Interface Name
            	**type**\:  str
            
            .. attribute:: modulation
            
            	Optics modulation
            	**type**\:  str
            
            .. attribute:: speed
            
            	Optics speed
            	**type**\:  str
            
            

            """

            _prefix = 'ncs5500-coherent-portmode-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.diff = None
                self.fec = None
                self.intf_name = None
                self.modulation = None
                self.speed = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-portmode-oper:port-mode-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.diff is not None:
                    return True

                if self.fec is not None:
                    return True

                if self.intf_name is not None:
                    return True

                if self.modulation is not None:
                    return True

                if self.speed is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_portmode_oper as meta
                return meta._meta_table['ControllerPortMode.OpticsName.PortModeInfo']['meta_info']

        @property
        def _common_path(self):
            if self.interface_name is None:
                raise YPYModelError('Key property interface_name is None')

            return '/Cisco-IOS-XR-ncs5500-coherent-portmode-oper:controller-port-mode/Cisco-IOS-XR-ncs5500-coherent-portmode-oper:optics-name[Cisco-IOS-XR-ncs5500-coherent-portmode-oper:interface-name = ' + str(self.interface_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.interface_name is not None:
                return True

            if self.port_mode_info is not None and self.port_mode_info._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_portmode_oper as meta
            return meta._meta_table['ControllerPortMode.OpticsName']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs5500-coherent-portmode-oper:controller-port-mode'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.optics_name is not None:
            for child_ref in self.optics_name:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_portmode_oper as meta
        return meta._meta_table['ControllerPortMode']['meta_info']


