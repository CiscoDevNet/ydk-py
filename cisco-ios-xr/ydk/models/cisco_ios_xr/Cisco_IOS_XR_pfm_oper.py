""" Cisco_IOS_XR_pfm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pfm package operational data.

This module contains definitions
for the following management objects\:
  platform\-fault\-manager\: PFM data space

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class PlatformFaultManager(Entity):
    """
    PFM data space
    
    .. attribute:: exclude
    
    	Exclude specic hw fault 
    	**type**\:  :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude>`
    
    	**config**\: False
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks>`
    
    	**config**\: False
    
    

    """

    _prefix = 'pfm-oper'
    _revision = '2017-03-28'

    def __init__(self):
        super(PlatformFaultManager, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-fault-manager"
        self.yang_parent_name = "Cisco-IOS-XR-pfm-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("exclude", ("exclude", PlatformFaultManager.Exclude)), ("racks", ("racks", PlatformFaultManager.Racks))])
        self._leafs = OrderedDict()

        self.exclude = PlatformFaultManager.Exclude()
        self.exclude.parent = self
        self._children_name_map["exclude"] = "exclude"

        self.racks = PlatformFaultManager.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._segment_path = lambda: "Cisco-IOS-XR-pfm-oper:platform-fault-manager"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PlatformFaultManager, [], name, value)


    class Exclude(Entity):
        """
        Exclude specic hw fault 
        
        .. attribute:: fault_type1s
        
        	Table of Hardware Failure Device
        	**type**\:  :py:class:`FaultType1s <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s>`
        
        	**config**\: False
        
        

        """

        _prefix = 'pfm-oper'
        _revision = '2017-03-28'

        def __init__(self):
            super(PlatformFaultManager.Exclude, self).__init__()

            self.yang_name = "exclude"
            self.yang_parent_name = "platform-fault-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("fault-type1s", ("fault_type1s", PlatformFaultManager.Exclude.FaultType1s))])
            self._leafs = OrderedDict()

            self.fault_type1s = PlatformFaultManager.Exclude.FaultType1s()
            self.fault_type1s.parent = self
            self._children_name_map["fault_type1s"] = "fault-type1s"
            self._segment_path = lambda: "exclude"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfm-oper:platform-fault-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformFaultManager.Exclude, [], name, value)


        class FaultType1s(Entity):
            """
            Table of Hardware Failure Device
            
            .. attribute:: fault_type1
            
            	Table of Hardware Failure Device
            	**type**\: list of  		 :py:class:`FaultType1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1>`
            
            	**config**\: False
            
            

            """

            _prefix = 'pfm-oper'
            _revision = '2017-03-28'

            def __init__(self):
                super(PlatformFaultManager.Exclude.FaultType1s, self).__init__()

                self.yang_name = "fault-type1s"
                self.yang_parent_name = "exclude"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("fault-type1", ("fault_type1", PlatformFaultManager.Exclude.FaultType1s.FaultType1))])
                self._leafs = OrderedDict()

                self.fault_type1 = YList(self)
                self._segment_path = lambda: "fault-type1s"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfm-oper:platform-fault-manager/exclude/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s, [], name, value)


            class FaultType1(Entity):
                """
                Table of Hardware Failure Device
                
                .. attribute:: hw_fault_type1  (key)
                
                	hw fault 1
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: fault_type2s
                
                	Table of Hardware Failure Device
                	**type**\:  :py:class:`FaultType2s <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s>`
                
                	**config**\: False
                
                .. attribute:: racks
                
                	Table of racks
                	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pfm-oper'
                _revision = '2017-03-28'

                def __init__(self):
                    super(PlatformFaultManager.Exclude.FaultType1s.FaultType1, self).__init__()

                    self.yang_name = "fault-type1"
                    self.yang_parent_name = "fault-type1s"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['hw_fault_type1']
                    self._child_classes = OrderedDict([("fault-type2s", ("fault_type2s", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s)), ("racks", ("racks", PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks))])
                    self._leafs = OrderedDict([
                        ('hw_fault_type1', (YLeaf(YType.str, 'hw-fault-type1'), ['str'])),
                    ])
                    self.hw_fault_type1 = None

                    self.fault_type2s = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s()
                    self.fault_type2s.parent = self
                    self._children_name_map["fault_type2s"] = "fault-type2s"

                    self.racks = PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks()
                    self.racks.parent = self
                    self._children_name_map["racks"] = "racks"
                    self._segment_path = lambda: "fault-type1" + "[hw-fault-type1='" + str(self.hw_fault_type1) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-pfm-oper:platform-fault-manager/exclude/fault-type1s/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1, ['hw_fault_type1'], name, value)


                class FaultType2s(Entity):
                    """
                    Table of Hardware Failure Device
                    
                    .. attribute:: fault_type2
                    
                    	Table of Hardware Failure Device
                    	**type**\: list of  		 :py:class:`FaultType2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pfm-oper'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s, self).__init__()

                        self.yang_name = "fault-type2s"
                        self.yang_parent_name = "fault-type1"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("fault-type2", ("fault_type2", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2))])
                        self._leafs = OrderedDict()

                        self.fault_type2 = YList(self)
                        self._segment_path = lambda: "fault-type2s"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s, [], name, value)


                    class FaultType2(Entity):
                        """
                        Table of Hardware Failure Device
                        
                        .. attribute:: hw_fault_type2  (key)
                        
                        	hw fault 2
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: fault_type3s
                        
                        	Table of Hardware Failure Device
                        	**type**\:  :py:class:`FaultType3s <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s>`
                        
                        	**config**\: False
                        
                        .. attribute:: racks
                        
                        	Table of racks
                        	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pfm-oper'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2, self).__init__()

                            self.yang_name = "fault-type2"
                            self.yang_parent_name = "fault-type2s"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['hw_fault_type2']
                            self._child_classes = OrderedDict([("fault-type3s", ("fault_type3s", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s)), ("racks", ("racks", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks))])
                            self._leafs = OrderedDict([
                                ('hw_fault_type2', (YLeaf(YType.str, 'hw-fault-type2'), ['str'])),
                            ])
                            self.hw_fault_type2 = None

                            self.fault_type3s = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s()
                            self.fault_type3s.parent = self
                            self._children_name_map["fault_type3s"] = "fault-type3s"

                            self.racks = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks()
                            self.racks.parent = self
                            self._children_name_map["racks"] = "racks"
                            self._segment_path = lambda: "fault-type2" + "[hw-fault-type2='" + str(self.hw_fault_type2) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2, ['hw_fault_type2'], name, value)


                        class FaultType3s(Entity):
                            """
                            Table of Hardware Failure Device
                            
                            .. attribute:: fault_type3
                            
                            	Table of Hardware Failure Device
                            	**type**\: list of  		 :py:class:`FaultType3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pfm-oper'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s, self).__init__()

                                self.yang_name = "fault-type3s"
                                self.yang_parent_name = "fault-type2"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("fault-type3", ("fault_type3", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3))])
                                self._leafs = OrderedDict()

                                self.fault_type3 = YList(self)
                                self._segment_path = lambda: "fault-type3s"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s, [], name, value)


                            class FaultType3(Entity):
                                """
                                Table of Hardware Failure Device
                                
                                .. attribute:: hw_fault_type3  (key)
                                
                                	hw fault 3
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                	**config**\: False
                                
                                .. attribute:: racks
                                
                                	Table of racks
                                	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pfm-oper'
                                _revision = '2017-03-28'

                                def __init__(self):
                                    super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3, self).__init__()

                                    self.yang_name = "fault-type3"
                                    self.yang_parent_name = "fault-type3s"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['hw_fault_type3']
                                    self._child_classes = OrderedDict([("racks", ("racks", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks))])
                                    self._leafs = OrderedDict([
                                        ('hw_fault_type3', (YLeaf(YType.str, 'hw-fault-type3'), ['str'])),
                                    ])
                                    self.hw_fault_type3 = None

                                    self.racks = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks()
                                    self.racks.parent = self
                                    self._children_name_map["racks"] = "racks"
                                    self._segment_path = lambda: "fault-type3" + "[hw-fault-type3='" + str(self.hw_fault_type3) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3, ['hw_fault_type3'], name, value)


                                class Racks(Entity):
                                    """
                                    Table of racks
                                    
                                    .. attribute:: rack
                                    
                                    	Number
                                    	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'pfm-oper'
                                    _revision = '2017-03-28'

                                    def __init__(self):
                                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks, self).__init__()

                                        self.yang_name = "racks"
                                        self.yang_parent_name = "fault-type3"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rack", ("rack", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack))])
                                        self._leafs = OrderedDict()

                                        self.rack = YList(self)
                                        self._segment_path = lambda: "racks"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks, [], name, value)


                                    class Rack(Entity):
                                        """
                                        Number
                                        
                                        .. attribute:: rack  (key)
                                        
                                        	Rack number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: slots
                                        
                                        	Table of slots
                                        	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'pfm-oper'
                                        _revision = '2017-03-28'

                                        def __init__(self):
                                            super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack, self).__init__()

                                            self.yang_name = "rack"
                                            self.yang_parent_name = "racks"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['rack']
                                            self._child_classes = OrderedDict([("slots", ("slots", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots))])
                                            self._leafs = OrderedDict([
                                                ('rack', (YLeaf(YType.uint32, 'rack'), ['int'])),
                                            ])
                                            self.rack = None

                                            self.slots = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots()
                                            self.slots.parent = self
                                            self._children_name_map["slots"] = "slots"
                                            self._segment_path = lambda: "rack" + "[rack='" + str(self.rack) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack, ['rack'], name, value)


                                        class Slots(Entity):
                                            """
                                            Table of slots
                                            
                                            .. attribute:: slot
                                            
                                            	Name
                                            	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'pfm-oper'
                                            _revision = '2017-03-28'

                                            def __init__(self):
                                                super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots, self).__init__()

                                                self.yang_name = "slots"
                                                self.yang_parent_name = "rack"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("slot", ("slot", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot))])
                                                self._leafs = OrderedDict()

                                                self.slot = YList(self)
                                                self._segment_path = lambda: "slots"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots, [], name, value)


                                            class Slot(Entity):
                                                """
                                                Name
                                                
                                                .. attribute:: slot  (key)
                                                
                                                	Slot name
                                                	**type**\: str
                                                
                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: fault_summary
                                                
                                                	Table of Hardware Summary
                                                	**type**\:  :py:class:`FaultSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.FaultSummary>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: hardware_fault_devices
                                                
                                                	Table of Hardware Failure
                                                	**type**\:  :py:class:`HardwareFaultDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'pfm-oper'
                                                _revision = '2017-03-28'

                                                def __init__(self):
                                                    super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot, self).__init__()

                                                    self.yang_name = "slot"
                                                    self.yang_parent_name = "slots"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['slot']
                                                    self._child_classes = OrderedDict([("fault-summary", ("fault_summary", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.FaultSummary)), ("hardware-fault-devices", ("hardware_fault_devices", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices))])
                                                    self._leafs = OrderedDict([
                                                        ('slot', (YLeaf(YType.str, 'slot'), ['str'])),
                                                    ])
                                                    self.slot = None

                                                    self.fault_summary = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.FaultSummary()
                                                    self.fault_summary.parent = self
                                                    self._children_name_map["fault_summary"] = "fault-summary"

                                                    self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                                    self.hardware_fault_devices.parent = self
                                                    self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                                    self._segment_path = lambda: "slot" + "[slot='" + str(self.slot) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot, ['slot'], name, value)


                                                class FaultSummary(Entity):
                                                    """
                                                    Table of Hardware Summary
                                                    
                                                    .. attribute:: severity_critical_count
                                                    
                                                    	Fault Severity Critical count
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: severity_emergency_or_alert_count
                                                    
                                                    	Fault Severity Emergency count
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: total
                                                    
                                                    	Faulty Hardware total count
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: severity_error_count
                                                    
                                                    	Fault Severity Error count
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'pfm-oper'
                                                    _revision = '2017-03-28'

                                                    def __init__(self):
                                                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.FaultSummary, self).__init__()

                                                        self.yang_name = "fault-summary"
                                                        self.yang_parent_name = "slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('severity_critical_count', (YLeaf(YType.int32, 'severity-critical-count'), ['int'])),
                                                            ('severity_emergency_or_alert_count', (YLeaf(YType.int32, 'severity-emergency-or-alert-count'), ['int'])),
                                                            ('total', (YLeaf(YType.int32, 'total'), ['int'])),
                                                            ('severity_error_count', (YLeaf(YType.int32, 'severity-error-count'), ['int'])),
                                                        ])
                                                        self.severity_critical_count = None
                                                        self.severity_emergency_or_alert_count = None
                                                        self.total = None
                                                        self.severity_error_count = None
                                                        self._segment_path = lambda: "fault-summary"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.FaultSummary, ['severity_critical_count', 'severity_emergency_or_alert_count', 'total', 'severity_error_count'], name, value)



                                                class HardwareFaultDevices(Entity):
                                                    """
                                                    Table of Hardware Failure
                                                    
                                                    .. attribute:: hardware_fault_device
                                                    
                                                    	Table of Hardware Failure Device
                                                    	**type**\: list of  		 :py:class:`HardwareFaultDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'pfm-oper'
                                                    _revision = '2017-03-28'

                                                    def __init__(self):
                                                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__init__()

                                                        self.yang_name = "hardware-fault-devices"
                                                        self.yang_parent_name = "slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("hardware-fault-device", ("hardware_fault_device", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice))])
                                                        self._leafs = OrderedDict()

                                                        self.hardware_fault_device = YList(self)
                                                        self._segment_path = lambda: "hardware-fault-devices"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices, [], name, value)


                                                    class HardwareFaultDevice(Entity):
                                                        """
                                                        Table of Hardware Failure Device
                                                        
                                                        .. attribute:: hw_fault_device  (key)
                                                        
                                                        	hw fault device list
                                                        	**type**\: str
                                                        
                                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: hardware_fault_type
                                                        
                                                        	Table of Hardware Failure Type
                                                        	**type**\: list of  		 :py:class:`HardwareFaultType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'pfm-oper'
                                                        _revision = '2017-03-28'

                                                        def __init__(self):
                                                            super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__init__()

                                                            self.yang_name = "hardware-fault-device"
                                                            self.yang_parent_name = "hardware-fault-devices"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['hw_fault_device']
                                                            self._child_classes = OrderedDict([("hardware-fault-type", ("hardware_fault_type", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType))])
                                                            self._leafs = OrderedDict([
                                                                ('hw_fault_device', (YLeaf(YType.str, 'hw-fault-device'), ['str'])),
                                                            ])
                                                            self.hw_fault_device = None

                                                            self.hardware_fault_type = YList(self)
                                                            self._segment_path = lambda: "hardware-fault-device" + "[hw-fault-device='" + str(self.hw_fault_device) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, ['hw_fault_device'], name, value)


                                                        class HardwareFaultType(Entity):
                                                            """
                                                            Table of Hardware Failure Type
                                                            
                                                            .. attribute:: hw_fault_type  (key)
                                                            
                                                            	hw fault type list
                                                            	**type**\: str
                                                            
                                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: condition_description
                                                            
                                                            	Faulty Hardware Condition Description
                                                            	**type**\: str
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: condition_name
                                                            
                                                            	Faulty Hardware Condition Name
                                                            	**type**\: str
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: device_key
                                                            
                                                            	Faulty Hardware Device Key
                                                            	**type**\: str
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: device_version
                                                            
                                                            	Faulty Hardware Device Version
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: condition_raised_timestamp
                                                            
                                                            	Fault Raised Timestamp
                                                            	**type**\: str
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: process_id
                                                            
                                                            	Faulty Hardware Process ID
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: device_description
                                                            
                                                            	Faulty Hardware Device Description
                                                            	**type**\: str
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: condition_severity
                                                            
                                                            	Faulty Hardware Condition Severity
                                                            	**type**\: str
                                                            
                                                            	**config**\: False
                                                            
                                                            

                                                            """

                                                            _prefix = 'pfm-oper'
                                                            _revision = '2017-03-28'

                                                            def __init__(self):
                                                                super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__init__()

                                                                self.yang_name = "hardware-fault-type"
                                                                self.yang_parent_name = "hardware-fault-device"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = ['hw_fault_type']
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('hw_fault_type', (YLeaf(YType.str, 'hw-fault-type'), ['str'])),
                                                                    ('condition_description', (YLeaf(YType.str, 'condition-description'), ['str'])),
                                                                    ('condition_name', (YLeaf(YType.str, 'condition-name'), ['str'])),
                                                                    ('device_key', (YLeaf(YType.str, 'device-key'), ['str'])),
                                                                    ('device_version', (YLeaf(YType.int32, 'device-version'), ['int'])),
                                                                    ('condition_raised_timestamp', (YLeaf(YType.str, 'condition-raised-timestamp'), ['str'])),
                                                                    ('process_id', (YLeaf(YType.int32, 'process-id'), ['int'])),
                                                                    ('device_description', (YLeaf(YType.str, 'device-description'), ['str'])),
                                                                    ('condition_severity', (YLeaf(YType.str, 'condition-severity'), ['str'])),
                                                                ])
                                                                self.hw_fault_type = None
                                                                self.condition_description = None
                                                                self.condition_name = None
                                                                self.device_key = None
                                                                self.device_version = None
                                                                self.condition_raised_timestamp = None
                                                                self.process_id = None
                                                                self.device_description = None
                                                                self.condition_severity = None
                                                                self._segment_path = lambda: "hardware-fault-type" + "[hw-fault-type='" + str(self.hw_fault_type) + "']"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.FaultType3s.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, ['hw_fault_type', 'condition_description', 'condition_name', 'device_key', 'device_version', 'condition_raised_timestamp', 'process_id', 'device_description', 'condition_severity'], name, value)











                        class Racks(Entity):
                            """
                            Table of racks
                            
                            .. attribute:: rack
                            
                            	Number
                            	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pfm-oper'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks, self).__init__()

                                self.yang_name = "racks"
                                self.yang_parent_name = "fault-type2"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("rack", ("rack", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack))])
                                self._leafs = OrderedDict()

                                self.rack = YList(self)
                                self._segment_path = lambda: "racks"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks, [], name, value)


                            class Rack(Entity):
                                """
                                Number
                                
                                .. attribute:: rack  (key)
                                
                                	Rack number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: slots
                                
                                	Table of slots
                                	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pfm-oper'
                                _revision = '2017-03-28'

                                def __init__(self):
                                    super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack, self).__init__()

                                    self.yang_name = "rack"
                                    self.yang_parent_name = "racks"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['rack']
                                    self._child_classes = OrderedDict([("slots", ("slots", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots))])
                                    self._leafs = OrderedDict([
                                        ('rack', (YLeaf(YType.uint32, 'rack'), ['int'])),
                                    ])
                                    self.rack = None

                                    self.slots = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots()
                                    self.slots.parent = self
                                    self._children_name_map["slots"] = "slots"
                                    self._segment_path = lambda: "rack" + "[rack='" + str(self.rack) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack, ['rack'], name, value)


                                class Slots(Entity):
                                    """
                                    Table of slots
                                    
                                    .. attribute:: slot
                                    
                                    	Name
                                    	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'pfm-oper'
                                    _revision = '2017-03-28'

                                    def __init__(self):
                                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots, self).__init__()

                                        self.yang_name = "slots"
                                        self.yang_parent_name = "rack"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("slot", ("slot", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot))])
                                        self._leafs = OrderedDict()

                                        self.slot = YList(self)
                                        self._segment_path = lambda: "slots"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots, [], name, value)


                                    class Slot(Entity):
                                        """
                                        Name
                                        
                                        .. attribute:: slot  (key)
                                        
                                        	Slot name
                                        	**type**\: str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fault_summary
                                        
                                        	Table of Hardware Summary
                                        	**type**\:  :py:class:`FaultSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.FaultSummary>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: hardware_fault_devices
                                        
                                        	Table of Hardware Failure
                                        	**type**\:  :py:class:`HardwareFaultDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'pfm-oper'
                                        _revision = '2017-03-28'

                                        def __init__(self):
                                            super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot, self).__init__()

                                            self.yang_name = "slot"
                                            self.yang_parent_name = "slots"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['slot']
                                            self._child_classes = OrderedDict([("fault-summary", ("fault_summary", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.FaultSummary)), ("hardware-fault-devices", ("hardware_fault_devices", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices))])
                                            self._leafs = OrderedDict([
                                                ('slot', (YLeaf(YType.str, 'slot'), ['str'])),
                                            ])
                                            self.slot = None

                                            self.fault_summary = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.FaultSummary()
                                            self.fault_summary.parent = self
                                            self._children_name_map["fault_summary"] = "fault-summary"

                                            self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                            self.hardware_fault_devices.parent = self
                                            self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                            self._segment_path = lambda: "slot" + "[slot='" + str(self.slot) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot, ['slot'], name, value)


                                        class FaultSummary(Entity):
                                            """
                                            Table of Hardware Summary
                                            
                                            .. attribute:: severity_critical_count
                                            
                                            	Fault Severity Critical count
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: severity_emergency_or_alert_count
                                            
                                            	Fault Severity Emergency count
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: total
                                            
                                            	Faulty Hardware total count
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: severity_error_count
                                            
                                            	Fault Severity Error count
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'pfm-oper'
                                            _revision = '2017-03-28'

                                            def __init__(self):
                                                super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.FaultSummary, self).__init__()

                                                self.yang_name = "fault-summary"
                                                self.yang_parent_name = "slot"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('severity_critical_count', (YLeaf(YType.int32, 'severity-critical-count'), ['int'])),
                                                    ('severity_emergency_or_alert_count', (YLeaf(YType.int32, 'severity-emergency-or-alert-count'), ['int'])),
                                                    ('total', (YLeaf(YType.int32, 'total'), ['int'])),
                                                    ('severity_error_count', (YLeaf(YType.int32, 'severity-error-count'), ['int'])),
                                                ])
                                                self.severity_critical_count = None
                                                self.severity_emergency_or_alert_count = None
                                                self.total = None
                                                self.severity_error_count = None
                                                self._segment_path = lambda: "fault-summary"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.FaultSummary, ['severity_critical_count', 'severity_emergency_or_alert_count', 'total', 'severity_error_count'], name, value)



                                        class HardwareFaultDevices(Entity):
                                            """
                                            Table of Hardware Failure
                                            
                                            .. attribute:: hardware_fault_device
                                            
                                            	Table of Hardware Failure Device
                                            	**type**\: list of  		 :py:class:`HardwareFaultDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'pfm-oper'
                                            _revision = '2017-03-28'

                                            def __init__(self):
                                                super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__init__()

                                                self.yang_name = "hardware-fault-devices"
                                                self.yang_parent_name = "slot"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("hardware-fault-device", ("hardware_fault_device", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice))])
                                                self._leafs = OrderedDict()

                                                self.hardware_fault_device = YList(self)
                                                self._segment_path = lambda: "hardware-fault-devices"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices, [], name, value)


                                            class HardwareFaultDevice(Entity):
                                                """
                                                Table of Hardware Failure Device
                                                
                                                .. attribute:: hw_fault_device  (key)
                                                
                                                	hw fault device list
                                                	**type**\: str
                                                
                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: hardware_fault_type
                                                
                                                	Table of Hardware Failure Type
                                                	**type**\: list of  		 :py:class:`HardwareFaultType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'pfm-oper'
                                                _revision = '2017-03-28'

                                                def __init__(self):
                                                    super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__init__()

                                                    self.yang_name = "hardware-fault-device"
                                                    self.yang_parent_name = "hardware-fault-devices"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['hw_fault_device']
                                                    self._child_classes = OrderedDict([("hardware-fault-type", ("hardware_fault_type", PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType))])
                                                    self._leafs = OrderedDict([
                                                        ('hw_fault_device', (YLeaf(YType.str, 'hw-fault-device'), ['str'])),
                                                    ])
                                                    self.hw_fault_device = None

                                                    self.hardware_fault_type = YList(self)
                                                    self._segment_path = lambda: "hardware-fault-device" + "[hw-fault-device='" + str(self.hw_fault_device) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, ['hw_fault_device'], name, value)


                                                class HardwareFaultType(Entity):
                                                    """
                                                    Table of Hardware Failure Type
                                                    
                                                    .. attribute:: hw_fault_type  (key)
                                                    
                                                    	hw fault type list
                                                    	**type**\: str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: condition_description
                                                    
                                                    	Faulty Hardware Condition Description
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: condition_name
                                                    
                                                    	Faulty Hardware Condition Name
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: device_key
                                                    
                                                    	Faulty Hardware Device Key
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: device_version
                                                    
                                                    	Faulty Hardware Device Version
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: condition_raised_timestamp
                                                    
                                                    	Fault Raised Timestamp
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: process_id
                                                    
                                                    	Faulty Hardware Process ID
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: device_description
                                                    
                                                    	Faulty Hardware Device Description
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: condition_severity
                                                    
                                                    	Faulty Hardware Condition Severity
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'pfm-oper'
                                                    _revision = '2017-03-28'

                                                    def __init__(self):
                                                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__init__()

                                                        self.yang_name = "hardware-fault-type"
                                                        self.yang_parent_name = "hardware-fault-device"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['hw_fault_type']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('hw_fault_type', (YLeaf(YType.str, 'hw-fault-type'), ['str'])),
                                                            ('condition_description', (YLeaf(YType.str, 'condition-description'), ['str'])),
                                                            ('condition_name', (YLeaf(YType.str, 'condition-name'), ['str'])),
                                                            ('device_key', (YLeaf(YType.str, 'device-key'), ['str'])),
                                                            ('device_version', (YLeaf(YType.int32, 'device-version'), ['int'])),
                                                            ('condition_raised_timestamp', (YLeaf(YType.str, 'condition-raised-timestamp'), ['str'])),
                                                            ('process_id', (YLeaf(YType.int32, 'process-id'), ['int'])),
                                                            ('device_description', (YLeaf(YType.str, 'device-description'), ['str'])),
                                                            ('condition_severity', (YLeaf(YType.str, 'condition-severity'), ['str'])),
                                                        ])
                                                        self.hw_fault_type = None
                                                        self.condition_description = None
                                                        self.condition_name = None
                                                        self.device_key = None
                                                        self.device_version = None
                                                        self.condition_raised_timestamp = None
                                                        self.process_id = None
                                                        self.device_description = None
                                                        self.condition_severity = None
                                                        self._segment_path = lambda: "hardware-fault-type" + "[hw-fault-type='" + str(self.hw_fault_type) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.FaultType2s.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, ['hw_fault_type', 'condition_description', 'condition_name', 'device_key', 'device_version', 'condition_raised_timestamp', 'process_id', 'device_description', 'condition_severity'], name, value)











                class Racks(Entity):
                    """
                    Table of racks
                    
                    .. attribute:: rack
                    
                    	Number
                    	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pfm-oper'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks, self).__init__()

                        self.yang_name = "racks"
                        self.yang_parent_name = "fault-type1"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rack", ("rack", PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack))])
                        self._leafs = OrderedDict()

                        self.rack = YList(self)
                        self._segment_path = lambda: "racks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks, [], name, value)


                    class Rack(Entity):
                        """
                        Number
                        
                        .. attribute:: rack  (key)
                        
                        	Rack number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: slots
                        
                        	Table of slots
                        	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pfm-oper'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack, self).__init__()

                            self.yang_name = "rack"
                            self.yang_parent_name = "racks"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rack']
                            self._child_classes = OrderedDict([("slots", ("slots", PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots))])
                            self._leafs = OrderedDict([
                                ('rack', (YLeaf(YType.uint32, 'rack'), ['int'])),
                            ])
                            self.rack = None

                            self.slots = PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots()
                            self.slots.parent = self
                            self._children_name_map["slots"] = "slots"
                            self._segment_path = lambda: "rack" + "[rack='" + str(self.rack) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack, ['rack'], name, value)


                        class Slots(Entity):
                            """
                            Table of slots
                            
                            .. attribute:: slot
                            
                            	Name
                            	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pfm-oper'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots, self).__init__()

                                self.yang_name = "slots"
                                self.yang_parent_name = "rack"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("slot", ("slot", PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot))])
                                self._leafs = OrderedDict()

                                self.slot = YList(self)
                                self._segment_path = lambda: "slots"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots, [], name, value)


                            class Slot(Entity):
                                """
                                Name
                                
                                .. attribute:: slot  (key)
                                
                                	Slot name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                	**config**\: False
                                
                                .. attribute:: fault_summary
                                
                                	Table of Hardware Summary
                                	**type**\:  :py:class:`FaultSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.FaultSummary>`
                                
                                	**config**\: False
                                
                                .. attribute:: hardware_fault_devices
                                
                                	Table of Hardware Failure
                                	**type**\:  :py:class:`HardwareFaultDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pfm-oper'
                                _revision = '2017-03-28'

                                def __init__(self):
                                    super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot, self).__init__()

                                    self.yang_name = "slot"
                                    self.yang_parent_name = "slots"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['slot']
                                    self._child_classes = OrderedDict([("fault-summary", ("fault_summary", PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.FaultSummary)), ("hardware-fault-devices", ("hardware_fault_devices", PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices))])
                                    self._leafs = OrderedDict([
                                        ('slot', (YLeaf(YType.str, 'slot'), ['str'])),
                                    ])
                                    self.slot = None

                                    self.fault_summary = PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.FaultSummary()
                                    self.fault_summary.parent = self
                                    self._children_name_map["fault_summary"] = "fault-summary"

                                    self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                    self.hardware_fault_devices.parent = self
                                    self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                    self._segment_path = lambda: "slot" + "[slot='" + str(self.slot) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot, ['slot'], name, value)


                                class FaultSummary(Entity):
                                    """
                                    Table of Hardware Summary
                                    
                                    .. attribute:: severity_critical_count
                                    
                                    	Fault Severity Critical count
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: severity_emergency_or_alert_count
                                    
                                    	Fault Severity Emergency count
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total
                                    
                                    	Faulty Hardware total count
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: severity_error_count
                                    
                                    	Fault Severity Error count
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'pfm-oper'
                                    _revision = '2017-03-28'

                                    def __init__(self):
                                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.FaultSummary, self).__init__()

                                        self.yang_name = "fault-summary"
                                        self.yang_parent_name = "slot"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('severity_critical_count', (YLeaf(YType.int32, 'severity-critical-count'), ['int'])),
                                            ('severity_emergency_or_alert_count', (YLeaf(YType.int32, 'severity-emergency-or-alert-count'), ['int'])),
                                            ('total', (YLeaf(YType.int32, 'total'), ['int'])),
                                            ('severity_error_count', (YLeaf(YType.int32, 'severity-error-count'), ['int'])),
                                        ])
                                        self.severity_critical_count = None
                                        self.severity_emergency_or_alert_count = None
                                        self.total = None
                                        self.severity_error_count = None
                                        self._segment_path = lambda: "fault-summary"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.FaultSummary, ['severity_critical_count', 'severity_emergency_or_alert_count', 'total', 'severity_error_count'], name, value)



                                class HardwareFaultDevices(Entity):
                                    """
                                    Table of Hardware Failure
                                    
                                    .. attribute:: hardware_fault_device
                                    
                                    	Table of Hardware Failure Device
                                    	**type**\: list of  		 :py:class:`HardwareFaultDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'pfm-oper'
                                    _revision = '2017-03-28'

                                    def __init__(self):
                                        super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__init__()

                                        self.yang_name = "hardware-fault-devices"
                                        self.yang_parent_name = "slot"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("hardware-fault-device", ("hardware_fault_device", PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice))])
                                        self._leafs = OrderedDict()

                                        self.hardware_fault_device = YList(self)
                                        self._segment_path = lambda: "hardware-fault-devices"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices, [], name, value)


                                    class HardwareFaultDevice(Entity):
                                        """
                                        Table of Hardware Failure Device
                                        
                                        .. attribute:: hw_fault_device  (key)
                                        
                                        	hw fault device list
                                        	**type**\: str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: hardware_fault_type
                                        
                                        	Table of Hardware Failure Type
                                        	**type**\: list of  		 :py:class:`HardwareFaultType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'pfm-oper'
                                        _revision = '2017-03-28'

                                        def __init__(self):
                                            super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__init__()

                                            self.yang_name = "hardware-fault-device"
                                            self.yang_parent_name = "hardware-fault-devices"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['hw_fault_device']
                                            self._child_classes = OrderedDict([("hardware-fault-type", ("hardware_fault_type", PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType))])
                                            self._leafs = OrderedDict([
                                                ('hw_fault_device', (YLeaf(YType.str, 'hw-fault-device'), ['str'])),
                                            ])
                                            self.hw_fault_device = None

                                            self.hardware_fault_type = YList(self)
                                            self._segment_path = lambda: "hardware-fault-device" + "[hw-fault-device='" + str(self.hw_fault_device) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, ['hw_fault_device'], name, value)


                                        class HardwareFaultType(Entity):
                                            """
                                            Table of Hardware Failure Type
                                            
                                            .. attribute:: hw_fault_type  (key)
                                            
                                            	hw fault type list
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: condition_description
                                            
                                            	Faulty Hardware Condition Description
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: condition_name
                                            
                                            	Faulty Hardware Condition Name
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: device_key
                                            
                                            	Faulty Hardware Device Key
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: device_version
                                            
                                            	Faulty Hardware Device Version
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: condition_raised_timestamp
                                            
                                            	Fault Raised Timestamp
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: process_id
                                            
                                            	Faulty Hardware Process ID
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: device_description
                                            
                                            	Faulty Hardware Device Description
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: condition_severity
                                            
                                            	Faulty Hardware Condition Severity
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'pfm-oper'
                                            _revision = '2017-03-28'

                                            def __init__(self):
                                                super(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__init__()

                                                self.yang_name = "hardware-fault-type"
                                                self.yang_parent_name = "hardware-fault-device"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['hw_fault_type']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('hw_fault_type', (YLeaf(YType.str, 'hw-fault-type'), ['str'])),
                                                    ('condition_description', (YLeaf(YType.str, 'condition-description'), ['str'])),
                                                    ('condition_name', (YLeaf(YType.str, 'condition-name'), ['str'])),
                                                    ('device_key', (YLeaf(YType.str, 'device-key'), ['str'])),
                                                    ('device_version', (YLeaf(YType.int32, 'device-version'), ['int'])),
                                                    ('condition_raised_timestamp', (YLeaf(YType.str, 'condition-raised-timestamp'), ['str'])),
                                                    ('process_id', (YLeaf(YType.int32, 'process-id'), ['int'])),
                                                    ('device_description', (YLeaf(YType.str, 'device-description'), ['str'])),
                                                    ('condition_severity', (YLeaf(YType.str, 'condition-severity'), ['str'])),
                                                ])
                                                self.hw_fault_type = None
                                                self.condition_description = None
                                                self.condition_name = None
                                                self.device_key = None
                                                self.device_version = None
                                                self.condition_raised_timestamp = None
                                                self.process_id = None
                                                self.device_description = None
                                                self.condition_severity = None
                                                self._segment_path = lambda: "hardware-fault-type" + "[hw-fault-type='" + str(self.hw_fault_type) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformFaultManager.Exclude.FaultType1s.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, ['hw_fault_type', 'condition_description', 'condition_name', 'device_key', 'device_version', 'condition_raised_timestamp', 'process_id', 'device_description', 'condition_severity'], name, value)












    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Number
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack>`
        
        	**config**\: False
        
        

        """

        _prefix = 'pfm-oper'
        _revision = '2017-03-28'

        def __init__(self):
            super(PlatformFaultManager.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "platform-fault-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack", ("rack", PlatformFaultManager.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfm-oper:platform-fault-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformFaultManager.Racks, [], name, value)


        class Rack(Entity):
            """
            Number
            
            .. attribute:: rack  (key)
            
            	Rack number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots>`
            
            	**config**\: False
            
            

            """

            _prefix = 'pfm-oper'
            _revision = '2017-03-28'

            def __init__(self):
                super(PlatformFaultManager.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rack']
                self._child_classes = OrderedDict([("slots", ("slots", PlatformFaultManager.Racks.Rack.Slots))])
                self._leafs = OrderedDict([
                    ('rack', (YLeaf(YType.uint32, 'rack'), ['int'])),
                ])
                self.rack = None

                self.slots = PlatformFaultManager.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._segment_path = lambda: "rack" + "[rack='" + str(self.rack) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfm-oper:platform-fault-manager/racks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformFaultManager.Racks.Rack, ['rack'], name, value)


            class Slots(Entity):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Name
                	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pfm-oper'
                _revision = '2017-03-28'

                def __init__(self):
                    super(PlatformFaultManager.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slot", ("slot", PlatformFaultManager.Racks.Rack.Slots.Slot))])
                    self._leafs = OrderedDict()

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformFaultManager.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
                    """
                    Name
                    
                    .. attribute:: slot  (key)
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: fault_summary
                    
                    	Table of Hardware Summary
                    	**type**\:  :py:class:`FaultSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary>`
                    
                    	**config**\: False
                    
                    .. attribute:: hardware_fault_devices
                    
                    	Table of Hardware Failure
                    	**type**\:  :py:class:`HardwareFaultDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pfm-oper'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(PlatformFaultManager.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['slot']
                        self._child_classes = OrderedDict([("fault-summary", ("fault_summary", PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary)), ("hardware-fault-devices", ("hardware_fault_devices", PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices))])
                        self._leafs = OrderedDict([
                            ('slot', (YLeaf(YType.str, 'slot'), ['str'])),
                        ])
                        self.slot = None

                        self.fault_summary = PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary()
                        self.fault_summary.parent = self
                        self._children_name_map["fault_summary"] = "fault-summary"

                        self.hardware_fault_devices = PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                        self.hardware_fault_devices.parent = self
                        self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                        self._segment_path = lambda: "slot" + "[slot='" + str(self.slot) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformFaultManager.Racks.Rack.Slots.Slot, ['slot'], name, value)


                    class FaultSummary(Entity):
                        """
                        Table of Hardware Summary
                        
                        .. attribute:: severity_critical_count
                        
                        	Fault Severity Critical count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: severity_emergency_or_alert_count
                        
                        	Fault Severity Emergency count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: total
                        
                        	Faulty Hardware total count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: severity_error_count
                        
                        	Fault Severity Error count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pfm-oper'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary, self).__init__()

                            self.yang_name = "fault-summary"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('severity_critical_count', (YLeaf(YType.int32, 'severity-critical-count'), ['int'])),
                                ('severity_emergency_or_alert_count', (YLeaf(YType.int32, 'severity-emergency-or-alert-count'), ['int'])),
                                ('total', (YLeaf(YType.int32, 'total'), ['int'])),
                                ('severity_error_count', (YLeaf(YType.int32, 'severity-error-count'), ['int'])),
                            ])
                            self.severity_critical_count = None
                            self.severity_emergency_or_alert_count = None
                            self.total = None
                            self.severity_error_count = None
                            self._segment_path = lambda: "fault-summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary, ['severity_critical_count', 'severity_emergency_or_alert_count', 'total', 'severity_error_count'], name, value)



                    class HardwareFaultDevices(Entity):
                        """
                        Table of Hardware Failure
                        
                        .. attribute:: hardware_fault_device
                        
                        	Table of Hardware Failure Device
                        	**type**\: list of  		 :py:class:`HardwareFaultDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pfm-oper'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__init__()

                            self.yang_name = "hardware-fault-devices"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hardware-fault-device", ("hardware_fault_device", PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice))])
                            self._leafs = OrderedDict()

                            self.hardware_fault_device = YList(self)
                            self._segment_path = lambda: "hardware-fault-devices"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices, [], name, value)


                        class HardwareFaultDevice(Entity):
                            """
                            Table of Hardware Failure Device
                            
                            .. attribute:: hw_fault_device  (key)
                            
                            	hw fault device list
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: hardware_fault_type
                            
                            	Table of Hardware Failure Type
                            	**type**\: list of  		 :py:class:`HardwareFaultType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pfm-oper'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__init__()

                                self.yang_name = "hardware-fault-device"
                                self.yang_parent_name = "hardware-fault-devices"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['hw_fault_device']
                                self._child_classes = OrderedDict([("hardware-fault-type", ("hardware_fault_type", PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType))])
                                self._leafs = OrderedDict([
                                    ('hw_fault_device', (YLeaf(YType.str, 'hw-fault-device'), ['str'])),
                                ])
                                self.hw_fault_device = None

                                self.hardware_fault_type = YList(self)
                                self._segment_path = lambda: "hardware-fault-device" + "[hw-fault-device='" + str(self.hw_fault_device) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, ['hw_fault_device'], name, value)


                            class HardwareFaultType(Entity):
                                """
                                Table of Hardware Failure Type
                                
                                .. attribute:: hw_fault_type  (key)
                                
                                	hw fault type list
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                	**config**\: False
                                
                                .. attribute:: condition_description
                                
                                	Faulty Hardware Condition Description
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: condition_name
                                
                                	Faulty Hardware Condition Name
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: device_key
                                
                                	Faulty Hardware Device Key
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: device_version
                                
                                	Faulty Hardware Device Version
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                .. attribute:: condition_raised_timestamp
                                
                                	Fault Raised Timestamp
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: process_id
                                
                                	Faulty Hardware Process ID
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                .. attribute:: device_description
                                
                                	Faulty Hardware Device Description
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: condition_severity
                                
                                	Faulty Hardware Condition Severity
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pfm-oper'
                                _revision = '2017-03-28'

                                def __init__(self):
                                    super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__init__()

                                    self.yang_name = "hardware-fault-type"
                                    self.yang_parent_name = "hardware-fault-device"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['hw_fault_type']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('hw_fault_type', (YLeaf(YType.str, 'hw-fault-type'), ['str'])),
                                        ('condition_description', (YLeaf(YType.str, 'condition-description'), ['str'])),
                                        ('condition_name', (YLeaf(YType.str, 'condition-name'), ['str'])),
                                        ('device_key', (YLeaf(YType.str, 'device-key'), ['str'])),
                                        ('device_version', (YLeaf(YType.int32, 'device-version'), ['int'])),
                                        ('condition_raised_timestamp', (YLeaf(YType.str, 'condition-raised-timestamp'), ['str'])),
                                        ('process_id', (YLeaf(YType.int32, 'process-id'), ['int'])),
                                        ('device_description', (YLeaf(YType.str, 'device-description'), ['str'])),
                                        ('condition_severity', (YLeaf(YType.str, 'condition-severity'), ['str'])),
                                    ])
                                    self.hw_fault_type = None
                                    self.condition_description = None
                                    self.condition_name = None
                                    self.device_key = None
                                    self.device_version = None
                                    self.condition_raised_timestamp = None
                                    self.process_id = None
                                    self.device_description = None
                                    self.condition_severity = None
                                    self._segment_path = lambda: "hardware-fault-type" + "[hw-fault-type='" + str(self.hw_fault_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, ['hw_fault_type', 'condition_description', 'condition_name', 'device_key', 'device_version', 'condition_raised_timestamp', 'process_id', 'device_description', 'condition_severity'], name, value)








    def clone_ptr(self):
        self._top_entity = PlatformFaultManager()
        return self._top_entity



