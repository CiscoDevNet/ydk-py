""" Cisco_IOS_XR_sysadmin_clear_asr9k 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the top level container for
all 'clear' commands for Sysadmin.

Copyright(c) 2012\-2016 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Clear(Entity):
    """
    
    
    .. attribute:: controller
    
    	
    	**type**\:  :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Controller>`
    
    .. attribute:: plugin
    
    	
    	**type**\:  :py:class:`Plugin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Plugin>`
    
    	**config**\: False
    
    

    """

    _prefix = 'calvados_clear'
    _revision = '2017-11-10'

    def __init__(self):
        super(Clear, self).__init__()
        self._top_entity = None

        self.yang_name = "clear"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-clear-asr9k"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("controller", ("controller", Clear.Controller)), ("plugin", ("plugin", Clear.Plugin))])
        self._leafs = OrderedDict()

        self.controller = Clear.Controller()
        self.controller.parent = self
        self._children_name_map["controller"] = "controller"

        self.plugin = Clear.Plugin()
        self.plugin.parent = self
        self._children_name_map["plugin"] = "plugin"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Clear, [], name, value)


    class Controller(Entity):
        """
        
        
        .. attribute:: switch
        
        	
        	**type**\:  :py:class:`Switch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Controller.Switch>`
        
        

        """

        _prefix = 'calvados_clear'
        _revision = '2017-11-10'

        def __init__(self):
            super(Clear.Controller, self).__init__()

            self.yang_name = "controller"
            self.yang_parent_name = "clear"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("switch", ("switch", Clear.Controller.Switch))])
            self._leafs = OrderedDict()

            self.switch = Clear.Controller.Switch()
            self.switch.parent = self
            self._children_name_map["switch"] = "switch"
            self._segment_path = lambda: "controller"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Clear.Controller, [], name, value)


        class Switch(Entity):
            """
            
            
            .. attribute:: oper
            
            	Control Ethernet switch operational data
            	**type**\:  :py:class:`Oper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Controller.Switch.Oper>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_clear'
            _revision = '2017-11-10'

            def __init__(self):
                super(Clear.Controller.Switch, self).__init__()

                self.yang_name = "switch"
                self.yang_parent_name = "controller"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("oper", ("oper", Clear.Controller.Switch.Oper))])
                self._leafs = OrderedDict()

                self.oper = Clear.Controller.Switch.Oper()
                self.oper.parent = self
                self._children_name_map["oper"] = "oper"
                self._segment_path = lambda: "switch"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/controller/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Clear.Controller.Switch, [], name, value)


            class Oper(Entity):
                """
                Control Ethernet switch operational data.
                
                .. attribute:: fdb
                
                	
                	**type**\:  :py:class:`Fdb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Controller.Switch.Oper.Fdb>`
                
                	**config**\: False
                
                .. attribute:: statistics
                
                	
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Controller.Switch.Oper.Statistics>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_clear'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Clear.Controller.Switch.Oper, self).__init__()

                    self.yang_name = "oper"
                    self.yang_parent_name = "switch"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("fdb", ("fdb", Clear.Controller.Switch.Oper.Fdb)), ("statistics", ("statistics", Clear.Controller.Switch.Oper.Statistics))])
                    self._leafs = OrderedDict()

                    self.fdb = Clear.Controller.Switch.Oper.Fdb()
                    self.fdb.parent = self
                    self._children_name_map["fdb"] = "fdb"

                    self.statistics = Clear.Controller.Switch.Oper.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._segment_path = lambda: "oper"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/controller/switch/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Controller.Switch.Oper, [], name, value)


                class Fdb(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Controller.Switch.Oper.Fdb.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Clear.Controller.Switch.Oper.Fdb, self).__init__()

                        self.yang_name = "fdb"
                        self.yang_parent_name = "oper"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.Controller.Switch.Oper.Fdb.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "fdb"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/controller/switch/oper/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.Controller.Switch.Oper.Fdb, [], name, value)


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

                        _prefix = 'calvados_clear'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Clear.Controller.Switch.Oper.Fdb.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "fdb"
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
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/controller/switch/oper/fdb/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.Controller.Switch.Oper.Fdb.Location, ['rack', 'card', 'switch_id'], name, value)




                class Statistics(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Controller.Switch.Oper.Statistics.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-11-10'

                    def __init__(self):
                        super(Clear.Controller.Switch.Oper.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "oper"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.Controller.Switch.Oper.Statistics.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/controller/switch/oper/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.Controller.Switch.Oper.Statistics, [], name, value)


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

                        _prefix = 'calvados_clear'
                        _revision = '2017-11-10'

                        def __init__(self):
                            super(Clear.Controller.Switch.Oper.Statistics.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "statistics"
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
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/controller/switch/oper/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.Controller.Switch.Oper.Statistics.Location, ['rack', 'card', 'switch_id'], name, value)







    class Plugin(Entity):
        """
        
        
        .. attribute:: slot
        
        	
        	**type**\:  :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Plugin.Slot>`
        
        	**config**\: False
        
        

        """

        _prefix = 'calvados_clear'
        _revision = '2017-11-10'

        def __init__(self):
            super(Clear.Plugin, self).__init__()

            self.yang_name = "plugin"
            self.yang_parent_name = "clear"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("slot", ("slot", Clear.Plugin.Slot))])
            self._leafs = OrderedDict()

            self.slot = Clear.Plugin.Slot()
            self.slot.parent = self
            self._children_name_map["slot"] = "slot"
            self._segment_path = lambda: "plugin"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Clear.Plugin, [], name, value)


        class Slot(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_asr9k.Clear.Plugin.Slot.Location>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_clear'
            _revision = '2017-11-10'

            def __init__(self):
                super(Clear.Plugin.Slot, self).__init__()

                self.yang_name = "slot"
                self.yang_parent_name = "plugin"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Clear.Plugin.Slot.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "slot"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/plugin/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Clear.Plugin.Slot, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_clear'
                _revision = '2017-11-10'

                def __init__(self):
                    super(Clear.Plugin.Slot.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "slot"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-asr9k:clear/plugin/slot/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Plugin.Slot.Location, ['location'], name, value)




    def clone_ptr(self):
        self._top_entity = Clear()
        return self._top_entity



