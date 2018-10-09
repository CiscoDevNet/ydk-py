""" Cisco_IOS_XR_config_cfgmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr package operational data.

This module contains definitions
for the following management objects\:
  config\: Configuration\-related operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Config(Entity):
    """
    Configuration\-related operational data
    
    .. attribute:: global_
    
    	Global operational data
    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global>`
    
    

    """

    _prefix = 'config-cfgmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Config, self).__init__()
        self._top_entity = None

        self.yang_name = "config"
        self.yang_parent_name = "Cisco-IOS-XR-config-cfgmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("global", ("global_", Config.Global))])
        self._leafs = OrderedDict()

        self.global_ = Config.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._segment_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Config, [], name, value)


    class Global(Entity):
        """
        Global operational data
        
        .. attribute:: validation
        
        	Configuration validation operational data
        	**type**\:  :py:class:`Validation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global.Validation>`
        
        

        """

        _prefix = 'config-cfgmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Config.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("Cisco-IOS-XR-config-valid-ccv-oper:validation", ("validation", Config.Global.Validation))])
            self._leafs = OrderedDict()

            self.validation = Config.Global.Validation()
            self.validation.parent = self
            self._children_name_map["validation"] = "Cisco-IOS-XR-config-valid-ccv-oper:validation"
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Config.Global, [], name, value)


        class Validation(Entity):
            """
            Configuration validation operational data
            
            .. attribute:: unsupported_configs
            
            	Unsupported config warnings present in running configuration
            	**type**\:  :py:class:`UnsupportedConfigs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global.Validation.UnsupportedConfigs>`
            
            .. attribute:: persistent_failures
            
            	Validation failures present in running configuration
            	**type**\:  :py:class:`PersistentFailures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global.Validation.PersistentFailures>`
            
            

            """

            _prefix = 'config-valid-ccv-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Config.Global.Validation, self).__init__()

                self.yang_name = "validation"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("unsupported-configs", ("unsupported_configs", Config.Global.Validation.UnsupportedConfigs)), ("persistent-failures", ("persistent_failures", Config.Global.Validation.PersistentFailures))])
                self._leafs = OrderedDict()

                self.unsupported_configs = Config.Global.Validation.UnsupportedConfigs()
                self.unsupported_configs.parent = self
                self._children_name_map["unsupported_configs"] = "unsupported-configs"

                self.persistent_failures = Config.Global.Validation.PersistentFailures()
                self.persistent_failures.parent = self
                self._children_name_map["persistent_failures"] = "persistent-failures"
                self._segment_path = lambda: "Cisco-IOS-XR-config-valid-ccv-oper:validation"
                self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Config.Global.Validation, [], name, value)


            class UnsupportedConfigs(Entity):
                """
                Unsupported config warnings present in running
                configuration
                
                .. attribute:: unsupported_config
                
                	Information about an unsupported warning
                	**type**\: list of  		 :py:class:`UnsupportedConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig>`
                
                

                """

                _prefix = 'config-valid-ccv-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Config.Global.Validation.UnsupportedConfigs, self).__init__()

                    self.yang_name = "unsupported-configs"
                    self.yang_parent_name = "validation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("unsupported-config", ("unsupported_config", Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig))])
                    self._leafs = OrderedDict()

                    self.unsupported_config = YList(self)
                    self._segment_path = lambda: "unsupported-configs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config/global/Cisco-IOS-XR-config-valid-ccv-oper:validation/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Config.Global.Validation.UnsupportedConfigs, [], name, value)


                class UnsupportedConfig(Entity):
                    """
                    Information about an unsupported warning
                    
                    .. attribute:: xpath  (key)
                    
                    	XPath of the unsupported configuration
                    	**type**\: str
                    
                    .. attribute:: group_name
                    
                    	The configuration group that this item is inherited from, if any
                    	**type**\: str
                    
                    .. attribute:: failure
                    
                    	Validation failures for this configuration item
                    	**type**\: list of  		 :py:class:`Failure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig.Failure>`
                    
                    

                    """

                    _prefix = 'config-valid-ccv-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig, self).__init__()

                        self.yang_name = "unsupported-config"
                        self.yang_parent_name = "unsupported-configs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['xpath']
                        self._child_classes = OrderedDict([("failure", ("failure", Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig.Failure))])
                        self._leafs = OrderedDict([
                            ('xpath', (YLeaf(YType.str, 'xpath'), ['str'])),
                            ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                        ])
                        self.xpath = None
                        self.group_name = None

                        self.failure = YList(self)
                        self._segment_path = lambda: "unsupported-config" + "[xpath='" + str(self.xpath) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config/global/Cisco-IOS-XR-config-valid-ccv-oper:validation/unsupported-configs/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig, ['xpath', 'group_name'], name, value)


                    class Failure(Entity):
                        """
                        Validation failures for this configuration item
                        
                        .. attribute:: error_app_tag
                        
                        	A unique string that identifies the error; equivalent to error\-app\-tag in RFC 6241
                        	**type**\: str
                        
                        .. attribute:: error_message
                        
                        	The error message; equivalent to error\-message in RFC 6241
                        	**type**\: str
                        
                        .. attribute:: error_severity
                        
                        	The severity of the error; equivalent to error\-severity in RFC 6241
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'config-valid-ccv-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig.Failure, self).__init__()

                            self.yang_name = "failure"
                            self.yang_parent_name = "unsupported-config"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('error_app_tag', (YLeaf(YType.str, 'error-app-tag'), ['str'])),
                                ('error_message', (YLeaf(YType.str, 'error-message'), ['str'])),
                                ('error_severity', (YLeaf(YType.str, 'error-severity'), ['str'])),
                            ])
                            self.error_app_tag = None
                            self.error_message = None
                            self.error_severity = None
                            self._segment_path = lambda: "failure"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig.Failure, ['error_app_tag', 'error_message', 'error_severity'], name, value)


            class PersistentFailures(Entity):
                """
                Validation failures present in running
                configuration
                
                .. attribute:: persistent_failure
                
                	Information about a validation failure
                	**type**\: list of  		 :py:class:`PersistentFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global.Validation.PersistentFailures.PersistentFailure>`
                
                

                """

                _prefix = 'config-valid-ccv-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Config.Global.Validation.PersistentFailures, self).__init__()

                    self.yang_name = "persistent-failures"
                    self.yang_parent_name = "validation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("persistent-failure", ("persistent_failure", Config.Global.Validation.PersistentFailures.PersistentFailure))])
                    self._leafs = OrderedDict()

                    self.persistent_failure = YList(self)
                    self._segment_path = lambda: "persistent-failures"
                    self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config/global/Cisco-IOS-XR-config-valid-ccv-oper:validation/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Config.Global.Validation.PersistentFailures, [], name, value)


                class PersistentFailure(Entity):
                    """
                    Information about a validation failure
                    
                    .. attribute:: xpath  (key)
                    
                    	XPath of the failed configuration
                    	**type**\: str
                    
                    .. attribute:: group_name
                    
                    	The configuration group that this item is inherited from, if any
                    	**type**\: str
                    
                    .. attribute:: failure
                    
                    	Validation failures for this configuration item
                    	**type**\: list of  		 :py:class:`Failure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global.Validation.PersistentFailures.PersistentFailure.Failure>`
                    
                    

                    """

                    _prefix = 'config-valid-ccv-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Config.Global.Validation.PersistentFailures.PersistentFailure, self).__init__()

                        self.yang_name = "persistent-failure"
                        self.yang_parent_name = "persistent-failures"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['xpath']
                        self._child_classes = OrderedDict([("failure", ("failure", Config.Global.Validation.PersistentFailures.PersistentFailure.Failure))])
                        self._leafs = OrderedDict([
                            ('xpath', (YLeaf(YType.str, 'xpath'), ['str'])),
                            ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                        ])
                        self.xpath = None
                        self.group_name = None

                        self.failure = YList(self)
                        self._segment_path = lambda: "persistent-failure" + "[xpath='" + str(self.xpath) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config/global/Cisco-IOS-XR-config-valid-ccv-oper:validation/persistent-failures/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Config.Global.Validation.PersistentFailures.PersistentFailure, ['xpath', 'group_name'], name, value)


                    class Failure(Entity):
                        """
                        Validation failures for this configuration item
                        
                        .. attribute:: error_app_tag
                        
                        	A unique string that identifies the error; equivalent to error\-app\-tag in RFC 6241
                        	**type**\: str
                        
                        .. attribute:: error_message
                        
                        	The error message; equivalent to error\-message in RFC 6241
                        	**type**\: str
                        
                        .. attribute:: error_severity
                        
                        	The severity of the error; equivalent to error\-severity in RFC 6241
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'config-valid-ccv-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Config.Global.Validation.PersistentFailures.PersistentFailure.Failure, self).__init__()

                            self.yang_name = "failure"
                            self.yang_parent_name = "persistent-failure"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('error_app_tag', (YLeaf(YType.str, 'error-app-tag'), ['str'])),
                                ('error_message', (YLeaf(YType.str, 'error-message'), ['str'])),
                                ('error_severity', (YLeaf(YType.str, 'error-severity'), ['str'])),
                            ])
                            self.error_app_tag = None
                            self.error_message = None
                            self.error_severity = None
                            self._segment_path = lambda: "failure"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Config.Global.Validation.PersistentFailures.PersistentFailure.Failure, ['error_app_tag', 'error_message', 'error_severity'], name, value)

    def clone_ptr(self):
        self._top_entity = Config()
        return self._top_entity

