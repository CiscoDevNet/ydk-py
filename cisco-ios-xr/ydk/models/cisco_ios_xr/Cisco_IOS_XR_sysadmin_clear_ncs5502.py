""" Cisco_IOS_XR_sysadmin_clear_ncs5502 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the top level container for
all 'clear' commands for Sysadmin.

Copyright(c) 2015\-2017 by Cisco Systems, Inc.
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
    
    	
    	**type**\:  :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller>`
    
    .. attribute:: clear_asic_errors_grp
    
    	
    	**type**\:  :py:class:`ClearAsicErrorsGrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp>`
    
    

    """

    _prefix = 'calvados_clear'
    _revision = '2017-10-11'

    def __init__(self):
        super(Clear, self).__init__()
        self._top_entity = None

        self.yang_name = "clear"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-clear-ncs5502"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("controller", ("controller", Clear.Controller)), ("clear-asic-errors-grp", ("clear_asic_errors_grp", Clear.ClearAsicErrorsGrp))])
        self._leafs = OrderedDict()

        self.controller = Clear.Controller()
        self.controller.parent = self
        self._children_name_map["controller"] = "controller"

        self.clear_asic_errors_grp = Clear.ClearAsicErrorsGrp()
        self.clear_asic_errors_grp.parent = self
        self._children_name_map["clear_asic_errors_grp"] = "clear-asic-errors-grp"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Clear, [], name, value)


    class Controller(Entity):
        """
        
        
        .. attribute:: switch
        
        	
        	**type**\:  :py:class:`Switch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Switch>`
        
        .. attribute:: fabric
        
        	Fabric resource commands
        	**type**\:  :py:class:`Fabric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Fabric>`
        
        

        """

        _prefix = 'calvados_clear'
        _revision = '2017-10-11'

        def __init__(self):
            super(Clear.Controller, self).__init__()

            self.yang_name = "controller"
            self.yang_parent_name = "clear"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("switch", ("switch", Clear.Controller.Switch)), ("fabric", ("fabric", Clear.Controller.Fabric))])
            self._leafs = OrderedDict()

            self.switch = Clear.Controller.Switch()
            self.switch.parent = self
            self._children_name_map["switch"] = "switch"

            self.fabric = Clear.Controller.Fabric()
            self.fabric.parent = self
            self._children_name_map["fabric"] = "fabric"
            self._segment_path = lambda: "controller"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Clear.Controller, [], name, value)


        class Switch(Entity):
            """
            
            
            .. attribute:: oper
            
            	Control Ethernet switch operational data
            	**type**\:  :py:class:`Oper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Switch.Oper>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_clear'
            _revision = '2017-10-11'

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
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Clear.Controller.Switch, [], name, value)


            class Oper(Entity):
                """
                Control Ethernet switch operational data.
                
                .. attribute:: fdb
                
                	
                	**type**\:  :py:class:`Fdb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Switch.Oper.Fdb>`
                
                	**config**\: False
                
                .. attribute:: statistics
                
                	
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Switch.Oper.Statistics>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_clear'
                _revision = '2017-10-11'

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
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/switch/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Controller.Switch.Oper, [], name, value)


                class Fdb(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Switch.Oper.Fdb.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

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
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/switch/oper/%s" % self._segment_path()
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
                        _revision = '2017-10-11'

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
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/switch/oper/fdb/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.Controller.Switch.Oper.Fdb.Location, ['rack', 'card', 'switch_id'], name, value)




                class Statistics(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Switch.Oper.Statistics.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

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
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/switch/oper/%s" % self._segment_path()
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
                        _revision = '2017-10-11'

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
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/switch/oper/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.Controller.Switch.Oper.Statistics.Location, ['rack', 'card', 'switch_id'], name, value)






        class Fabric(Entity):
            """
            Fabric resource commands
            
            .. attribute:: counter
            
            	
            	**type**\:  :py:class:`Counter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Fabric.Counter>`
            
            	**config**\: False
            
            .. attribute:: clear_statistics
            
            	
            	**type**\:  :py:class:`ClearStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Fabric.ClearStatistics>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_clear'
            _revision = '2017-10-11'

            def __init__(self):
                super(Clear.Controller.Fabric, self).__init__()

                self.yang_name = "fabric"
                self.yang_parent_name = "controller"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("counter", ("counter", Clear.Controller.Fabric.Counter)), ("clear_statistics", ("clear_statistics", Clear.Controller.Fabric.ClearStatistics))])
                self._leafs = OrderedDict()

                self.counter = Clear.Controller.Fabric.Counter()
                self.counter.parent = self
                self._children_name_map["counter"] = "counter"

                self.clear_statistics = Clear.Controller.Fabric.ClearStatistics()
                self.clear_statistics.parent = self
                self._children_name_map["clear_statistics"] = "clear_statistics"
                self._segment_path = lambda: "fabric"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Clear.Controller.Fabric, [], name, value)


            class Counter(Entity):
                """
                
                
                .. attribute:: plane
                
                	
                	**type**\: list of  		 :py:class:`Plane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Fabric.Counter.Plane>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_clear'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Clear.Controller.Fabric.Counter, self).__init__()

                    self.yang_name = "counter"
                    self.yang_parent_name = "fabric"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("plane", ("plane", Clear.Controller.Fabric.Counter.Plane))])
                    self._leafs = OrderedDict()

                    self.plane = YList(self)
                    self._segment_path = lambda: "counter"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/fabric/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Controller.Fabric.Counter, [], name, value)


                class Plane(Entity):
                    """
                    
                    
                    .. attribute:: planeid  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** all\|0
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.Controller.Fabric.Counter.Plane, self).__init__()

                        self.yang_name = "plane"
                        self.yang_parent_name = "counter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['planeid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('planeid', (YLeaf(YType.str, 'planeid'), ['str'])),
                        ])
                        self.planeid = None
                        self._segment_path = lambda: "plane" + "[planeid='" + str(self.planeid) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/fabric/counter/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.Controller.Fabric.Counter.Plane, [u'planeid'], name, value)




            class ClearStatistics(Entity):
                """
                
                
                .. attribute:: plane
                
                	
                	**type**\: list of  		 :py:class:`Plane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.Controller.Fabric.ClearStatistics.Plane>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_clear'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Clear.Controller.Fabric.ClearStatistics, self).__init__()

                    self.yang_name = "clear_statistics"
                    self.yang_parent_name = "fabric"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("plane", ("plane", Clear.Controller.Fabric.ClearStatistics.Plane))])
                    self._leafs = OrderedDict()

                    self.plane = YList(self)
                    self._segment_path = lambda: "clear_statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/fabric/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Controller.Fabric.ClearStatistics, [], name, value)


                class Plane(Entity):
                    """
                    
                    
                    .. attribute:: planeid  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** all\|0
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.Controller.Fabric.ClearStatistics.Plane, self).__init__()

                        self.yang_name = "plane"
                        self.yang_parent_name = "clear_statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['planeid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('planeid', (YLeaf(YType.str, 'planeid'), ['str'])),
                        ])
                        self.planeid = None
                        self._segment_path = lambda: "plane" + "[planeid='" + str(self.planeid) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/controller/fabric/clear_statistics/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.Controller.Fabric.ClearStatistics.Plane, [u'planeid'], name, value)






    class ClearAsicErrorsGrp(Entity):
        """
        
        
        .. attribute:: clear_device
        
        	
        	**type**\: list of  		 :py:class:`ClearDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice>`
        
        	**config**\: False
        
        

        """

        _prefix = 'calvados_clear'
        _revision = '2017-10-11'

        def __init__(self):
            super(Clear.ClearAsicErrorsGrp, self).__init__()

            self.yang_name = "clear-asic-errors-grp"
            self.yang_parent_name = "clear"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("clear-device", ("clear_device", Clear.ClearAsicErrorsGrp.ClearDevice))])
            self._leafs = OrderedDict()

            self.clear_device = YList(self)
            self._segment_path = lambda: "clear-asic-errors-grp"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Clear.ClearAsicErrorsGrp, [], name, value)


        class ClearDevice(Entity):
            """
            
            
            .. attribute:: device_name  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: instance
            
            	
            	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance>`
            
            	**config**\: False
            
            .. attribute:: all_instances
            
            	
            	**type**\:  :py:class:`AllInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_clear'
            _revision = '2017-10-11'

            def __init__(self):
                super(Clear.ClearAsicErrorsGrp.ClearDevice, self).__init__()

                self.yang_name = "clear-device"
                self.yang_parent_name = "clear-asic-errors-grp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['device_name']
                self._child_classes = OrderedDict([("instance", ("instance", Clear.ClearAsicErrorsGrp.ClearDevice.Instance)), ("all-instances", ("all_instances", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances))])
                self._leafs = OrderedDict([
                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                ])
                self.device_name = None

                self.all_instances = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances()
                self.all_instances.parent = self
                self._children_name_map["all_instances"] = "all-instances"

                self.instance = YList(self)
                self._segment_path = lambda: "clear-device" + "[device-name='" + str(self.device_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-clear-ncs5502:clear/clear-asic-errors-grp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice, ['device_name'], name, value)


            class Instance(Entity):
                """
                
                
                .. attribute:: instance_num  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sbe
                
                	
                	**type**\:  :py:class:`Sbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe>`
                
                	**config**\: False
                
                .. attribute:: mbe
                
                	
                	**type**\:  :py:class:`Mbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe>`
                
                	**config**\: False
                
                .. attribute:: parity
                
                	
                	**type**\:  :py:class:`Parity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity>`
                
                	**config**\: False
                
                .. attribute:: generic
                
                	
                	**type**\:  :py:class:`Generic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic>`
                
                	**config**\: False
                
                .. attribute:: crc
                
                	
                	**type**\:  :py:class:`Crc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc>`
                
                	**config**\: False
                
                .. attribute:: reset
                
                	
                	**type**\:  :py:class:`Reset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset>`
                
                	**config**\: False
                
                .. attribute:: barrier
                
                	
                	**type**\:  :py:class:`Barrier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier>`
                
                	**config**\: False
                
                .. attribute:: unexpected
                
                	
                	**type**\:  :py:class:`Unexpected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected>`
                
                	**config**\: False
                
                .. attribute:: link
                
                	
                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link>`
                
                	**config**\: False
                
                .. attribute:: oor_thresh
                
                	
                	**type**\:  :py:class:`OorThresh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh>`
                
                	**config**\: False
                
                .. attribute:: bp
                
                	
                	**type**\:  :py:class:`Bp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp>`
                
                	**config**\: False
                
                .. attribute:: io
                
                	
                	**type**\:  :py:class:`Io <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io>`
                
                	**config**\: False
                
                .. attribute:: ucode
                
                	
                	**type**\:  :py:class:`Ucode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode>`
                
                	**config**\: False
                
                .. attribute:: config
                
                	
                	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config>`
                
                	**config**\: False
                
                .. attribute:: indirect
                
                	
                	**type**\:  :py:class:`Indirect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect>`
                
                	**config**\: False
                
                .. attribute:: nonerr
                
                	
                	**type**\:  :py:class:`Nonerr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr>`
                
                	**config**\: False
                
                .. attribute:: summary
                
                	
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary>`
                
                	**config**\: False
                
                .. attribute:: all
                
                	
                	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_clear'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance, self).__init__()

                    self.yang_name = "instance"
                    self.yang_parent_name = "clear-device"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['instance_num']
                    self._child_classes = OrderedDict([("sbe", ("sbe", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe)), ("mbe", ("mbe", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe)), ("parity", ("parity", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity)), ("generic", ("generic", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic)), ("crc", ("crc", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc)), ("reset", ("reset", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset)), ("barrier", ("barrier", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier)), ("unexpected", ("unexpected", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected)), ("link", ("link", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link)), ("oor-thresh", ("oor_thresh", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh)), ("bp", ("bp", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp)), ("io", ("io", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io)), ("ucode", ("ucode", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode)), ("config", ("config", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config)), ("indirect", ("indirect", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect)), ("nonerr", ("nonerr", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr)), ("summary", ("summary", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary)), ("all", ("all", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All))])
                    self._leafs = OrderedDict([
                        ('instance_num', (YLeaf(YType.uint32, 'instance-num'), ['int'])),
                    ])
                    self.instance_num = None

                    self.sbe = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe()
                    self.sbe.parent = self
                    self._children_name_map["sbe"] = "sbe"

                    self.mbe = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe()
                    self.mbe.parent = self
                    self._children_name_map["mbe"] = "mbe"

                    self.parity = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity()
                    self.parity.parent = self
                    self._children_name_map["parity"] = "parity"

                    self.generic = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic()
                    self.generic.parent = self
                    self._children_name_map["generic"] = "generic"

                    self.crc = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc()
                    self.crc.parent = self
                    self._children_name_map["crc"] = "crc"

                    self.reset = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset()
                    self.reset.parent = self
                    self._children_name_map["reset"] = "reset"

                    self.barrier = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier()
                    self.barrier.parent = self
                    self._children_name_map["barrier"] = "barrier"

                    self.unexpected = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected()
                    self.unexpected.parent = self
                    self._children_name_map["unexpected"] = "unexpected"

                    self.link = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link()
                    self.link.parent = self
                    self._children_name_map["link"] = "link"

                    self.oor_thresh = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh()
                    self.oor_thresh.parent = self
                    self._children_name_map["oor_thresh"] = "oor-thresh"

                    self.bp = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp()
                    self.bp.parent = self
                    self._children_name_map["bp"] = "bp"

                    self.io = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io()
                    self.io.parent = self
                    self._children_name_map["io"] = "io"

                    self.ucode = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode()
                    self.ucode.parent = self
                    self._children_name_map["ucode"] = "ucode"

                    self.config = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.indirect = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect()
                    self.indirect.parent = self
                    self._children_name_map["indirect"] = "indirect"

                    self.nonerr = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr()
                    self.nonerr.parent = self
                    self._children_name_map["nonerr"] = "nonerr"

                    self.summary = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"

                    self.all = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All()
                    self.all.parent = self
                    self._children_name_map["all"] = "all"
                    self._segment_path = lambda: "instance" + "[instance-num='" + str(self.instance_num) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance, ['instance_num'], name, value)


                class Sbe(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe, self).__init__()

                        self.yang_name = "sbe"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "sbe"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "sbe"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Sbe.Location, ['location_name'], name, value)




                class Mbe(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe, self).__init__()

                        self.yang_name = "mbe"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "mbe"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "mbe"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Mbe.Location, ['location_name'], name, value)




                class Parity(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity, self).__init__()

                        self.yang_name = "parity"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "parity"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "parity"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Parity.Location, ['location_name'], name, value)




                class Generic(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic, self).__init__()

                        self.yang_name = "generic"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "generic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "generic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Generic.Location, ['location_name'], name, value)




                class Crc(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc, self).__init__()

                        self.yang_name = "crc"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "crc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "crc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Crc.Location, ['location_name'], name, value)




                class Reset(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset, self).__init__()

                        self.yang_name = "reset"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "reset"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "reset"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Reset.Location, ['location_name'], name, value)




                class Barrier(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier, self).__init__()

                        self.yang_name = "barrier"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "barrier"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "barrier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Barrier.Location, ['location_name'], name, value)




                class Unexpected(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected, self).__init__()

                        self.yang_name = "unexpected"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "unexpected"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "unexpected"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Unexpected.Location, ['location_name'], name, value)




                class Link(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link, self).__init__()

                        self.yang_name = "link"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "link"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Link.Location, ['location_name'], name, value)




                class OorThresh(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh, self).__init__()

                        self.yang_name = "oor-thresh"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "oor-thresh"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "oor-thresh"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.OorThresh.Location, ['location_name'], name, value)




                class Bp(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp, self).__init__()

                        self.yang_name = "bp"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "bp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "bp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Bp.Location, ['location_name'], name, value)




                class Io(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io, self).__init__()

                        self.yang_name = "io"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "io"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "io"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Io.Location, ['location_name'], name, value)




                class Ucode(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode, self).__init__()

                        self.yang_name = "ucode"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "ucode"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "ucode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Ucode.Location, ['location_name'], name, value)




                class Config(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "config"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Config.Location, ['location_name'], name, value)




                class Indirect(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect, self).__init__()

                        self.yang_name = "indirect"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "indirect"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "indirect"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Indirect.Location, ['location_name'], name, value)




                class Nonerr(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr, self).__init__()

                        self.yang_name = "nonerr"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "nonerr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "nonerr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Nonerr.Location, ['location_name'], name, value)




                class Summary(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.Summary.Location, ['location_name'], name, value)




                class All(Entity):
                    """
                    
                    
                    .. attribute:: history
                    
                    	
                    	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History>`
                    
                    	**config**\: False
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All, self).__init__()

                        self.yang_name = "all"
                        self.yang_parent_name = "instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("history", ("history", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History)), ("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.Location))])
                        self._leafs = OrderedDict()

                        self.history = Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"

                        self.location = YList(self)
                        self._segment_path = lambda: "all"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All, [], name, value)


                    class History(Entity):
                        """
                        
                        
                        .. attribute:: location
                        
                        	
                        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History.Location>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History, self).__init__()

                            self.yang_name = "history"
                            self.yang_parent_name = "all"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History.Location))])
                            self._leafs = OrderedDict()

                            self.location = YList(self)
                            self._segment_path = lambda: "history"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History, [], name, value)


                        class Location(Entity):
                            """
                            
                            
                            .. attribute:: location_name  (key)
                            
                            	
                            	**type**\: str
                            
                            	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_clear'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "history"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['location_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                                ])
                                self.location_name = None
                                self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.History.Location, ['location_name'], name, value)




                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "all"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.Instance.All.Location, ['location_name'], name, value)





            class AllInstances(Entity):
                """
                
                
                .. attribute:: sbe
                
                	
                	**type**\:  :py:class:`Sbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe>`
                
                	**config**\: False
                
                .. attribute:: mbe
                
                	
                	**type**\:  :py:class:`Mbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe>`
                
                	**config**\: False
                
                .. attribute:: parity
                
                	
                	**type**\:  :py:class:`Parity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity>`
                
                	**config**\: False
                
                .. attribute:: generic
                
                	
                	**type**\:  :py:class:`Generic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic>`
                
                	**config**\: False
                
                .. attribute:: crc
                
                	
                	**type**\:  :py:class:`Crc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc>`
                
                	**config**\: False
                
                .. attribute:: reset
                
                	
                	**type**\:  :py:class:`Reset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset>`
                
                	**config**\: False
                
                .. attribute:: barrier
                
                	
                	**type**\:  :py:class:`Barrier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier>`
                
                	**config**\: False
                
                .. attribute:: unexpected
                
                	
                	**type**\:  :py:class:`Unexpected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected>`
                
                	**config**\: False
                
                .. attribute:: link
                
                	
                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link>`
                
                	**config**\: False
                
                .. attribute:: oor_thresh
                
                	
                	**type**\:  :py:class:`OorThresh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh>`
                
                	**config**\: False
                
                .. attribute:: bp
                
                	
                	**type**\:  :py:class:`Bp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp>`
                
                	**config**\: False
                
                .. attribute:: io
                
                	
                	**type**\:  :py:class:`Io <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io>`
                
                	**config**\: False
                
                .. attribute:: ucode
                
                	
                	**type**\:  :py:class:`Ucode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode>`
                
                	**config**\: False
                
                .. attribute:: config
                
                	
                	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config>`
                
                	**config**\: False
                
                .. attribute:: indirect
                
                	
                	**type**\:  :py:class:`Indirect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect>`
                
                	**config**\: False
                
                .. attribute:: nonerr
                
                	
                	**type**\:  :py:class:`Nonerr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr>`
                
                	**config**\: False
                
                .. attribute:: summary
                
                	
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary>`
                
                	**config**\: False
                
                .. attribute:: all
                
                	
                	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_clear'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances, self).__init__()

                    self.yang_name = "all-instances"
                    self.yang_parent_name = "clear-device"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sbe", ("sbe", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe)), ("mbe", ("mbe", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe)), ("parity", ("parity", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity)), ("generic", ("generic", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic)), ("crc", ("crc", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc)), ("reset", ("reset", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset)), ("barrier", ("barrier", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier)), ("unexpected", ("unexpected", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected)), ("link", ("link", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link)), ("oor-thresh", ("oor_thresh", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh)), ("bp", ("bp", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp)), ("io", ("io", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io)), ("ucode", ("ucode", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode)), ("config", ("config", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config)), ("indirect", ("indirect", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect)), ("nonerr", ("nonerr", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr)), ("summary", ("summary", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary)), ("all", ("all", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All))])
                    self._leafs = OrderedDict()

                    self.sbe = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe()
                    self.sbe.parent = self
                    self._children_name_map["sbe"] = "sbe"

                    self.mbe = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe()
                    self.mbe.parent = self
                    self._children_name_map["mbe"] = "mbe"

                    self.parity = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity()
                    self.parity.parent = self
                    self._children_name_map["parity"] = "parity"

                    self.generic = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic()
                    self.generic.parent = self
                    self._children_name_map["generic"] = "generic"

                    self.crc = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc()
                    self.crc.parent = self
                    self._children_name_map["crc"] = "crc"

                    self.reset = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset()
                    self.reset.parent = self
                    self._children_name_map["reset"] = "reset"

                    self.barrier = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier()
                    self.barrier.parent = self
                    self._children_name_map["barrier"] = "barrier"

                    self.unexpected = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected()
                    self.unexpected.parent = self
                    self._children_name_map["unexpected"] = "unexpected"

                    self.link = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link()
                    self.link.parent = self
                    self._children_name_map["link"] = "link"

                    self.oor_thresh = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh()
                    self.oor_thresh.parent = self
                    self._children_name_map["oor_thresh"] = "oor-thresh"

                    self.bp = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp()
                    self.bp.parent = self
                    self._children_name_map["bp"] = "bp"

                    self.io = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io()
                    self.io.parent = self
                    self._children_name_map["io"] = "io"

                    self.ucode = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode()
                    self.ucode.parent = self
                    self._children_name_map["ucode"] = "ucode"

                    self.config = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.indirect = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect()
                    self.indirect.parent = self
                    self._children_name_map["indirect"] = "indirect"

                    self.nonerr = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr()
                    self.nonerr.parent = self
                    self._children_name_map["nonerr"] = "nonerr"

                    self.summary = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"

                    self.all = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All()
                    self.all.parent = self
                    self._children_name_map["all"] = "all"
                    self._segment_path = lambda: "all-instances"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances, [], name, value)


                class Sbe(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe, self).__init__()

                        self.yang_name = "sbe"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "sbe"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "sbe"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Sbe.Location, ['location_name'], name, value)




                class Mbe(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe, self).__init__()

                        self.yang_name = "mbe"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "mbe"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "mbe"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Mbe.Location, ['location_name'], name, value)




                class Parity(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity, self).__init__()

                        self.yang_name = "parity"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "parity"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "parity"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Parity.Location, ['location_name'], name, value)




                class Generic(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic, self).__init__()

                        self.yang_name = "generic"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "generic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "generic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Generic.Location, ['location_name'], name, value)




                class Crc(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc, self).__init__()

                        self.yang_name = "crc"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "crc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "crc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Crc.Location, ['location_name'], name, value)




                class Reset(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset, self).__init__()

                        self.yang_name = "reset"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "reset"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "reset"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Reset.Location, ['location_name'], name, value)




                class Barrier(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier, self).__init__()

                        self.yang_name = "barrier"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "barrier"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "barrier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Barrier.Location, ['location_name'], name, value)




                class Unexpected(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected, self).__init__()

                        self.yang_name = "unexpected"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "unexpected"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "unexpected"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Unexpected.Location, ['location_name'], name, value)




                class Link(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link, self).__init__()

                        self.yang_name = "link"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "link"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Link.Location, ['location_name'], name, value)




                class OorThresh(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh, self).__init__()

                        self.yang_name = "oor-thresh"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "oor-thresh"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "oor-thresh"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.OorThresh.Location, ['location_name'], name, value)




                class Bp(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp, self).__init__()

                        self.yang_name = "bp"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "bp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "bp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Bp.Location, ['location_name'], name, value)




                class Io(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io, self).__init__()

                        self.yang_name = "io"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "io"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "io"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Io.Location, ['location_name'], name, value)




                class Ucode(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode, self).__init__()

                        self.yang_name = "ucode"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "ucode"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "ucode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Ucode.Location, ['location_name'], name, value)




                class Config(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "config"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Config.Location, ['location_name'], name, value)




                class Indirect(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect, self).__init__()

                        self.yang_name = "indirect"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "indirect"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "indirect"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Indirect.Location, ['location_name'], name, value)




                class Nonerr(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr, self).__init__()

                        self.yang_name = "nonerr"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "nonerr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "nonerr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Nonerr.Location, ['location_name'], name, value)




                class Summary(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.Summary.Location, ['location_name'], name, value)




                class All(Entity):
                    """
                    
                    
                    .. attribute:: history
                    
                    	
                    	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History>`
                    
                    	**config**\: False
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.Location>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_clear'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All, self).__init__()

                        self.yang_name = "all"
                        self.yang_parent_name = "all-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("history", ("history", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History)), ("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.Location))])
                        self._leafs = OrderedDict()

                        self.history = Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"

                        self.location = YList(self)
                        self._segment_path = lambda: "all"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All, [], name, value)


                    class History(Entity):
                        """
                        
                        
                        .. attribute:: location
                        
                        	
                        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_clear_ncs5502.Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History.Location>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History, self).__init__()

                            self.yang_name = "history"
                            self.yang_parent_name = "all"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("location", ("location", Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History.Location))])
                            self._leafs = OrderedDict()

                            self.location = YList(self)
                            self._segment_path = lambda: "history"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History, [], name, value)


                        class Location(Entity):
                            """
                            
                            
                            .. attribute:: location_name  (key)
                            
                            	
                            	**type**\: str
                            
                            	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_clear'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "history"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['location_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                                ])
                                self.location_name = None
                                self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.History.Location, ['location_name'], name, value)




                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: location_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_clear'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "all"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                            ])
                            self.location_name = None
                            self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.ClearAsicErrorsGrp.ClearDevice.AllInstances.All.Location, ['location_name'], name, value)






    def clone_ptr(self):
        self._top_entity = Clear()
        return self._top_entity



