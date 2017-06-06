""" Cisco_IOS_XR_mystique_ots_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mystique\-ots package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: NCS1k HW module config

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class OtsAmplifierGridModeEnum(Enum):
    """
    OtsAmplifierGridModeEnum

    Ots amplifier grid mode

    .. data:: Y_100g_hz = 0

    	100GHz mode

    .. data:: Y_50g_hz = 1

    	50GHz mode

    .. data:: gr_idle_ss = 2

    	Gridless mode

    """

    Y_100g_hz = 0

    Y_50g_hz = 1

    gr_idle_ss = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
        return meta._meta_table['OtsAmplifierGridModeEnum']


class OtsAmplifierNodeEnum(Enum):
    """
    OtsAmplifierNodeEnum

    Ots amplifier node

    .. data:: term = 0

    	Nodetype TERM

    .. data:: ila = 1

    	Nodetype InLine Amplifier

    .. data:: roadm = 2

    	Nodetype ROADM

    """

    term = 0

    ila = 1

    roadm = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
        return meta._meta_table['OtsAmplifierNodeEnum']


class OtsPsmLockoutFromEnum(Enum):
    """
    OtsPsmLockoutFromEnum

    Ots psm lockout from

    .. data:: working = 1

    	Working port

    .. data:: protected = 2

    	Protected port

    """

    working = 1

    protected = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
        return meta._meta_table['OtsPsmLockoutFromEnum']


class OtsPsmManualSwitchEnum(Enum):
    """
    OtsPsmManualSwitchEnum

    Ots psm manual switch

    .. data:: working = 1

    	Working port

    .. data:: protected = 2

    	Protected port

    """

    working = 1

    protected = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
        return meta._meta_table['OtsPsmManualSwitchEnum']



class HardwareModule(object):
    """
    NCS1k HW module config
    
    .. attribute:: node
    
    	Node
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg.HardwareModule.Node>`
    
    

    """

    _prefix = 'mystique-ots-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.node = YList()
        self.node.parent = self
        self.node.name = 'node'


    class Node(object):
        """
        Node
        
        .. attribute:: location  <key>
        
        	Fully qualified line card specification
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: slot
        
        	Slot Id
        	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg.HardwareModule.Node.Slot>`
        
        

        """

        _prefix = 'mystique-ots-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.location = None
            self.slot = YList()
            self.slot.parent = self
            self.slot.name = 'slot'


        class Slot(object):
            """
            Slot Id
            
            .. attribute:: slot_id  <key>
            
            	Set Slot
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: amplifier
            
            	Amplifier Configs
            	**type**\:   :py:class:`Amplifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg.HardwareModule.Node.Slot.Amplifier>`
            
            .. attribute:: psm
            
            	PSM Configs
            	**type**\:   :py:class:`Psm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg.HardwareModule.Node.Slot.Psm>`
            
            

            """

            _prefix = 'mystique-ots-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.slot_id = None
                self.amplifier = HardwareModule.Node.Slot.Amplifier()
                self.amplifier.parent = self
                self.psm = HardwareModule.Node.Slot.Psm()
                self.psm.parent = self


            class Amplifier(object):
                """
                Amplifier Configs
                
                .. attribute:: grid_mode
                
                	Define the working mode for the optical module
                	**type**\:   :py:class:`OtsAmplifierGridModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg.OtsAmplifierGridModeEnum>`
                
                .. attribute:: node_type
                
                	Define the type of node in which the amplifier is set to work
                	**type**\:   :py:class:`OtsAmplifierNodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg.OtsAmplifierNodeEnum>`
                
                .. attribute:: udc_vlan
                
                	Define the VLAN ID in range <2\-4080>
                	**type**\:  int
                
                	**range:** 2..4080
                
                

                """

                _prefix = 'mystique-ots-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.grid_mode = None
                    self.node_type = None
                    self.udc_vlan = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mystique-ots-cfg:amplifier'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.grid_mode is not None:
                        return True

                    if self.node_type is not None:
                        return True

                    if self.udc_vlan is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
                    return meta._meta_table['HardwareModule.Node.Slot.Amplifier']['meta_info']


            class Psm(object):
                """
                PSM Configs
                
                .. attribute:: lockout_from
                
                	Exclude selected port from protection
                	**type**\:   :py:class:`OtsPsmLockoutFromEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg.OtsPsmLockoutFromEnum>`
                
                .. attribute:: manual_switch_to
                
                	Switch active path on selected port
                	**type**\:   :py:class:`OtsPsmManualSwitchEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg.OtsPsmManualSwitchEnum>`
                
                

                """

                _prefix = 'mystique-ots-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lockout_from = None
                    self.manual_switch_to = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mystique-ots-cfg:psm'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lockout_from is not None:
                        return True

                    if self.manual_switch_to is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
                    return meta._meta_table['HardwareModule.Node.Slot.Psm']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.slot_id is None:
                    raise YPYModelError('Key property slot_id is None')

                return self.parent._common_path +'/Cisco-IOS-XR-mystique-ots-cfg:slot[Cisco-IOS-XR-mystique-ots-cfg:slot-id = ' + str(self.slot_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.slot_id is not None:
                    return True

                if self.amplifier is not None and self.amplifier._has_data():
                    return True

                if self.psm is not None and self.psm._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
                return meta._meta_table['HardwareModule.Node.Slot']['meta_info']

        @property
        def _common_path(self):
            if self.location is None:
                raise YPYModelError('Key property location is None')

            return '/Cisco-IOS-XR-mystique-ots-cfg:hardware-module/Cisco-IOS-XR-mystique-ots-cfg:node[Cisco-IOS-XR-mystique-ots-cfg:location = ' + str(self.location) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.location is not None:
                return True

            if self.slot is not None:
                for child_ref in self.slot:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
            return meta._meta_table['HardwareModule.Node']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mystique-ots-cfg:hardware-module'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.node is not None:
            for child_ref in self.node:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mystique_ots_cfg as meta
        return meta._meta_table['HardwareModule']['meta_info']


