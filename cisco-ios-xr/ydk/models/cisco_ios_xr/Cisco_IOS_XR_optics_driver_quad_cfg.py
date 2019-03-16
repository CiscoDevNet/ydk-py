""" Cisco_IOS_XR_optics_driver_quad_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR optics\-driver\-quad package configuration.

This module contains definitions
for the following management objects\:
  node\: HW module Quad Config

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Node(Entity):
    """
    HW module Quad Config
    
    .. attribute:: acts
    
    	none
    	**type**\:  :py:class:`Acts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg.Node.Acts>`
    
    

    """

    _prefix = 'optics-driver-quad-cfg'
    _revision = '2018-07-21'

    def __init__(self):
        super(Node, self).__init__()
        self._top_entity = None

        self.yang_name = "node"
        self.yang_parent_name = "Cisco-IOS-XR-optics-driver-quad-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("acts", ("acts", Node.Acts))])
        self._leafs = OrderedDict()

        self.acts = Node.Acts()
        self.acts.parent = self
        self._children_name_map["acts"] = "acts"
        self._segment_path = lambda: "Cisco-IOS-XR-optics-driver-quad-cfg:node"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Node, [], name, value)


    class Acts(Entity):
        """
        none
        
        .. attribute:: act
        
        	Nodename
        	**type**\: list of  		 :py:class:`Act <ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg.Node.Acts.Act>`
        
        

        """

        _prefix = 'optics-driver-quad-cfg'
        _revision = '2018-07-21'

        def __init__(self):
            super(Node.Acts, self).__init__()

            self.yang_name = "acts"
            self.yang_parent_name = "node"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("act", ("act", Node.Acts.Act))])
            self._leafs = OrderedDict()

            self.act = YList(self)
            self._segment_path = lambda: "acts"
            self._absolute_path = lambda: "Cisco-IOS-XR-optics-driver-quad-cfg:node/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Node.Acts, [], name, value)


        class Act(Entity):
            """
            Nodename
            
            .. attribute:: node_name  (key)
            
            	NodeName
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: quad_configs
            
            	quad configuration
            	**type**\:  :py:class:`QuadConfigs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg.Node.Acts.Act.QuadConfigs>`
            
            

            """

            _prefix = 'optics-driver-quad-cfg'
            _revision = '2018-07-21'

            def __init__(self):
                super(Node.Acts.Act, self).__init__()

                self.yang_name = "act"
                self.yang_parent_name = "acts"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("quad-configs", ("quad_configs", Node.Acts.Act.QuadConfigs))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.quad_configs = Node.Acts.Act.QuadConfigs()
                self.quad_configs.parent = self
                self._children_name_map["quad_configs"] = "quad-configs"
                self._segment_path = lambda: "act" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-optics-driver-quad-cfg:node/acts/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Node.Acts.Act, ['node_name'], name, value)


            class QuadConfigs(Entity):
                """
                quad configuration
                
                .. attribute:: quad_config
                
                	none
                	**type**\: list of  		 :py:class:`QuadConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg.Node.Acts.Act.QuadConfigs.QuadConfig>`
                
                

                """

                _prefix = 'optics-driver-quad-cfg'
                _revision = '2018-07-21'

                def __init__(self):
                    super(Node.Acts.Act.QuadConfigs, self).__init__()

                    self.yang_name = "quad-configs"
                    self.yang_parent_name = "act"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("quad-config", ("quad_config", Node.Acts.Act.QuadConfigs.QuadConfig))])
                    self._leafs = OrderedDict()

                    self.quad_config = YList(self)
                    self._segment_path = lambda: "quad-configs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Node.Acts.Act.QuadConfigs, [], name, value)


                class QuadConfig(Entity):
                    """
                    none
                    
                    .. attribute:: id1  (key)
                    
                    	none
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mode
                    
                    	select mode 10g or 25g for a quad(group of 4 ports)
                    	**type**\:  :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg.Node.Acts.Act.QuadConfigs.QuadConfig.Mode>`
                    
                    

                    """

                    _prefix = 'optics-driver-quad-cfg'
                    _revision = '2018-07-21'

                    def __init__(self):
                        super(Node.Acts.Act.QuadConfigs.QuadConfig, self).__init__()

                        self.yang_name = "quad-config"
                        self.yang_parent_name = "quad-configs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id1']
                        self._child_classes = OrderedDict([("mode", ("mode", Node.Acts.Act.QuadConfigs.QuadConfig.Mode))])
                        self._leafs = OrderedDict([
                            ('id1', (YLeaf(YType.uint32, 'id1'), ['int'])),
                        ])
                        self.id1 = None

                        self.mode = Node.Acts.Act.QuadConfigs.QuadConfig.Mode()
                        self.mode.parent = self
                        self._children_name_map["mode"] = "mode"
                        self._segment_path = lambda: "quad-config" + "[id1='" + str(self.id1) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Node.Acts.Act.QuadConfigs.QuadConfig, ['id1'], name, value)


                    class Mode(Entity):
                        """
                        select mode 10g or 25g for a quad(group of 4
                        ports).
                        
                        .. attribute:: speed
                        
                        	speed 10g or 25g
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'optics-driver-quad-cfg'
                        _revision = '2018-07-21'

                        def __init__(self):
                            super(Node.Acts.Act.QuadConfigs.QuadConfig.Mode, self).__init__()

                            self.yang_name = "mode"
                            self.yang_parent_name = "quad-config"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('speed', (YLeaf(YType.str, 'speed'), ['str'])),
                            ])
                            self.speed = None
                            self._segment_path = lambda: "mode"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Node.Acts.Act.QuadConfigs.QuadConfig.Mode, ['speed'], name, value)






    def clone_ptr(self):
        self._top_entity = Node()
        return self._top_entity



