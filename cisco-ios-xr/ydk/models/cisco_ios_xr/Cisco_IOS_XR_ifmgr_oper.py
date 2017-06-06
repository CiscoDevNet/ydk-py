""" Cisco_IOS_XR_ifmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ifmgr package operational data.

This module contains definitions
for the following management objects\:
  interface\-dampening\: Interface dampening data
  interface\-properties\: interface properties

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ImStateEnumEnum(Enum):
    """
    ImStateEnumEnum

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = 0

    im_state_admin_down = 1

    im_state_down = 2

    im_state_up = 3

    im_state_shutdown = 4

    im_state_err_disable = 5

    im_state_down_immediate = 6

    im_state_down_immediate_admin = 7

    im_state_down_graceful = 8

    im_state_begin_shutdown = 9

    im_state_end_shutdown = 10

    im_state_begin_error_disable = 11

    im_state_end_error_disable = 12

    im_state_begin_down_graceful = 13

    im_state_reset = 14

    im_state_operational = 15

    im_state_not_operational = 16

    im_state_unknown = 17

    im_state_last = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
        return meta._meta_table['ImStateEnumEnum']



class InterfaceDampening(object):
    """
    Interface dampening data
    
    .. attribute:: interfaces
    
    	The interface list for which dampening info is available
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces>`
    
    .. attribute:: nodes
    
    	The location of the interface(s) being queried
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes>`
    
    

    """

    _prefix = 'ifmgr-oper'
    _revision = '2015-07-30'

    def __init__(self):
        self.interfaces = InterfaceDampening.Interfaces()
        self.interfaces.parent = self
        self.nodes = InterfaceDampening.Nodes()
        self.nodes.parent = self


    class Interfaces(object):
        """
        The interface list for which dampening info is
        available
        
        .. attribute:: interface
        
        	The interface for which dampening info is being queried
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            The interface for which dampening info is being
            queried
            
            .. attribute:: interface_name  <key>
            
            	The name of the
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: if_dampening
            
            	Dampening info for the interface
            	**type**\:   :py:class:`IfDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.if_dampening = InterfaceDampening.Interfaces.Interface.IfDampening()
                self.if_dampening.parent = self


            class IfDampening(object):
                """
                Dampening info for the interface
                
                .. attribute:: capsulation
                
                	Dampening information for capsulations
                	**type**\: list of    :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation>`
                
                .. attribute:: half_life
                
                	Configured decay half life in mins
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: interface_dampening
                
                	Interface dampening
                	**type**\:   :py:class:`InterfaceDampening_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_>`
                
                .. attribute:: is_dampening_enabled
                
                	Flag showing if dampening is enabled
                	**type**\:  bool
                
                .. attribute:: last_state_transition_time
                
                	The time elasped after the last state transition
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_suppress_time
                
                	Maximum suppress time in mins
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: restart_penalty
                
                	Configured restart penalty
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: reuse_threshold
                
                	Configured reuse threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_transition_count
                
                	The number of times the state has changed
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: suppress_threshold
                
                	Value of suppress threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.capsulation = YList()
                    self.capsulation.parent = self
                    self.capsulation.name = 'capsulation'
                    self.half_life = None
                    self.interface_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_()
                    self.interface_dampening.parent = self
                    self.is_dampening_enabled = None
                    self.last_state_transition_time = None
                    self.maximum_suppress_time = None
                    self.restart_penalty = None
                    self.reuse_threshold = None
                    self.state_transition_count = None
                    self.suppress_threshold = None


                class InterfaceDampening_(object):
                    """
                    Interface dampening
                    
                    .. attribute:: flaps
                    
                    	Number of underlying state flaps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_suppressed_enabled
                    
                    	Flag showing if state is suppressed
                    	**type**\:  bool
                    
                    .. attribute:: penalty
                    
                    	Dampening penalty of the interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_remaining
                    
                    	Remaining period of suppression in secs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: state
                    
                    	Underlying state of the node
                    	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.flaps = None
                        self.is_suppressed_enabled = None
                        self.penalty = None
                        self.seconds_remaining = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interface-dampening'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.flaps is not None:
                            return True

                        if self.is_suppressed_enabled is not None:
                            return True

                        if self.penalty is not None:
                            return True

                        if self.seconds_remaining is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                        return meta._meta_table['InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_']['meta_info']


                class Capsulation(object):
                    """
                    Dampening information for capsulations
                    
                    .. attribute:: capsulation_dampening
                    
                    	Capsulation dampening
                    	**type**\:   :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening>`
                    
                    .. attribute:: capsulation_number
                    
                    	Capsulation number
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.capsulation_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening()
                        self.capsulation_dampening.parent = self
                        self.capsulation_number = None


                    class CapsulationDampening(object):
                        """
                        Capsulation dampening
                        
                        .. attribute:: flaps
                        
                        	Number of underlying state flaps
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_suppressed_enabled
                        
                        	Flag showing if state is suppressed
                        	**type**\:  bool
                        
                        .. attribute:: penalty
                        
                        	Dampening penalty of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: seconds_remaining
                        
                        	Remaining period of suppression in secs
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: state
                        
                        	Underlying state of the node
                        	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.flaps = None
                            self.is_suppressed_enabled = None
                            self.penalty = None
                            self.seconds_remaining = None
                            self.state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:capsulation-dampening'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.flaps is not None:
                                return True

                            if self.is_suppressed_enabled is not None:
                                return True

                            if self.penalty is not None:
                                return True

                            if self.seconds_remaining is not None:
                                return True

                            if self.state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                            return meta._meta_table['InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:capsulation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.capsulation_dampening is not None and self.capsulation_dampening._has_data():
                            return True

                        if self.capsulation_number is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                        return meta._meta_table['InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:if-dampening'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.capsulation is not None:
                        for child_ref in self.capsulation:
                            if child_ref._has_data():
                                return True

                    if self.half_life is not None:
                        return True

                    if self.interface_dampening is not None and self.interface_dampening._has_data():
                        return True

                    if self.is_dampening_enabled is not None:
                        return True

                    if self.last_state_transition_time is not None:
                        return True

                    if self.maximum_suppress_time is not None:
                        return True

                    if self.restart_penalty is not None:
                        return True

                    if self.reuse_threshold is not None:
                        return True

                    if self.state_transition_count is not None:
                        return True

                    if self.suppress_threshold is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                    return meta._meta_table['InterfaceDampening.Interfaces.Interface.IfDampening']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-ifmgr-oper:interface-dampening/Cisco-IOS-XR-ifmgr-oper:interfaces/Cisco-IOS-XR-ifmgr-oper:interface[Cisco-IOS-XR-ifmgr-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.if_dampening is not None and self.if_dampening._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                return meta._meta_table['InterfaceDampening.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ifmgr-oper:interface-dampening/Cisco-IOS-XR-ifmgr-oper:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
            return meta._meta_table['InterfaceDampening.Interfaces']['meta_info']


    class Nodes(object):
        """
        The location of the interface(s) being queried
        
        .. attribute:: node
        
        	The location of the interface(s) being queried
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            The location of the interface(s) being queried
            
            .. attribute:: node_name  <key>
            
            	The location of the interface(s)
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: show
            
            	Show details for the interfaces
            	**type**\:   :py:class:`Show <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.show = InterfaceDampening.Nodes.Node.Show()
                self.show.parent = self


            class Show(object):
                """
                Show details for the interfaces
                
                .. attribute:: dampening
                
                	Dampening information of the interface(s) being queried
                	**type**\:   :py:class:`Dampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.dampening = InterfaceDampening.Nodes.Node.Show.Dampening()
                    self.dampening.parent = self


                class Dampening(object):
                    """
                    Dampening information of the interface(s)
                    being queried
                    
                    .. attribute:: if_handles
                    
                    	Interface handle for which dampening info queried
                    	**type**\:   :py:class:`IfHandles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles>`
                    
                    .. attribute:: interfaces
                    
                    	Table of interfaces for which dampening info can be queried
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.if_handles = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles()
                        self.if_handles.parent = self
                        self.interfaces = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces()
                        self.interfaces.parent = self


                    class IfHandles(object):
                        """
                        Interface handle for which dampening info
                        queried
                        
                        .. attribute:: if_handle
                        
                        	Dampening info for the interface handle
                        	**type**\: list of    :py:class:`IfHandle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.if_handle = YList()
                            self.if_handle.parent = self
                            self.if_handle.name = 'if_handle'


                        class IfHandle(object):
                            """
                            Dampening info for the interface handle
                            
                            .. attribute:: interface_handle_name  <key>
                            
                            	The interface handle
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: capsulation
                            
                            	Dampening information for capsulations
                            	**type**\: list of    :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation>`
                            
                            .. attribute:: half_life
                            
                            	Configured decay half life in mins
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: interface_dampening
                            
                            	Interface dampening
                            	**type**\:   :py:class:`InterfaceDampening_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_>`
                            
                            .. attribute:: is_dampening_enabled
                            
                            	Flag showing if dampening is enabled
                            	**type**\:  bool
                            
                            .. attribute:: last_state_transition_time
                            
                            	The time elasped after the last state transition
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum_suppress_time
                            
                            	Maximum suppress time in mins
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: restart_penalty
                            
                            	Configured restart penalty
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reuse_threshold
                            
                            	Configured reuse threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state_transition_count
                            
                            	The number of times the state has changed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suppress_threshold
                            
                            	Value of suppress threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.interface_handle_name = None
                                self.capsulation = YList()
                                self.capsulation.parent = self
                                self.capsulation.name = 'capsulation'
                                self.half_life = None
                                self.interface_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_()
                                self.interface_dampening.parent = self
                                self.is_dampening_enabled = None
                                self.last_state_transition_time = None
                                self.maximum_suppress_time = None
                                self.restart_penalty = None
                                self.reuse_threshold = None
                                self.state_transition_count = None
                                self.suppress_threshold = None


                            class InterfaceDampening_(object):
                                """
                                Interface dampening
                                
                                .. attribute:: flaps
                                
                                	Number of underlying state flaps
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_suppressed_enabled
                                
                                	Flag showing if state is suppressed
                                	**type**\:  bool
                                
                                .. attribute:: penalty
                                
                                	Dampening penalty of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: seconds_remaining
                                
                                	Remaining period of suppression in secs
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: state
                                
                                	Underlying state of the node
                                	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    self.parent = None
                                    self.flaps = None
                                    self.is_suppressed_enabled = None
                                    self.penalty = None
                                    self.seconds_remaining = None
                                    self.state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interface-dampening'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.flaps is not None:
                                        return True

                                    if self.is_suppressed_enabled is not None:
                                        return True

                                    if self.penalty is not None:
                                        return True

                                    if self.seconds_remaining is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                    return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_']['meta_info']


                            class Capsulation(object):
                                """
                                Dampening information for capsulations
                                
                                .. attribute:: capsulation_dampening
                                
                                	Capsulation dampening
                                	**type**\:   :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening>`
                                
                                .. attribute:: capsulation_number
                                
                                	Capsulation number
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    self.parent = None
                                    self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening()
                                    self.capsulation_dampening.parent = self
                                    self.capsulation_number = None


                                class CapsulationDampening(object):
                                    """
                                    Capsulation dampening
                                    
                                    .. attribute:: flaps
                                    
                                    	Number of underlying state flaps
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_suppressed_enabled
                                    
                                    	Flag showing if state is suppressed
                                    	**type**\:  bool
                                    
                                    .. attribute:: penalty
                                    
                                    	Dampening penalty of the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: seconds_remaining
                                    
                                    	Remaining period of suppression in secs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: state
                                    
                                    	Underlying state of the node
                                    	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ifmgr-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        self.parent = None
                                        self.flaps = None
                                        self.is_suppressed_enabled = None
                                        self.penalty = None
                                        self.seconds_remaining = None
                                        self.state = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:capsulation-dampening'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.flaps is not None:
                                            return True

                                        if self.is_suppressed_enabled is not None:
                                            return True

                                        if self.penalty is not None:
                                            return True

                                        if self.seconds_remaining is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                        return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:capsulation'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.capsulation_dampening is not None and self.capsulation_dampening._has_data():
                                        return True

                                    if self.capsulation_number is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                    return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_handle_name is None:
                                    raise YPYModelError('Key property interface_handle_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:if-handle[Cisco-IOS-XR-ifmgr-oper:interface-handle-name = ' + str(self.interface_handle_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_handle_name is not None:
                                    return True

                                if self.capsulation is not None:
                                    for child_ref in self.capsulation:
                                        if child_ref._has_data():
                                            return True

                                if self.half_life is not None:
                                    return True

                                if self.interface_dampening is not None and self.interface_dampening._has_data():
                                    return True

                                if self.is_dampening_enabled is not None:
                                    return True

                                if self.last_state_transition_time is not None:
                                    return True

                                if self.maximum_suppress_time is not None:
                                    return True

                                if self.restart_penalty is not None:
                                    return True

                                if self.reuse_threshold is not None:
                                    return True

                                if self.state_transition_count is not None:
                                    return True

                                if self.suppress_threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:if-handles'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.if_handle is not None:
                                for child_ref in self.if_handle:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                            return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles']['meta_info']


                    class Interfaces(object):
                        """
                        Table of interfaces for which dampening info
                        can be queried
                        
                        .. attribute:: interface
                        
                        	Dampening info for the interface
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.interface = YList()
                            self.interface.parent = self
                            self.interface.name = 'interface'


                        class Interface(object):
                            """
                            Dampening info for the interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: capsulation
                            
                            	Dampening information for capsulations
                            	**type**\: list of    :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation>`
                            
                            .. attribute:: half_life
                            
                            	Configured decay half life in mins
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: interface_dampening
                            
                            	Interface dampening
                            	**type**\:   :py:class:`InterfaceDampening_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_>`
                            
                            .. attribute:: is_dampening_enabled
                            
                            	Flag showing if dampening is enabled
                            	**type**\:  bool
                            
                            .. attribute:: last_state_transition_time
                            
                            	The time elasped after the last state transition
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum_suppress_time
                            
                            	Maximum suppress time in mins
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: restart_penalty
                            
                            	Configured restart penalty
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reuse_threshold
                            
                            	Configured reuse threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state_transition_count
                            
                            	The number of times the state has changed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suppress_threshold
                            
                            	Value of suppress threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.capsulation = YList()
                                self.capsulation.parent = self
                                self.capsulation.name = 'capsulation'
                                self.half_life = None
                                self.interface_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_()
                                self.interface_dampening.parent = self
                                self.is_dampening_enabled = None
                                self.last_state_transition_time = None
                                self.maximum_suppress_time = None
                                self.restart_penalty = None
                                self.reuse_threshold = None
                                self.state_transition_count = None
                                self.suppress_threshold = None


                            class InterfaceDampening_(object):
                                """
                                Interface dampening
                                
                                .. attribute:: flaps
                                
                                	Number of underlying state flaps
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_suppressed_enabled
                                
                                	Flag showing if state is suppressed
                                	**type**\:  bool
                                
                                .. attribute:: penalty
                                
                                	Dampening penalty of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: seconds_remaining
                                
                                	Remaining period of suppression in secs
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: state
                                
                                	Underlying state of the node
                                	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    self.parent = None
                                    self.flaps = None
                                    self.is_suppressed_enabled = None
                                    self.penalty = None
                                    self.seconds_remaining = None
                                    self.state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interface-dampening'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.flaps is not None:
                                        return True

                                    if self.is_suppressed_enabled is not None:
                                        return True

                                    if self.penalty is not None:
                                        return True

                                    if self.seconds_remaining is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                    return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_']['meta_info']


                            class Capsulation(object):
                                """
                                Dampening information for capsulations
                                
                                .. attribute:: capsulation_dampening
                                
                                	Capsulation dampening
                                	**type**\:   :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening>`
                                
                                .. attribute:: capsulation_number
                                
                                	Capsulation number
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    self.parent = None
                                    self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening()
                                    self.capsulation_dampening.parent = self
                                    self.capsulation_number = None


                                class CapsulationDampening(object):
                                    """
                                    Capsulation dampening
                                    
                                    .. attribute:: flaps
                                    
                                    	Number of underlying state flaps
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_suppressed_enabled
                                    
                                    	Flag showing if state is suppressed
                                    	**type**\:  bool
                                    
                                    .. attribute:: penalty
                                    
                                    	Dampening penalty of the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: seconds_remaining
                                    
                                    	Remaining period of suppression in secs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: state
                                    
                                    	Underlying state of the node
                                    	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ifmgr-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        self.parent = None
                                        self.flaps = None
                                        self.is_suppressed_enabled = None
                                        self.penalty = None
                                        self.seconds_remaining = None
                                        self.state = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:capsulation-dampening'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.flaps is not None:
                                            return True

                                        if self.is_suppressed_enabled is not None:
                                            return True

                                        if self.penalty is not None:
                                            return True

                                        if self.seconds_remaining is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                        return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:capsulation'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.capsulation_dampening is not None and self.capsulation_dampening._has_data():
                                        return True

                                    if self.capsulation_number is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                    return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYModelError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interface[Cisco-IOS-XR-ifmgr-oper:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_name is not None:
                                    return True

                                if self.capsulation is not None:
                                    for child_ref in self.capsulation:
                                        if child_ref._has_data():
                                            return True

                                if self.half_life is not None:
                                    return True

                                if self.interface_dampening is not None and self.interface_dampening._has_data():
                                    return True

                                if self.is_dampening_enabled is not None:
                                    return True

                                if self.last_state_transition_time is not None:
                                    return True

                                if self.maximum_suppress_time is not None:
                                    return True

                                if self.restart_penalty is not None:
                                    return True

                                if self.reuse_threshold is not None:
                                    return True

                                if self.state_transition_count is not None:
                                    return True

                                if self.suppress_threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface is not None:
                                for child_ref in self.interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                            return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:dampening'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.if_handles is not None and self.if_handles._has_data():
                            return True

                        if self.interfaces is not None and self.interfaces._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                        return meta._meta_table['InterfaceDampening.Nodes.Node.Show.Dampening']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:show'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.dampening is not None and self.dampening._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                    return meta._meta_table['InterfaceDampening.Nodes.Node.Show']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ifmgr-oper:interface-dampening/Cisco-IOS-XR-ifmgr-oper:nodes/Cisco-IOS-XR-ifmgr-oper:node[Cisco-IOS-XR-ifmgr-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.show is not None and self.show._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                return meta._meta_table['InterfaceDampening.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ifmgr-oper:interface-dampening/Cisco-IOS-XR-ifmgr-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
            return meta._meta_table['InterfaceDampening.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ifmgr-oper:interface-dampening'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
        return meta._meta_table['InterfaceDampening']['meta_info']


class InterfaceProperties(object):
    """
    interface properties
    
    .. attribute:: data_nodes
    
    	Operational data for interfaces
    	**type**\:   :py:class:`DataNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes>`
    
    

    """

    _prefix = 'ifmgr-oper'
    _revision = '2015-07-30'

    def __init__(self):
        self.data_nodes = InterfaceProperties.DataNodes()
        self.data_nodes.parent = self


    class DataNodes(object):
        """
        Operational data for interfaces
        
        .. attribute:: data_node
        
        	The location of a (D)RP in the same LR as the interface being queried
        	**type**\: list of    :py:class:`DataNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.data_node = YList()
            self.data_node.parent = self
            self.data_node.name = 'data_node'


        class DataNode(object):
            """
            The location of a (D)RP in the same LR as the
            interface being queried
            
            .. attribute:: data_node_name  <key>
            
            	The location of the (D)RP
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: locationviews
            
            	Location\-specific view of interface operational data
            	**type**\:   :py:class:`Locationviews <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews>`
            
            .. attribute:: pq_node_locations
            
            	Partially qualified Location\-specific view of interface operational data
            	**type**\:   :py:class:`PqNodeLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations>`
            
            .. attribute:: system_view
            
            	System\-wide view of interface operational data
            	**type**\:   :py:class:`SystemView <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.data_node_name = None
                self.locationviews = InterfaceProperties.DataNodes.DataNode.Locationviews()
                self.locationviews.parent = self
                self.pq_node_locations = InterfaceProperties.DataNodes.DataNode.PqNodeLocations()
                self.pq_node_locations.parent = self
                self.system_view = InterfaceProperties.DataNodes.DataNode.SystemView()
                self.system_view.parent = self


            class Locationviews(object):
                """
                Location\-specific view of interface
                operational data
                
                .. attribute:: locationview
                
                	Operational data for all interfaces and controllers on a particular node
                	**type**\: list of    :py:class:`Locationview <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.locationview = YList()
                    self.locationview.parent = self
                    self.locationview.name = 'locationview'


                class Locationview(object):
                    """
                    Operational data for all interfaces and
                    controllers on a particular node
                    
                    .. attribute:: locationview_name  <key>
                    
                    	The location to filter on
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: interfaces
                    
                    	Operational data for all interfaces and controllers
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.locationview_name = None
                        self.interfaces = InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces()
                        self.interfaces.parent = self


                    class Interfaces(object):
                        """
                        Operational data for all interfaces and
                        controllers
                        
                        .. attribute:: interface
                        
                        	The operational attributes for a particular interface
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.interface = YList()
                            self.interface.parent = self
                            self.interface.name = 'interface'


                        class Interface(object):
                            """
                            The operational attributes for a particular
                            interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: actual_line_state
                            
                            	Line protocol state with no translation of error disable or shutdown
                            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                            
                            .. attribute:: actual_state
                            
                            	Operational state with no translation of error disable or shutdown
                            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                            
                            .. attribute:: bandwidth
                            
                            	Interface bandwidth (Kb/s)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: encapsulation
                            
                            	Interface encapsulation
                            	**type**\:  str
                            
                            .. attribute:: encapsulation_type_string
                            
                            	Interface encapsulation description string
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            .. attribute:: interface
                            
                            	Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: l2_transport
                            
                            	L2 transport
                            	**type**\:  bool
                            
                            .. attribute:: line_state
                            
                            	Line protocol state
                            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                            
                            .. attribute:: mtu
                            
                            	MTU in bytes
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: parent_interface
                            
                            	Parent Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: state
                            
                            	Operational state
                            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                            
                            .. attribute:: sub_interface_mtu_overhead
                            
                            	Subif MTU overhead
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Interface type
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.actual_line_state = None
                                self.actual_state = None
                                self.bandwidth = None
                                self.encapsulation = None
                                self.encapsulation_type_string = None
                                self.interface = None
                                self.l2_transport = None
                                self.line_state = None
                                self.mtu = None
                                self.parent_interface = None
                                self.state = None
                                self.sub_interface_mtu_overhead = None
                                self.type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYModelError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interface[Cisco-IOS-XR-ifmgr-oper:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_name is not None:
                                    return True

                                if self.actual_line_state is not None:
                                    return True

                                if self.actual_state is not None:
                                    return True

                                if self.bandwidth is not None:
                                    return True

                                if self.encapsulation is not None:
                                    return True

                                if self.encapsulation_type_string is not None:
                                    return True

                                if self.interface is not None:
                                    return True

                                if self.l2_transport is not None:
                                    return True

                                if self.line_state is not None:
                                    return True

                                if self.mtu is not None:
                                    return True

                                if self.parent_interface is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                if self.sub_interface_mtu_overhead is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                return meta._meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface is not None:
                                for child_ref in self.interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                            return meta._meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.locationview_name is None:
                            raise YPYModelError('Key property locationview_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:locationview[Cisco-IOS-XR-ifmgr-oper:locationview-name = ' + str(self.locationview_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.locationview_name is not None:
                            return True

                        if self.interfaces is not None and self.interfaces._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                        return meta._meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:locationviews'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.locationview is not None:
                        for child_ref in self.locationview:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                    return meta._meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews']['meta_info']


            class PqNodeLocations(object):
                """
                Partially qualified Location\-specific view of
                interface operational data
                
                .. attribute:: pq_node_location
                
                	Operational data for all interfaces and controllers on a particular pq\_node
                	**type**\: list of    :py:class:`PqNodeLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.pq_node_location = YList()
                    self.pq_node_location.parent = self
                    self.pq_node_location.name = 'pq_node_location'


                class PqNodeLocation(object):
                    """
                    Operational data for all interfaces and
                    controllers on a particular pq\_node
                    
                    .. attribute:: pq_node_name  <key>
                    
                    	The partially qualified location to filter on
                    	**type**\:  str
                    
                    	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
                    
                    .. attribute:: interfaces
                    
                    	Operational data for all interfaces and controllers
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.pq_node_name = None
                        self.interfaces = InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces()
                        self.interfaces.parent = self


                    class Interfaces(object):
                        """
                        Operational data for all interfaces and
                        controllers
                        
                        .. attribute:: interface
                        
                        	The operational attributes for a particular interface
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.interface = YList()
                            self.interface.parent = self
                            self.interface.name = 'interface'


                        class Interface(object):
                            """
                            The operational attributes for a particular
                            interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: actual_line_state
                            
                            	Line protocol state with no translation of error disable or shutdown
                            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                            
                            .. attribute:: actual_state
                            
                            	Operational state with no translation of error disable or shutdown
                            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                            
                            .. attribute:: bandwidth
                            
                            	Interface bandwidth (Kb/s)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: encapsulation
                            
                            	Interface encapsulation
                            	**type**\:  str
                            
                            .. attribute:: encapsulation_type_string
                            
                            	Interface encapsulation description string
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            .. attribute:: interface
                            
                            	Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: l2_transport
                            
                            	L2 transport
                            	**type**\:  bool
                            
                            .. attribute:: line_state
                            
                            	Line protocol state
                            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                            
                            .. attribute:: mtu
                            
                            	MTU in bytes
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: parent_interface
                            
                            	Parent Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: state
                            
                            	Operational state
                            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                            
                            .. attribute:: sub_interface_mtu_overhead
                            
                            	Subif MTU overhead
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Interface type
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.actual_line_state = None
                                self.actual_state = None
                                self.bandwidth = None
                                self.encapsulation = None
                                self.encapsulation_type_string = None
                                self.interface = None
                                self.l2_transport = None
                                self.line_state = None
                                self.mtu = None
                                self.parent_interface = None
                                self.state = None
                                self.sub_interface_mtu_overhead = None
                                self.type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYModelError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interface[Cisco-IOS-XR-ifmgr-oper:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_name is not None:
                                    return True

                                if self.actual_line_state is not None:
                                    return True

                                if self.actual_state is not None:
                                    return True

                                if self.bandwidth is not None:
                                    return True

                                if self.encapsulation is not None:
                                    return True

                                if self.encapsulation_type_string is not None:
                                    return True

                                if self.interface is not None:
                                    return True

                                if self.l2_transport is not None:
                                    return True

                                if self.line_state is not None:
                                    return True

                                if self.mtu is not None:
                                    return True

                                if self.parent_interface is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                if self.sub_interface_mtu_overhead is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                                return meta._meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface is not None:
                                for child_ref in self.interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                            return meta._meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.pq_node_name is None:
                            raise YPYModelError('Key property pq_node_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:pq-node-location[Cisco-IOS-XR-ifmgr-oper:pq-node-name = ' + str(self.pq_node_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pq_node_name is not None:
                            return True

                        if self.interfaces is not None and self.interfaces._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                        return meta._meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:pq-node-locations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.pq_node_location is not None:
                        for child_ref in self.pq_node_location:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                    return meta._meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations']['meta_info']


            class SystemView(object):
                """
                System\-wide view of interface operational data
                
                .. attribute:: interfaces
                
                	Operational data for all interfaces and controllers
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.interfaces = InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces()
                    self.interfaces.parent = self


                class Interfaces(object):
                    """
                    Operational data for all interfaces and
                    controllers
                    
                    .. attribute:: interface
                    
                    	The operational attributes for a particular interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        The operational attributes for a particular
                        interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	The name of the interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: actual_line_state
                        
                        	Line protocol state with no translation of error disable or shutdown
                        	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                        
                        .. attribute:: actual_state
                        
                        	Operational state with no translation of error disable or shutdown
                        	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                        
                        .. attribute:: bandwidth
                        
                        	Interface bandwidth (Kb/s)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: encapsulation
                        
                        	Interface encapsulation
                        	**type**\:  str
                        
                        .. attribute:: encapsulation_type_string
                        
                        	Interface encapsulation description string
                        	**type**\:  str
                        
                        	**length:** 0..32
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: l2_transport
                        
                        	L2 transport
                        	**type**\:  bool
                        
                        .. attribute:: line_state
                        
                        	Line protocol state
                        	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                        
                        .. attribute:: mtu
                        
                        	MTU in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: parent_interface
                        
                        	Parent Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: state
                        
                        	Operational state
                        	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnumEnum>`
                        
                        .. attribute:: sub_interface_mtu_overhead
                        
                        	Subif MTU overhead
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Interface type
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.actual_line_state = None
                            self.actual_state = None
                            self.bandwidth = None
                            self.encapsulation = None
                            self.encapsulation_type_string = None
                            self.interface = None
                            self.l2_transport = None
                            self.line_state = None
                            self.mtu = None
                            self.parent_interface = None
                            self.state = None
                            self.sub_interface_mtu_overhead = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interface[Cisco-IOS-XR-ifmgr-oper:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.actual_line_state is not None:
                                return True

                            if self.actual_state is not None:
                                return True

                            if self.bandwidth is not None:
                                return True

                            if self.encapsulation is not None:
                                return True

                            if self.encapsulation_type_string is not None:
                                return True

                            if self.interface is not None:
                                return True

                            if self.l2_transport is not None:
                                return True

                            if self.line_state is not None:
                                return True

                            if self.mtu is not None:
                                return True

                            if self.parent_interface is not None:
                                return True

                            if self.state is not None:
                                return True

                            if self.sub_interface_mtu_overhead is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                            return meta._meta_table['InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            for child_ref in self.interface:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                        return meta._meta_table['InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ifmgr-oper:system-view'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                    return meta._meta_table['InterfaceProperties.DataNodes.DataNode.SystemView']['meta_info']

            @property
            def _common_path(self):
                if self.data_node_name is None:
                    raise YPYModelError('Key property data_node_name is None')

                return '/Cisco-IOS-XR-ifmgr-oper:interface-properties/Cisco-IOS-XR-ifmgr-oper:data-nodes/Cisco-IOS-XR-ifmgr-oper:data-node[Cisco-IOS-XR-ifmgr-oper:data-node-name = ' + str(self.data_node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.data_node_name is not None:
                    return True

                if self.locationviews is not None and self.locationviews._has_data():
                    return True

                if self.pq_node_locations is not None and self.pq_node_locations._has_data():
                    return True

                if self.system_view is not None and self.system_view._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
                return meta._meta_table['InterfaceProperties.DataNodes.DataNode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ifmgr-oper:interface-properties/Cisco-IOS-XR-ifmgr-oper:data-nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.data_node is not None:
                for child_ref in self.data_node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
            return meta._meta_table['InterfaceProperties.DataNodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ifmgr-oper:interface-properties'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.data_nodes is not None and self.data_nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ifmgr_oper as meta
        return meta._meta_table['InterfaceProperties']['meta_info']


