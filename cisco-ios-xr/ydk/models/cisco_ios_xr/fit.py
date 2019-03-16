""" fit 

This module contains definitions
for the Calvados model objects.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Set(Entity):
    """
    
    
    .. attribute:: asic
    
    	
    	**type**\: list of  		 :py:class:`Asic <ydk.models.cisco_ios_xr.fit.Set.Asic>`
    
    	**config**\: False
    
    

    """

    _prefix = 'fit'
    _revision = '2012-05-20'

    def __init__(self):
        super(Set, self).__init__()
        self._top_entity = None

        self.yang_name = "set"
        self.yang_parent_name = "fit"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("asic", ("asic", Set.Asic))])
        self._leafs = OrderedDict()

        self.asic = YList(self)
        self._segment_path = lambda: "fit:set"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Set, [], name, value)


    class Asic(Entity):
        """
        
        
        .. attribute:: asic_name  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: instance
        
        	
        	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance>`
        
        	**config**\: False
        
        

        """

        _prefix = 'fit'
        _revision = '2012-05-20'

        def __init__(self):
            super(Set.Asic, self).__init__()

            self.yang_name = "asic"
            self.yang_parent_name = "set"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['asic_name']
            self._child_classes = OrderedDict([("instance", ("instance", Set.Asic.Instance))])
            self._leafs = OrderedDict([
                ('asic_name', (YLeaf(YType.str, 'asic-name'), ['str'])),
            ])
            self.asic_name = None

            self.instance = YList(self)
            self._segment_path = lambda: "asic" + "[asic-name='" + str(self.asic_name) + "']"
            self._absolute_path = lambda: "fit:set/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Set.Asic, [u'asic_name'], name, value)


        class Instance(Entity):
            """
            
            
            .. attribute:: instance_ids  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: fault_injection
            
            	
            	**type**\:  :py:class:`FaultInjection <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fit'
            _revision = '2012-05-20'

            def __init__(self):
                super(Set.Asic.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "asic"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['instance_ids']
                self._child_classes = OrderedDict([("fault-injection", ("fault_injection", Set.Asic.Instance.FaultInjection))])
                self._leafs = OrderedDict([
                    ('instance_ids', (YLeaf(YType.uint32, 'instance-ids'), ['int'])),
                ])
                self.instance_ids = None

                self.fault_injection = Set.Asic.Instance.FaultInjection()
                self.fault_injection.parent = self
                self._children_name_map["fault_injection"] = "fault-injection"
                self._segment_path = lambda: "instance" + "[instance-ids='" + str(self.instance_ids) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Set.Asic.Instance, [u'instance_ids'], name, value)


            class FaultInjection(Entity):
                """
                
                
                .. attribute:: module
                
                	
                	**type**\: list of  		 :py:class:`Module <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module>`
                
                	**config**\: False
                
                

                """

                _prefix = 'fit'
                _revision = '2012-05-20'

                def __init__(self):
                    super(Set.Asic.Instance.FaultInjection, self).__init__()

                    self.yang_name = "fault-injection"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("module", ("module", Set.Asic.Instance.FaultInjection.Module))])
                    self._leafs = OrderedDict()

                    self.module = YList(self)
                    self._segment_path = lambda: "fault-injection"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Set.Asic.Instance.FaultInjection, [], name, value)


                class Module(Entity):
                    """
                    
                    
                    .. attribute:: module_name  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fault_type
                    
                    	
                    	**type**\:  :py:class:`FaultType <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fit'
                    _revision = '2012-05-20'

                    def __init__(self):
                        super(Set.Asic.Instance.FaultInjection.Module, self).__init__()

                        self.yang_name = "module"
                        self.yang_parent_name = "fault-injection"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['module_name']
                        self._child_classes = OrderedDict([("fault-type", ("fault_type", Set.Asic.Instance.FaultInjection.Module.FaultType))])
                        self._leafs = OrderedDict([
                            ('module_name', (YLeaf(YType.str, 'module-name'), ['str'])),
                        ])
                        self.module_name = None

                        self.fault_type = Set.Asic.Instance.FaultInjection.Module.FaultType()
                        self.fault_type.parent = self
                        self._children_name_map["fault_type"] = "fault-type"
                        self._segment_path = lambda: "module" + "[module-name='" + str(self.module_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module, [u'module_name'], name, value)


                    class FaultType(Entity):
                        """
                        
                        
                        .. attribute:: ecc
                        
                        	
                        	**type**\:  :py:class:`Ecc <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc>`
                        
                        	**config**\: False
                        
                        .. attribute:: parity
                        
                        	
                        	**type**\:  :py:class:`Parity <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity>`
                        
                        	**config**\: False
                        
                        .. attribute:: other
                        
                        	
                        	**type**\:  :py:class:`Other <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fit'
                        _revision = '2012-05-20'

                        def __init__(self):
                            super(Set.Asic.Instance.FaultInjection.Module.FaultType, self).__init__()

                            self.yang_name = "fault-type"
                            self.yang_parent_name = "module"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ecc", ("ecc", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc)), ("parity", ("parity", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity)), ("other", ("other", Set.Asic.Instance.FaultInjection.Module.FaultType.Other))])
                            self._leafs = OrderedDict()

                            self.ecc = Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc()
                            self.ecc.parent = self
                            self._children_name_map["ecc"] = "ecc"

                            self.parity = Set.Asic.Instance.FaultInjection.Module.FaultType.Parity()
                            self.parity.parent = self
                            self._children_name_map["parity"] = "parity"

                            self.other = Set.Asic.Instance.FaultInjection.Module.FaultType.Other()
                            self.other.parent = self
                            self._children_name_map["other"] = "other"
                            self._segment_path = lambda: "fault-type"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType, [], name, value)


                        class Ecc(Entity):
                            """
                            
                            
                            .. attribute:: all
                            
                            	
                            	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All>`
                            
                            	**config**\: False
                            
                            .. attribute:: block_name_lst
                            
                            	
                            	**type**\: list of  		 :py:class:`BlockNameLst <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fit'
                            _revision = '2012-05-20'

                            def __init__(self):
                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc, self).__init__()

                                self.yang_name = "ecc"
                                self.yang_parent_name = "fault-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("all", ("all", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All)), ("block-name-lst", ("block_name_lst", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst))])
                                self._leafs = OrderedDict()

                                self.all = Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All()
                                self.all.parent = self
                                self._children_name_map["all"] = "all"

                                self.block_name_lst = YList(self)
                                self._segment_path = lambda: "ecc"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc, [], name, value)


                            class All(Entity):
                                """
                                
                                
                                .. attribute:: threshold
                                
                                	
                                	**type**\: list of  		 :py:class:`Threshold <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Threshold>`
                                
                                	**config**\: False
                                
                                .. attribute:: location
                                
                                	
                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Location>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fit'
                                _revision = '2012-05-20'

                                def __init__(self):
                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All, self).__init__()

                                    self.yang_name = "all"
                                    self.yang_parent_name = "ecc"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("threshold", ("threshold", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Threshold)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Location))])
                                    self._leafs = OrderedDict()

                                    self.threshold = YList(self)
                                    self.location = YList(self)
                                    self._segment_path = lambda: "all"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All, [], name, value)


                                class Threshold(Entity):
                                    """
                                    
                                    
                                    .. attribute:: num_seconds  (key)
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**mandatory**\: True
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Threshold.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Threshold, self).__init__()

                                        self.yang_name = "threshold"
                                        self.yang_parent_name = "all"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['num_seconds']
                                        self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Threshold.Location))])
                                        self._leafs = OrderedDict([
                                            ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                        ])
                                        self.num_seconds = None

                                        self.location = YList(self)
                                        self._segment_path = lambda: "threshold" + "[num-seconds='" + str(self.num_seconds) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Threshold, [u'num_seconds'], name, value)


                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Threshold.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "threshold"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Threshold.Location, [u'fit_location_name'], name, value)




                                class Location(Entity):
                                    """
                                    
                                    
                                    .. attribute:: fit_location_name  (key)
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Location, self).__init__()

                                        self.yang_name = "location"
                                        self.yang_parent_name = "all"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['fit_location_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                        ])
                                        self.fit_location_name = None
                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.All.Location, [u'fit_location_name'], name, value)




                            class BlockNameLst(Entity):
                                """
                                
                                
                                .. attribute:: block_name  (key)
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: one
                                
                                	
                                	**type**\:  :py:class:`One <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One>`
                                
                                	**config**\: False
                                
                                .. attribute:: continuous
                                
                                	
                                	**type**\:  :py:class:`Continuous <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous>`
                                
                                	**config**\: False
                                
                                .. attribute:: stop
                                
                                	
                                	**type**\:  :py:class:`Stop <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fit'
                                _revision = '2012-05-20'

                                def __init__(self):
                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst, self).__init__()

                                    self.yang_name = "block-name-lst"
                                    self.yang_parent_name = "ecc"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['block_name']
                                    self._child_classes = OrderedDict([("one", ("one", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One)), ("continuous", ("continuous", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous)), ("stop", ("stop", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop))])
                                    self._leafs = OrderedDict([
                                        ('block_name', (YLeaf(YType.str, 'block-name'), ['str'])),
                                    ])
                                    self.block_name = None

                                    self.one = Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One()
                                    self.one.parent = self
                                    self._children_name_map["one"] = "one"

                                    self.continuous = Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous()
                                    self.continuous.parent = self
                                    self._children_name_map["continuous"] = "continuous"

                                    self.stop = Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop()
                                    self.stop.parent = self
                                    self._children_name_map["stop"] = "stop"
                                    self._segment_path = lambda: "block-name-lst" + "[block-name='" + str(self.block_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst, [u'block_name'], name, value)


                                class One(Entity):
                                    """
                                    
                                    
                                    .. attribute:: rate
                                    
                                    	
                                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One, self).__init__()

                                        self.yang_name = "one"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rate", ("rate", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Location))])
                                        self._leafs = OrderedDict()

                                        self.rate = Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate()
                                        self.rate.parent = self
                                        self._children_name_map["rate"] = "rate"

                                        self.location = YList(self)
                                        self._segment_path = lambda: "one"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One, [], name, value)


                                    class Rate(Entity):
                                        """
                                        
                                        
                                        .. attribute:: error_number
                                        
                                        	
                                        	**type**\: list of  		 :py:class:`ErrorNumber <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate, self).__init__()

                                            self.yang_name = "rate"
                                            self.yang_parent_name = "one"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("error-number", ("error_number", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber))])
                                            self._leafs = OrderedDict()

                                            self.error_number = YList(self)
                                            self._segment_path = lambda: "rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate, [], name, value)


                                        class ErrorNumber(Entity):
                                            """
                                            
                                            
                                            .. attribute:: num_errs  (key)
                                            
                                            	
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: duration
                                            
                                            	
                                            	**type**\: list of  		 :py:class:`Duration <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber.Duration>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'fit'
                                            _revision = '2012-05-20'

                                            def __init__(self):
                                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber, self).__init__()

                                                self.yang_name = "error-number"
                                                self.yang_parent_name = "rate"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['num_errs']
                                                self._child_classes = OrderedDict([("duration", ("duration", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber.Duration))])
                                                self._leafs = OrderedDict([
                                                    ('num_errs', (YLeaf(YType.uint32, 'num-errs'), ['int'])),
                                                ])
                                                self.num_errs = None

                                                self.duration = YList(self)
                                                self._segment_path = lambda: "error-number" + "[num-errs='" + str(self.num_errs) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber, [u'num_errs'], name, value)


                                            class Duration(Entity):
                                                """
                                                
                                                
                                                .. attribute:: num_seconds  (key)
                                                
                                                	
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: location
                                                
                                                	
                                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber.Duration.Location>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'fit'
                                                _revision = '2012-05-20'

                                                def __init__(self):
                                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber.Duration, self).__init__()

                                                    self.yang_name = "duration"
                                                    self.yang_parent_name = "error-number"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['num_seconds']
                                                    self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber.Duration.Location))])
                                                    self._leafs = OrderedDict([
                                                        ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                                    ])
                                                    self.num_seconds = None

                                                    self.location = YList(self)
                                                    self._segment_path = lambda: "duration" + "[num-seconds='" + str(self.num_seconds) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber.Duration, [u'num_seconds'], name, value)


                                                class Location(Entity):
                                                    """
                                                    
                                                    
                                                    .. attribute:: fit_location_name  (key)
                                                    
                                                    	
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'fit'
                                                    _revision = '2012-05-20'

                                                    def __init__(self):
                                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber.Duration.Location, self).__init__()

                                                        self.yang_name = "location"
                                                        self.yang_parent_name = "duration"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['fit_location_name']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                                        ])
                                                        self.fit_location_name = None
                                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Rate.ErrorNumber.Duration.Location, [u'fit_location_name'], name, value)






                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "one"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.One.Location, [u'fit_location_name'], name, value)




                                class Continuous(Entity):
                                    """
                                    
                                    
                                    .. attribute:: rate
                                    
                                    	
                                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous, self).__init__()

                                        self.yang_name = "continuous"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rate", ("rate", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Location))])
                                        self._leafs = OrderedDict()

                                        self.rate = Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate()
                                        self.rate.parent = self
                                        self._children_name_map["rate"] = "rate"

                                        self.location = YList(self)
                                        self._segment_path = lambda: "continuous"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous, [], name, value)


                                    class Rate(Entity):
                                        """
                                        
                                        
                                        .. attribute:: error_number
                                        
                                        	
                                        	**type**\: list of  		 :py:class:`ErrorNumber <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate, self).__init__()

                                            self.yang_name = "rate"
                                            self.yang_parent_name = "continuous"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("error-number", ("error_number", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber))])
                                            self._leafs = OrderedDict()

                                            self.error_number = YList(self)
                                            self._segment_path = lambda: "rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate, [], name, value)


                                        class ErrorNumber(Entity):
                                            """
                                            
                                            
                                            .. attribute:: num_errs  (key)
                                            
                                            	
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: duration
                                            
                                            	
                                            	**type**\: list of  		 :py:class:`Duration <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber.Duration>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'fit'
                                            _revision = '2012-05-20'

                                            def __init__(self):
                                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber, self).__init__()

                                                self.yang_name = "error-number"
                                                self.yang_parent_name = "rate"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['num_errs']
                                                self._child_classes = OrderedDict([("duration", ("duration", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber.Duration))])
                                                self._leafs = OrderedDict([
                                                    ('num_errs', (YLeaf(YType.uint32, 'num-errs'), ['int'])),
                                                ])
                                                self.num_errs = None

                                                self.duration = YList(self)
                                                self._segment_path = lambda: "error-number" + "[num-errs='" + str(self.num_errs) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber, [u'num_errs'], name, value)


                                            class Duration(Entity):
                                                """
                                                
                                                
                                                .. attribute:: num_seconds  (key)
                                                
                                                	
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: location
                                                
                                                	
                                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'fit'
                                                _revision = '2012-05-20'

                                                def __init__(self):
                                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber.Duration, self).__init__()

                                                    self.yang_name = "duration"
                                                    self.yang_parent_name = "error-number"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['num_seconds']
                                                    self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location))])
                                                    self._leafs = OrderedDict([
                                                        ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                                    ])
                                                    self.num_seconds = None

                                                    self.location = YList(self)
                                                    self._segment_path = lambda: "duration" + "[num-seconds='" + str(self.num_seconds) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber.Duration, [u'num_seconds'], name, value)


                                                class Location(Entity):
                                                    """
                                                    
                                                    
                                                    .. attribute:: fit_location_name  (key)
                                                    
                                                    	
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'fit'
                                                    _revision = '2012-05-20'

                                                    def __init__(self):
                                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location, self).__init__()

                                                        self.yang_name = "location"
                                                        self.yang_parent_name = "duration"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['fit_location_name']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                                        ])
                                                        self.fit_location_name = None
                                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location, [u'fit_location_name'], name, value)






                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "continuous"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Continuous.Location, [u'fit_location_name'], name, value)




                                class Stop(Entity):
                                    """
                                    
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop, self).__init__()

                                        self.yang_name = "stop"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop.Location))])
                                        self._leafs = OrderedDict()

                                        self.location = YList(self)
                                        self._segment_path = lambda: "stop"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop, [], name, value)


                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "stop"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Ecc.BlockNameLst.Stop.Location, [u'fit_location_name'], name, value)






                        class Parity(Entity):
                            """
                            
                            
                            .. attribute:: all
                            
                            	
                            	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All>`
                            
                            	**config**\: False
                            
                            .. attribute:: block_name_lst
                            
                            	
                            	**type**\: list of  		 :py:class:`BlockNameLst <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fit'
                            _revision = '2012-05-20'

                            def __init__(self):
                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity, self).__init__()

                                self.yang_name = "parity"
                                self.yang_parent_name = "fault-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("all", ("all", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All)), ("block-name-lst", ("block_name_lst", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst))])
                                self._leafs = OrderedDict()

                                self.all = Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All()
                                self.all.parent = self
                                self._children_name_map["all"] = "all"

                                self.block_name_lst = YList(self)
                                self._segment_path = lambda: "parity"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity, [], name, value)


                            class All(Entity):
                                """
                                
                                
                                .. attribute:: threshold
                                
                                	
                                	**type**\: list of  		 :py:class:`Threshold <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Threshold>`
                                
                                	**config**\: False
                                
                                .. attribute:: location
                                
                                	
                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Location>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fit'
                                _revision = '2012-05-20'

                                def __init__(self):
                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All, self).__init__()

                                    self.yang_name = "all"
                                    self.yang_parent_name = "parity"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("threshold", ("threshold", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Threshold)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Location))])
                                    self._leafs = OrderedDict()

                                    self.threshold = YList(self)
                                    self.location = YList(self)
                                    self._segment_path = lambda: "all"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All, [], name, value)


                                class Threshold(Entity):
                                    """
                                    
                                    
                                    .. attribute:: num_seconds  (key)
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**mandatory**\: True
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Threshold.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Threshold, self).__init__()

                                        self.yang_name = "threshold"
                                        self.yang_parent_name = "all"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['num_seconds']
                                        self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Threshold.Location))])
                                        self._leafs = OrderedDict([
                                            ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                        ])
                                        self.num_seconds = None

                                        self.location = YList(self)
                                        self._segment_path = lambda: "threshold" + "[num-seconds='" + str(self.num_seconds) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Threshold, [u'num_seconds'], name, value)


                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Threshold.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "threshold"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Threshold.Location, [u'fit_location_name'], name, value)




                                class Location(Entity):
                                    """
                                    
                                    
                                    .. attribute:: fit_location_name  (key)
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Location, self).__init__()

                                        self.yang_name = "location"
                                        self.yang_parent_name = "all"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['fit_location_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                        ])
                                        self.fit_location_name = None
                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.All.Location, [u'fit_location_name'], name, value)




                            class BlockNameLst(Entity):
                                """
                                
                                
                                .. attribute:: block_name  (key)
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: one
                                
                                	
                                	**type**\:  :py:class:`One <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One>`
                                
                                	**config**\: False
                                
                                .. attribute:: continuous
                                
                                	
                                	**type**\:  :py:class:`Continuous <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous>`
                                
                                	**config**\: False
                                
                                .. attribute:: stop
                                
                                	
                                	**type**\:  :py:class:`Stop <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fit'
                                _revision = '2012-05-20'

                                def __init__(self):
                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst, self).__init__()

                                    self.yang_name = "block-name-lst"
                                    self.yang_parent_name = "parity"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['block_name']
                                    self._child_classes = OrderedDict([("one", ("one", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One)), ("continuous", ("continuous", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous)), ("stop", ("stop", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop))])
                                    self._leafs = OrderedDict([
                                        ('block_name', (YLeaf(YType.str, 'block-name'), ['str'])),
                                    ])
                                    self.block_name = None

                                    self.one = Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One()
                                    self.one.parent = self
                                    self._children_name_map["one"] = "one"

                                    self.continuous = Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous()
                                    self.continuous.parent = self
                                    self._children_name_map["continuous"] = "continuous"

                                    self.stop = Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop()
                                    self.stop.parent = self
                                    self._children_name_map["stop"] = "stop"
                                    self._segment_path = lambda: "block-name-lst" + "[block-name='" + str(self.block_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst, [u'block_name'], name, value)


                                class One(Entity):
                                    """
                                    
                                    
                                    .. attribute:: rate
                                    
                                    	
                                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One, self).__init__()

                                        self.yang_name = "one"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rate", ("rate", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Location))])
                                        self._leafs = OrderedDict()

                                        self.rate = Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate()
                                        self.rate.parent = self
                                        self._children_name_map["rate"] = "rate"

                                        self.location = YList(self)
                                        self._segment_path = lambda: "one"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One, [], name, value)


                                    class Rate(Entity):
                                        """
                                        
                                        
                                        .. attribute:: error_number
                                        
                                        	
                                        	**type**\: list of  		 :py:class:`ErrorNumber <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate, self).__init__()

                                            self.yang_name = "rate"
                                            self.yang_parent_name = "one"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("error-number", ("error_number", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber))])
                                            self._leafs = OrderedDict()

                                            self.error_number = YList(self)
                                            self._segment_path = lambda: "rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate, [], name, value)


                                        class ErrorNumber(Entity):
                                            """
                                            
                                            
                                            .. attribute:: num_errs  (key)
                                            
                                            	
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: duration
                                            
                                            	
                                            	**type**\: list of  		 :py:class:`Duration <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber.Duration>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'fit'
                                            _revision = '2012-05-20'

                                            def __init__(self):
                                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber, self).__init__()

                                                self.yang_name = "error-number"
                                                self.yang_parent_name = "rate"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['num_errs']
                                                self._child_classes = OrderedDict([("duration", ("duration", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber.Duration))])
                                                self._leafs = OrderedDict([
                                                    ('num_errs', (YLeaf(YType.uint32, 'num-errs'), ['int'])),
                                                ])
                                                self.num_errs = None

                                                self.duration = YList(self)
                                                self._segment_path = lambda: "error-number" + "[num-errs='" + str(self.num_errs) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber, [u'num_errs'], name, value)


                                            class Duration(Entity):
                                                """
                                                
                                                
                                                .. attribute:: num_seconds  (key)
                                                
                                                	
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: location
                                                
                                                	
                                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber.Duration.Location>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'fit'
                                                _revision = '2012-05-20'

                                                def __init__(self):
                                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber.Duration, self).__init__()

                                                    self.yang_name = "duration"
                                                    self.yang_parent_name = "error-number"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['num_seconds']
                                                    self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber.Duration.Location))])
                                                    self._leafs = OrderedDict([
                                                        ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                                    ])
                                                    self.num_seconds = None

                                                    self.location = YList(self)
                                                    self._segment_path = lambda: "duration" + "[num-seconds='" + str(self.num_seconds) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber.Duration, [u'num_seconds'], name, value)


                                                class Location(Entity):
                                                    """
                                                    
                                                    
                                                    .. attribute:: fit_location_name  (key)
                                                    
                                                    	
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'fit'
                                                    _revision = '2012-05-20'

                                                    def __init__(self):
                                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber.Duration.Location, self).__init__()

                                                        self.yang_name = "location"
                                                        self.yang_parent_name = "duration"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['fit_location_name']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                                        ])
                                                        self.fit_location_name = None
                                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Rate.ErrorNumber.Duration.Location, [u'fit_location_name'], name, value)






                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "one"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.One.Location, [u'fit_location_name'], name, value)




                                class Continuous(Entity):
                                    """
                                    
                                    
                                    .. attribute:: rate
                                    
                                    	
                                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous, self).__init__()

                                        self.yang_name = "continuous"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rate", ("rate", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Location))])
                                        self._leafs = OrderedDict()

                                        self.rate = Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate()
                                        self.rate.parent = self
                                        self._children_name_map["rate"] = "rate"

                                        self.location = YList(self)
                                        self._segment_path = lambda: "continuous"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous, [], name, value)


                                    class Rate(Entity):
                                        """
                                        
                                        
                                        .. attribute:: error_number
                                        
                                        	
                                        	**type**\: list of  		 :py:class:`ErrorNumber <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate, self).__init__()

                                            self.yang_name = "rate"
                                            self.yang_parent_name = "continuous"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("error-number", ("error_number", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber))])
                                            self._leafs = OrderedDict()

                                            self.error_number = YList(self)
                                            self._segment_path = lambda: "rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate, [], name, value)


                                        class ErrorNumber(Entity):
                                            """
                                            
                                            
                                            .. attribute:: num_errs  (key)
                                            
                                            	
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: duration
                                            
                                            	
                                            	**type**\: list of  		 :py:class:`Duration <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber.Duration>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'fit'
                                            _revision = '2012-05-20'

                                            def __init__(self):
                                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber, self).__init__()

                                                self.yang_name = "error-number"
                                                self.yang_parent_name = "rate"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['num_errs']
                                                self._child_classes = OrderedDict([("duration", ("duration", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber.Duration))])
                                                self._leafs = OrderedDict([
                                                    ('num_errs', (YLeaf(YType.uint32, 'num-errs'), ['int'])),
                                                ])
                                                self.num_errs = None

                                                self.duration = YList(self)
                                                self._segment_path = lambda: "error-number" + "[num-errs='" + str(self.num_errs) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber, [u'num_errs'], name, value)


                                            class Duration(Entity):
                                                """
                                                
                                                
                                                .. attribute:: num_seconds  (key)
                                                
                                                	
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: location
                                                
                                                	
                                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'fit'
                                                _revision = '2012-05-20'

                                                def __init__(self):
                                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber.Duration, self).__init__()

                                                    self.yang_name = "duration"
                                                    self.yang_parent_name = "error-number"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['num_seconds']
                                                    self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location))])
                                                    self._leafs = OrderedDict([
                                                        ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                                    ])
                                                    self.num_seconds = None

                                                    self.location = YList(self)
                                                    self._segment_path = lambda: "duration" + "[num-seconds='" + str(self.num_seconds) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber.Duration, [u'num_seconds'], name, value)


                                                class Location(Entity):
                                                    """
                                                    
                                                    
                                                    .. attribute:: fit_location_name  (key)
                                                    
                                                    	
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'fit'
                                                    _revision = '2012-05-20'

                                                    def __init__(self):
                                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location, self).__init__()

                                                        self.yang_name = "location"
                                                        self.yang_parent_name = "duration"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['fit_location_name']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                                        ])
                                                        self.fit_location_name = None
                                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location, [u'fit_location_name'], name, value)






                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "continuous"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Continuous.Location, [u'fit_location_name'], name, value)




                                class Stop(Entity):
                                    """
                                    
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop, self).__init__()

                                        self.yang_name = "stop"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop.Location))])
                                        self._leafs = OrderedDict()

                                        self.location = YList(self)
                                        self._segment_path = lambda: "stop"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop, [], name, value)


                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "stop"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Parity.BlockNameLst.Stop.Location, [u'fit_location_name'], name, value)






                        class Other(Entity):
                            """
                            
                            
                            .. attribute:: all
                            
                            	
                            	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All>`
                            
                            	**config**\: False
                            
                            .. attribute:: block_name_lst
                            
                            	
                            	**type**\: list of  		 :py:class:`BlockNameLst <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fit'
                            _revision = '2012-05-20'

                            def __init__(self):
                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other, self).__init__()

                                self.yang_name = "other"
                                self.yang_parent_name = "fault-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("all", ("all", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All)), ("block-name-lst", ("block_name_lst", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst))])
                                self._leafs = OrderedDict()

                                self.all = Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All()
                                self.all.parent = self
                                self._children_name_map["all"] = "all"

                                self.block_name_lst = YList(self)
                                self._segment_path = lambda: "other"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other, [], name, value)


                            class All(Entity):
                                """
                                
                                
                                .. attribute:: threshold
                                
                                	
                                	**type**\: list of  		 :py:class:`Threshold <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Threshold>`
                                
                                	**config**\: False
                                
                                .. attribute:: location
                                
                                	
                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Location>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fit'
                                _revision = '2012-05-20'

                                def __init__(self):
                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All, self).__init__()

                                    self.yang_name = "all"
                                    self.yang_parent_name = "other"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("threshold", ("threshold", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Threshold)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Location))])
                                    self._leafs = OrderedDict()

                                    self.threshold = YList(self)
                                    self.location = YList(self)
                                    self._segment_path = lambda: "all"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All, [], name, value)


                                class Threshold(Entity):
                                    """
                                    
                                    
                                    .. attribute:: num_seconds  (key)
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**mandatory**\: True
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Threshold.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Threshold, self).__init__()

                                        self.yang_name = "threshold"
                                        self.yang_parent_name = "all"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['num_seconds']
                                        self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Threshold.Location))])
                                        self._leafs = OrderedDict([
                                            ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                        ])
                                        self.num_seconds = None

                                        self.location = YList(self)
                                        self._segment_path = lambda: "threshold" + "[num-seconds='" + str(self.num_seconds) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Threshold, [u'num_seconds'], name, value)


                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Threshold.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "threshold"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Threshold.Location, [u'fit_location_name'], name, value)




                                class Location(Entity):
                                    """
                                    
                                    
                                    .. attribute:: fit_location_name  (key)
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Location, self).__init__()

                                        self.yang_name = "location"
                                        self.yang_parent_name = "all"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['fit_location_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                        ])
                                        self.fit_location_name = None
                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.All.Location, [u'fit_location_name'], name, value)




                            class BlockNameLst(Entity):
                                """
                                
                                
                                .. attribute:: block_name  (key)
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: one
                                
                                	
                                	**type**\:  :py:class:`One <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One>`
                                
                                	**config**\: False
                                
                                .. attribute:: continuous
                                
                                	
                                	**type**\:  :py:class:`Continuous <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous>`
                                
                                	**config**\: False
                                
                                .. attribute:: stop
                                
                                	
                                	**type**\:  :py:class:`Stop <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fit'
                                _revision = '2012-05-20'

                                def __init__(self):
                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst, self).__init__()

                                    self.yang_name = "block-name-lst"
                                    self.yang_parent_name = "other"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['block_name']
                                    self._child_classes = OrderedDict([("one", ("one", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One)), ("continuous", ("continuous", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous)), ("stop", ("stop", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop))])
                                    self._leafs = OrderedDict([
                                        ('block_name', (YLeaf(YType.str, 'block-name'), ['str'])),
                                    ])
                                    self.block_name = None

                                    self.one = Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One()
                                    self.one.parent = self
                                    self._children_name_map["one"] = "one"

                                    self.continuous = Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous()
                                    self.continuous.parent = self
                                    self._children_name_map["continuous"] = "continuous"

                                    self.stop = Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop()
                                    self.stop.parent = self
                                    self._children_name_map["stop"] = "stop"
                                    self._segment_path = lambda: "block-name-lst" + "[block-name='" + str(self.block_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst, [u'block_name'], name, value)


                                class One(Entity):
                                    """
                                    
                                    
                                    .. attribute:: rate
                                    
                                    	
                                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One, self).__init__()

                                        self.yang_name = "one"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rate", ("rate", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Location))])
                                        self._leafs = OrderedDict()

                                        self.rate = Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate()
                                        self.rate.parent = self
                                        self._children_name_map["rate"] = "rate"

                                        self.location = YList(self)
                                        self._segment_path = lambda: "one"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One, [], name, value)


                                    class Rate(Entity):
                                        """
                                        
                                        
                                        .. attribute:: error_number
                                        
                                        	
                                        	**type**\: list of  		 :py:class:`ErrorNumber <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate, self).__init__()

                                            self.yang_name = "rate"
                                            self.yang_parent_name = "one"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("error-number", ("error_number", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber))])
                                            self._leafs = OrderedDict()

                                            self.error_number = YList(self)
                                            self._segment_path = lambda: "rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate, [], name, value)


                                        class ErrorNumber(Entity):
                                            """
                                            
                                            
                                            .. attribute:: num_errs  (key)
                                            
                                            	
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: duration
                                            
                                            	
                                            	**type**\: list of  		 :py:class:`Duration <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber.Duration>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'fit'
                                            _revision = '2012-05-20'

                                            def __init__(self):
                                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber, self).__init__()

                                                self.yang_name = "error-number"
                                                self.yang_parent_name = "rate"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['num_errs']
                                                self._child_classes = OrderedDict([("duration", ("duration", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber.Duration))])
                                                self._leafs = OrderedDict([
                                                    ('num_errs', (YLeaf(YType.uint32, 'num-errs'), ['int'])),
                                                ])
                                                self.num_errs = None

                                                self.duration = YList(self)
                                                self._segment_path = lambda: "error-number" + "[num-errs='" + str(self.num_errs) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber, [u'num_errs'], name, value)


                                            class Duration(Entity):
                                                """
                                                
                                                
                                                .. attribute:: num_seconds  (key)
                                                
                                                	
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: location
                                                
                                                	
                                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber.Duration.Location>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'fit'
                                                _revision = '2012-05-20'

                                                def __init__(self):
                                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber.Duration, self).__init__()

                                                    self.yang_name = "duration"
                                                    self.yang_parent_name = "error-number"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['num_seconds']
                                                    self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber.Duration.Location))])
                                                    self._leafs = OrderedDict([
                                                        ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                                    ])
                                                    self.num_seconds = None

                                                    self.location = YList(self)
                                                    self._segment_path = lambda: "duration" + "[num-seconds='" + str(self.num_seconds) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber.Duration, [u'num_seconds'], name, value)


                                                class Location(Entity):
                                                    """
                                                    
                                                    
                                                    .. attribute:: fit_location_name  (key)
                                                    
                                                    	
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'fit'
                                                    _revision = '2012-05-20'

                                                    def __init__(self):
                                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber.Duration.Location, self).__init__()

                                                        self.yang_name = "location"
                                                        self.yang_parent_name = "duration"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['fit_location_name']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                                        ])
                                                        self.fit_location_name = None
                                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Rate.ErrorNumber.Duration.Location, [u'fit_location_name'], name, value)






                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "one"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.One.Location, [u'fit_location_name'], name, value)




                                class Continuous(Entity):
                                    """
                                    
                                    
                                    .. attribute:: rate
                                    
                                    	
                                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous, self).__init__()

                                        self.yang_name = "continuous"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rate", ("rate", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate)), ("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Location))])
                                        self._leafs = OrderedDict()

                                        self.rate = Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate()
                                        self.rate.parent = self
                                        self._children_name_map["rate"] = "rate"

                                        self.location = YList(self)
                                        self._segment_path = lambda: "continuous"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous, [], name, value)


                                    class Rate(Entity):
                                        """
                                        
                                        
                                        .. attribute:: error_number
                                        
                                        	
                                        	**type**\: list of  		 :py:class:`ErrorNumber <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate, self).__init__()

                                            self.yang_name = "rate"
                                            self.yang_parent_name = "continuous"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("error-number", ("error_number", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber))])
                                            self._leafs = OrderedDict()

                                            self.error_number = YList(self)
                                            self._segment_path = lambda: "rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate, [], name, value)


                                        class ErrorNumber(Entity):
                                            """
                                            
                                            
                                            .. attribute:: num_errs  (key)
                                            
                                            	
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: duration
                                            
                                            	
                                            	**type**\: list of  		 :py:class:`Duration <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber.Duration>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'fit'
                                            _revision = '2012-05-20'

                                            def __init__(self):
                                                super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber, self).__init__()

                                                self.yang_name = "error-number"
                                                self.yang_parent_name = "rate"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['num_errs']
                                                self._child_classes = OrderedDict([("duration", ("duration", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber.Duration))])
                                                self._leafs = OrderedDict([
                                                    ('num_errs', (YLeaf(YType.uint32, 'num-errs'), ['int'])),
                                                ])
                                                self.num_errs = None

                                                self.duration = YList(self)
                                                self._segment_path = lambda: "error-number" + "[num-errs='" + str(self.num_errs) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber, [u'num_errs'], name, value)


                                            class Duration(Entity):
                                                """
                                                
                                                
                                                .. attribute:: num_seconds  (key)
                                                
                                                	
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: location
                                                
                                                	
                                                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'fit'
                                                _revision = '2012-05-20'

                                                def __init__(self):
                                                    super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber.Duration, self).__init__()

                                                    self.yang_name = "duration"
                                                    self.yang_parent_name = "error-number"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['num_seconds']
                                                    self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location))])
                                                    self._leafs = OrderedDict([
                                                        ('num_seconds', (YLeaf(YType.uint32, 'num-seconds'), ['int'])),
                                                    ])
                                                    self.num_seconds = None

                                                    self.location = YList(self)
                                                    self._segment_path = lambda: "duration" + "[num-seconds='" + str(self.num_seconds) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber.Duration, [u'num_seconds'], name, value)


                                                class Location(Entity):
                                                    """
                                                    
                                                    
                                                    .. attribute:: fit_location_name  (key)
                                                    
                                                    	
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'fit'
                                                    _revision = '2012-05-20'

                                                    def __init__(self):
                                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location, self).__init__()

                                                        self.yang_name = "location"
                                                        self.yang_parent_name = "duration"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['fit_location_name']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                                        ])
                                                        self.fit_location_name = None
                                                        self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Rate.ErrorNumber.Duration.Location, [u'fit_location_name'], name, value)






                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "continuous"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Continuous.Location, [u'fit_location_name'], name, value)




                                class Stop(Entity):
                                    """
                                    
                                    
                                    .. attribute:: location
                                    
                                    	
                                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.fit.Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop.Location>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fit'
                                    _revision = '2012-05-20'

                                    def __init__(self):
                                        super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop, self).__init__()

                                        self.yang_name = "stop"
                                        self.yang_parent_name = "block-name-lst"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("location", ("location", Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop.Location))])
                                        self._leafs = OrderedDict()

                                        self.location = YList(self)
                                        self._segment_path = lambda: "stop"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop, [], name, value)


                                    class Location(Entity):
                                        """
                                        
                                        
                                        .. attribute:: fit_location_name  (key)
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fit'
                                        _revision = '2012-05-20'

                                        def __init__(self):
                                            super(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop.Location, self).__init__()

                                            self.yang_name = "location"
                                            self.yang_parent_name = "stop"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['fit_location_name']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fit_location_name', (YLeaf(YType.str, 'fit-location-name'), ['str'])),
                                            ])
                                            self.fit_location_name = None
                                            self._segment_path = lambda: "location" + "[fit-location-name='" + str(self.fit_location_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Set.Asic.Instance.FaultInjection.Module.FaultType.Other.BlockNameLst.Stop.Location, [u'fit_location_name'], name, value)










    def clone_ptr(self):
        self._top_entity = Set()
        return self._top_entity



