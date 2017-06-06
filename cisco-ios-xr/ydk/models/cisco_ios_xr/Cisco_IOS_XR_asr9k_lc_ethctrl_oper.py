""" Cisco_IOS_XR_asr9k_lc_ethctrl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-ethctrl package operational data.

This module contains definitions
for the following management objects\:
  mlan\: Management LAN Operational data space

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Mlan(object):
    """
    Management LAN Operational data space
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-ethctrl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Mlan.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-ethctrl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Number
            
            .. attribute:: node  <key>
            
            	node number
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: atu_entry_numbers
            
            	Table of switch ATU
            	**type**\:   :py:class:`AtuEntryNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers>`
            
            .. attribute:: port_counters_numbers
            
            	Table of port counters
            	**type**\:   :py:class:`PortCountersNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers>`
            
            .. attribute:: port_status_numbers
            
            	Table of port status
            	**type**\:   :py:class:`PortStatusNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers>`
            
            .. attribute:: switch_status_table
            
            	Table of switch status
            	**type**\:   :py:class:`SwitchStatusTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable>`
            
            

            """

            _prefix = 'asr9k-lc-ethctrl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = None
                self.atu_entry_numbers = Mlan.Nodes.Node.AtuEntryNumbers()
                self.atu_entry_numbers.parent = self
                self.port_counters_numbers = Mlan.Nodes.Node.PortCountersNumbers()
                self.port_counters_numbers.parent = self
                self.port_status_numbers = Mlan.Nodes.Node.PortStatusNumbers()
                self.port_status_numbers.parent = self
                self.switch_status_table = Mlan.Nodes.Node.SwitchStatusTable()
                self.switch_status_table.parent = self


            class PortStatusNumbers(object):
                """
                Table of port status
                
                .. attribute:: port_status_number
                
                	Number
                	**type**\: list of    :py:class:`PortStatusNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.port_status_number = YList()
                    self.port_status_number.parent = self
                    self.port_status_number.name = 'port_status_number'


                class PortStatusNumber(object):
                    """
                    Number
                    
                    .. attribute:: number  <key>
                    
                    	port number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: port_status
                    
                    	mlan port status info
                    	**type**\:   :py:class:`PortStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.number = None
                        self.port_status = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus()
                        self.port_status.parent = self


                    class PortStatus(object):
                        """
                        mlan port status info
                        
                        .. attribute:: config
                        
                        	Configuration Data
                        	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config>`
                        
                        .. attribute:: mac
                        
                        	MAC Registers
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac>`
                        
                        .. attribute:: mac_valid
                        
                        	MAC data valid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: phy
                        
                        	PHY Registers
                        	**type**\:   :py:class:`Phy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy>`
                        
                        .. attribute:: phy_valid
                        
                        	PHY data valid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_num
                        
                        	Port Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: serdes
                        
                        	SERDES Registers
                        	**type**\:   :py:class:`Serdes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes>`
                        
                        .. attribute:: serdes_valid
                        
                        	SERDES data valid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.config = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config()
                            self.config.parent = self
                            self.mac = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac()
                            self.mac.parent = self
                            self.mac_valid = None
                            self.phy = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy()
                            self.phy.parent = self
                            self.phy_valid = None
                            self.port_num = None
                            self.serdes = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes()
                            self.serdes.parent = self
                            self.serdes_valid = None


                        class Config(object):
                            """
                            Configuration Data
                            
                            .. attribute:: duplex
                            
                            	duplex
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: loopback
                            
                            	loopback
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: my_pause
                            
                            	myPause
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: pause
                            
                            	pauseEn
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: speed
                            
                            	speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.duplex = None
                                self.loopback = None
                                self.my_pause = None
                                self.pause = None
                                self.speed = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.duplex is not None:
                                    return True

                                if self.loopback is not None:
                                    return True

                                if self.my_pause is not None:
                                    return True

                                if self.pause is not None:
                                    return True

                                if self.speed is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                                return meta._meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config']['meta_info']


                        class Phy(object):
                            """
                            PHY Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\:  list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.reg = YLeafList()
                                self.reg.parent = self
                                self.reg.name = 'reg'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:phy'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.reg is not None:
                                    for child in self.reg:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                                return meta._meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy']['meta_info']


                        class Serdes(object):
                            """
                            SERDES Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\:  list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.reg = YLeafList()
                                self.reg.parent = self
                                self.reg.name = 'reg'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:serdes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.reg is not None:
                                    for child in self.reg:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                                return meta._meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes']['meta_info']


                        class Mac(object):
                            """
                            MAC Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\:  list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.reg = YLeafList()
                                self.reg.parent = self
                                self.reg.name = 'reg'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mac'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.reg is not None:
                                    for child in self.reg:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                                return meta._meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:port-status'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.mac is not None and self.mac._has_data():
                                return True

                            if self.mac_valid is not None:
                                return True

                            if self.phy is not None and self.phy._has_data():
                                return True

                            if self.phy_valid is not None:
                                return True

                            if self.port_num is not None:
                                return True

                            if self.serdes is not None and self.serdes._has_data():
                                return True

                            if self.serdes_valid is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                            return meta._meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:port-status-number[Cisco-IOS-XR-asr9k-lc-ethctrl-oper:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.number is not None:
                            return True

                        if self.port_status is not None and self.port_status._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                        return meta._meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:port-status-numbers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.port_status_number is not None:
                        for child_ref in self.port_status_number:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                    return meta._meta_table['Mlan.Nodes.Node.PortStatusNumbers']['meta_info']


            class SwitchStatusTable(object):
                """
                Table of switch status
                
                .. attribute:: switch_status
                
                	mlan switch status info
                	**type**\:   :py:class:`SwitchStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.switch_status = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus()
                    self.switch_status.parent = self


                class SwitchStatus(object):
                    """
                    mlan switch status info
                    
                    .. attribute:: rate_limit
                    
                    	CPU Interface Rate Limit
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: sw_reg_1
                    
                    	Switch Global Registers
                    	**type**\:   :py:class:`SwReg1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1>`
                    
                    .. attribute:: sw_reg_2
                    
                    	Switch Global Registers
                    	**type**\:   :py:class:`SwReg2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2>`
                    
                    .. attribute:: sw_status
                    
                    	Switch Status Data
                    	**type**\:   :py:class:`SwStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.rate_limit = None
                        self.sw_reg_1 = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1()
                        self.sw_reg_1.parent = self
                        self.sw_reg_2 = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2()
                        self.sw_reg_2.parent = self
                        self.sw_status = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus()
                        self.sw_status.parent = self


                    class SwReg1(object):
                        """
                        Switch Global Registers
                        
                        .. attribute:: reg
                        
                        	reg
                        	**type**\:  list of int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reg = YLeafList()
                            self.reg.parent = self
                            self.reg.name = 'reg'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:sw-reg-1'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reg is not None:
                                for child in self.reg:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                            return meta._meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1']['meta_info']


                    class SwReg2(object):
                        """
                        Switch Global Registers
                        
                        .. attribute:: reg
                        
                        	reg
                        	**type**\:  list of int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reg = YLeafList()
                            self.reg.parent = self
                            self.reg.name = 'reg'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:sw-reg-2'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reg is not None:
                                for child in self.reg:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                            return meta._meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2']['meta_info']


                    class SwStatus(object):
                        """
                        Switch Status Data
                        
                        .. attribute:: cpu_mac
                        
                        	cpu mac
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: cpu_port
                        
                        	cpu port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: initialized
                        
                        	initialized
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mac
                        
                        	mac
                        	**type**\:  str
                        
                        	**length:** 0..6
                        
                        .. attribute:: mtu
                        
                        	mtu
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ppu
                        
                        	ppu
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restarted
                        
                        	restarted
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.cpu_mac = None
                            self.cpu_port = None
                            self.initialized = None
                            self.mac = None
                            self.mtu = None
                            self.ppu = None
                            self.restarted = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:sw-status'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.cpu_mac is not None:
                                return True

                            if self.cpu_port is not None:
                                return True

                            if self.initialized is not None:
                                return True

                            if self.mac is not None:
                                return True

                            if self.mtu is not None:
                                return True

                            if self.ppu is not None:
                                return True

                            if self.restarted is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                            return meta._meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:switch-status'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.rate_limit is not None:
                            return True

                        if self.sw_reg_1 is not None and self.sw_reg_1._has_data():
                            return True

                        if self.sw_reg_2 is not None and self.sw_reg_2._has_data():
                            return True

                        if self.sw_status is not None and self.sw_status._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                        return meta._meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:switch-status-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.switch_status is not None and self.switch_status._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                    return meta._meta_table['Mlan.Nodes.Node.SwitchStatusTable']['meta_info']


            class PortCountersNumbers(object):
                """
                Table of port counters
                
                .. attribute:: port_counters_number
                
                	Number
                	**type**\: list of    :py:class:`PortCountersNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.port_counters_number = YList()
                    self.port_counters_number.parent = self
                    self.port_counters_number.name = 'port_counters_number'


                class PortCountersNumber(object):
                    """
                    Number
                    
                    .. attribute:: number  <key>
                    
                    	port number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: port_counters
                    
                    	mlan port counters info
                    	**type**\:   :py:class:`PortCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.number = None
                        self.port_counters = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters()
                        self.port_counters.parent = self


                    class PortCounters(object):
                        """
                        mlan port counters info
                        
                        .. attribute:: mlan_stats
                        
                        	Switch Port Statistics
                        	**type**\:   :py:class:`MlanStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats>`
                        
                        .. attribute:: port_num
                        
                        	Port Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.mlan_stats = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats()
                            self.mlan_stats.parent = self
                            self.port_num = None


                        class MlanStats(object):
                            """
                            Switch Port Statistics
                            
                            .. attribute:: collisions
                            
                            	collisions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: deferred
                            
                            	deferred
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excessive
                            
                            	excessive
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_bad_octets
                            
                            	inBadOctets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_bcast_pkt
                            
                            	inBcastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_discards
                            
                            	inDiscards
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_fcs_err
                            
                            	inFcsErr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_filtered
                            
                            	inFiltered
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_fragments
                            
                            	inFragments
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_good_octets
                            
                            	inGoodOctets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_good_octets_hi
                            
                            	inGoodOctets hi
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_jabber
                            
                            	inJabber
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_mcast_pkt
                            
                            	inMcastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_oversize
                            
                            	inOversize
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_pause_pkt
                            
                            	inPausePkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_rx_err
                            
                            	inRxErr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_undersize_pkt
                            
                            	inUndersizePkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_unicast_pkt
                            
                            	inUnicastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: late
                            
                            	late
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: multiple
                            
                            	multiple
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_bcast_pkt
                            
                            	outBcastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_fcs_err
                            
                            	outFcsErr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_filtered
                            
                            	outFiltered
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_mcast_pkt
                            
                            	outMcastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_octets
                            
                            	outOctets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_octets_hi
                            
                            	outOctets hi
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_pause_pkt
                            
                            	outPausePkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_unicast_pkt
                            
                            	outUnicastPkt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_1024_max_octets
                            
                            	rx tx 1024 Max Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_128_255_octets
                            
                            	rx tx 128 255 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_256_511_octets
                            
                            	rx tx 256 511 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_512_1023_octets
                            
                            	rx tx 512 1023 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_64_octets
                            
                            	rx tx 64 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_65_127_octets
                            
                            	rx tx 65 127 Octets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: single
                            
                            	single
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.collisions = None
                                self.deferred = None
                                self.excessive = None
                                self.in_bad_octets = None
                                self.in_bcast_pkt = None
                                self.in_discards = None
                                self.in_fcs_err = None
                                self.in_filtered = None
                                self.in_fragments = None
                                self.in_good_octets = None
                                self.in_good_octets_hi = None
                                self.in_jabber = None
                                self.in_mcast_pkt = None
                                self.in_oversize = None
                                self.in_pause_pkt = None
                                self.in_rx_err = None
                                self.in_undersize_pkt = None
                                self.in_unicast_pkt = None
                                self.late = None
                                self.multiple = None
                                self.out_bcast_pkt = None
                                self.out_fcs_err = None
                                self.out_filtered = None
                                self.out_mcast_pkt = None
                                self.out_octets = None
                                self.out_octets_hi = None
                                self.out_pause_pkt = None
                                self.out_unicast_pkt = None
                                self.rx_tx_1024_max_octets = None
                                self.rx_tx_128_255_octets = None
                                self.rx_tx_256_511_octets = None
                                self.rx_tx_512_1023_octets = None
                                self.rx_tx_64_octets = None
                                self.rx_tx_65_127_octets = None
                                self.single = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.collisions is not None:
                                    return True

                                if self.deferred is not None:
                                    return True

                                if self.excessive is not None:
                                    return True

                                if self.in_bad_octets is not None:
                                    return True

                                if self.in_bcast_pkt is not None:
                                    return True

                                if self.in_discards is not None:
                                    return True

                                if self.in_fcs_err is not None:
                                    return True

                                if self.in_filtered is not None:
                                    return True

                                if self.in_fragments is not None:
                                    return True

                                if self.in_good_octets is not None:
                                    return True

                                if self.in_good_octets_hi is not None:
                                    return True

                                if self.in_jabber is not None:
                                    return True

                                if self.in_mcast_pkt is not None:
                                    return True

                                if self.in_oversize is not None:
                                    return True

                                if self.in_pause_pkt is not None:
                                    return True

                                if self.in_rx_err is not None:
                                    return True

                                if self.in_undersize_pkt is not None:
                                    return True

                                if self.in_unicast_pkt is not None:
                                    return True

                                if self.late is not None:
                                    return True

                                if self.multiple is not None:
                                    return True

                                if self.out_bcast_pkt is not None:
                                    return True

                                if self.out_fcs_err is not None:
                                    return True

                                if self.out_filtered is not None:
                                    return True

                                if self.out_mcast_pkt is not None:
                                    return True

                                if self.out_octets is not None:
                                    return True

                                if self.out_octets_hi is not None:
                                    return True

                                if self.out_pause_pkt is not None:
                                    return True

                                if self.out_unicast_pkt is not None:
                                    return True

                                if self.rx_tx_1024_max_octets is not None:
                                    return True

                                if self.rx_tx_128_255_octets is not None:
                                    return True

                                if self.rx_tx_256_511_octets is not None:
                                    return True

                                if self.rx_tx_512_1023_octets is not None:
                                    return True

                                if self.rx_tx_64_octets is not None:
                                    return True

                                if self.rx_tx_65_127_octets is not None:
                                    return True

                                if self.single is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                                return meta._meta_table['Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:port-counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.mlan_stats is not None and self.mlan_stats._has_data():
                                return True

                            if self.port_num is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                            return meta._meta_table['Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:port-counters-number[Cisco-IOS-XR-asr9k-lc-ethctrl-oper:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.number is not None:
                            return True

                        if self.port_counters is not None and self.port_counters._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                        return meta._meta_table['Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:port-counters-numbers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.port_counters_number is not None:
                        for child_ref in self.port_counters_number:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                    return meta._meta_table['Mlan.Nodes.Node.PortCountersNumbers']['meta_info']


            class AtuEntryNumbers(object):
                """
                Table of switch ATU
                
                .. attribute:: atu_entry_number
                
                	Entry number
                	**type**\: list of    :py:class:`AtuEntryNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.atu_entry_number = YList()
                    self.atu_entry_number.parent = self
                    self.atu_entry_number.name = 'atu_entry_number'


                class AtuEntryNumber(object):
                    """
                    Entry number
                    
                    .. attribute:: entry  <key>
                    
                    	entry number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: switch_counters
                    
                    	mlan switch counters info
                    	**type**\:   :py:class:`SwitchCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.entry = None
                        self.switch_counters = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters()
                        self.switch_counters.parent = self


                    class SwitchCounters(object):
                        """
                        mlan switch counters info
                        
                        .. attribute:: atu
                        
                        	Switch ATU Data
                        	**type**\:   :py:class:`Atu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu>`
                        
                        .. attribute:: entry_num
                        
                        	Index of ATU Entry
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.atu = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu()
                            self.atu.parent = self
                            self.entry_num = None


                        class Atu(object):
                            """
                            Switch ATU Data
                            
                            .. attribute:: db_num
                            
                            	dbNum
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: dpv
                            
                            	dpv
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: es
                            
                            	es
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: macaddr
                            
                            	macaddr
                            	**type**\:  list of int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: trunk
                            
                            	trunk
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.db_num = None
                                self.dpv = None
                                self.es = None
                                self.macaddr = YLeafList()
                                self.macaddr.parent = self
                                self.macaddr.name = 'macaddr'
                                self.priority = None
                                self.trunk = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:atu'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.db_num is not None:
                                    return True

                                if self.dpv is not None:
                                    return True

                                if self.es is not None:
                                    return True

                                if self.macaddr is not None:
                                    for child in self.macaddr:
                                        if child is not None:
                                            return True

                                if self.priority is not None:
                                    return True

                                if self.trunk is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                                return meta._meta_table['Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:switch-counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.atu is not None and self.atu._has_data():
                                return True

                            if self.entry_num is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                            return meta._meta_table['Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.entry is None:
                            raise YPYModelError('Key property entry is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:atu-entry-number[Cisco-IOS-XR-asr9k-lc-ethctrl-oper:entry = ' + str(self.entry) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.entry is not None:
                            return True

                        if self.switch_counters is not None and self.switch_counters._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                        return meta._meta_table['Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:atu-entry-numbers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.atu_entry_number is not None:
                        for child_ref in self.atu_entry_number:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                    return meta._meta_table['Mlan.Nodes.Node.AtuEntryNumbers']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYModelError('Key property node is None')

                return '/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:nodes/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:node[Cisco-IOS-XR-asr9k-lc-ethctrl-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    return True

                if self.atu_entry_numbers is not None and self.atu_entry_numbers._has_data():
                    return True

                if self.port_counters_numbers is not None and self.port_counters_numbers._has_data():
                    return True

                if self.port_status_numbers is not None and self.port_status_numbers._has_data():
                    return True

                if self.switch_status_table is not None and self.switch_status_table._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
                return meta._meta_table['Mlan.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
            return meta._meta_table['Mlan.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_oper as meta
        return meta._meta_table['Mlan']['meta_info']


