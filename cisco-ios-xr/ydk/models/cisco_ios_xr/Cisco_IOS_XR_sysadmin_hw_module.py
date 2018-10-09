""" Cisco_IOS_XR_sysadmin_hw_module 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the top level container for
all 'hw\-module' commands for Sysadmin.

Copyright(c) 2012\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class HwModule(Entity):
    """
    
    
    .. attribute:: config
    
    	
    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config>`
    
    .. attribute:: oper
    
    	
    	**type**\:  :py:class:`Oper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Oper>`
    
    .. attribute:: shhwfpd
    
    	
    	**type**\:  :py:class:`Shhwfpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Shhwfpd>`
    
    

    """

    _prefix = 'calvados_hw_module'
    _revision = '2017-01-31'

    def __init__(self):
        super(HwModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-hw-module"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", HwModule.Config)), ("oper", ("oper", HwModule.Oper)), ("shhwfpd", ("shhwfpd", HwModule.Shhwfpd))])
        self._leafs = OrderedDict()

        self.config = HwModule.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"

        self.oper = HwModule.Oper()
        self.oper.parent = self
        self._children_name_map["oper"] = "oper"

        self.shhwfpd = HwModule.Shhwfpd()
        self.shhwfpd.parent = self
        self._children_name_map["shhwfpd"] = "shhwfpd"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HwModule, [], name, value)


    class Config(Entity):
        """
        
        
        .. attribute:: shutdown
        
        	
        	**type**\:  :py:class:`Shutdown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Shutdown>`
        
        .. attribute:: reset
        
        	
        	**type**\:  :py:class:`Reset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Reset>`
        
        .. attribute:: offline
        
        	
        	**type**\:  :py:class:`Offline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Offline>`
        
        .. attribute:: attention_led
        
        	
        	**type**\:  :py:class:`AttentionLed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.AttentionLed>`
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Location>`
        
        

        """

        _prefix = 'calvados_hw_module'
        _revision = '2017-01-31'

        def __init__(self):
            super(HwModule.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("shutdown", ("shutdown", HwModule.Config.Shutdown)), ("reset", ("reset", HwModule.Config.Reset)), ("offline", ("offline", HwModule.Config.Offline)), ("attention-led", ("attention_led", HwModule.Config.AttentionLed)), ("location", ("location", HwModule.Config.Location))])
            self._leafs = OrderedDict()

            self.shutdown = HwModule.Config.Shutdown()
            self.shutdown.parent = self
            self._children_name_map["shutdown"] = "shutdown"

            self.reset = HwModule.Config.Reset()
            self.reset.parent = self
            self._children_name_map["reset"] = "reset"

            self.offline = HwModule.Config.Offline()
            self.offline.parent = self
            self._children_name_map["offline"] = "offline"

            self.attention_led = HwModule.Config.AttentionLed()
            self.attention_led.parent = self
            self._children_name_map["attention_led"] = "attention-led"

            self.location = YList(self)
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.Config, [], name, value)


        class Shutdown(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Shutdown.Location>`
            
            

            """

            _prefix = 'calvados_hw_module'
            _revision = '2017-01-31'

            def __init__(self):
                super(HwModule.Config.Shutdown, self).__init__()

                self.yang_name = "shutdown"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", HwModule.Config.Shutdown.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "shutdown"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Config.Shutdown, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'calvados_hw_module'
                _revision = '2017-01-31'

                def __init__(self):
                    super(HwModule.Config.Shutdown.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "shutdown"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/shutdown/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.Config.Shutdown.Location, ['location'], name, value)


        class Reset(Entity):
            """
            
            
            .. attribute:: auto
            
            	
            	**type**\:  :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Reset.Auto>`
            
            

            """

            _prefix = 'calvados_hw_module'
            _revision = '2017-01-31'

            def __init__(self):
                super(HwModule.Config.Reset, self).__init__()

                self.yang_name = "reset"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("auto", ("auto", HwModule.Config.Reset.Auto))])
                self._leafs = OrderedDict()

                self.auto = HwModule.Config.Reset.Auto()
                self.auto.parent = self
                self._children_name_map["auto"] = "auto"
                self._segment_path = lambda: "reset"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Config.Reset, [], name, value)


            class Auto(Entity):
                """
                
                
                .. attribute:: disable
                
                	
                	**type**\:  :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Reset.Auto.Disable>`
                
                

                """

                _prefix = 'calvados_hw_module'
                _revision = '2017-01-31'

                def __init__(self):
                    super(HwModule.Config.Reset.Auto, self).__init__()

                    self.yang_name = "auto"
                    self.yang_parent_name = "reset"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("disable", ("disable", HwModule.Config.Reset.Auto.Disable))])
                    self._leafs = OrderedDict()

                    self.disable = HwModule.Config.Reset.Auto.Disable()
                    self.disable.parent = self
                    self._children_name_map["disable"] = "disable"
                    self._segment_path = lambda: "auto"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/reset/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.Config.Reset.Auto, [], name, value)


                class Disable(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Reset.Auto.Disable.Location>`
                    
                    

                    """

                    _prefix = 'calvados_hw_module'
                    _revision = '2017-01-31'

                    def __init__(self):
                        super(HwModule.Config.Reset.Auto.Disable, self).__init__()

                        self.yang_name = "disable"
                        self.yang_parent_name = "auto"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", HwModule.Config.Reset.Auto.Disable.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "disable"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/reset/auto/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.Config.Reset.Auto.Disable, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'calvados_hw_module'
                        _revision = '2017-01-31'

                        def __init__(self):
                            super(HwModule.Config.Reset.Auto.Disable.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "disable"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['location']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ])
                            self.location = None
                            self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/reset/auto/disable/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModule.Config.Reset.Auto.Disable.Location, ['location'], name, value)


        class Offline(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Offline.Location>`
            
            

            """

            _prefix = 'calvados_hw_module'
            _revision = '2017-01-31'

            def __init__(self):
                super(HwModule.Config.Offline, self).__init__()

                self.yang_name = "offline"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", HwModule.Config.Offline.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "offline"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Config.Offline, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'calvados_hw_module'
                _revision = '2017-01-31'

                def __init__(self):
                    super(HwModule.Config.Offline.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "offline"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/offline/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.Config.Offline.Location, ['location'], name, value)


        class AttentionLed(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.AttentionLed.Location>`
            
            

            """

            _prefix = 'calvados_hw_module'
            _revision = '2017-01-31'

            def __init__(self):
                super(HwModule.Config.AttentionLed, self).__init__()

                self.yang_name = "attention-led"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", HwModule.Config.AttentionLed.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "attention-led"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Config.AttentionLed, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ([0\-255])\|((0?[0\-9]\|1[0\-5])/(FC(0?[0\-5])))\|((0?[0\-9]\|1[0\-5])/(RP(0?[0\-1])))\|((0?[0\-9]\|1[0\-5])/(0?[0\-9]\|1[0\-5])(/[1\-2])?)\|((F[0\-3])/(FC(0?[0\-9]\|1[0\-1])))\|((F[0\-3])/(SC(0?[0\-1])))\|(0?[0\-9]/(SC(0?[0\-1])))\|(0?[0\-9]/(FT(0?[0\-2])))\|(0?[0\-9]/(PM(0?[0\-9])))
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'calvados_hw_module'
                _revision = '2017-01-31'

                def __init__(self):
                    super(HwModule.Config.AttentionLed.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "attention-led"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/attention-led/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.Config.AttentionLed.Location, ['location'], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            .. attribute:: logging
            
            	
            	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Location.Logging>`
            
            

            """

            _prefix = 'calvados_hw_module'
            _revision = '2017-01-31'

            def __init__(self):
                super(HwModule.Config.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("logging", ("logging", HwModule.Config.Location.Logging))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.logging = HwModule.Config.Location.Logging()
                self.logging.parent = self
                self._children_name_map["logging"] = "logging"
                self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Config.Location, ['location'], name, value)


            class Logging(Entity):
                """
                
                
                .. attribute:: onboard
                
                	
                	**type**\:  :py:class:`Onboard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Config.Location.Logging.Onboard>`
                
                

                """

                _prefix = 'calvados_hw_module'
                _revision = '2017-01-31'

                def __init__(self):
                    super(HwModule.Config.Location.Logging, self).__init__()

                    self.yang_name = "logging"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("onboard", ("onboard", HwModule.Config.Location.Logging.Onboard))])
                    self._leafs = OrderedDict()

                    self.onboard = HwModule.Config.Location.Logging.Onboard()
                    self.onboard.parent = self
                    self._children_name_map["onboard"] = "onboard"
                    self._segment_path = lambda: "logging"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.Config.Location.Logging, [], name, value)


                class Onboard(Entity):
                    """
                    
                    
                    .. attribute:: disable
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'calvados_hw_module'
                    _revision = '2017-01-31'

                    def __init__(self):
                        super(HwModule.Config.Location.Logging.Onboard, self).__init__()

                        self.yang_name = "onboard"
                        self.yang_parent_name = "logging"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                        ])
                        self.disable = None
                        self._segment_path = lambda: "onboard"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.Config.Location.Logging.Onboard, ['disable'], name, value)


    class Oper(Entity):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Oper.Location>`
        
        

        """

        _prefix = 'calvados_hw_module'
        _revision = '2017-01-31'

        def __init__(self):
            super(HwModule.Oper, self).__init__()

            self.yang_name = "oper"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("location", ("location", HwModule.Oper.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "oper"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.Oper, [], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            .. attribute:: actions
            
            	
            	**type**\:  :py:class:`Actions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Oper.Location.Actions>`
            
            .. attribute:: show
            
            	
            	**type**\:  :py:class:`Show <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Oper.Location.Show>`
            
            

            """

            _prefix = 'calvados_hw_module'
            _revision = '2017-01-31'

            def __init__(self):
                super(HwModule.Oper.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "oper"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("actions", ("actions", HwModule.Oper.Location.Actions)), ("show", ("show", HwModule.Oper.Location.Show))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.actions = HwModule.Oper.Location.Actions()
                self.actions.parent = self
                self._children_name_map["actions"] = "actions"

                self.show = HwModule.Oper.Location.Show()
                self.show.parent = self
                self._children_name_map["show"] = "show"
                self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/oper/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Oper.Location, ['location'], name, value)


            class Actions(Entity):
                """
                
                
                .. attribute:: cbootmedia
                
                	
                	**type**\:  :py:class:`Cbootmedia <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Oper.Location.Actions.Cbootmedia>`
                
                

                """

                _prefix = 'calvados_hw_module'
                _revision = '2017-01-31'

                def __init__(self):
                    super(HwModule.Oper.Location.Actions, self).__init__()

                    self.yang_name = "actions"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("cbootmedia", ("cbootmedia", HwModule.Oper.Location.Actions.Cbootmedia))])
                    self._leafs = OrderedDict()

                    self.cbootmedia = HwModule.Oper.Location.Actions.Cbootmedia()
                    self.cbootmedia.parent = self
                    self._children_name_map["cbootmedia"] = "cbootmedia"
                    self._segment_path = lambda: "actions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.Oper.Location.Actions, [], name, value)


                class Cbootmedia(Entity):
                    """
                    
                    
                    .. attribute:: bootmedia
                    
                    	
                    	**type**\: list of  		 :py:class:`Bootmedia <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Oper.Location.Actions.Cbootmedia.Bootmedia>`
                    
                    

                    """

                    _prefix = 'calvados_hw_module'
                    _revision = '2017-01-31'

                    def __init__(self):
                        super(HwModule.Oper.Location.Actions.Cbootmedia, self).__init__()

                        self.yang_name = "cbootmedia"
                        self.yang_parent_name = "actions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("bootmedia", ("bootmedia", HwModule.Oper.Location.Actions.Cbootmedia.Bootmedia))])
                        self._leafs = OrderedDict()

                        self.bootmedia = YList(self)
                        self._segment_path = lambda: "cbootmedia"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.Oper.Location.Actions.Cbootmedia, [], name, value)


                    class Bootmedia(Entity):
                        """
                        
                        
                        .. attribute:: bootmedium  (key)
                        
                        	
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'calvados_hw_module'
                        _revision = '2017-01-31'

                        def __init__(self):
                            super(HwModule.Oper.Location.Actions.Cbootmedia.Bootmedia, self).__init__()

                            self.yang_name = "bootmedia"
                            self.yang_parent_name = "cbootmedia"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['bootmedium']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('bootmedium', (YLeaf(YType.str, 'bootmedium'), ['str'])),
                            ])
                            self.bootmedium = None
                            self._segment_path = lambda: "bootmedia" + "[bootmedium='" + str(self.bootmedium) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModule.Oper.Location.Actions.Cbootmedia.Bootmedia, ['bootmedium'], name, value)


            class Show(Entity):
                """
                
                
                

                """

                _prefix = 'calvados_hw_module'
                _revision = '2017-01-31'

                def __init__(self):
                    super(HwModule.Oper.Location.Show, self).__init__()

                    self.yang_name = "show"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "show"
                    self._is_frozen = True


    class Shhwfpd(Entity):
        """
        
        
        .. attribute:: alocation
        
        	
        	**type**\: list of  		 :py:class:`Alocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Shhwfpd.Alocation>`
        
        .. attribute:: fpd
        
        	
        	**type**\: list of  		 :py:class:`Fpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Shhwfpd.Fpd>`
        
        

        """

        _prefix = 'calvados_hw_module'
        _revision = '2017-01-31'

        def __init__(self):
            super(HwModule.Shhwfpd, self).__init__()

            self.yang_name = "shhwfpd"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("alocation", ("alocation", HwModule.Shhwfpd.Alocation)), ("fpd", ("fpd", HwModule.Shhwfpd.Fpd))])
            self._leafs = OrderedDict()

            self.alocation = YList(self)
            self.fpd = YList(self)
            self._segment_path = lambda: "shhwfpd"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.Shhwfpd, [], name, value)


        class Alocation(Entity):
            """
            
            
            .. attribute:: locs  (key)
            
            	
            	**type**\: str
            
            .. attribute:: fpd
            
            	
            	**type**\: list of  		 :py:class:`Fpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_hw_module.HwModule.Shhwfpd.Alocation.Fpd>`
            
            

            """

            _prefix = 'calvados_hw_module'
            _revision = '2017-01-31'

            def __init__(self):
                super(HwModule.Shhwfpd.Alocation, self).__init__()

                self.yang_name = "alocation"
                self.yang_parent_name = "shhwfpd"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['locs']
                self._child_classes = OrderedDict([("fpd", ("fpd", HwModule.Shhwfpd.Alocation.Fpd))])
                self._leafs = OrderedDict([
                    ('locs', (YLeaf(YType.str, 'locs'), ['str'])),
                ])
                self.locs = None

                self.fpd = YList(self)
                self._segment_path = lambda: "alocation" + "[locs='" + str(self.locs) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/shhwfpd/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Shhwfpd.Alocation, ['locs'], name, value)


            class Fpd(Entity):
                """
                
                
                .. attribute:: fpdname  (key)
                
                	
                	**type**\: str
                
                .. attribute:: state
                
                	Status
                	**type**\: str
                
                .. attribute:: hwver
                
                	HWver
                	**type**\: str
                
                .. attribute:: fpdver
                
                	FPD ver
                	**type**\: str
                
                .. attribute:: cardname
                
                	Card type
                	**type**\: str
                
                .. attribute:: attr
                
                	Attribute
                	**type**\: str
                
                .. attribute:: fpddnld
                
                	FPD Programed
                	**type**\: str
                
                

                """

                _prefix = 'calvados_hw_module'
                _revision = '2017-01-31'

                def __init__(self):
                    super(HwModule.Shhwfpd.Alocation.Fpd, self).__init__()

                    self.yang_name = "fpd"
                    self.yang_parent_name = "alocation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['fpdname']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('fpdname', (YLeaf(YType.str, 'fpdname'), ['str'])),
                        ('state', (YLeaf(YType.str, 'state'), ['str'])),
                        ('hwver', (YLeaf(YType.str, 'hwver'), ['str'])),
                        ('fpdver', (YLeaf(YType.str, 'fpdver'), ['str'])),
                        ('cardname', (YLeaf(YType.str, 'cardname'), ['str'])),
                        ('attr', (YLeaf(YType.str, 'attr'), ['str'])),
                        ('fpddnld', (YLeaf(YType.str, 'fpddnld'), ['str'])),
                    ])
                    self.fpdname = None
                    self.state = None
                    self.hwver = None
                    self.fpdver = None
                    self.cardname = None
                    self.attr = None
                    self.fpddnld = None
                    self._segment_path = lambda: "fpd" + "[fpdname='" + str(self.fpdname) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.Shhwfpd.Alocation.Fpd, ['fpdname', 'state', 'hwver', 'fpdver', 'cardname', 'attr', 'fpddnld'], name, value)


        class Fpd(Entity):
            """
            
            
            .. attribute:: fpdname  (key)
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'calvados_hw_module'
            _revision = '2017-01-31'

            def __init__(self):
                super(HwModule.Shhwfpd.Fpd, self).__init__()

                self.yang_name = "fpd"
                self.yang_parent_name = "shhwfpd"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['fpdname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('fpdname', (YLeaf(YType.str, 'fpdname'), ['str'])),
                ])
                self.fpdname = None
                self._segment_path = lambda: "fpd" + "[fpdname='" + str(self.fpdname) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-hw-module:hw-module/shhwfpd/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Shhwfpd.Fpd, ['fpdname'], name, value)

    def clone_ptr(self):
        self._top_entity = HwModule()
        return self._top_entity

