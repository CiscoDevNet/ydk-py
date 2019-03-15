""" Cisco_IOS_XR_sysadmin_controllers_asr9k 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the top level container for
all hardware devices managed in Sysadmin.

Copyright(c) 2011\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Controller(Entity):
    """
    
    
    .. attribute:: switch
    
    	
    	**type**\:  :py:class:`Switch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch>`
    
    

    """

    _prefix = 'calvados_controllers_asr9k'
    _revision = '2017-11-10'

    def __init__(self):
        super(Controller, self).__init__()
        self._top_entity = None

        self.yang_name = "controller"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-controllers-asr9k"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("switch", ("switch", Controller.Switch))])
        self._leafs = OrderedDict()

        self.switch = Controller.Switch()
        self.switch.parent = self
        self._children_name_map["switch"] = "switch"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Controller, [], name, value)


    class Switch(Entity):
        """
        
        
        .. attribute:: oper
        
        	Control Ethernet switch operational data
        	**type**\:  :py:class:`Oper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper>`
        
        	**config**\: False
        
        

        """

        _prefix = 'calvados_controllers_asr9k'
        _revision = '2017-11-10'

        def __init__(self):
            super(Controller.Switch, self).__init__()

            self.yang_name = "switch"
            self.yang_parent_name = "controller"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("oper", ("oper", Controller.Switch.Oper))])
            self._leafs = OrderedDict()

            self.oper = Controller.Switch.Oper()
            self.oper.parent = self
            self._children_name_map["oper"] = "oper"
            self._segment_path = lambda: "switch"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Controller.Switch, [], name, value)


        class Oper(Entity):
            """
            Control Ethernet switch operational data.
            
            .. attribute:: reachable
            
            	
            	**type**\:  :py:class:`Reachable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Reachable>`
            
            	**config**\: False
            
            .. attribute:: summary
            
            	
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Summary>`
            
            	**config**\: False
            
            .. attribute:: statistics
            
            	
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Statistics>`
            
            	**config**\: False
            
            .. attribute:: mac
            
            	
            	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Mac>`
            
            	**config**\: False
            
            .. attribute:: bridge
            
            	
            	**type**\:  :py:class:`Bridge <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Bridge>`
            
            	**config**\: False
            
            .. attribute:: fdb
            
            	
            	**type**\:  :py:class:`Fdb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb>`
            
            	**config**\: False
            
            .. attribute:: vlan
            
            	
            	**type**\:  :py:class:`Vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan>`
            
            	**config**\: False
            
            .. attribute:: esd
            
            	
            	**type**\:  :py:class:`Esd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Esd>`
            
            	**config**\: False
            
            .. attribute:: mgmt_agent
            
            	
            	**type**\:  :py:class:`MgmtAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent>`
            
            	**config**\: False
            
            .. attribute:: sdr
            
            	
            	**type**\:  :py:class:`Sdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr>`
            
            	**config**\: False
            
            .. attribute:: port_state
            
            	
            	**type**\:  :py:class:`PortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.PortState>`
            
            	**config**\: False
            
            .. attribute:: trunk
            
            	
            	**type**\:  :py:class:`Trunk <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Trunk>`
            
            	**config**\: False
            
            .. attribute:: switch_debug_cont
            
            	
            	**type**\:  :py:class:`SwitchDebugCont <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.SwitchDebugCont>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers_asr9k'
            _revision = '2017-11-10'

            def __init__(self):
                super(Controller.Switch.Oper, self).__init__()

                self.yang_name = "oper"
                self.yang_parent_name = "switch"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("reachable", ("reachable", Controller.Switch.Oper.Reachable)), ("summary", ("summary", Controller.Switch.Oper.Summary)), ("statistics", ("statistics", Controller.Switch.Oper.Statistics)), ("mac", ("mac", Controller.Switch.Oper.Mac)), ("bridge", ("bridge", Controller.Switch.Oper.Bridge)), ("fdb", ("fdb", Controller.Switch.Oper.Fdb)), ("vlan", ("vlan", Controller.Switch.Oper.Vlan)), ("esd", ("esd", Controller.Switch.Oper.Esd)), ("mgmt-agent", ("mgmt_agent", Controller.Switch.Oper.MgmtAgent)), ("sdr", ("sdr", Controller.Switch.Oper.Sdr)), ("port-state", ("port_state", Controller.Switch.Oper.PortState)), ("trunk", ("trunk", Controller.Switch.Oper.Trunk)), ("switch-debug-cont", ("switch_debug_cont", Controller.Switch.Oper.SwitchDebugCont))])
                self._leafs = OrderedDict()

                self.reachable = Controller.Switch.Oper.Reachable()
                self.reachable.parent = self
                self._children_name_map["reachable"] = "reachable"

                self.summary = Controller.Switch.Oper.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.statistics = Controller.Switch.Oper.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"

                self.mac = Controller.Switch.Oper.Mac()
                self.mac.parent = self
                self._children_name_map["mac"] = "mac"

                self.bridge = Controller.Switch.Oper.Bridge()
                self.bridge.parent = self
                self._children_name_map["bridge"] = "bridge"

                self.fdb = Controller.Switch.Oper.Fdb()
                self.fdb.parent = self
                self._children_name_map["fdb"] = "fdb"

                self.vlan = Controller.Switch.Oper.Vlan()
                self.vlan.parent = self
                self._children_name_map["vlan"] = "vlan"

                self.esd = Controller.Switch.Oper.Esd()
                self.esd.parent = self
                self._children_name_map["esd"] = "esd"

                self.mgmt_agent = Controller.Switch.Oper.MgmtAgent()
                self.mgmt_agent.parent = self
                self._children_name_map["mgmt_agent"] = "mgmt-agent"

                self.sdr = Controller.Switch.Oper.Sdr()
                self.sdr.parent = self
                self._children_name_map["sdr"] = "sdr"

                self.port_state = Controller.Switch.Oper.PortState()
                self.port_state.parent = self
                self._children_name_map["port_state"] = "port-state"

                self.trunk = Controller.Switch.Oper.Trunk()
                self.trunk.parent = self
                self._children_name_map["trunk"] = "trunk"

                self.switch_debug_cont = Controller.Switch.Oper.SwitchDebugCont()
                self.switch_debug_cont.parent = self
                self._children_name_map["switch_debug_cont"] = "switch-debug-cont"
                self._segment_path = lambda: "oper"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.Switch.Oper, [], name, value)


            class Reachable(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Reachable.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Reachable, self).__init__()

                    self.yang_name = "reachable"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Reachable.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "reachable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Reachable, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: rack  (key)
                    
                    	
                    	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                    
                    	**config**\: False
                    
                    .. attribute:: card  (key)
                    
                    	
                    	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                    
                    	**config**\: False
                    
                    .. attribute:: switch_id  (key)
                    
                    	
                    	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Reachable.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "reachable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rack','card','switch_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                            ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                            ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                        ])
                        self.rack = None
                        self.card = None
                        self.switch_id = None
                        self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/reachable/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Reachable.Location, [u'rack', u'card', u'switch_id'], name, value)




            class Summary(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Summary.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Summary.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Summary, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: rack  (key)
                    
                    	
                    	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                    
                    	**config**\: False
                    
                    .. attribute:: card  (key)
                    
                    	Card that owns a switch of interest
                    	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                    
                    	**config**\: False
                    
                    .. attribute:: switch_id  (key)
                    
                    	Switch type
                    	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                    
                    	**config**\: False
                    
                    .. attribute:: serial_num
                    
                    	Rack serial number
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: port_iter
                    
                    	
                    	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Summary.Location.PortIter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Summary.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rack','card','switch_id']
                        self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Summary.Location.PortIter))])
                        self._leafs = OrderedDict([
                            ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                            ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                            ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ('serial_num', (YLeaf(YType.str, 'serial-num'), ['str'])),
                        ])
                        self.rack = None
                        self.card = None
                        self.switch_id = None
                        self.serial_num = None

                        self.port_iter = YList(self)
                        self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Summary.Location, [u'rack', u'card', u'switch_id', u'serial_num'], name, value)


                    class PortIter(Entity):
                        """
                        
                        
                        .. attribute:: port  (key)
                        
                        	Switch port
                        	**type**\: int
                        
                        	**range:** 0..127
                        
                        	**config**\: False
                        
                        .. attribute:: phys_state
                        
                        	Physical port state
                        	**type**\:  :py:class:`EsdmaSwitchPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchPortState>`
                        
                        	**config**\: False
                        
                        .. attribute:: admin_state
                        
                        	Administrative port state
                        	**type**\:  :py:class:`EsdmaSwitchPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchPortState>`
                        
                        	**config**\: False
                        
                        .. attribute:: port_speed
                        
                        	Indicates the port speed in bits per second
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: protocol_state
                        
                        	Protocol invoked port state
                        	**type**\:  :py:class:`MlapStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.MlapStateEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: forwarding
                        
                        	Indicates whether this port is allowed to forward traffic
                        	**type**\:  :py:class:`SwitchForwardingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchForwardingState>`
                        
                        	**config**\: False
                        
                        .. attribute:: connects_to
                        
                        	Indicates what this port connects to
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Summary.Location.PortIter, self).__init__()

                            self.yang_name = "port-iter"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['port']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                                ('phys_state', (YLeaf(YType.enumeration, 'phys-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchPortState', '')])),
                                ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchPortState', '')])),
                                ('port_speed', (YLeaf(YType.str, 'port-speed'), ['str'])),
                                ('protocol_state', (YLeaf(YType.enumeration, 'protocol-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'MlapStateEnum', '')])),
                                ('forwarding', (YLeaf(YType.enumeration, 'forwarding'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchForwardingState', '')])),
                                ('connects_to', (YLeaf(YType.str, 'connects-to'), ['str'])),
                            ])
                            self.port = None
                            self.phys_state = None
                            self.admin_state = None
                            self.port_speed = None
                            self.protocol_state = None
                            self.forwarding = None
                            self.connects_to = None
                            self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Summary.Location.PortIter, [u'port', u'phys_state', u'admin_state', u'port_speed', u'protocol_state', u'forwarding', u'connects_to'], name, value)





            class Statistics(Entity):
                """
                
                
                .. attribute:: summary_statistics
                
                	
                	**type**\:  :py:class:`SummaryStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Statistics.SummaryStatistics>`
                
                	**config**\: False
                
                .. attribute:: detail
                
                	
                	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Statistics.Detail>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("summary-statistics", ("summary_statistics", Controller.Switch.Oper.Statistics.SummaryStatistics)), ("detail", ("detail", Controller.Switch.Oper.Statistics.Detail))])
                    self._leafs = OrderedDict()

                    self.summary_statistics = Controller.Switch.Oper.Statistics.SummaryStatistics()
                    self.summary_statistics.parent = self
                    self._children_name_map["summary_statistics"] = "summary-statistics"

                    self.detail = Controller.Switch.Oper.Statistics.Detail()
                    self.detail.parent = self
                    self._children_name_map["detail"] = "detail"
                    self._segment_path = lambda: "statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Statistics, [], name, value)


                class SummaryStatistics(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Statistics.SummaryStatistics.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Statistics.SummaryStatistics, self).__init__()

                        self.yang_name = "summary-statistics"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Statistics.SummaryStatistics.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "summary-statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/statistics/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Statistics.SummaryStatistics, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card that owns a switch of interest
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: serial_num
                        
                        	Rack serial number
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: port_iter
                        
                        	
                        	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Statistics.SummaryStatistics.Location.PortIter>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Statistics.SummaryStatistics.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "summary-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Statistics.SummaryStatistics.Location.PortIter))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                ('serial_num', (YLeaf(YType.str, 'serial-num'), ['str'])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None
                            self.serial_num = None

                            self.port_iter = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/statistics/summary-statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Statistics.SummaryStatistics.Location, [u'rack', u'card', u'switch_id', u'serial_num'], name, value)


                        class PortIter(Entity):
                            """
                            
                            
                            .. attribute:: port  (key)
                            
                            	Switch port
                            	**type**\: int
                            
                            	**range:** 0..127
                            
                            	**config**\: False
                            
                            .. attribute:: phys_state
                            
                            	Physical port state
                            	**type**\:  :py:class:`EsdmaSwitchPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchPortState>`
                            
                            	**config**\: False
                            
                            .. attribute:: state_changes
                            
                            	Physical port state changes
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sw_sum_tx_packets
                            
                            	Packets transmitted on this switch port
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: sw_sum_rx_packets
                            
                            	Indicates the port speed in bits per second
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: sw_sum_tx_drops_errors
                            
                            	Indicates the number of transmitted packets that had an error or were dropped by the policer
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: sw_sum_rx_drops_errors
                            
                            	Indicates the number of received packets that had an error or were dropped by the policer
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: connects_to
                            
                            	Indicates what this port connects to
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Statistics.SummaryStatistics.Location.PortIter, self).__init__()

                                self.yang_name = "port-iter"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['port']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                                    ('phys_state', (YLeaf(YType.enumeration, 'phys-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchPortState', '')])),
                                    ('state_changes', (YLeaf(YType.uint32, 'state-changes'), ['int'])),
                                    ('sw_sum_tx_packets', (YLeaf(YType.uint64, 'sw-sum-tx-packets'), ['int'])),
                                    ('sw_sum_rx_packets', (YLeaf(YType.uint64, 'sw-sum-rx-packets'), ['int'])),
                                    ('sw_sum_tx_drops_errors', (YLeaf(YType.uint64, 'sw-sum-tx-drops-errors'), ['int'])),
                                    ('sw_sum_rx_drops_errors', (YLeaf(YType.uint64, 'sw-sum-rx-drops-errors'), ['int'])),
                                    ('connects_to', (YLeaf(YType.str, 'connects-to'), ['str'])),
                                ])
                                self.port = None
                                self.phys_state = None
                                self.state_changes = None
                                self.sw_sum_tx_packets = None
                                self.sw_sum_rx_packets = None
                                self.sw_sum_tx_drops_errors = None
                                self.sw_sum_rx_drops_errors = None
                                self.connects_to = None
                                self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Statistics.SummaryStatistics.Location.PortIter, [u'port', u'phys_state', u'state_changes', u'sw_sum_tx_packets', u'sw_sum_rx_packets', u'sw_sum_tx_drops_errors', u'sw_sum_rx_drops_errors', u'connects_to'], name, value)





                class Detail(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Statistics.Detail.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Statistics.Detail, self).__init__()

                        self.yang_name = "detail"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Statistics.Detail.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "detail"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/statistics/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Statistics.Detail, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card that owns a switch of interest
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: port_iter
                        
                        	
                        	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Statistics.Detail.Location.PortIter>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Statistics.Detail.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Statistics.Detail.Location.PortIter))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.port_iter = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/statistics/detail/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Statistics.Detail.Location, [u'rack', u'card', u'switch_id'], name, value)


                        class PortIter(Entity):
                            """
                            
                            
                            .. attribute:: port  (key)
                            
                            	Switch port
                            	**type**\: int
                            
                            	**range:** 0..127
                            
                            	**config**\: False
                            
                            .. attribute:: phys_state
                            
                            	Physical port state
                            	**type**\:  :py:class:`EsdmaSwitchPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchPortState>`
                            
                            	**config**\: False
                            
                            .. attribute:: port_speed
                            
                            	Indicates the port speed in bits per second
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: connects_to
                            
                            	Indicates what this port connects to
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: counters
                            
                            	
                            	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Statistics.Detail.Location.PortIter.Counters>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Statistics.Detail.Location.PortIter, self).__init__()

                                self.yang_name = "port-iter"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['port']
                                self._child_classes = OrderedDict([("counters", ("counters", Controller.Switch.Oper.Statistics.Detail.Location.PortIter.Counters))])
                                self._leafs = OrderedDict([
                                    ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                                    ('phys_state', (YLeaf(YType.enumeration, 'phys-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchPortState', '')])),
                                    ('port_speed', (YLeaf(YType.str, 'port-speed'), ['str'])),
                                    ('connects_to', (YLeaf(YType.str, 'connects-to'), ['str'])),
                                ])
                                self.port = None
                                self.phys_state = None
                                self.port_speed = None
                                self.connects_to = None

                                self.counters = Controller.Switch.Oper.Statistics.Detail.Location.PortIter.Counters()
                                self.counters.parent = self
                                self._children_name_map["counters"] = "counters"
                                self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Statistics.Detail.Location.PortIter, [u'port', u'phys_state', u'port_speed', u'connects_to'], name, value)


                            class Counters(Entity):
                                """
                                
                                
                                .. attribute:: sw_det_rx_ucast_packets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_mcast_packets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_bcast_packets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_flow_control
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_good_octets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_bad_octets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_fifo_overrun
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_undersize
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_fragments
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_oversize
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_jabber
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_errors
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_bad_crc
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_collisions
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rx_policing_drops
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_ucast_packets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_mcast_packets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_bcast_packets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_flow_control
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_good_octets
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_deferred
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_fifo_unrun
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_mult_collision
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_excess_collision
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_late_collisions
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_tx_policing_drops
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_txq_drops
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rxtx_packets_64
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rxtx_packets_65_127
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rxtx_packets_128_255
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rxtx_packets_256_511
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rxtx_packets_512_1023
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: sw_det_rxtx_packets_1024_max
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Statistics.Detail.Location.PortIter.Counters, self).__init__()

                                    self.yang_name = "counters"
                                    self.yang_parent_name = "port-iter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('sw_det_rx_ucast_packets', (YLeaf(YType.uint64, 'sw-det-rx-ucast-packets'), ['int'])),
                                        ('sw_det_rx_mcast_packets', (YLeaf(YType.uint64, 'sw-det-rx-mcast-packets'), ['int'])),
                                        ('sw_det_rx_bcast_packets', (YLeaf(YType.uint64, 'sw-det-rx-bcast-packets'), ['int'])),
                                        ('sw_det_rx_flow_control', (YLeaf(YType.uint64, 'sw-det-rx-flow-control'), ['int'])),
                                        ('sw_det_rx_good_octets', (YLeaf(YType.uint64, 'sw-det-rx-good-octets'), ['int'])),
                                        ('sw_det_rx_bad_octets', (YLeaf(YType.uint64, 'sw-det-rx-bad-octets'), ['int'])),
                                        ('sw_det_rx_fifo_overrun', (YLeaf(YType.uint64, 'sw-det-rx-fifo-overrun'), ['int'])),
                                        ('sw_det_rx_undersize', (YLeaf(YType.uint64, 'sw-det-rx-undersize'), ['int'])),
                                        ('sw_det_rx_fragments', (YLeaf(YType.uint64, 'sw-det-rx-fragments'), ['int'])),
                                        ('sw_det_rx_oversize', (YLeaf(YType.uint64, 'sw-det-rx-oversize'), ['int'])),
                                        ('sw_det_rx_jabber', (YLeaf(YType.uint64, 'sw-det-rx-jabber'), ['int'])),
                                        ('sw_det_rx_errors', (YLeaf(YType.uint64, 'sw-det-rx-errors'), ['int'])),
                                        ('sw_det_rx_bad_crc', (YLeaf(YType.uint64, 'sw-det-rx-bad-crc'), ['int'])),
                                        ('sw_det_rx_collisions', (YLeaf(YType.uint64, 'sw-det-rx-collisions'), ['int'])),
                                        ('sw_det_rx_policing_drops', (YLeaf(YType.uint64, 'sw-det-rx-policing-drops'), ['int'])),
                                        ('sw_det_tx_ucast_packets', (YLeaf(YType.uint64, 'sw-det-tx-ucast-packets'), ['int'])),
                                        ('sw_det_tx_mcast_packets', (YLeaf(YType.uint64, 'sw-det-tx-mcast-packets'), ['int'])),
                                        ('sw_det_tx_bcast_packets', (YLeaf(YType.uint64, 'sw-det-tx-bcast-packets'), ['int'])),
                                        ('sw_det_tx_flow_control', (YLeaf(YType.uint64, 'sw-det-tx-flow-control'), ['int'])),
                                        ('sw_det_tx_good_octets', (YLeaf(YType.uint64, 'sw-det-tx-good-octets'), ['int'])),
                                        ('sw_det_tx_deferred', (YLeaf(YType.uint64, 'sw-det-tx-deferred'), ['int'])),
                                        ('sw_det_tx_fifo_unrun', (YLeaf(YType.uint64, 'sw-det-tx-fifo-unrun'), ['int'])),
                                        ('sw_det_tx_mult_collision', (YLeaf(YType.uint64, 'sw-det-tx-mult-collision'), ['int'])),
                                        ('sw_det_tx_excess_collision', (YLeaf(YType.uint64, 'sw-det-tx-excess-collision'), ['int'])),
                                        ('sw_det_tx_late_collisions', (YLeaf(YType.uint64, 'sw-det-tx-late-collisions'), ['int'])),
                                        ('sw_det_tx_policing_drops', (YLeaf(YType.uint64, 'sw-det-tx-policing-drops'), ['int'])),
                                        ('sw_det_txq_drops', (YLeaf(YType.uint64, 'sw-det-txq-drops'), ['int'])),
                                        ('sw_det_rxtx_packets_64', (YLeaf(YType.uint64, 'sw-det-rxtx-packets-64'), ['int'])),
                                        ('sw_det_rxtx_packets_65_127', (YLeaf(YType.uint64, 'sw-det-rxtx-packets-65-127'), ['int'])),
                                        ('sw_det_rxtx_packets_128_255', (YLeaf(YType.uint64, 'sw-det-rxtx-packets-128-255'), ['int'])),
                                        ('sw_det_rxtx_packets_256_511', (YLeaf(YType.uint64, 'sw-det-rxtx-packets-256-511'), ['int'])),
                                        ('sw_det_rxtx_packets_512_1023', (YLeaf(YType.uint64, 'sw-det-rxtx-packets-512-1023'), ['int'])),
                                        ('sw_det_rxtx_packets_1024_max', (YLeaf(YType.uint64, 'sw-det-rxtx-packets-1024-max'), ['int'])),
                                    ])
                                    self.sw_det_rx_ucast_packets = None
                                    self.sw_det_rx_mcast_packets = None
                                    self.sw_det_rx_bcast_packets = None
                                    self.sw_det_rx_flow_control = None
                                    self.sw_det_rx_good_octets = None
                                    self.sw_det_rx_bad_octets = None
                                    self.sw_det_rx_fifo_overrun = None
                                    self.sw_det_rx_undersize = None
                                    self.sw_det_rx_fragments = None
                                    self.sw_det_rx_oversize = None
                                    self.sw_det_rx_jabber = None
                                    self.sw_det_rx_errors = None
                                    self.sw_det_rx_bad_crc = None
                                    self.sw_det_rx_collisions = None
                                    self.sw_det_rx_policing_drops = None
                                    self.sw_det_tx_ucast_packets = None
                                    self.sw_det_tx_mcast_packets = None
                                    self.sw_det_tx_bcast_packets = None
                                    self.sw_det_tx_flow_control = None
                                    self.sw_det_tx_good_octets = None
                                    self.sw_det_tx_deferred = None
                                    self.sw_det_tx_fifo_unrun = None
                                    self.sw_det_tx_mult_collision = None
                                    self.sw_det_tx_excess_collision = None
                                    self.sw_det_tx_late_collisions = None
                                    self.sw_det_tx_policing_drops = None
                                    self.sw_det_txq_drops = None
                                    self.sw_det_rxtx_packets_64 = None
                                    self.sw_det_rxtx_packets_65_127 = None
                                    self.sw_det_rxtx_packets_128_255 = None
                                    self.sw_det_rxtx_packets_256_511 = None
                                    self.sw_det_rxtx_packets_512_1023 = None
                                    self.sw_det_rxtx_packets_1024_max = None
                                    self._segment_path = lambda: "counters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Statistics.Detail.Location.PortIter.Counters, [u'sw_det_rx_ucast_packets', u'sw_det_rx_mcast_packets', u'sw_det_rx_bcast_packets', u'sw_det_rx_flow_control', u'sw_det_rx_good_octets', u'sw_det_rx_bad_octets', u'sw_det_rx_fifo_overrun', u'sw_det_rx_undersize', u'sw_det_rx_fragments', u'sw_det_rx_oversize', u'sw_det_rx_jabber', u'sw_det_rx_errors', u'sw_det_rx_bad_crc', u'sw_det_rx_collisions', u'sw_det_rx_policing_drops', u'sw_det_tx_ucast_packets', u'sw_det_tx_mcast_packets', u'sw_det_tx_bcast_packets', u'sw_det_tx_flow_control', u'sw_det_tx_good_octets', u'sw_det_tx_deferred', u'sw_det_tx_fifo_unrun', u'sw_det_tx_mult_collision', u'sw_det_tx_excess_collision', u'sw_det_tx_late_collisions', u'sw_det_tx_policing_drops', u'sw_det_txq_drops', u'sw_det_rxtx_packets_64', u'sw_det_rxtx_packets_65_127', u'sw_det_rxtx_packets_128_255', u'sw_det_rxtx_packets_256_511', u'sw_det_rxtx_packets_512_1023', u'sw_det_rxtx_packets_1024_max'], name, value)







            class Mac(Entity):
                """
                
                
                .. attribute:: mac_statistics
                
                	
                	**type**\:  :py:class:`MacStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Mac.MacStatistics>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Mac, self).__init__()

                    self.yang_name = "mac"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("mac-statistics", ("mac_statistics", Controller.Switch.Oper.Mac.MacStatistics))])
                    self._leafs = OrderedDict()

                    self.mac_statistics = Controller.Switch.Oper.Mac.MacStatistics()
                    self.mac_statistics.parent = self
                    self._children_name_map["mac_statistics"] = "mac-statistics"
                    self._segment_path = lambda: "mac"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Mac, [], name, value)


                class MacStatistics(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Mac.MacStatistics.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Mac.MacStatistics, self).__init__()

                        self.yang_name = "mac-statistics"
                        self.yang_parent_name = "mac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Mac.MacStatistics.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "mac-statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mac/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Mac.MacStatistics, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card to list the switch MAC information for
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: port_iter
                        
                        	
                        	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Mac.MacStatistics.Location.PortIter>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Mac.MacStatistics.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "mac-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Mac.MacStatistics.Location.PortIter))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.port_iter = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mac/mac-statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Mac.MacStatistics.Location, [u'rack', u'card', u'switch_id'], name, value)


                        class PortIter(Entity):
                            """
                            
                            
                            .. attribute:: port  (key)
                            
                            	Switch port
                            	**type**\: int
                            
                            	**range:** 0..127
                            
                            	**config**\: False
                            
                            .. attribute:: mac_entry
                            
                            	
                            	**type**\: list of  		 :py:class:`MacEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Mac.MacStatistics.Location.PortIter.MacEntry>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Mac.MacStatistics.Location.PortIter, self).__init__()

                                self.yang_name = "port-iter"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['port']
                                self._child_classes = OrderedDict([("mac-entry", ("mac_entry", Controller.Switch.Oper.Mac.MacStatistics.Location.PortIter.MacEntry))])
                                self._leafs = OrderedDict([
                                    ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                                ])
                                self.port = None

                                self.mac_entry = YList(self)
                                self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Mac.MacStatistics.Location.PortIter, [u'port'], name, value)


                            class MacEntry(Entity):
                                """
                                
                                
                                .. attribute:: id  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: base_reg
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: desc
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: value
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Mac.MacStatistics.Location.PortIter.MacEntry, self).__init__()

                                    self.yang_name = "mac-entry"
                                    self.yang_parent_name = "port-iter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('base_reg', (YLeaf(YType.str, 'base-reg'), ['str'])),
                                        ('desc', (YLeaf(YType.str, 'desc'), ['str'])),
                                        ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                    ])
                                    self.id = None
                                    self.base_reg = None
                                    self.desc = None
                                    self.value = None
                                    self._segment_path = lambda: "mac-entry" + "[id='" + str(self.id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Mac.MacStatistics.Location.PortIter.MacEntry, [u'id', u'base_reg', u'desc', u'value'], name, value)







            class Bridge(Entity):
                """
                
                
                .. attribute:: statistics
                
                	
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Bridge.Statistics>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Bridge, self).__init__()

                    self.yang_name = "bridge"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics", ("statistics", Controller.Switch.Oper.Bridge.Statistics))])
                    self._leafs = OrderedDict()

                    self.statistics = Controller.Switch.Oper.Bridge.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._segment_path = lambda: "bridge"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Bridge, [], name, value)


                class Statistics(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Bridge.Statistics.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Bridge.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "bridge"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Bridge.Statistics.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/bridge/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Bridge.Statistics, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: ingress_set_id
                        
                        	
                        	**type**\: list of  		 :py:class:`IngressSetId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Bridge.Statistics.Location.IngressSetId>`
                        
                        	**config**\: False
                        
                        .. attribute:: egress_set_id
                        
                        	
                        	**type**\: list of  		 :py:class:`EgressSetId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Bridge.Statistics.Location.EgressSetId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Bridge.Statistics.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("ingress-set-id", ("ingress_set_id", Controller.Switch.Oper.Bridge.Statistics.Location.IngressSetId)), ("egress-set-id", ("egress_set_id", Controller.Switch.Oper.Bridge.Statistics.Location.EgressSetId))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.ingress_set_id = YList(self)
                            self.egress_set_id = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/bridge/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Bridge.Statistics.Location, ['rack', 'card', 'switch_id'], name, value)


                        class IngressSetId(Entity):
                            """
                            
                            
                            .. attribute:: ingress_set  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: ingress_set_name
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: ingress_frames
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ingress_vlan_discards
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ingress_security_discards
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ingress_other_discards
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Bridge.Statistics.Location.IngressSetId, self).__init__()

                                self.yang_name = "ingress-set-id"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['ingress_set']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ingress_set', (YLeaf(YType.uint32, 'ingress-set'), ['int'])),
                                    ('ingress_set_name', (YLeaf(YType.str, 'ingress-set-name'), ['str'])),
                                    ('ingress_frames', (YLeaf(YType.uint64, 'ingress-frames'), ['int'])),
                                    ('ingress_vlan_discards', (YLeaf(YType.uint64, 'ingress-vlan-discards'), ['int'])),
                                    ('ingress_security_discards', (YLeaf(YType.uint64, 'ingress-security-discards'), ['int'])),
                                    ('ingress_other_discards', (YLeaf(YType.uint64, 'ingress-other-discards'), ['int'])),
                                ])
                                self.ingress_set = None
                                self.ingress_set_name = None
                                self.ingress_frames = None
                                self.ingress_vlan_discards = None
                                self.ingress_security_discards = None
                                self.ingress_other_discards = None
                                self._segment_path = lambda: "ingress-set-id" + "[ingress-set='" + str(self.ingress_set) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Bridge.Statistics.Location.IngressSetId, ['ingress_set', 'ingress_set_name', 'ingress_frames', 'ingress_vlan_discards', 'ingress_security_discards', 'ingress_other_discards'], name, value)



                        class EgressSetId(Entity):
                            """
                            
                            
                            .. attribute:: egress_set  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: egress_set_name
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: egress_ucast_frames
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: egress_mcast_frames
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: egress_bcast_frames
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: egress_discarded_frames
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: egress_txq_congestion
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: egress_ctrl_packets
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: egress_other_drops
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Bridge.Statistics.Location.EgressSetId, self).__init__()

                                self.yang_name = "egress-set-id"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['egress_set']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('egress_set', (YLeaf(YType.uint32, 'egress-set'), ['int'])),
                                    ('egress_set_name', (YLeaf(YType.str, 'egress-set-name'), ['str'])),
                                    ('egress_ucast_frames', (YLeaf(YType.uint64, 'egress-ucast-frames'), ['int'])),
                                    ('egress_mcast_frames', (YLeaf(YType.uint64, 'egress-mcast-frames'), ['int'])),
                                    ('egress_bcast_frames', (YLeaf(YType.uint64, 'egress-bcast-frames'), ['int'])),
                                    ('egress_discarded_frames', (YLeaf(YType.uint64, 'egress-discarded-frames'), ['int'])),
                                    ('egress_txq_congestion', (YLeaf(YType.uint64, 'egress-txq-congestion'), ['int'])),
                                    ('egress_ctrl_packets', (YLeaf(YType.uint64, 'egress-ctrl-packets'), ['int'])),
                                    ('egress_other_drops', (YLeaf(YType.uint64, 'egress-other-drops'), ['int'])),
                                ])
                                self.egress_set = None
                                self.egress_set_name = None
                                self.egress_ucast_frames = None
                                self.egress_mcast_frames = None
                                self.egress_bcast_frames = None
                                self.egress_discarded_frames = None
                                self.egress_txq_congestion = None
                                self.egress_ctrl_packets = None
                                self.egress_other_drops = None
                                self._segment_path = lambda: "egress-set-id" + "[egress-set='" + str(self.egress_set) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Bridge.Statistics.Location.EgressSetId, ['egress_set', 'egress_set_name', 'egress_ucast_frames', 'egress_mcast_frames', 'egress_bcast_frames', 'egress_discarded_frames', 'egress_txq_congestion', 'egress_ctrl_packets', 'egress_other_drops'], name, value)






            class Fdb(Entity):
                """
                
                
                .. attribute:: vlan
                
                	
                	**type**\:  :py:class:`Vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Vlan>`
                
                	**config**\: False
                
                .. attribute:: mac
                
                	
                	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Mac>`
                
                	**config**\: False
                
                .. attribute:: port
                
                	
                	**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Port>`
                
                	**config**\: False
                
                .. attribute:: statistics
                
                	
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Statistics>`
                
                	**config**\: False
                
                .. attribute:: switch_fdb_common
                
                	
                	**type**\:  :py:class:`SwitchFdbCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.SwitchFdbCommon>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Fdb, self).__init__()

                    self.yang_name = "fdb"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vlan", ("vlan", Controller.Switch.Oper.Fdb.Vlan)), ("mac", ("mac", Controller.Switch.Oper.Fdb.Mac)), ("port", ("port", Controller.Switch.Oper.Fdb.Port)), ("statistics", ("statistics", Controller.Switch.Oper.Fdb.Statistics)), ("switch-fdb-common", ("switch_fdb_common", Controller.Switch.Oper.Fdb.SwitchFdbCommon))])
                    self._leafs = OrderedDict()

                    self.vlan = Controller.Switch.Oper.Fdb.Vlan()
                    self.vlan.parent = self
                    self._children_name_map["vlan"] = "vlan"

                    self.mac = Controller.Switch.Oper.Fdb.Mac()
                    self.mac.parent = self
                    self._children_name_map["mac"] = "mac"

                    self.port = Controller.Switch.Oper.Fdb.Port()
                    self.port.parent = self
                    self._children_name_map["port"] = "port"

                    self.statistics = Controller.Switch.Oper.Fdb.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"

                    self.switch_fdb_common = Controller.Switch.Oper.Fdb.SwitchFdbCommon()
                    self.switch_fdb_common.parent = self
                    self._children_name_map["switch_fdb_common"] = "switch-fdb-common"
                    self._segment_path = lambda: "fdb"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Fdb, [], name, value)


                class Vlan(Entity):
                    """
                    
                    
                    .. attribute:: vlan_iter
                    
                    	
                    	**type**\: list of  		 :py:class:`VlanIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Vlan.VlanIter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Fdb.Vlan, self).__init__()

                        self.yang_name = "vlan"
                        self.yang_parent_name = "fdb"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vlan-iter", ("vlan_iter", Controller.Switch.Oper.Fdb.Vlan.VlanIter))])
                        self._leafs = OrderedDict()

                        self.vlan_iter = YList(self)
                        self._segment_path = lambda: "vlan"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Fdb.Vlan, [], name, value)


                    class VlanIter(Entity):
                        """
                        
                        
                        .. attribute:: vlan  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4095
                        
                        	**config**\: False
                        
                        .. attribute:: switch_fdb_common
                        
                        	
                        	**type**\:  :py:class:`SwitchFdbCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Fdb.Vlan.VlanIter, self).__init__()

                            self.yang_name = "vlan-iter"
                            self.yang_parent_name = "vlan"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['vlan']
                            self._child_classes = OrderedDict([("switch-fdb-common", ("switch_fdb_common", Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon))])
                            self._leafs = OrderedDict([
                                ('vlan', (YLeaf(YType.uint16, 'vlan'), ['int'])),
                            ])
                            self.vlan = None

                            self.switch_fdb_common = Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon()
                            self.switch_fdb_common.parent = self
                            self._children_name_map["switch_fdb_common"] = "switch-fdb-common"
                            self._segment_path = lambda: "vlan-iter" + "[vlan='" + str(self.vlan) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/vlan/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Fdb.Vlan.VlanIter, ['vlan'], name, value)


                        class SwitchFdbCommon(Entity):
                            """
                            
                            
                            .. attribute:: location
                            
                            	
                            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon, self).__init__()

                                self.yang_name = "switch-fdb-common"
                                self.yang_parent_name = "vlan-iter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location))])
                                self._leafs = OrderedDict()

                                self.location = YList(self)
                                self._segment_path = lambda: "switch-fdb-common"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon, [], name, value)


                            class Location(Entity):
                                """
                                
                                
                                .. attribute:: rack  (key)
                                
                                	
                                	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: card  (key)
                                
                                	Card to list the switch FDB information for
                                	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                                
                                	**config**\: False
                                
                                .. attribute:: switch_id  (key)
                                
                                	Switch type
                                	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: num_entries
                                
                                	Number of FDB entries in the table
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: has_trunk_entry
                                
                                	FDB entries contain an entry from the trunk
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: trunk_entry_message
                                
                                	Message displayed when an FDB entry contains an entry for a trunk member port
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_block
                                
                                	
                                	**type**\:  :py:class:`FdbBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location, self).__init__()

                                    self.yang_name = "location"
                                    self.yang_parent_name = "switch-fdb-common"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['rack','card','switch_id']
                                    self._child_classes = OrderedDict([("fdb-block", ("fdb_block", Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock))])
                                    self._leafs = OrderedDict([
                                        ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                        ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                        ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                        ('num_entries', (YLeaf(YType.uint32, 'num-entries'), ['int'])),
                                        ('has_trunk_entry', (YLeaf(YType.uint8, 'has-trunk-entry'), ['int'])),
                                        ('trunk_entry_message', (YLeaf(YType.str, 'trunk-entry-message'), ['str'])),
                                    ])
                                    self.rack = None
                                    self.card = None
                                    self.switch_id = None
                                    self.num_entries = None
                                    self.has_trunk_entry = None
                                    self.trunk_entry_message = None

                                    self.fdb_block = Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock()
                                    self.fdb_block.parent = self
                                    self._children_name_map["fdb_block"] = "fdb-block"
                                    self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location, ['rack', 'card', 'switch_id', 'num_entries', 'has_trunk_entry', 'trunk_entry_message'], name, value)


                                class FdbBlock(Entity):
                                    """
                                    
                                    
                                    .. attribute:: fdb_entry
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`FdbEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock, self).__init__()

                                        self.yang_name = "fdb-block"
                                        self.yang_parent_name = "location"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("fdb-entry", ("fdb_entry", Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry))])
                                        self._leafs = OrderedDict()

                                        self.fdb_entry = YList(self)
                                        self._segment_path = lambda: "fdb-block"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock, [], name, value)


                                    class FdbEntry(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fdb_index  (key)
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_mac_addr
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_vlan
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4095
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_vlan_hex
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4095
                                        
                                        	**refers to**\:  :py:class:`fdb_vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_port
                                        
                                        	Switch port MAC address learned on
                                        	**type**\: int
                                        
                                        	**range:** \-1..128
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_trap_entry
                                        
                                        	
                                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_static_entry
                                        
                                        	
                                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_synced_cores
                                        
                                        	
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'calvados_controllers_asr9k'
                                        _revision = '2017-11-10'

                                        def __init__(self):
                                            super(Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry, self).__init__()

                                            self.yang_name = "fdb-entry"
                                            self.yang_parent_name = "fdb-block"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fdb_index']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fdb_index', (YLeaf(YType.uint32, 'fdb-index'), ['int'])),
                                                ('fdb_mac_addr', (YLeaf(YType.str, 'fdb-mac-addr'), ['str'])),
                                                ('fdb_vlan', (YLeaf(YType.uint16, 'fdb-vlan'), ['int'])),
                                                ('fdb_vlan_hex', (YLeaf(YType.str, 'fdb-vlan-hex'), ['int'])),
                                                ('fdb_port', (YLeaf(YType.int32, 'fdb-port'), ['int'])),
                                                ('fdb_trap_entry', (YLeaf(YType.enumeration, 'fdb-trap-entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                                ('fdb_static_entry', (YLeaf(YType.enumeration, 'fdb-static-entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                                ('fdb_synced_cores', (YLeafList(YType.uint8, 'fdb-synced-cores'), ['int'])),
                                            ])
                                            self.fdb_index = None
                                            self.fdb_mac_addr = None
                                            self.fdb_vlan = None
                                            self.fdb_vlan_hex = None
                                            self.fdb_port = None
                                            self.fdb_trap_entry = None
                                            self.fdb_static_entry = None
                                            self.fdb_synced_cores = []
                                            self._segment_path = lambda: "fdb-entry" + "[fdb-index='" + str(self.fdb_index) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Controller.Switch.Oper.Fdb.Vlan.VlanIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry, ['fdb_index', 'fdb_mac_addr', 'fdb_vlan', 'fdb_vlan_hex', 'fdb_port', 'fdb_trap_entry', 'fdb_static_entry', 'fdb_synced_cores'], name, value)








                class Mac(Entity):
                    """
                    
                    
                    .. attribute:: mac_iter
                    
                    	
                    	**type**\: list of  		 :py:class:`MacIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Mac.MacIter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Fdb.Mac, self).__init__()

                        self.yang_name = "mac"
                        self.yang_parent_name = "fdb"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mac-iter", ("mac_iter", Controller.Switch.Oper.Fdb.Mac.MacIter))])
                        self._leafs = OrderedDict()

                        self.mac_iter = YList(self)
                        self._segment_path = lambda: "mac"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Fdb.Mac, [], name, value)


                    class MacIter(Entity):
                        """
                        
                        
                        .. attribute:: mac  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        .. attribute:: switch_fdb_common
                        
                        	
                        	**type**\:  :py:class:`SwitchFdbCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Fdb.Mac.MacIter, self).__init__()

                            self.yang_name = "mac-iter"
                            self.yang_parent_name = "mac"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['mac']
                            self._child_classes = OrderedDict([("switch-fdb-common", ("switch_fdb_common", Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon))])
                            self._leafs = OrderedDict([
                                ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                            ])
                            self.mac = None

                            self.switch_fdb_common = Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon()
                            self.switch_fdb_common.parent = self
                            self._children_name_map["switch_fdb_common"] = "switch-fdb-common"
                            self._segment_path = lambda: "mac-iter" + "[mac='" + str(self.mac) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/mac/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Fdb.Mac.MacIter, ['mac'], name, value)


                        class SwitchFdbCommon(Entity):
                            """
                            
                            
                            .. attribute:: location
                            
                            	
                            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon, self).__init__()

                                self.yang_name = "switch-fdb-common"
                                self.yang_parent_name = "mac-iter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location))])
                                self._leafs = OrderedDict()

                                self.location = YList(self)
                                self._segment_path = lambda: "switch-fdb-common"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon, [], name, value)


                            class Location(Entity):
                                """
                                
                                
                                .. attribute:: rack  (key)
                                
                                	
                                	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: card  (key)
                                
                                	Card to list the switch FDB information for
                                	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                                
                                	**config**\: False
                                
                                .. attribute:: switch_id  (key)
                                
                                	Switch type
                                	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: num_entries
                                
                                	Number of FDB entries in the table
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: has_trunk_entry
                                
                                	FDB entries contain an entry from the trunk
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: trunk_entry_message
                                
                                	Message displayed when an FDB entry contains an entry for a trunk member port
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_block
                                
                                	
                                	**type**\:  :py:class:`FdbBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location, self).__init__()

                                    self.yang_name = "location"
                                    self.yang_parent_name = "switch-fdb-common"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['rack','card','switch_id']
                                    self._child_classes = OrderedDict([("fdb-block", ("fdb_block", Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock))])
                                    self._leafs = OrderedDict([
                                        ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                        ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                        ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                        ('num_entries', (YLeaf(YType.uint32, 'num-entries'), ['int'])),
                                        ('has_trunk_entry', (YLeaf(YType.uint8, 'has-trunk-entry'), ['int'])),
                                        ('trunk_entry_message', (YLeaf(YType.str, 'trunk-entry-message'), ['str'])),
                                    ])
                                    self.rack = None
                                    self.card = None
                                    self.switch_id = None
                                    self.num_entries = None
                                    self.has_trunk_entry = None
                                    self.trunk_entry_message = None

                                    self.fdb_block = Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock()
                                    self.fdb_block.parent = self
                                    self._children_name_map["fdb_block"] = "fdb-block"
                                    self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location, ['rack', 'card', 'switch_id', 'num_entries', 'has_trunk_entry', 'trunk_entry_message'], name, value)


                                class FdbBlock(Entity):
                                    """
                                    
                                    
                                    .. attribute:: fdb_entry
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`FdbEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock, self).__init__()

                                        self.yang_name = "fdb-block"
                                        self.yang_parent_name = "location"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("fdb-entry", ("fdb_entry", Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry))])
                                        self._leafs = OrderedDict()

                                        self.fdb_entry = YList(self)
                                        self._segment_path = lambda: "fdb-block"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock, [], name, value)


                                    class FdbEntry(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fdb_index  (key)
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_mac_addr
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_vlan
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4095
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_vlan_hex
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4095
                                        
                                        	**refers to**\:  :py:class:`fdb_vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_port
                                        
                                        	Switch port MAC address learned on
                                        	**type**\: int
                                        
                                        	**range:** \-1..128
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_trap_entry
                                        
                                        	
                                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_static_entry
                                        
                                        	
                                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_synced_cores
                                        
                                        	
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'calvados_controllers_asr9k'
                                        _revision = '2017-11-10'

                                        def __init__(self):
                                            super(Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry, self).__init__()

                                            self.yang_name = "fdb-entry"
                                            self.yang_parent_name = "fdb-block"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fdb_index']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fdb_index', (YLeaf(YType.uint32, 'fdb-index'), ['int'])),
                                                ('fdb_mac_addr', (YLeaf(YType.str, 'fdb-mac-addr'), ['str'])),
                                                ('fdb_vlan', (YLeaf(YType.uint16, 'fdb-vlan'), ['int'])),
                                                ('fdb_vlan_hex', (YLeaf(YType.str, 'fdb-vlan-hex'), ['int'])),
                                                ('fdb_port', (YLeaf(YType.int32, 'fdb-port'), ['int'])),
                                                ('fdb_trap_entry', (YLeaf(YType.enumeration, 'fdb-trap-entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                                ('fdb_static_entry', (YLeaf(YType.enumeration, 'fdb-static-entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                                ('fdb_synced_cores', (YLeafList(YType.uint8, 'fdb-synced-cores'), ['int'])),
                                            ])
                                            self.fdb_index = None
                                            self.fdb_mac_addr = None
                                            self.fdb_vlan = None
                                            self.fdb_vlan_hex = None
                                            self.fdb_port = None
                                            self.fdb_trap_entry = None
                                            self.fdb_static_entry = None
                                            self.fdb_synced_cores = []
                                            self._segment_path = lambda: "fdb-entry" + "[fdb-index='" + str(self.fdb_index) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Controller.Switch.Oper.Fdb.Mac.MacIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry, ['fdb_index', 'fdb_mac_addr', 'fdb_vlan', 'fdb_vlan_hex', 'fdb_port', 'fdb_trap_entry', 'fdb_static_entry', 'fdb_synced_cores'], name, value)








                class Port(Entity):
                    """
                    
                    
                    .. attribute:: port_iter
                    
                    	
                    	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Port.PortIter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Fdb.Port, self).__init__()

                        self.yang_name = "port"
                        self.yang_parent_name = "fdb"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Fdb.Port.PortIter))])
                        self._leafs = OrderedDict()

                        self.port_iter = YList(self)
                        self._segment_path = lambda: "port"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Fdb.Port, [], name, value)


                    class PortIter(Entity):
                        """
                        
                        
                        .. attribute:: port  (key)
                        
                        	Switch port used for filtering
                        	**type**\: int
                        
                        	**range:** 0..127
                        
                        	**config**\: False
                        
                        .. attribute:: switch_fdb_common
                        
                        	
                        	**type**\:  :py:class:`SwitchFdbCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Fdb.Port.PortIter, self).__init__()

                            self.yang_name = "port-iter"
                            self.yang_parent_name = "port"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['port']
                            self._child_classes = OrderedDict([("switch-fdb-common", ("switch_fdb_common", Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon))])
                            self._leafs = OrderedDict([
                                ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                            ])
                            self.port = None

                            self.switch_fdb_common = Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon()
                            self.switch_fdb_common.parent = self
                            self._children_name_map["switch_fdb_common"] = "switch-fdb-common"
                            self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/port/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Fdb.Port.PortIter, ['port'], name, value)


                        class SwitchFdbCommon(Entity):
                            """
                            
                            
                            .. attribute:: location
                            
                            	
                            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon, self).__init__()

                                self.yang_name = "switch-fdb-common"
                                self.yang_parent_name = "port-iter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location))])
                                self._leafs = OrderedDict()

                                self.location = YList(self)
                                self._segment_path = lambda: "switch-fdb-common"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon, [], name, value)


                            class Location(Entity):
                                """
                                
                                
                                .. attribute:: rack  (key)
                                
                                	
                                	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: card  (key)
                                
                                	Card to list the switch FDB information for
                                	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                                
                                	**config**\: False
                                
                                .. attribute:: switch_id  (key)
                                
                                	Switch type
                                	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: num_entries
                                
                                	Number of FDB entries in the table
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: has_trunk_entry
                                
                                	FDB entries contain an entry from the trunk
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: trunk_entry_message
                                
                                	Message displayed when an FDB entry contains an entry for a trunk member port
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_block
                                
                                	
                                	**type**\:  :py:class:`FdbBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location, self).__init__()

                                    self.yang_name = "location"
                                    self.yang_parent_name = "switch-fdb-common"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['rack','card','switch_id']
                                    self._child_classes = OrderedDict([("fdb-block", ("fdb_block", Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock))])
                                    self._leafs = OrderedDict([
                                        ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                        ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                        ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                        ('num_entries', (YLeaf(YType.uint32, 'num-entries'), ['int'])),
                                        ('has_trunk_entry', (YLeaf(YType.uint8, 'has-trunk-entry'), ['int'])),
                                        ('trunk_entry_message', (YLeaf(YType.str, 'trunk-entry-message'), ['str'])),
                                    ])
                                    self.rack = None
                                    self.card = None
                                    self.switch_id = None
                                    self.num_entries = None
                                    self.has_trunk_entry = None
                                    self.trunk_entry_message = None

                                    self.fdb_block = Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock()
                                    self.fdb_block.parent = self
                                    self._children_name_map["fdb_block"] = "fdb-block"
                                    self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location, ['rack', 'card', 'switch_id', 'num_entries', 'has_trunk_entry', 'trunk_entry_message'], name, value)


                                class FdbBlock(Entity):
                                    """
                                    
                                    
                                    .. attribute:: fdb_entry
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`FdbEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock, self).__init__()

                                        self.yang_name = "fdb-block"
                                        self.yang_parent_name = "location"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("fdb-entry", ("fdb_entry", Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry))])
                                        self._leafs = OrderedDict()

                                        self.fdb_entry = YList(self)
                                        self._segment_path = lambda: "fdb-block"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock, [], name, value)


                                    class FdbEntry(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fdb_index  (key)
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_mac_addr
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_vlan
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4095
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_vlan_hex
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4095
                                        
                                        	**refers to**\:  :py:class:`fdb_vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_port
                                        
                                        	Switch port MAC address learned on
                                        	**type**\: int
                                        
                                        	**range:** \-1..128
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_trap_entry
                                        
                                        	
                                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_static_entry
                                        
                                        	
                                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fdb_synced_cores
                                        
                                        	
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'calvados_controllers_asr9k'
                                        _revision = '2017-11-10'

                                        def __init__(self):
                                            super(Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry, self).__init__()

                                            self.yang_name = "fdb-entry"
                                            self.yang_parent_name = "fdb-block"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fdb_index']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fdb_index', (YLeaf(YType.uint32, 'fdb-index'), ['int'])),
                                                ('fdb_mac_addr', (YLeaf(YType.str, 'fdb-mac-addr'), ['str'])),
                                                ('fdb_vlan', (YLeaf(YType.uint16, 'fdb-vlan'), ['int'])),
                                                ('fdb_vlan_hex', (YLeaf(YType.str, 'fdb-vlan-hex'), ['int'])),
                                                ('fdb_port', (YLeaf(YType.int32, 'fdb-port'), ['int'])),
                                                ('fdb_trap_entry', (YLeaf(YType.enumeration, 'fdb-trap-entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                                ('fdb_static_entry', (YLeaf(YType.enumeration, 'fdb-static-entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                                ('fdb_synced_cores', (YLeafList(YType.uint8, 'fdb-synced-cores'), ['int'])),
                                            ])
                                            self.fdb_index = None
                                            self.fdb_mac_addr = None
                                            self.fdb_vlan = None
                                            self.fdb_vlan_hex = None
                                            self.fdb_port = None
                                            self.fdb_trap_entry = None
                                            self.fdb_static_entry = None
                                            self.fdb_synced_cores = []
                                            self._segment_path = lambda: "fdb-entry" + "[fdb-index='" + str(self.fdb_index) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Controller.Switch.Oper.Fdb.Port.PortIter.SwitchFdbCommon.Location.FdbBlock.FdbEntry, ['fdb_index', 'fdb_mac_addr', 'fdb_vlan', 'fdb_vlan_hex', 'fdb_port', 'fdb_trap_entry', 'fdb_static_entry', 'fdb_synced_cores'], name, value)








                class Statistics(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Statistics.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Fdb.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "fdb"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Fdb.Statistics.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Fdb.Statistics, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: counter_info
                        
                        	
                        	**type**\:  :py:class:`CounterInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Statistics.Location.CounterInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: core_id
                        
                        	
                        	**type**\: list of  		 :py:class:`CoreId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.Statistics.Location.CoreId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Fdb.Statistics.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("counter-info", ("counter_info", Controller.Switch.Oper.Fdb.Statistics.Location.CounterInfo)), ("core-id", ("core_id", Controller.Switch.Oper.Fdb.Statistics.Location.CoreId))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.counter_info = Controller.Switch.Oper.Fdb.Statistics.Location.CounterInfo()
                            self.counter_info.parent = self
                            self._children_name_map["counter_info"] = "counter-info"

                            self.core_id = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Fdb.Statistics.Location, ['rack', 'card', 'switch_id'], name, value)


                        class CounterInfo(Entity):
                            """
                            
                            
                            .. attribute:: fdb_shadow_entries
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_max_shadow_entries
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_max_hash_chain
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_entries_added
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_entries_deleted
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_entries_updated
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_flushes
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_address_updates
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_new_addresses
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_aged_updates
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_transplant_updates
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_forwarding_updates
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_address_insert_errors
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_address_update_errors
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_memory_errors
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_allocation_errors
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_address_updates_queued
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_address_queue_full
                            
                            	
                            	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_forwarding_updates_queued
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fdb_forwarding_queue_full
                            
                            	
                            	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Fdb.Statistics.Location.CounterInfo, self).__init__()

                                self.yang_name = "counter-info"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('fdb_shadow_entries', (YLeaf(YType.uint32, 'fdb-shadow-entries'), ['int'])),
                                    ('fdb_max_shadow_entries', (YLeaf(YType.uint32, 'fdb-max-shadow-entries'), ['int'])),
                                    ('fdb_max_hash_chain', (YLeaf(YType.uint32, 'fdb-max-hash-chain'), ['int'])),
                                    ('fdb_entries_added', (YLeaf(YType.uint32, 'fdb-entries-added'), ['int'])),
                                    ('fdb_entries_deleted', (YLeaf(YType.uint32, 'fdb-entries-deleted'), ['int'])),
                                    ('fdb_entries_updated', (YLeaf(YType.uint32, 'fdb-entries-updated'), ['int'])),
                                    ('fdb_flushes', (YLeaf(YType.uint32, 'fdb-flushes'), ['int'])),
                                    ('fdb_address_updates', (YLeaf(YType.uint32, 'fdb-address-updates'), ['int'])),
                                    ('fdb_new_addresses', (YLeaf(YType.uint32, 'fdb-new-addresses'), ['int'])),
                                    ('fdb_aged_updates', (YLeaf(YType.uint32, 'fdb-aged-updates'), ['int'])),
                                    ('fdb_transplant_updates', (YLeaf(YType.uint32, 'fdb-transplant-updates'), ['int'])),
                                    ('fdb_forwarding_updates', (YLeaf(YType.uint32, 'fdb-forwarding-updates'), ['int'])),
                                    ('fdb_address_insert_errors', (YLeaf(YType.uint32, 'fdb-address-insert-errors'), ['int'])),
                                    ('fdb_address_update_errors', (YLeaf(YType.uint32, 'fdb-address-update-errors'), ['int'])),
                                    ('fdb_memory_errors', (YLeaf(YType.uint32, 'fdb-memory-errors'), ['int'])),
                                    ('fdb_allocation_errors', (YLeaf(YType.uint32, 'fdb-allocation-errors'), ['int'])),
                                    ('fdb_address_updates_queued', (YLeaf(YType.uint32, 'fdb-address-updates-queued'), ['int'])),
                                    ('fdb_address_queue_full', (YLeaf(YType.enumeration, 'fdb-address-queue-full'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                    ('fdb_forwarding_updates_queued', (YLeaf(YType.uint32, 'fdb-forwarding-updates-queued'), ['int'])),
                                    ('fdb_forwarding_queue_full', (YLeaf(YType.enumeration, 'fdb-forwarding-queue-full'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                ])
                                self.fdb_shadow_entries = None
                                self.fdb_max_shadow_entries = None
                                self.fdb_max_hash_chain = None
                                self.fdb_entries_added = None
                                self.fdb_entries_deleted = None
                                self.fdb_entries_updated = None
                                self.fdb_flushes = None
                                self.fdb_address_updates = None
                                self.fdb_new_addresses = None
                                self.fdb_aged_updates = None
                                self.fdb_transplant_updates = None
                                self.fdb_forwarding_updates = None
                                self.fdb_address_insert_errors = None
                                self.fdb_address_update_errors = None
                                self.fdb_memory_errors = None
                                self.fdb_allocation_errors = None
                                self.fdb_address_updates_queued = None
                                self.fdb_address_queue_full = None
                                self.fdb_forwarding_updates_queued = None
                                self.fdb_forwarding_queue_full = None
                                self._segment_path = lambda: "counter-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Fdb.Statistics.Location.CounterInfo, ['fdb_shadow_entries', 'fdb_max_shadow_entries', 'fdb_max_hash_chain', 'fdb_entries_added', 'fdb_entries_deleted', 'fdb_entries_updated', 'fdb_flushes', 'fdb_address_updates', 'fdb_new_addresses', 'fdb_aged_updates', 'fdb_transplant_updates', 'fdb_forwarding_updates', 'fdb_address_insert_errors', 'fdb_address_update_errors', 'fdb_memory_errors', 'fdb_allocation_errors', 'fdb_address_updates_queued', 'fdb_address_queue_full', 'fdb_forwarding_updates_queued', 'fdb_forwarding_queue_full'], name, value)



                        class CoreId(Entity):
                            """
                            
                            
                            .. attribute:: core  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: core_entries
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: core_static_entries
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Fdb.Statistics.Location.CoreId, self).__init__()

                                self.yang_name = "core-id"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['core']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('core', (YLeaf(YType.int32, 'core'), ['int'])),
                                    ('core_entries', (YLeaf(YType.uint32, 'core-entries'), ['int'])),
                                    ('core_static_entries', (YLeaf(YType.uint32, 'core-static-entries'), ['int'])),
                                ])
                                self.core = None
                                self.core_entries = None
                                self.core_static_entries = None
                                self._segment_path = lambda: "core-id" + "[core='" + str(self.core) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Fdb.Statistics.Location.CoreId, ['core', 'core_entries', 'core_static_entries'], name, value)





                class SwitchFdbCommon(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Fdb.SwitchFdbCommon, self).__init__()

                        self.yang_name = "switch-fdb-common"
                        self.yang_parent_name = "fdb"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "switch-fdb-common"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Fdb.SwitchFdbCommon, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card to list the switch FDB information for
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: num_entries
                        
                        	Number of FDB entries in the table
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: has_trunk_entry
                        
                        	FDB entries contain an entry from the trunk
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: trunk_entry_message
                        
                        	Message displayed when an FDB entry contains an entry for a trunk member port
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: fdb_block
                        
                        	
                        	**type**\:  :py:class:`FdbBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "switch-fdb-common"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("fdb-block", ("fdb_block", Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                ('num_entries', (YLeaf(YType.uint32, 'num-entries'), ['int'])),
                                ('has_trunk_entry', (YLeaf(YType.uint8, 'has-trunk-entry'), ['int'])),
                                ('trunk_entry_message', (YLeaf(YType.str, 'trunk-entry-message'), ['str'])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None
                            self.num_entries = None
                            self.has_trunk_entry = None
                            self.trunk_entry_message = None

                            self.fdb_block = Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock()
                            self.fdb_block.parent = self
                            self._children_name_map["fdb_block"] = "fdb-block"
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/fdb/switch-fdb-common/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location, ['rack', 'card', 'switch_id', 'num_entries', 'has_trunk_entry', 'trunk_entry_message'], name, value)


                        class FdbBlock(Entity):
                            """
                            
                            
                            .. attribute:: fdb_entry
                            
                            	
                            	**type**\: list of  		 :py:class:`FdbEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock.FdbEntry>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock, self).__init__()

                                self.yang_name = "fdb-block"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("fdb-entry", ("fdb_entry", Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock.FdbEntry))])
                                self._leafs = OrderedDict()

                                self.fdb_entry = YList(self)
                                self._segment_path = lambda: "fdb-block"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock, [], name, value)


                            class FdbEntry(Entity):
                                """
                                
                                
                                .. attribute:: fdb_index  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_mac_addr
                                
                                	
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_vlan
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4095
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_vlan_hex
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4095
                                
                                	**refers to**\:  :py:class:`fdb_vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock.FdbEntry>`
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_port
                                
                                	Switch port MAC address learned on
                                	**type**\: int
                                
                                	**range:** \-1..128
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_trap_entry
                                
                                	
                                	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_static_entry
                                
                                	
                                	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: fdb_synced_cores
                                
                                	
                                	**type**\: list of int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock.FdbEntry, self).__init__()

                                    self.yang_name = "fdb-entry"
                                    self.yang_parent_name = "fdb-block"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['fdb_index']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('fdb_index', (YLeaf(YType.uint32, 'fdb-index'), ['int'])),
                                        ('fdb_mac_addr', (YLeaf(YType.str, 'fdb-mac-addr'), ['str'])),
                                        ('fdb_vlan', (YLeaf(YType.uint16, 'fdb-vlan'), ['int'])),
                                        ('fdb_vlan_hex', (YLeaf(YType.str, 'fdb-vlan-hex'), ['int'])),
                                        ('fdb_port', (YLeaf(YType.int32, 'fdb-port'), ['int'])),
                                        ('fdb_trap_entry', (YLeaf(YType.enumeration, 'fdb-trap-entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                        ('fdb_static_entry', (YLeaf(YType.enumeration, 'fdb-static-entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                        ('fdb_synced_cores', (YLeafList(YType.uint8, 'fdb-synced-cores'), ['int'])),
                                    ])
                                    self.fdb_index = None
                                    self.fdb_mac_addr = None
                                    self.fdb_vlan = None
                                    self.fdb_vlan_hex = None
                                    self.fdb_port = None
                                    self.fdb_trap_entry = None
                                    self.fdb_static_entry = None
                                    self.fdb_synced_cores = []
                                    self._segment_path = lambda: "fdb-entry" + "[fdb-index='" + str(self.fdb_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Fdb.SwitchFdbCommon.Location.FdbBlock.FdbEntry, ['fdb_index', 'fdb_mac_addr', 'fdb_vlan', 'fdb_vlan_hex', 'fdb_port', 'fdb_trap_entry', 'fdb_static_entry', 'fdb_synced_cores'], name, value)







            class Vlan(Entity):
                """
                
                
                .. attribute:: rules
                
                	
                	**type**\:  :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Rules>`
                
                	**config**\: False
                
                .. attribute:: information
                
                	
                	**type**\:  :py:class:`Information <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information>`
                
                	**config**\: False
                
                .. attribute:: vlan_detail
                
                	
                	**type**\:  :py:class:`VlanDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.VlanDetail>`
                
                	**config**\: False
                
                .. attribute:: membership
                
                	
                	**type**\:  :py:class:`Membership <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Membership>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Vlan, self).__init__()

                    self.yang_name = "vlan"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rules", ("rules", Controller.Switch.Oper.Vlan.Rules)), ("information", ("information", Controller.Switch.Oper.Vlan.Information)), ("vlan-detail", ("vlan_detail", Controller.Switch.Oper.Vlan.VlanDetail)), ("membership", ("membership", Controller.Switch.Oper.Vlan.Membership))])
                    self._leafs = OrderedDict()

                    self.rules = Controller.Switch.Oper.Vlan.Rules()
                    self.rules.parent = self
                    self._children_name_map["rules"] = "rules"

                    self.information = Controller.Switch.Oper.Vlan.Information()
                    self.information.parent = self
                    self._children_name_map["information"] = "information"

                    self.vlan_detail = Controller.Switch.Oper.Vlan.VlanDetail()
                    self.vlan_detail.parent = self
                    self._children_name_map["vlan_detail"] = "vlan-detail"

                    self.membership = Controller.Switch.Oper.Vlan.Membership()
                    self.membership.parent = self
                    self._children_name_map["membership"] = "membership"
                    self._segment_path = lambda: "vlan"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Vlan, [], name, value)


                class Rules(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Rules.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Vlan.Rules, self).__init__()

                        self.yang_name = "rules"
                        self.yang_parent_name = "vlan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Vlan.Rules.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "rules"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Vlan.Rules, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card that owns a switch of interest to display the VLAN configuration for
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: port_iter
                        
                        	
                        	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Rules.Location.PortIter>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Vlan.Rules.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rules"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Vlan.Rules.Location.PortIter))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.port_iter = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/rules/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Vlan.Rules.Location, [u'rack', u'card', u'switch_id'], name, value)


                        class PortIter(Entity):
                            """
                            
                            
                            .. attribute:: port  (key)
                            
                            	Switch port
                            	**type**\: int
                            
                            	**range:** 0..127
                            
                            	**config**\: False
                            
                            .. attribute:: vlan_id
                            
                            	
                            	**type**\: list of  		 :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Rules.Location.PortIter.VlanId>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Vlan.Rules.Location.PortIter, self).__init__()

                                self.yang_name = "port-iter"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['port']
                                self._child_classes = OrderedDict([("vlan-id", ("vlan_id", Controller.Switch.Oper.Vlan.Rules.Location.PortIter.VlanId))])
                                self._leafs = OrderedDict([
                                    ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                                ])
                                self.port = None

                                self.vlan_id = YList(self)
                                self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Vlan.Rules.Location.PortIter, [u'port'], name, value)


                            class VlanId(Entity):
                                """
                                
                                
                                .. attribute:: vlan  (key)
                                
                                	This VLAN represents a VLAN membership for this switch port. Multiple rules may exist to support this VLAN
                                	**type**\: int
                                
                                	**range:** 0..4095
                                
                                	**config**\: False
                                
                                .. attribute:: rule_id
                                
                                	
                                	**type**\: list of  		 :py:class:`RuleId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Rules.Location.PortIter.VlanId.RuleId>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Vlan.Rules.Location.PortIter.VlanId, self).__init__()

                                    self.yang_name = "vlan-id"
                                    self.yang_parent_name = "port-iter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vlan']
                                    self._child_classes = OrderedDict([("rule-id", ("rule_id", Controller.Switch.Oper.Vlan.Rules.Location.PortIter.VlanId.RuleId))])
                                    self._leafs = OrderedDict([
                                        ('vlan', (YLeaf(YType.uint16, 'vlan'), ['int'])),
                                    ])
                                    self.vlan = None

                                    self.rule_id = YList(self)
                                    self._segment_path = lambda: "vlan-id" + "[vlan='" + str(self.vlan) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Vlan.Rules.Location.PortIter.VlanId, [u'vlan'], name, value)


                                class RuleId(Entity):
                                    """
                                    
                                    
                                    .. attribute:: direction
                                    
                                    	Packet direction this rule applies to
                                    	**type**\:  :py:class:`SwitchDataDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchDataDirectionEnum>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: match_table
                                    
                                    	
                                    	**type**\:  :py:class:`SwitchTableTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchTableTypeEnum>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: match_type
                                    
                                    	
                                    	**type**\:  :py:class:`SwitchMatchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchMatchTypeEnum>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: match_vlan_id
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4095
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: action
                                    
                                    	
                                    	**type**\:  :py:class:`SwitchActionTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchActionTypeEnum>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: action_vlan_id
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4095
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Vlan.Rules.Location.PortIter.VlanId.RuleId, self).__init__()

                                        self.yang_name = "rule-id"
                                        self.yang_parent_name = "vlan-id"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchDataDirectionEnum', '')])),
                                            ('match_table', (YLeaf(YType.enumeration, 'match-table'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchTableTypeEnum', '')])),
                                            ('match_type', (YLeaf(YType.enumeration, 'match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchMatchTypeEnum', '')])),
                                            ('match_vlan_id', (YLeaf(YType.uint16, 'match-vlan-id'), ['int'])),
                                            ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchActionTypeEnum', '')])),
                                            ('action_vlan_id', (YLeaf(YType.uint16, 'action-vlan-id'), ['int'])),
                                        ])
                                        self.direction = None
                                        self.match_table = None
                                        self.match_type = None
                                        self.match_vlan_id = None
                                        self.action = None
                                        self.action_vlan_id = None
                                        self._segment_path = lambda: "rule-id"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Vlan.Rules.Location.PortIter.VlanId.RuleId, [u'direction', u'match_table', u'match_type', u'match_vlan_id', u'action', u'action_vlan_id'], name, value)







                class Information(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information.Location>`
                    
                    	**config**\: False
                    
                    .. attribute:: summary
                    
                    	
                    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information.Summary>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Vlan.Information, self).__init__()

                        self.yang_name = "information"
                        self.yang_parent_name = "vlan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Vlan.Information.Location)), ("summary", ("summary", Controller.Switch.Oper.Vlan.Information.Summary))])
                        self._leafs = OrderedDict()

                        self.summary = Controller.Switch.Oper.Vlan.Information.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"

                        self.location = YList(self)
                        self._segment_path = lambda: "information"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Vlan.Information, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card to list the switch VLAN information for
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: serial_num
                        
                        	Rack serial number
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sdr_id
                        
                        	
                        	**type**\: list of  		 :py:class:`SdrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information.Location.SdrId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Vlan.Information.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("sdr-id", ("sdr_id", Controller.Switch.Oper.Vlan.Information.Location.SdrId))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                ('serial_num', (YLeaf(YType.str, 'serial-num'), ['str'])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None
                            self.serial_num = None

                            self.sdr_id = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/information/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Vlan.Information.Location, [u'rack', u'card', u'switch_id', u'serial_num'], name, value)


                        class SdrId(Entity):
                            """
                            
                            
                            .. attribute:: sdr  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: esd_sdr_name
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: vlan_id
                            
                            	
                            	**type**\: list of  		 :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information.Location.SdrId.VlanId>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Vlan.Information.Location.SdrId, self).__init__()

                                self.yang_name = "sdr-id"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sdr']
                                self._child_classes = OrderedDict([("vlan-id", ("vlan_id", Controller.Switch.Oper.Vlan.Information.Location.SdrId.VlanId))])
                                self._leafs = OrderedDict([
                                    ('sdr', (YLeaf(YType.uint8, 'sdr'), ['int'])),
                                    ('esd_sdr_name', (YLeaf(YType.str, 'esd-sdr-name'), ['str'])),
                                ])
                                self.sdr = None
                                self.esd_sdr_name = None

                                self.vlan_id = YList(self)
                                self._segment_path = lambda: "sdr-id" + "[sdr='" + str(self.sdr) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Vlan.Information.Location.SdrId, [u'sdr', u'esd_sdr_name'], name, value)


                            class VlanId(Entity):
                                """
                                
                                
                                .. attribute:: vlan  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4095
                                
                                	**config**\: False
                                
                                .. attribute:: vlan_hex
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4095
                                
                                	**refers to**\:  :py:class:`vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information.Location.SdrId.VlanId>`
                                
                                	**config**\: False
                                
                                .. attribute:: vlan_use
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Vlan.Information.Location.SdrId.VlanId, self).__init__()

                                    self.yang_name = "vlan-id"
                                    self.yang_parent_name = "sdr-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vlan']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('vlan', (YLeaf(YType.uint16, 'vlan'), ['int'])),
                                        ('vlan_hex', (YLeaf(YType.str, 'vlan-hex'), ['int'])),
                                        ('vlan_use', (YLeaf(YType.str, 'vlan-use'), ['str'])),
                                    ])
                                    self.vlan = None
                                    self.vlan_hex = None
                                    self.vlan_use = None
                                    self._segment_path = lambda: "vlan-id" + "[vlan='" + str(self.vlan) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Vlan.Information.Location.SdrId.VlanId, [u'vlan', u'vlan_hex', u'vlan_use'], name, value)





                    class Summary(Entity):
                        """
                        
                        
                        .. attribute:: sdr_id
                        
                        	
                        	**type**\: list of  		 :py:class:`SdrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information.Summary.SdrId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Vlan.Information.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sdr-id", ("sdr_id", Controller.Switch.Oper.Vlan.Information.Summary.SdrId))])
                            self._leafs = OrderedDict()

                            self.sdr_id = YList(self)
                            self._segment_path = lambda: "summary"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/information/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Vlan.Information.Summary, [], name, value)


                        class SdrId(Entity):
                            """
                            
                            
                            .. attribute:: sdr  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: esd_sdr_name
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: vlan_id
                            
                            	
                            	**type**\: list of  		 :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information.Summary.SdrId.VlanId>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Vlan.Information.Summary.SdrId, self).__init__()

                                self.yang_name = "sdr-id"
                                self.yang_parent_name = "summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['sdr']
                                self._child_classes = OrderedDict([("vlan-id", ("vlan_id", Controller.Switch.Oper.Vlan.Information.Summary.SdrId.VlanId))])
                                self._leafs = OrderedDict([
                                    ('sdr', (YLeaf(YType.uint8, 'sdr'), ['int'])),
                                    ('esd_sdr_name', (YLeaf(YType.str, 'esd-sdr-name'), ['str'])),
                                ])
                                self.sdr = None
                                self.esd_sdr_name = None

                                self.vlan_id = YList(self)
                                self._segment_path = lambda: "sdr-id" + "[sdr='" + str(self.sdr) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/information/summary/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Vlan.Information.Summary.SdrId, [u'sdr', u'esd_sdr_name'], name, value)


                            class VlanId(Entity):
                                """
                                
                                
                                .. attribute:: vlan  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4095
                                
                                	**config**\: False
                                
                                .. attribute:: vlan_hex
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4095
                                
                                	**refers to**\:  :py:class:`vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Information.Summary.SdrId.VlanId>`
                                
                                	**config**\: False
                                
                                .. attribute:: vlan_use
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Vlan.Information.Summary.SdrId.VlanId, self).__init__()

                                    self.yang_name = "vlan-id"
                                    self.yang_parent_name = "sdr-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vlan']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('vlan', (YLeaf(YType.uint16, 'vlan'), ['int'])),
                                        ('vlan_hex', (YLeaf(YType.str, 'vlan-hex'), ['int'])),
                                        ('vlan_use', (YLeaf(YType.str, 'vlan-use'), ['str'])),
                                    ])
                                    self.vlan = None
                                    self.vlan_hex = None
                                    self.vlan_use = None
                                    self._segment_path = lambda: "vlan-id" + "[vlan='" + str(self.vlan) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Vlan.Information.Summary.SdrId.VlanId, [u'vlan', u'vlan_hex', u'vlan_use'], name, value)






                class VlanDetail(Entity):
                    """
                    
                    
                    .. attribute:: vlan_id
                    
                    	
                    	**type**\: list of  		 :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.VlanDetail.VlanId>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Vlan.VlanDetail, self).__init__()

                        self.yang_name = "vlan-detail"
                        self.yang_parent_name = "vlan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vlan-id", ("vlan_id", Controller.Switch.Oper.Vlan.VlanDetail.VlanId))])
                        self._leafs = OrderedDict()

                        self.vlan_id = YList(self)
                        self._segment_path = lambda: "vlan-detail"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Vlan.VlanDetail, [], name, value)


                    class VlanId(Entity):
                        """
                        
                        
                        .. attribute:: vlan  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4095
                        
                        	**config**\: False
                        
                        .. attribute:: rules
                        
                        	
                        	**type**\:  :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Vlan.VlanDetail.VlanId, self).__init__()

                            self.yang_name = "vlan-id"
                            self.yang_parent_name = "vlan-detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['vlan']
                            self._child_classes = OrderedDict([("rules", ("rules", Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules))])
                            self._leafs = OrderedDict([
                                ('vlan', (YLeaf(YType.uint16, 'vlan'), ['int'])),
                            ])
                            self.vlan = None

                            self.rules = Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules()
                            self.rules.parent = self
                            self._children_name_map["rules"] = "rules"
                            self._segment_path = lambda: "vlan-id" + "[vlan='" + str(self.vlan) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/vlan-detail/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Vlan.VlanDetail.VlanId, [u'vlan'], name, value)


                        class Rules(Entity):
                            """
                            
                            
                            .. attribute:: location
                            
                            	
                            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules, self).__init__()

                                self.yang_name = "rules"
                                self.yang_parent_name = "vlan-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location))])
                                self._leafs = OrderedDict()

                                self.location = YList(self)
                                self._segment_path = lambda: "rules"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules, [], name, value)


                            class Location(Entity):
                                """
                                
                                
                                .. attribute:: rack  (key)
                                
                                	
                                	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: card  (key)
                                
                                	Card that owns a switch of interest
                                	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                                
                                	**config**\: False
                                
                                .. attribute:: switch_id  (key)
                                
                                	Switch type
                                	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: port_iter
                                
                                	
                                	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location.PortIter>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location, self).__init__()

                                    self.yang_name = "location"
                                    self.yang_parent_name = "rules"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['rack','card','switch_id']
                                    self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location.PortIter))])
                                    self._leafs = OrderedDict([
                                        ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                        ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                        ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                    ])
                                    self.rack = None
                                    self.card = None
                                    self.switch_id = None

                                    self.port_iter = YList(self)
                                    self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location, [u'rack', u'card', u'switch_id'], name, value)


                                class PortIter(Entity):
                                    """
                                    
                                    
                                    .. attribute:: port  (key)
                                    
                                    	Switch port
                                    	**type**\: int
                                    
                                    	**range:** 0..127
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rule_id
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`RuleId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location.PortIter.RuleId>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location.PortIter, self).__init__()

                                        self.yang_name = "port-iter"
                                        self.yang_parent_name = "location"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['port']
                                        self._child_classes = OrderedDict([("rule-id", ("rule_id", Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location.PortIter.RuleId))])
                                        self._leafs = OrderedDict([
                                            ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                                        ])
                                        self.port = None

                                        self.rule_id = YList(self)
                                        self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location.PortIter, [u'port'], name, value)


                                    class RuleId(Entity):
                                        """
                                        
                                        
                                        .. attribute:: direction
                                        
                                        	Packet direction this rule applies to
                                        	**type**\:  :py:class:`SwitchDataDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchDataDirectionEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: match_table
                                        
                                        	
                                        	**type**\:  :py:class:`SwitchTableTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchTableTypeEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: match_type
                                        
                                        	
                                        	**type**\:  :py:class:`SwitchMatchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchMatchTypeEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: match_vlan_id
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4095
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: action
                                        
                                        	
                                        	**type**\:  :py:class:`SwitchActionTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchActionTypeEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: action_vlan_id
                                        
                                        	
                                        	**type**\: int
                                        
                                        	**range:** 0..4095
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'calvados_controllers_asr9k'
                                        _revision = '2017-11-10'

                                        def __init__(self):
                                            super(Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location.PortIter.RuleId, self).__init__()

                                            self.yang_name = "rule-id"
                                            self.yang_parent_name = "port-iter"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchDataDirectionEnum', '')])),
                                                ('match_table', (YLeaf(YType.enumeration, 'match-table'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchTableTypeEnum', '')])),
                                                ('match_type', (YLeaf(YType.enumeration, 'match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchMatchTypeEnum', '')])),
                                                ('match_vlan_id', (YLeaf(YType.uint16, 'match-vlan-id'), ['int'])),
                                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchActionTypeEnum', '')])),
                                                ('action_vlan_id', (YLeaf(YType.uint16, 'action-vlan-id'), ['int'])),
                                            ])
                                            self.direction = None
                                            self.match_table = None
                                            self.match_type = None
                                            self.match_vlan_id = None
                                            self.action = None
                                            self.action_vlan_id = None
                                            self._segment_path = lambda: "rule-id"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Controller.Switch.Oper.Vlan.VlanDetail.VlanId.Rules.Location.PortIter.RuleId, [u'direction', u'match_table', u'match_type', u'match_vlan_id', u'action', u'action_vlan_id'], name, value)








                class Membership(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Membership.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Vlan.Membership, self).__init__()

                        self.yang_name = "membership"
                        self.yang_parent_name = "vlan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Vlan.Membership.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "membership"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Vlan.Membership, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card that owns a switch of interest to display the VLAN configuration for
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: vlan_id
                        
                        	
                        	**type**\: list of  		 :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Membership.Location.VlanId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Vlan.Membership.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "membership"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("vlan-id", ("vlan_id", Controller.Switch.Oper.Vlan.Membership.Location.VlanId))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.vlan_id = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/vlan/membership/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Vlan.Membership.Location, [u'rack', u'card', u'switch_id'], name, value)


                        class VlanId(Entity):
                            """
                            
                            
                            .. attribute:: vlan  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            	**config**\: False
                            
                            .. attribute:: vlan_hex
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            	**refers to**\:  :py:class:`vlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Vlan.Membership.Location.VlanId>`
                            
                            	**config**\: False
                            
                            .. attribute:: port
                            
                            	
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Vlan.Membership.Location.VlanId, self).__init__()

                                self.yang_name = "vlan-id"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['vlan']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('vlan', (YLeaf(YType.uint16, 'vlan'), ['int'])),
                                    ('vlan_hex', (YLeaf(YType.str, 'vlan-hex'), ['int'])),
                                    ('port', (YLeafList(YType.uint8, 'port'), ['int'])),
                                ])
                                self.vlan = None
                                self.vlan_hex = None
                                self.port = []
                                self._segment_path = lambda: "vlan-id" + "[vlan='" + str(self.vlan) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Vlan.Membership.Location.VlanId, [u'vlan', u'vlan_hex', u'port'], name, value)






            class Esd(Entity):
                """
                
                
                .. attribute:: instance
                
                	show traceable process instance names
                	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Esd.Instance>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Esd, self).__init__()

                    self.yang_name = "esd"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("instance", ("instance", Controller.Switch.Oper.Esd.Instance))])
                    self._leafs = OrderedDict()

                    self.instance = YList(self)
                    self._segment_path = lambda: "esd"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Esd, [], name, value)


                class Instance(Entity):
                    """
                    show traceable process instance names
                    
                    .. attribute:: process_name  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trace
                    
                    	show traceable processes
                    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Esd.Instance.Trace>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Esd.Instance, self).__init__()

                        self.yang_name = "instance"
                        self.yang_parent_name = "esd"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['process_name']
                        self._child_classes = OrderedDict([("trace", ("trace", Controller.Switch.Oper.Esd.Instance.Trace))])
                        self._leafs = OrderedDict([
                            ('process_name', (YLeaf(YType.str, 'process_name'), ['str'])),
                        ])
                        self.process_name = None

                        self.trace = YList(self)
                        self._segment_path = lambda: "instance" + "[process_name='" + str(self.process_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/esd/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Esd.Instance, [u'process_name'], name, value)


                    class Trace(Entity):
                        """
                        show traceable processes
                        
                        .. attribute:: buffer  (key)
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: location
                        
                        	
                        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Esd.Instance.Trace.Location>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Esd.Instance.Trace, self).__init__()

                            self.yang_name = "trace"
                            self.yang_parent_name = "instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['buffer']
                            self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Esd.Instance.Trace.Location))])
                            self._leafs = OrderedDict([
                                ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                            ])
                            self.buffer = None

                            self.location = YList(self)
                            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Esd.Instance.Trace, [u'buffer'], name, value)


                        class Location(Entity):
                            """
                            
                            
                            .. attribute:: location_name  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: all_options
                            
                            	
                            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Esd.Instance.Trace.Location.AllOptions>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Esd.Instance.Trace.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['location_name']
                                self._child_classes = OrderedDict([("all-options", ("all_options", Controller.Switch.Oper.Esd.Instance.Trace.Location.AllOptions))])
                                self._leafs = OrderedDict([
                                    ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                                ])
                                self.location_name = None

                                self.all_options = YList(self)
                                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Esd.Instance.Trace.Location, [u'location_name'], name, value)


                            class AllOptions(Entity):
                                """
                                
                                
                                .. attribute:: option  (key)
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: trace_blocks
                                
                                	
                                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Esd.Instance.Trace.Location.AllOptions.TraceBlocks>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Esd.Instance.Trace.Location.AllOptions, self).__init__()

                                    self.yang_name = "all-options"
                                    self.yang_parent_name = "location"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['option']
                                    self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Controller.Switch.Oper.Esd.Instance.Trace.Location.AllOptions.TraceBlocks))])
                                    self._leafs = OrderedDict([
                                        ('option', (YLeaf(YType.str, 'option'), ['str'])),
                                    ])
                                    self.option = None

                                    self.trace_blocks = YList(self)
                                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Esd.Instance.Trace.Location.AllOptions, [u'option'], name, value)


                                class TraceBlocks(Entity):
                                    """
                                    
                                    
                                    .. attribute:: data
                                    
                                    	Trace output block
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Esd.Instance.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                                        self.yang_name = "trace-blocks"
                                        self.yang_parent_name = "all-options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('data', (YLeaf(YType.str, 'data'), ['str'])),
                                        ])
                                        self.data = None
                                        self._segment_path = lambda: "trace-blocks"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Esd.Instance.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)








            class MgmtAgent(Entity):
                """
                
                
                .. attribute:: esdma
                
                	
                	**type**\:  :py:class:`Esdma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Esdma>`
                
                	**config**\: False
                
                .. attribute:: connections
                
                	
                	**type**\:  :py:class:`Connections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Connections>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.MgmtAgent, self).__init__()

                    self.yang_name = "mgmt-agent"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("esdma", ("esdma", Controller.Switch.Oper.MgmtAgent.Esdma)), ("connections", ("connections", Controller.Switch.Oper.MgmtAgent.Connections))])
                    self._leafs = OrderedDict()

                    self.esdma = Controller.Switch.Oper.MgmtAgent.Esdma()
                    self.esdma.parent = self
                    self._children_name_map["esdma"] = "esdma"

                    self.connections = Controller.Switch.Oper.MgmtAgent.Connections()
                    self.connections.parent = self
                    self._children_name_map["connections"] = "connections"
                    self._segment_path = lambda: "mgmt-agent"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.MgmtAgent, [], name, value)


                class Esdma(Entity):
                    """
                    
                    
                    .. attribute:: trace
                    
                    	show traceable processes
                    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Esdma.Trace>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.MgmtAgent.Esdma, self).__init__()

                        self.yang_name = "esdma"
                        self.yang_parent_name = "mgmt-agent"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("trace", ("trace", Controller.Switch.Oper.MgmtAgent.Esdma.Trace))])
                        self._leafs = OrderedDict()

                        self.trace = YList(self)
                        self._segment_path = lambda: "esdma"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mgmt-agent/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Esdma, [], name, value)


                    class Trace(Entity):
                        """
                        show traceable processes
                        
                        .. attribute:: buffer  (key)
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: location
                        
                        	
                        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.MgmtAgent.Esdma.Trace, self).__init__()

                            self.yang_name = "trace"
                            self.yang_parent_name = "esdma"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['buffer']
                            self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location))])
                            self._leafs = OrderedDict([
                                ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                            ])
                            self.buffer = None

                            self.location = YList(self)
                            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mgmt-agent/esdma/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Esdma.Trace, [u'buffer'], name, value)


                        class Location(Entity):
                            """
                            
                            
                            .. attribute:: location_name  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: all_options
                            
                            	
                            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location.AllOptions>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['location_name']
                                self._child_classes = OrderedDict([("all-options", ("all_options", Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location.AllOptions))])
                                self._leafs = OrderedDict([
                                    ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                                ])
                                self.location_name = None

                                self.all_options = YList(self)
                                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location, [u'location_name'], name, value)


                            class AllOptions(Entity):
                                """
                                
                                
                                .. attribute:: option  (key)
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: trace_blocks
                                
                                	
                                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location.AllOptions.TraceBlocks>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location.AllOptions, self).__init__()

                                    self.yang_name = "all-options"
                                    self.yang_parent_name = "location"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['option']
                                    self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location.AllOptions.TraceBlocks))])
                                    self._leafs = OrderedDict([
                                        ('option', (YLeaf(YType.str, 'option'), ['str'])),
                                    ])
                                    self.option = None

                                    self.trace_blocks = YList(self)
                                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location.AllOptions, [u'option'], name, value)


                                class TraceBlocks(Entity):
                                    """
                                    
                                    
                                    .. attribute:: data
                                    
                                    	Trace output block
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                                        self.yang_name = "trace-blocks"
                                        self.yang_parent_name = "all-options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('data', (YLeaf(YType.str, 'data'), ['str'])),
                                        ])
                                        self.data = None
                                        self._segment_path = lambda: "trace-blocks"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Esdma.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)







                class Connections(Entity):
                    """
                    
                    
                    .. attribute:: esdma_info
                    
                    	
                    	**type**\:  :py:class:`EsdmaInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Connections.EsdmaInfo>`
                    
                    	**config**\: False
                    
                    .. attribute:: sdr_nm_client_id
                    
                    	
                    	**type**\: list of  		 :py:class:`SdrNmClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Connections.SdrNmClientId>`
                    
                    	**config**\: False
                    
                    .. attribute:: sdr_nm_num_clients
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: esd_client_id
                    
                    	
                    	**type**\: list of  		 :py:class:`EsdClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Connections.EsdClientId>`
                    
                    	**config**\: False
                    
                    .. attribute:: esd_client_num_clients
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: mlap_client_id
                    
                    	
                    	**type**\: list of  		 :py:class:`MlapClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.MgmtAgent.Connections.MlapClientId>`
                    
                    	**config**\: False
                    
                    .. attribute:: mlap_client_num_clients
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.MgmtAgent.Connections, self).__init__()

                        self.yang_name = "connections"
                        self.yang_parent_name = "mgmt-agent"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("esdma-info", ("esdma_info", Controller.Switch.Oper.MgmtAgent.Connections.EsdmaInfo)), ("sdr-nm-client-id", ("sdr_nm_client_id", Controller.Switch.Oper.MgmtAgent.Connections.SdrNmClientId)), ("esd-client-id", ("esd_client_id", Controller.Switch.Oper.MgmtAgent.Connections.EsdClientId)), ("mlap-client-id", ("mlap_client_id", Controller.Switch.Oper.MgmtAgent.Connections.MlapClientId))])
                        self._leafs = OrderedDict([
                            ('sdr_nm_num_clients', (YLeaf(YType.uint32, 'sdr-nm-num-clients'), ['int'])),
                            ('esd_client_num_clients', (YLeaf(YType.uint32, 'esd-client-num-clients'), ['int'])),
                            ('mlap_client_num_clients', (YLeaf(YType.uint32, 'mlap-client-num-clients'), ['int'])),
                        ])
                        self.sdr_nm_num_clients = None
                        self.esd_client_num_clients = None
                        self.mlap_client_num_clients = None

                        self.esdma_info = Controller.Switch.Oper.MgmtAgent.Connections.EsdmaInfo()
                        self.esdma_info.parent = self
                        self._children_name_map["esdma_info"] = "esdma-info"

                        self.sdr_nm_client_id = YList(self)
                        self.esd_client_id = YList(self)
                        self.mlap_client_id = YList(self)
                        self._segment_path = lambda: "connections"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mgmt-agent/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Connections, ['sdr_nm_num_clients', 'esd_client_num_clients', 'mlap_client_num_clients'], name, value)


                    class EsdmaInfo(Entity):
                        """
                        
                        
                        .. attribute:: active_esdma_address
                        
                        	
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.MgmtAgent.Connections.EsdmaInfo, self).__init__()

                            self.yang_name = "esdma-info"
                            self.yang_parent_name = "connections"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('active_esdma_address', (YLeaf(YType.str, 'active-esdma-address'), ['str','str'])),
                            ])
                            self.active_esdma_address = None
                            self._segment_path = lambda: "esdma-info"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mgmt-agent/connections/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Connections.EsdmaInfo, ['active_esdma_address'], name, value)



                    class SdrNmClientId(Entity):
                        """
                        
                        
                        .. attribute:: sdr_nm_ip_address
                        
                        	
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: sdr_nm_port_num
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.MgmtAgent.Connections.SdrNmClientId, self).__init__()

                            self.yang_name = "sdr-nm-client-id"
                            self.yang_parent_name = "connections"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sdr_nm_ip_address', (YLeaf(YType.str, 'sdr-nm-ip-address'), ['str','str'])),
                                ('sdr_nm_port_num', (YLeaf(YType.uint16, 'sdr-nm-port-num'), ['int'])),
                            ])
                            self.sdr_nm_ip_address = None
                            self.sdr_nm_port_num = None
                            self._segment_path = lambda: "sdr-nm-client-id"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mgmt-agent/connections/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Connections.SdrNmClientId, ['sdr_nm_ip_address', 'sdr_nm_port_num'], name, value)



                    class EsdClientId(Entity):
                        """
                        
                        
                        .. attribute:: esd_client_ip_address
                        
                        	
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: esd_client_port_num
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: esd_client_location
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: esd_client_switch_info_cached
                        
                        	
                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: esd_client_sdr_info_cached
                        
                        	
                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.MgmtAgent.Connections.EsdClientId, self).__init__()

                            self.yang_name = "esd-client-id"
                            self.yang_parent_name = "connections"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('esd_client_ip_address', (YLeaf(YType.str, 'esd-client-ip-address'), ['str','str'])),
                                ('esd_client_port_num', (YLeaf(YType.uint16, 'esd-client-port-num'), ['int'])),
                                ('esd_client_location', (YLeaf(YType.str, 'esd-client-location'), ['str'])),
                                ('esd_client_switch_info_cached', (YLeaf(YType.enumeration, 'esd-client-switch-info-cached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                ('esd_client_sdr_info_cached', (YLeaf(YType.enumeration, 'esd-client-sdr-info-cached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                            ])
                            self.esd_client_ip_address = None
                            self.esd_client_port_num = None
                            self.esd_client_location = None
                            self.esd_client_switch_info_cached = None
                            self.esd_client_sdr_info_cached = None
                            self._segment_path = lambda: "esd-client-id"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mgmt-agent/connections/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Connections.EsdClientId, ['esd_client_ip_address', 'esd_client_port_num', 'esd_client_location', 'esd_client_switch_info_cached', 'esd_client_sdr_info_cached'], name, value)



                    class MlapClientId(Entity):
                        """
                        
                        
                        .. attribute:: mlap_client_ip_address
                        
                        	
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: mlap_client_port_num
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: mlap_client_location
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: mlap_client_switch_info_cached
                        
                        	
                        	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.MgmtAgent.Connections.MlapClientId, self).__init__()

                            self.yang_name = "mlap-client-id"
                            self.yang_parent_name = "connections"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mlap_client_ip_address', (YLeaf(YType.str, 'mlap-client-ip-address'), ['str','str'])),
                                ('mlap_client_port_num', (YLeaf(YType.uint16, 'mlap-client-port-num'), ['int'])),
                                ('mlap_client_location', (YLeaf(YType.str, 'mlap-client-location'), ['str'])),
                                ('mlap_client_switch_info_cached', (YLeaf(YType.enumeration, 'mlap-client-switch-info-cached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                            ])
                            self.mlap_client_ip_address = None
                            self.mlap_client_port_num = None
                            self.mlap_client_location = None
                            self.mlap_client_switch_info_cached = None
                            self._segment_path = lambda: "mlap-client-id"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/mgmt-agent/connections/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.MgmtAgent.Connections.MlapClientId, ['mlap_client_ip_address', 'mlap_client_port_num', 'mlap_client_location', 'mlap_client_switch_info_cached'], name, value)





            class Sdr(Entity):
                """
                
                
                .. attribute:: port_statistics
                
                	
                	**type**\:  :py:class:`PortStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.PortStatistics>`
                
                	**config**\: False
                
                .. attribute:: global_statistics
                
                	
                	**type**\:  :py:class:`GlobalStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.GlobalStatistics>`
                
                	**config**\: False
                
                .. attribute:: policers
                
                	
                	**type**\:  :py:class:`Policers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.Policers>`
                
                	**config**\: False
                
                .. attribute:: sdr_detail
                
                	
                	**type**\:  :py:class:`SdrDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.SdrDetail>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Sdr, self).__init__()

                    self.yang_name = "sdr"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("port-statistics", ("port_statistics", Controller.Switch.Oper.Sdr.PortStatistics)), ("global-statistics", ("global_statistics", Controller.Switch.Oper.Sdr.GlobalStatistics)), ("policers", ("policers", Controller.Switch.Oper.Sdr.Policers)), ("sdr-detail", ("sdr_detail", Controller.Switch.Oper.Sdr.SdrDetail))])
                    self._leafs = OrderedDict()

                    self.port_statistics = Controller.Switch.Oper.Sdr.PortStatistics()
                    self.port_statistics.parent = self
                    self._children_name_map["port_statistics"] = "port-statistics"

                    self.global_statistics = Controller.Switch.Oper.Sdr.GlobalStatistics()
                    self.global_statistics.parent = self
                    self._children_name_map["global_statistics"] = "global-statistics"

                    self.policers = Controller.Switch.Oper.Sdr.Policers()
                    self.policers.parent = self
                    self._children_name_map["policers"] = "policers"

                    self.sdr_detail = Controller.Switch.Oper.Sdr.SdrDetail()
                    self.sdr_detail.parent = self
                    self._children_name_map["sdr_detail"] = "sdr-detail"
                    self._segment_path = lambda: "sdr"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Sdr, [], name, value)


                class PortStatistics(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.PortStatistics.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Sdr.PortStatistics, self).__init__()

                        self.yang_name = "port-statistics"
                        self.yang_parent_name = "sdr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Sdr.PortStatistics.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "port-statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/sdr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Sdr.PortStatistics, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card that owns a switch of interest to display the SDR configuration for
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: port_iter
                        
                        	
                        	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Sdr.PortStatistics.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "port-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.port_iter = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/sdr/port-statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Sdr.PortStatistics.Location, [u'rack', u'card', u'switch_id'], name, value)


                        class PortIter(Entity):
                            """
                            
                            
                            .. attribute:: port  (key)
                            
                            	Switch port
                            	**type**\: int
                            
                            	**range:** 0..127
                            
                            	**config**\: False
                            
                            .. attribute:: sdr_id
                            
                            	
                            	**type**\: list of  		 :py:class:`SdrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter, self).__init__()

                                self.yang_name = "port-iter"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['port']
                                self._child_classes = OrderedDict([("sdr-id", ("sdr_id", Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId))])
                                self._leafs = OrderedDict([
                                    ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                                ])
                                self.port = None

                                self.sdr_id = YList(self)
                                self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter, [u'port'], name, value)


                            class SdrId(Entity):
                                """
                                
                                
                                .. attribute:: sdr  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_name
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: traffic_type_id
                                
                                	
                                	**type**\: list of  		 :py:class:`TrafficTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId.TrafficTypeId>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId, self).__init__()

                                    self.yang_name = "sdr-id"
                                    self.yang_parent_name = "port-iter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['sdr']
                                    self._child_classes = OrderedDict([("traffic-type-id", ("traffic_type_id", Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId.TrafficTypeId))])
                                    self._leafs = OrderedDict([
                                        ('sdr', (YLeaf(YType.uint8, 'sdr'), ['int'])),
                                        ('esd_sdr_name', (YLeaf(YType.str, 'esd-sdr-name'), ['str'])),
                                    ])
                                    self.sdr = None
                                    self.esd_sdr_name = None

                                    self.traffic_type_id = YList(self)
                                    self._segment_path = lambda: "sdr-id" + "[sdr='" + str(self.sdr) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId, [u'sdr', u'esd_sdr_name'], name, value)


                                class TrafficTypeId(Entity):
                                    """
                                    
                                    
                                    .. attribute:: traffic_type  (key)
                                    
                                    	
                                    	**type**\:  :py:class:`EsdmaSdrTrafficType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSdrTrafficType>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: direction_id
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`DirectionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId.TrafficTypeId.DirectionId>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId.TrafficTypeId, self).__init__()

                                        self.yang_name = "traffic-type-id"
                                        self.yang_parent_name = "sdr-id"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['traffic_type']
                                        self._child_classes = OrderedDict([("direction-id", ("direction_id", Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId.TrafficTypeId.DirectionId))])
                                        self._leafs = OrderedDict([
                                            ('traffic_type', (YLeaf(YType.enumeration, 'traffic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSdrTrafficType', '')])),
                                        ])
                                        self.traffic_type = None

                                        self.direction_id = YList(self)
                                        self._segment_path = lambda: "traffic-type-id" + "[traffic-type='" + str(self.traffic_type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId.TrafficTypeId, [u'traffic_type'], name, value)


                                    class DirectionId(Entity):
                                        """
                                        
                                        
                                        .. attribute:: direction  (key)
                                        
                                        	Packet direction this rule applies to
                                        	**type**\:  :py:class:`SwitchDataDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchDataDirectionEnum>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: green_packets
                                        
                                        	Counts packets within the committed information rate for all traffic classes on this SDR
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: yellow_packets
                                        
                                        	Counts packets above the committed information rate, but within the excess information rate for all traffic classes on this SDR
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: red_packets
                                        
                                        	Counts packets above the excess information rate for all traffic classes on this SDR. Generally, these packets are dropped
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'calvados_controllers_asr9k'
                                        _revision = '2017-11-10'

                                        def __init__(self):
                                            super(Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId.TrafficTypeId.DirectionId, self).__init__()

                                            self.yang_name = "direction-id"
                                            self.yang_parent_name = "traffic-type-id"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['direction']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchDataDirectionEnum', '')])),
                                                ('green_packets', (YLeaf(YType.uint64, 'green-packets'), ['int'])),
                                                ('yellow_packets', (YLeaf(YType.uint64, 'yellow-packets'), ['int'])),
                                                ('red_packets', (YLeaf(YType.uint64, 'red-packets'), ['int'])),
                                            ])
                                            self.direction = None
                                            self.green_packets = None
                                            self.yellow_packets = None
                                            self.red_packets = None
                                            self._segment_path = lambda: "direction-id" + "[direction='" + str(self.direction) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Controller.Switch.Oper.Sdr.PortStatistics.Location.PortIter.SdrId.TrafficTypeId.DirectionId, [u'direction', u'green_packets', u'yellow_packets', u'red_packets'], name, value)








                class GlobalStatistics(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.GlobalStatistics.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Sdr.GlobalStatistics, self).__init__()

                        self.yang_name = "global-statistics"
                        self.yang_parent_name = "sdr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Sdr.GlobalStatistics.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "global-statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/sdr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Sdr.GlobalStatistics, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	Card that owns a switch of interest to display the SDR configuration for
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	Switch type
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: sdr_id
                        
                        	
                        	**type**\: list of  		 :py:class:`SdrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Sdr.GlobalStatistics.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "global-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("sdr-id", ("sdr_id", Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.sdr_id = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/sdr/global-statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Sdr.GlobalStatistics.Location, [u'rack', u'card', u'switch_id'], name, value)


                        class SdrId(Entity):
                            """
                            
                            
                            .. attribute:: sdr  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: esd_sdr_name
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: traffic_type_id
                            
                            	
                            	**type**\: list of  		 :py:class:`TrafficTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId.TrafficTypeId>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId, self).__init__()

                                self.yang_name = "sdr-id"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sdr']
                                self._child_classes = OrderedDict([("traffic-type-id", ("traffic_type_id", Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId.TrafficTypeId))])
                                self._leafs = OrderedDict([
                                    ('sdr', (YLeaf(YType.uint8, 'sdr'), ['int'])),
                                    ('esd_sdr_name', (YLeaf(YType.str, 'esd-sdr-name'), ['str'])),
                                ])
                                self.sdr = None
                                self.esd_sdr_name = None

                                self.traffic_type_id = YList(self)
                                self._segment_path = lambda: "sdr-id" + "[sdr='" + str(self.sdr) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId, [u'sdr', u'esd_sdr_name'], name, value)


                            class TrafficTypeId(Entity):
                                """
                                
                                
                                .. attribute:: traffic_type  (key)
                                
                                	
                                	**type**\:  :py:class:`EsdmaSdrTrafficType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSdrTrafficType>`
                                
                                	**config**\: False
                                
                                .. attribute:: traffic_class_id
                                
                                	
                                	**type**\: list of  		 :py:class:`TrafficClassId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId.TrafficTypeId.TrafficClassId>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId.TrafficTypeId, self).__init__()

                                    self.yang_name = "traffic-type-id"
                                    self.yang_parent_name = "sdr-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['traffic_type']
                                    self._child_classes = OrderedDict([("traffic-class-id", ("traffic_class_id", Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId.TrafficTypeId.TrafficClassId))])
                                    self._leafs = OrderedDict([
                                        ('traffic_type', (YLeaf(YType.enumeration, 'traffic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSdrTrafficType', '')])),
                                    ])
                                    self.traffic_type = None

                                    self.traffic_class_id = YList(self)
                                    self._segment_path = lambda: "traffic-type-id" + "[traffic-type='" + str(self.traffic_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId.TrafficTypeId, [u'traffic_type'], name, value)


                                class TrafficClassId(Entity):
                                    """
                                    
                                    
                                    .. attribute:: tc  (key)
                                    
                                    	Traffic class (0\->7) for these statistics
                                    	**type**\: int
                                    
                                    	**range:** \-1..7
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: green_packets
                                    
                                    	Counts packets within the committed information rate for a traffic class on this VLAN
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: yellow_packets
                                    
                                    	Counts packets above the committed information rate, but within the excess information rate for a traffic class on this VLAN
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: red_packets
                                    
                                    	Counts packets above the excess information rate for a traffic class on this VLAN. Generally, these packets are dropped
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId.TrafficTypeId.TrafficClassId, self).__init__()

                                        self.yang_name = "traffic-class-id"
                                        self.yang_parent_name = "traffic-type-id"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['tc']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('tc', (YLeaf(YType.int8, 'tc'), ['int'])),
                                            ('green_packets', (YLeaf(YType.uint64, 'green-packets'), ['int'])),
                                            ('yellow_packets', (YLeaf(YType.uint64, 'yellow-packets'), ['int'])),
                                            ('red_packets', (YLeaf(YType.uint64, 'red-packets'), ['int'])),
                                        ])
                                        self.tc = None
                                        self.green_packets = None
                                        self.yellow_packets = None
                                        self.red_packets = None
                                        self._segment_path = lambda: "traffic-class-id" + "[tc='" + str(self.tc) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Sdr.GlobalStatistics.Location.SdrId.TrafficTypeId.TrafficClassId, [u'tc', u'green_packets', u'yellow_packets', u'red_packets'], name, value)







                class Policers(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.Policers.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Sdr.Policers, self).__init__()

                        self.yang_name = "policers"
                        self.yang_parent_name = "sdr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Sdr.Policers.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "policers"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/sdr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Sdr.Policers, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rack  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: card  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                        
                        	**config**\: False
                        
                        .. attribute:: switch_id  (key)
                        
                        	
                        	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                        
                        	**config**\: False
                        
                        .. attribute:: esd_policer_status
                        
                        	
                        	**type**\:  :py:class:`EsdPolicerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus>`
                        
                        	**config**\: False
                        
                        .. attribute:: sdr_id
                        
                        	
                        	**type**\: list of  		 :py:class:`SdrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.Policers.Location.SdrId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Sdr.Policers.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "policers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rack','card','switch_id']
                            self._child_classes = OrderedDict([("esd-policer-status", ("esd_policer_status", Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus)), ("sdr-id", ("sdr_id", Controller.Switch.Oper.Sdr.Policers.Location.SdrId))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ])
                            self.rack = None
                            self.card = None
                            self.switch_id = None

                            self.esd_policer_status = Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus()
                            self.esd_policer_status.parent = self
                            self._children_name_map["esd_policer_status"] = "esd-policer-status"

                            self.sdr_id = YList(self)
                            self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/sdr/policers/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Sdr.Policers.Location, [u'rack', u'card', u'switch_id'], name, value)


                        class EsdPolicerStatus(Entity):
                            """
                            
                            
                            .. attribute:: indent_group
                            
                            	
                            	**type**\:  :py:class:`IndentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus.IndentGroup>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus, self).__init__()

                                self.yang_name = "esd-policer-status"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("indent-group", ("indent_group", Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus.IndentGroup))])
                                self._leafs = OrderedDict()

                                self.indent_group = Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus.IndentGroup()
                                self.indent_group.parent = self
                                self._children_name_map["indent_group"] = "indent-group"
                                self._segment_path = lambda: "esd-policer-status"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus, [], name, value)


                            class IndentGroup(Entity):
                                """
                                
                                
                                .. attribute:: esd_port_policing_enabled
                                
                                	
                                	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: esd_port_committed_burst_size
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: esd_port_peak_burst_size
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: esd_port_policer_mru
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: esd_global_policing_enabled
                                
                                	
                                	**type**\:  :py:class:`EsdmaSwitchYesNoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchYesNoEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: esd_global_committed_burst_size
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: esd_global_peak_burst_size
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: esd_global_policer_mru
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus.IndentGroup, self).__init__()

                                    self.yang_name = "indent-group"
                                    self.yang_parent_name = "esd-policer-status"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('esd_port_policing_enabled', (YLeaf(YType.enumeration, 'esd-port-policing-enabled'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                        ('esd_port_committed_burst_size', (YLeaf(YType.uint32, 'esd-port-committed-burst-size'), ['int'])),
                                        ('esd_port_peak_burst_size', (YLeaf(YType.uint32, 'esd-port-peak-burst-size'), ['int'])),
                                        ('esd_port_policer_mru', (YLeaf(YType.uint32, 'esd-port-policer-mru'), ['int'])),
                                        ('esd_global_policing_enabled', (YLeaf(YType.enumeration, 'esd-global-policing-enabled'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchYesNoEnum', '')])),
                                        ('esd_global_committed_burst_size', (YLeaf(YType.uint32, 'esd-global-committed-burst-size'), ['int'])),
                                        ('esd_global_peak_burst_size', (YLeaf(YType.uint32, 'esd-global-peak-burst-size'), ['int'])),
                                        ('esd_global_policer_mru', (YLeaf(YType.uint32, 'esd-global-policer-mru'), ['int'])),
                                    ])
                                    self.esd_port_policing_enabled = None
                                    self.esd_port_committed_burst_size = None
                                    self.esd_port_peak_burst_size = None
                                    self.esd_port_policer_mru = None
                                    self.esd_global_policing_enabled = None
                                    self.esd_global_committed_burst_size = None
                                    self.esd_global_peak_burst_size = None
                                    self.esd_global_policer_mru = None
                                    self._segment_path = lambda: "indent-group"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Sdr.Policers.Location.EsdPolicerStatus.IndentGroup, [u'esd_port_policing_enabled', u'esd_port_committed_burst_size', u'esd_port_peak_burst_size', u'esd_port_policer_mru', u'esd_global_policing_enabled', u'esd_global_committed_burst_size', u'esd_global_peak_burst_size', u'esd_global_policer_mru'], name, value)




                        class SdrId(Entity):
                            """
                            
                            
                            .. attribute:: sdr  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: esd_sdr_name
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: esd_sdr_cir
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            	**config**\: False
                            
                            .. attribute:: esd_sdr_pir
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            	**config**\: False
                            
                            .. attribute:: esd_sdr_cos_type_iter
                            
                            	
                            	**type**\: list of  		 :py:class:`EsdSdrCosTypeIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.Policers.Location.SdrId.EsdSdrCosTypeIter>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Sdr.Policers.Location.SdrId, self).__init__()

                                self.yang_name = "sdr-id"
                                self.yang_parent_name = "location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sdr']
                                self._child_classes = OrderedDict([("esd-sdr-cos-type-iter", ("esd_sdr_cos_type_iter", Controller.Switch.Oper.Sdr.Policers.Location.SdrId.EsdSdrCosTypeIter))])
                                self._leafs = OrderedDict([
                                    ('sdr', (YLeaf(YType.uint8, 'sdr'), ['int'])),
                                    ('esd_sdr_name', (YLeaf(YType.str, 'esd-sdr-name'), ['str'])),
                                    ('esd_sdr_cir', (YLeaf(YType.uint8, 'esd-sdr-cir'), ['int'])),
                                    ('esd_sdr_pir', (YLeaf(YType.uint8, 'esd-sdr-pir'), ['int'])),
                                ])
                                self.sdr = None
                                self.esd_sdr_name = None
                                self.esd_sdr_cir = None
                                self.esd_sdr_pir = None

                                self.esd_sdr_cos_type_iter = YList(self)
                                self._segment_path = lambda: "sdr-id" + "[sdr='" + str(self.sdr) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Sdr.Policers.Location.SdrId, [u'sdr', u'esd_sdr_name', u'esd_sdr_cir', u'esd_sdr_pir'], name, value)


                            class EsdSdrCosTypeIter(Entity):
                                """
                                
                                
                                .. attribute:: esd_sdr_cos_type  (key)
                                
                                	
                                	**type**\:  :py:class:`EsdCirEirType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdCirEirType>`
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_cos_0
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_cos_1
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_cos_2
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_cos_3
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_cos_4
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_cos_5
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_cos_6
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                .. attribute:: esd_sdr_cos_7
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Sdr.Policers.Location.SdrId.EsdSdrCosTypeIter, self).__init__()

                                    self.yang_name = "esd-sdr-cos-type-iter"
                                    self.yang_parent_name = "sdr-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['esd_sdr_cos_type']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('esd_sdr_cos_type', (YLeaf(YType.enumeration, 'esd-sdr-cos-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdCirEirType', '')])),
                                        ('esd_sdr_cos_0', (YLeaf(YType.uint8, 'esd-sdr-cos-0'), ['int'])),
                                        ('esd_sdr_cos_1', (YLeaf(YType.uint8, 'esd-sdr-cos-1'), ['int'])),
                                        ('esd_sdr_cos_2', (YLeaf(YType.uint8, 'esd-sdr-cos-2'), ['int'])),
                                        ('esd_sdr_cos_3', (YLeaf(YType.uint8, 'esd-sdr-cos-3'), ['int'])),
                                        ('esd_sdr_cos_4', (YLeaf(YType.uint8, 'esd-sdr-cos-4'), ['int'])),
                                        ('esd_sdr_cos_5', (YLeaf(YType.uint8, 'esd-sdr-cos-5'), ['int'])),
                                        ('esd_sdr_cos_6', (YLeaf(YType.uint8, 'esd-sdr-cos-6'), ['int'])),
                                        ('esd_sdr_cos_7', (YLeaf(YType.uint8, 'esd-sdr-cos-7'), ['int'])),
                                    ])
                                    self.esd_sdr_cos_type = None
                                    self.esd_sdr_cos_0 = None
                                    self.esd_sdr_cos_1 = None
                                    self.esd_sdr_cos_2 = None
                                    self.esd_sdr_cos_3 = None
                                    self.esd_sdr_cos_4 = None
                                    self.esd_sdr_cos_5 = None
                                    self.esd_sdr_cos_6 = None
                                    self.esd_sdr_cos_7 = None
                                    self._segment_path = lambda: "esd-sdr-cos-type-iter" + "[esd-sdr-cos-type='" + str(self.esd_sdr_cos_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Sdr.Policers.Location.SdrId.EsdSdrCosTypeIter, [u'esd_sdr_cos_type', u'esd_sdr_cos_0', u'esd_sdr_cos_1', u'esd_sdr_cos_2', u'esd_sdr_cos_3', u'esd_sdr_cos_4', u'esd_sdr_cos_5', u'esd_sdr_cos_6', u'esd_sdr_cos_7'], name, value)






                class SdrDetail(Entity):
                    """
                    
                    
                    .. attribute:: sdr_id
                    
                    	
                    	**type**\: list of  		 :py:class:`SdrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.SdrDetail.SdrId>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Sdr.SdrDetail, self).__init__()

                        self.yang_name = "sdr-detail"
                        self.yang_parent_name = "sdr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sdr-id", ("sdr_id", Controller.Switch.Oper.Sdr.SdrDetail.SdrId))])
                        self._leafs = OrderedDict()

                        self.sdr_id = YList(self)
                        self._segment_path = lambda: "sdr-detail"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/sdr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Sdr.SdrDetail, [], name, value)


                    class SdrId(Entity):
                        """
                        
                        
                        .. attribute:: sdr  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: port_statistics
                        
                        	
                        	**type**\:  :py:class:`PortStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Sdr.SdrDetail.SdrId, self).__init__()

                            self.yang_name = "sdr-id"
                            self.yang_parent_name = "sdr-detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['sdr']
                            self._child_classes = OrderedDict([("port-statistics", ("port_statistics", Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics))])
                            self._leafs = OrderedDict([
                                ('sdr', (YLeaf(YType.uint8, 'sdr'), ['int'])),
                            ])
                            self.sdr = None

                            self.port_statistics = Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics()
                            self.port_statistics.parent = self
                            self._children_name_map["port_statistics"] = "port-statistics"
                            self._segment_path = lambda: "sdr-id" + "[sdr='" + str(self.sdr) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/sdr/sdr-detail/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Sdr.SdrDetail.SdrId, [u'sdr'], name, value)


                        class PortStatistics(Entity):
                            """
                            
                            
                            .. attribute:: location
                            
                            	
                            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics, self).__init__()

                                self.yang_name = "port-statistics"
                                self.yang_parent_name = "sdr-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location))])
                                self._leafs = OrderedDict()

                                self.location = YList(self)
                                self._segment_path = lambda: "port-statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics, [], name, value)


                            class Location(Entity):
                                """
                                
                                
                                .. attribute:: rack  (key)
                                
                                	
                                	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: card  (key)
                                
                                	Card that owns a switch of interest
                                	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                                
                                	**config**\: False
                                
                                .. attribute:: switch_id  (key)
                                
                                	Switch type
                                	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: port_iter
                                
                                	
                                	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location, self).__init__()

                                    self.yang_name = "location"
                                    self.yang_parent_name = "port-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['rack','card','switch_id']
                                    self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter))])
                                    self._leafs = OrderedDict([
                                        ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                        ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                        ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                    ])
                                    self.rack = None
                                    self.card = None
                                    self.switch_id = None

                                    self.port_iter = YList(self)
                                    self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location, [u'rack', u'card', u'switch_id'], name, value)


                                class PortIter(Entity):
                                    """
                                    
                                    
                                    .. attribute:: port  (key)
                                    
                                    	Switch port
                                    	**type**\: int
                                    
                                    	**range:** 0..127
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: traffic_type_id
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`TrafficTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter, self).__init__()

                                        self.yang_name = "port-iter"
                                        self.yang_parent_name = "location"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['port']
                                        self._child_classes = OrderedDict([("traffic-type-id", ("traffic_type_id", Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId))])
                                        self._leafs = OrderedDict([
                                            ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                                        ])
                                        self.port = None

                                        self.traffic_type_id = YList(self)
                                        self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter, [u'port'], name, value)


                                    class TrafficTypeId(Entity):
                                        """
                                        
                                        
                                        .. attribute:: traffic_type  (key)
                                        
                                        	
                                        	**type**\:  :py:class:`EsdmaSdrTrafficType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSdrTrafficType>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: direction_id
                                        
                                        	
                                        	**type**\: list of  		 :py:class:`DirectionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId.DirectionId>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'calvados_controllers_asr9k'
                                        _revision = '2017-11-10'

                                        def __init__(self):
                                            super(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId, self).__init__()

                                            self.yang_name = "traffic-type-id"
                                            self.yang_parent_name = "port-iter"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['traffic_type']
                                            self._child_classes = OrderedDict([("direction-id", ("direction_id", Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId.DirectionId))])
                                            self._leafs = OrderedDict([
                                                ('traffic_type', (YLeaf(YType.enumeration, 'traffic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSdrTrafficType', '')])),
                                            ])
                                            self.traffic_type = None

                                            self.direction_id = YList(self)
                                            self._segment_path = lambda: "traffic-type-id" + "[traffic-type='" + str(self.traffic_type) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId, [u'traffic_type'], name, value)


                                        class DirectionId(Entity):
                                            """
                                            
                                            
                                            .. attribute:: direction  (key)
                                            
                                            	Packet direction this rule applies to
                                            	**type**\:  :py:class:`SwitchDataDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.SwitchDataDirectionEnum>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: traffic_class_id
                                            
                                            	
                                            	**type**\: list of  		 :py:class:`TrafficClassId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId.DirectionId.TrafficClassId>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'calvados_controllers_asr9k'
                                            _revision = '2017-11-10'

                                            def __init__(self):
                                                super(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId.DirectionId, self).__init__()

                                                self.yang_name = "direction-id"
                                                self.yang_parent_name = "traffic-type-id"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['direction']
                                                self._child_classes = OrderedDict([("traffic-class-id", ("traffic_class_id", Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId.DirectionId.TrafficClassId))])
                                                self._leafs = OrderedDict([
                                                    ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'SwitchDataDirectionEnum', '')])),
                                                ])
                                                self.direction = None

                                                self.traffic_class_id = YList(self)
                                                self._segment_path = lambda: "direction-id" + "[direction='" + str(self.direction) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId.DirectionId, [u'direction'], name, value)


                                            class TrafficClassId(Entity):
                                                """
                                                
                                                
                                                .. attribute:: tc  (key)
                                                
                                                	Traffic class (0\->7) for these statistics
                                                	**type**\: int
                                                
                                                	**range:** \-1..7
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: green_packets
                                                
                                                	Counts packets within the committed information rate for a traffic class on this VLAN
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: yellow_packets
                                                
                                                	Counts packets above the committed information rate, but within the excess information rate for a traffic class on this VLAN
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: red_packets
                                                
                                                	Counts packets above the excess information rate for a traffic class on this VLAN. Generally, these packets are dropped
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'calvados_controllers_asr9k'
                                                _revision = '2017-11-10'

                                                def __init__(self):
                                                    super(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId.DirectionId.TrafficClassId, self).__init__()

                                                    self.yang_name = "traffic-class-id"
                                                    self.yang_parent_name = "direction-id"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['tc']
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('tc', (YLeaf(YType.int8, 'tc'), ['int'])),
                                                        ('green_packets', (YLeaf(YType.uint64, 'green-packets'), ['int'])),
                                                        ('yellow_packets', (YLeaf(YType.uint64, 'yellow-packets'), ['int'])),
                                                        ('red_packets', (YLeaf(YType.uint64, 'red-packets'), ['int'])),
                                                    ])
                                                    self.tc = None
                                                    self.green_packets = None
                                                    self.yellow_packets = None
                                                    self.red_packets = None
                                                    self._segment_path = lambda: "traffic-class-id" + "[tc='" + str(self.tc) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Controller.Switch.Oper.Sdr.SdrDetail.SdrId.PortStatistics.Location.PortIter.TrafficTypeId.DirectionId.TrafficClassId, [u'tc', u'green_packets', u'yellow_packets', u'red_packets'], name, value)











            class PortState(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.PortState.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.PortState, self).__init__()

                    self.yang_name = "port-state"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.PortState.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "port-state"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.PortState, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: rack  (key)
                    
                    	
                    	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                    
                    	**config**\: False
                    
                    .. attribute:: card  (key)
                    
                    	Card that owns a switch of interest
                    	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                    
                    	**config**\: False
                    
                    .. attribute:: switch_id  (key)
                    
                    	Switch type
                    	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                    
                    	**config**\: False
                    
                    .. attribute:: port_iter
                    
                    	
                    	**type**\: list of  		 :py:class:`PortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.PortState.Location.PortIter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.PortState.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "port-state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rack','card','switch_id']
                        self._child_classes = OrderedDict([("port-iter", ("port_iter", Controller.Switch.Oper.PortState.Location.PortIter))])
                        self._leafs = OrderedDict([
                            ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                            ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                            ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                        ])
                        self.rack = None
                        self.card = None
                        self.switch_id = None

                        self.port_iter = YList(self)
                        self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/port-state/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.PortState.Location, [u'rack', u'card', u'switch_id'], name, value)


                    class PortIter(Entity):
                        """
                        
                        
                        .. attribute:: port  (key)
                        
                        	Switch port
                        	**type**\: int
                        
                        	**range:** 0..127
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.PortState.Location.PortIter, self).__init__()

                            self.yang_name = "port-iter"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['port']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('port', (YLeaf(YType.int32, 'port'), ['int'])),
                            ])
                            self.port = None
                            self._segment_path = lambda: "port-iter" + "[port='" + str(self.port) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.PortState.Location.PortIter, [u'port'], name, value)





            class Trunk(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Trunk.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.Trunk, self).__init__()

                    self.yang_name = "trunk"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.Trunk.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "trunk"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.Trunk, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: rack  (key)
                    
                    	Rack to display the switch trunk group information for
                    	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                    
                    	**config**\: False
                    
                    .. attribute:: card  (key)
                    
                    	Card to display the switch trunk group information for
                    	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                    
                    	**config**\: False
                    
                    .. attribute:: switch_id  (key)
                    
                    	Switch type to display the switch trunk group information for
                    	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                    
                    	**config**\: False
                    
                    .. attribute:: trunk_member_count
                    
                    	Number of member ports in the trunk group
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: trunk_name
                    
                    	Name of the trunk group
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trunk_member_port_iter
                    
                    	
                    	**type**\: list of  		 :py:class:`TrunkMemberPortIter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.Trunk.Location.TrunkMemberPortIter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.Trunk.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "trunk"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rack','card','switch_id']
                        self._child_classes = OrderedDict([("trunk-member-port-iter", ("trunk_member_port_iter", Controller.Switch.Oper.Trunk.Location.TrunkMemberPortIter))])
                        self._leafs = OrderedDict([
                            ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                            ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                            ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                            ('trunk_member_count', (YLeaf(YType.uint32, 'trunk-member-count'), ['int'])),
                            ('trunk_name', (YLeaf(YType.str, 'trunk-name'), ['str'])),
                        ])
                        self.rack = None
                        self.card = None
                        self.switch_id = None
                        self.trunk_member_count = None
                        self.trunk_name = None

                        self.trunk_member_port_iter = YList(self)
                        self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/trunk/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.Trunk.Location, [u'rack', u'card', u'switch_id', u'trunk_member_count', u'trunk_name'], name, value)


                    class TrunkMemberPortIter(Entity):
                        """
                        
                        
                        .. attribute:: trunk_member_port  (key)
                        
                        	Trunk Member Port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: trunk_member_status
                        
                        	Trunk Member Status
                        	**type**\:  :py:class:`EsdmaTrunkMemberStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaTrunkMemberStatus>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.Trunk.Location.TrunkMemberPortIter, self).__init__()

                            self.yang_name = "trunk-member-port-iter"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['trunk_member_port']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('trunk_member_port', (YLeaf(YType.uint32, 'trunk-member-port'), ['int'])),
                                ('trunk_member_status', (YLeaf(YType.enumeration, 'trunk-member-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaTrunkMemberStatus', '')])),
                            ])
                            self.trunk_member_port = None
                            self.trunk_member_status = None
                            self._segment_path = lambda: "trunk-member-port-iter" + "[trunk-member-port='" + str(self.trunk_member_port) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.Trunk.Location.TrunkMemberPortIter, [u'trunk_member_port', u'trunk_member_status'], name, value)





            class SwitchDebugCont(Entity):
                """
                
                
                .. attribute:: debug
                
                	
                	**type**\:  :py:class:`Debug <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.SwitchDebugCont.Debug>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers_asr9k'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Controller.Switch.Oper.SwitchDebugCont, self).__init__()

                    self.yang_name = "switch-debug-cont"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("debug", ("debug", Controller.Switch.Oper.SwitchDebugCont.Debug))])
                    self._leafs = OrderedDict()

                    self.debug = Controller.Switch.Oper.SwitchDebugCont.Debug()
                    self.debug.parent = self
                    self._children_name_map["debug"] = "debug"
                    self._segment_path = lambda: "switch-debug-cont"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Switch.Oper.SwitchDebugCont, [], name, value)


                class Debug(Entity):
                    """
                    
                    
                    .. attribute:: counters
                    
                    	
                    	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.SwitchDebugCont.Debug.Counters>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers_asr9k'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Controller.Switch.Oper.SwitchDebugCont.Debug, self).__init__()

                        self.yang_name = "debug"
                        self.yang_parent_name = "switch-debug-cont"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("counters", ("counters", Controller.Switch.Oper.SwitchDebugCont.Debug.Counters))])
                        self._leafs = OrderedDict()

                        self.counters = Controller.Switch.Oper.SwitchDebugCont.Debug.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._segment_path = lambda: "debug"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/switch-debug-cont/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Switch.Oper.SwitchDebugCont.Debug, [], name, value)


                    class Counters(Entity):
                        """
                        
                        
                        .. attribute:: location
                        
                        	
                        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers_asr9k'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Controller.Switch.Oper.SwitchDebugCont.Debug.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "debug"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("location", ("location", Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location))])
                            self._leafs = OrderedDict()

                            self.location = YList(self)
                            self._segment_path = lambda: "counters"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/switch-debug-cont/debug/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Switch.Oper.SwitchDebugCont.Debug.Counters, [], name, value)


                        class Location(Entity):
                            """
                            
                            
                            .. attribute:: rack  (key)
                            
                            	
                            	**type**\:  :py:class:`EsdmaRackNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaRackNumEnum>`
                            
                            	**config**\: False
                            
                            .. attribute:: card  (key)
                            
                            	
                            	**type**\:  :py:class:`EsdmaCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaCpu>`
                            
                            	**config**\: False
                            
                            .. attribute:: switch_id  (key)
                            
                            	
                            	**type**\:  :py:class:`EsdmaSwitchTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types.EsdmaSwitchTypeEnum>`
                            
                            	**config**\: False
                            
                            .. attribute:: counters
                            
                            	
                            	**type**\:  :py:class:`Counters_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers_asr9k'
                            _revision = '2017-11-10'

                            def __init__(self):
                                super(Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['rack','card','switch_id']
                                self._child_classes = OrderedDict([("counters", ("counters", Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_))])
                                self._leafs = OrderedDict([
                                    ('rack', (YLeaf(YType.enumeration, 'rack'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaRackNumEnum', '')])),
                                    ('card', (YLeaf(YType.enumeration, 'card'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaCpu', '')])),
                                    ('switch_id', (YLeaf(YType.enumeration, 'switch-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ethsw_esdma_types', 'EsdmaSwitchTypeEnum', '')])),
                                ])
                                self.rack = None
                                self.card = None
                                self.switch_id = None

                                self.counters = Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_()
                                self.counters.parent = self
                                self._children_name_map["counters"] = "counters"
                                self._segment_path = lambda: "location" + "[rack='" + str(self.rack) + "']" + "[card='" + str(self.card) + "']" + "[switch-id='" + str(self.switch_id) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-asr9k:controller/switch/oper/switch-debug-cont/debug/counters/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location, [u'rack', u'card', u'switch_id'], name, value)


                            class Counters_(Entity):
                                """
                                
                                
                                .. attribute:: phy_polling_enabled
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: tx_thread_wdog_cnt
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: rx_thread_wdog_cnt
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: task_lock_longest_wait_time
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: task_lock_longest_wait_event
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: task_lock_longest_held_time
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: task_lock_longest_held_event
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: task_unlock_longest_wait_time
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: task_unlock_longest_wait_event
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: dma_max_rx_dequeued_per_int
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_rx_packets_dequeued
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_rx_packet_dequeue_errors
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_packets_queued
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_packets_completed
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_packet_no_msg_errors
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_packet_msg_too_big_errors
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_packet_no_buffer_errors
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_packet_queue_errors
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_packet_completion_errors
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_max_tx_freed_per_int
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_buf_alloc_count
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dma_tx_buf_free_count
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: switch_core
                                
                                	
                                	**type**\: list of  		 :py:class:`SwitchCore <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_asr9k.Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_.SwitchCore>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers_asr9k'
                                _revision = '2017-11-10'

                                def __init__(self):
                                    super(Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_, self).__init__()

                                    self.yang_name = "counters"
                                    self.yang_parent_name = "location"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("switch-core", ("switch_core", Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_.SwitchCore))])
                                    self._leafs = OrderedDict([
                                        ('phy_polling_enabled', (YLeaf(YType.boolean, 'phy-polling-enabled'), ['bool'])),
                                        ('tx_thread_wdog_cnt', (YLeaf(YType.uint64, 'tx-thread-wdog-cnt'), ['int'])),
                                        ('rx_thread_wdog_cnt', (YLeaf(YType.uint64, 'rx-thread-wdog-cnt'), ['int'])),
                                        ('task_lock_longest_wait_time', (YLeaf(YType.uint64, 'task-lock-longest-wait-time'), ['int'])),
                                        ('task_lock_longest_wait_event', (YLeaf(YType.uint32, 'task-lock-longest-wait-event'), ['int'])),
                                        ('task_lock_longest_held_time', (YLeaf(YType.uint64, 'task-lock-longest-held-time'), ['int'])),
                                        ('task_lock_longest_held_event', (YLeaf(YType.uint32, 'task-lock-longest-held-event'), ['int'])),
                                        ('task_unlock_longest_wait_time', (YLeaf(YType.uint64, 'task-unlock-longest-wait-time'), ['int'])),
                                        ('task_unlock_longest_wait_event', (YLeaf(YType.uint32, 'task-unlock-longest-wait-event'), ['int'])),
                                        ('dma_max_rx_dequeued_per_int', (YLeaf(YType.uint64, 'dma-max-rx-dequeued-per-int'), ['int'])),
                                        ('dma_rx_packets_dequeued', (YLeaf(YType.uint64, 'dma-rx-packets-dequeued'), ['int'])),
                                        ('dma_rx_packet_dequeue_errors', (YLeaf(YType.uint64, 'dma-rx-packet-dequeue-errors'), ['int'])),
                                        ('dma_tx_packets_queued', (YLeaf(YType.uint64, 'dma-tx-packets-queued'), ['int'])),
                                        ('dma_tx_packets_completed', (YLeaf(YType.uint64, 'dma-tx-packets-completed'), ['int'])),
                                        ('dma_tx_packet_no_msg_errors', (YLeaf(YType.uint64, 'dma-tx-packet-no-msg-errors'), ['int'])),
                                        ('dma_tx_packet_msg_too_big_errors', (YLeaf(YType.uint64, 'dma-tx-packet-msg-too-big-errors'), ['int'])),
                                        ('dma_tx_packet_no_buffer_errors', (YLeaf(YType.uint64, 'dma-tx-packet-no-buffer-errors'), ['int'])),
                                        ('dma_tx_packet_queue_errors', (YLeaf(YType.uint64, 'dma-tx-packet-queue-errors'), ['int'])),
                                        ('dma_tx_packet_completion_errors', (YLeaf(YType.uint64, 'dma-tx-packet-completion-errors'), ['int'])),
                                        ('dma_max_tx_freed_per_int', (YLeaf(YType.uint64, 'dma-max-tx-freed-per-int'), ['int'])),
                                        ('dma_tx_buf_alloc_count', (YLeaf(YType.uint64, 'dma-tx-buf-alloc-count'), ['int'])),
                                        ('dma_tx_buf_free_count', (YLeaf(YType.uint64, 'dma-tx-buf-free-count'), ['int'])),
                                    ])
                                    self.phy_polling_enabled = None
                                    self.tx_thread_wdog_cnt = None
                                    self.rx_thread_wdog_cnt = None
                                    self.task_lock_longest_wait_time = None
                                    self.task_lock_longest_wait_event = None
                                    self.task_lock_longest_held_time = None
                                    self.task_lock_longest_held_event = None
                                    self.task_unlock_longest_wait_time = None
                                    self.task_unlock_longest_wait_event = None
                                    self.dma_max_rx_dequeued_per_int = None
                                    self.dma_rx_packets_dequeued = None
                                    self.dma_rx_packet_dequeue_errors = None
                                    self.dma_tx_packets_queued = None
                                    self.dma_tx_packets_completed = None
                                    self.dma_tx_packet_no_msg_errors = None
                                    self.dma_tx_packet_msg_too_big_errors = None
                                    self.dma_tx_packet_no_buffer_errors = None
                                    self.dma_tx_packet_queue_errors = None
                                    self.dma_tx_packet_completion_errors = None
                                    self.dma_max_tx_freed_per_int = None
                                    self.dma_tx_buf_alloc_count = None
                                    self.dma_tx_buf_free_count = None

                                    self.switch_core = YList(self)
                                    self._segment_path = lambda: "counters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_, [u'phy_polling_enabled', u'tx_thread_wdog_cnt', u'rx_thread_wdog_cnt', u'task_lock_longest_wait_time', u'task_lock_longest_wait_event', u'task_lock_longest_held_time', u'task_lock_longest_held_event', u'task_unlock_longest_wait_time', u'task_unlock_longest_wait_event', u'dma_max_rx_dequeued_per_int', u'dma_rx_packets_dequeued', u'dma_rx_packet_dequeue_errors', u'dma_tx_packets_queued', u'dma_tx_packets_completed', u'dma_tx_packet_no_msg_errors', u'dma_tx_packet_msg_too_big_errors', u'dma_tx_packet_no_buffer_errors', u'dma_tx_packet_queue_errors', u'dma_tx_packet_completion_errors', u'dma_max_tx_freed_per_int', u'dma_tx_buf_alloc_count', u'dma_tx_buf_free_count'], name, value)


                                class SwitchCore(Entity):
                                    """
                                    
                                    
                                    .. attribute:: core  (key)
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: msi_count
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: aer_count
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hp_count
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wdog_count
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: core_task_lock_longest_wait_time
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: core_task_lock_longest_held_time
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: core_task_unlock_longest_wait_time
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers_asr9k'
                                    _revision = '2017-11-10'

                                    def __init__(self):
                                        super(Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_.SwitchCore, self).__init__()

                                        self.yang_name = "switch-core"
                                        self.yang_parent_name = "counters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['core']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('core', (YLeaf(YType.uint8, 'core'), ['int'])),
                                            ('msi_count', (YLeaf(YType.uint64, 'msi-count'), ['int'])),
                                            ('aer_count', (YLeaf(YType.uint64, 'aer-count'), ['int'])),
                                            ('hp_count', (YLeaf(YType.uint64, 'hp-count'), ['int'])),
                                            ('wdog_count', (YLeaf(YType.uint64, 'wdog-count'), ['int'])),
                                            ('core_task_lock_longest_wait_time', (YLeaf(YType.uint64, 'core-task-lock-longest-wait-time'), ['int'])),
                                            ('core_task_lock_longest_held_time', (YLeaf(YType.uint64, 'core-task-lock-longest-held-time'), ['int'])),
                                            ('core_task_unlock_longest_wait_time', (YLeaf(YType.uint64, 'core-task-unlock-longest-wait-time'), ['int'])),
                                        ])
                                        self.core = None
                                        self.msi_count = None
                                        self.aer_count = None
                                        self.hp_count = None
                                        self.wdog_count = None
                                        self.core_task_lock_longest_wait_time = None
                                        self.core_task_lock_longest_held_time = None
                                        self.core_task_unlock_longest_wait_time = None
                                        self._segment_path = lambda: "switch-core" + "[core='" + str(self.core) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Switch.Oper.SwitchDebugCont.Debug.Counters.Location.Counters_.SwitchCore, [u'core', u'msi_count', u'aer_count', u'hp_count', u'wdog_count', u'core_task_lock_longest_wait_time', u'core_task_lock_longest_held_time', u'core_task_unlock_longest_wait_time'], name, value)









    def clone_ptr(self):
        self._top_entity = Controller()
        return self._top_entity



