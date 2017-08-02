""" Cisco_IOS_XR_pfm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pfm package operational data.

This module contains definitions
for the following management objects\:
  platform\-fault\-manager\: PFM data space

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PlatformFaultManager(Entity):
    """
    PFM data space
    
    .. attribute:: exclude
    
    	Exclude specic hw fault 
    	**type**\:   :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude>`
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks>`
    
    

    """

    _prefix = 'pfm-oper'
    _revision = '2017-03-28'

    def __init__(self):
        super(PlatformFaultManager, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-fault-manager"
        self.yang_parent_name = "Cisco-IOS-XR-pfm-oper"

        self.exclude = PlatformFaultManager.Exclude()
        self.exclude.parent = self
        self._children_name_map["exclude"] = "exclude"
        self._children_yang_names.add("exclude")

        self.racks = PlatformFaultManager.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")


    class Exclude(Entity):
        """
        Exclude specic hw fault 
        
        .. attribute:: fault_type1s
        
        	Table of Hardware Failure Device
        	**type**\:   :py:class:`FaultType1S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S>`
        
        

        """

        _prefix = 'pfm-oper'
        _revision = '2017-03-28'

        def __init__(self):
            super(PlatformFaultManager.Exclude, self).__init__()

            self.yang_name = "exclude"
            self.yang_parent_name = "platform-fault-manager"

            self.fault_type1s = PlatformFaultManager.Exclude.FaultType1S()
            self.fault_type1s.parent = self
            self._children_name_map["fault_type1s"] = "fault-type1s"
            self._children_yang_names.add("fault-type1s")


        class FaultType1S(Entity):
            """
            Table of Hardware Failure Device
            
            .. attribute:: fault_type1
            
            	Table of Hardware Failure Device
            	**type**\: list of    :py:class:`FaultType1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1>`
            
            

            """

            _prefix = 'pfm-oper'
            _revision = '2017-03-28'

            def __init__(self):
                super(PlatformFaultManager.Exclude.FaultType1S, self).__init__()

                self.yang_name = "fault-type1s"
                self.yang_parent_name = "exclude"

                self.fault_type1 = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PlatformFaultManager.Exclude.FaultType1S, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PlatformFaultManager.Exclude.FaultType1S, self).__setattr__(name, value)


            class FaultType1(Entity):
                """
                Table of Hardware Failure Device
                
                .. attribute:: hw_fault_type1  <key>
                
                	hw fault 1
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: fault_type2s
                
                	Table of Hardware Failure Device
                	**type**\:   :py:class:`FaultType2S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S>`
                
                .. attribute:: racks
                
                	Table of racks
                	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks>`
                
                

                """

                _prefix = 'pfm-oper'
                _revision = '2017-03-28'

                def __init__(self):
                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1, self).__init__()

                    self.yang_name = "fault-type1"
                    self.yang_parent_name = "fault-type1s"

                    self.hw_fault_type1 = YLeaf(YType.str, "hw-fault-type1")

                    self.fault_type2s = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S()
                    self.fault_type2s.parent = self
                    self._children_name_map["fault_type2s"] = "fault-type2s"
                    self._children_yang_names.add("fault-type2s")

                    self.racks = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks()
                    self.racks.parent = self
                    self._children_name_map["racks"] = "racks"
                    self._children_yang_names.add("racks")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("hw_fault_type1") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1, self).__setattr__(name, value)


                class FaultType2S(Entity):
                    """
                    Table of Hardware Failure Device
                    
                    .. attribute:: fault_type2
                    
                    	Table of Hardware Failure Device
                    	**type**\: list of    :py:class:`FaultType2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2>`
                    
                    

                    """

                    _prefix = 'pfm-oper'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S, self).__init__()

                        self.yang_name = "fault-type2s"
                        self.yang_parent_name = "fault-type1"

                        self.fault_type2 = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S, self).__setattr__(name, value)


                    class FaultType2(Entity):
                        """
                        Table of Hardware Failure Device
                        
                        .. attribute:: hw_fault_type2  <key>
                        
                        	hw fault 2
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: fault_type3s
                        
                        	Table of Hardware Failure Device
                        	**type**\:   :py:class:`FaultType3S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S>`
                        
                        .. attribute:: racks
                        
                        	Table of racks
                        	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks>`
                        
                        

                        """

                        _prefix = 'pfm-oper'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2, self).__init__()

                            self.yang_name = "fault-type2"
                            self.yang_parent_name = "fault-type2s"

                            self.hw_fault_type2 = YLeaf(YType.str, "hw-fault-type2")

                            self.fault_type3s = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S()
                            self.fault_type3s.parent = self
                            self._children_name_map["fault_type3s"] = "fault-type3s"
                            self._children_yang_names.add("fault-type3s")

                            self.racks = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks()
                            self.racks.parent = self
                            self._children_name_map["racks"] = "racks"
                            self._children_yang_names.add("racks")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("hw_fault_type2") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2, self).__setattr__(name, value)


                        class FaultType3S(Entity):
                            """
                            Table of Hardware Failure Device
                            
                            .. attribute:: fault_type3
                            
                            	Table of Hardware Failure Device
                            	**type**\: list of    :py:class:`FaultType3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3>`
                            
                            

                            """

                            _prefix = 'pfm-oper'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S, self).__init__()

                                self.yang_name = "fault-type3s"
                                self.yang_parent_name = "fault-type2"

                                self.fault_type3 = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S, self).__setattr__(name, value)


                            class FaultType3(Entity):
                                """
                                Table of Hardware Failure Device
                                
                                .. attribute:: hw_fault_type3  <key>
                                
                                	hw fault 3
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: racks
                                
                                	Table of racks
                                	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks>`
                                
                                

                                """

                                _prefix = 'pfm-oper'
                                _revision = '2017-03-28'

                                def __init__(self):
                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3, self).__init__()

                                    self.yang_name = "fault-type3"
                                    self.yang_parent_name = "fault-type3s"

                                    self.hw_fault_type3 = YLeaf(YType.str, "hw-fault-type3")

                                    self.racks = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks()
                                    self.racks.parent = self
                                    self._children_name_map["racks"] = "racks"
                                    self._children_yang_names.add("racks")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("hw_fault_type3") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3, self).__setattr__(name, value)


                                class Racks(Entity):
                                    """
                                    Table of racks
                                    
                                    .. attribute:: rack
                                    
                                    	Number
                                    	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack>`
                                    
                                    

                                    """

                                    _prefix = 'pfm-oper'
                                    _revision = '2017-03-28'

                                    def __init__(self):
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks, self).__init__()

                                        self.yang_name = "racks"
                                        self.yang_parent_name = "fault-type3"

                                        self.rack = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in () and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks, self).__setattr__(name, value)


                                    class Rack(Entity):
                                        """
                                        Number
                                        
                                        .. attribute:: rack  <key>
                                        
                                        	Rack number
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: slots
                                        
                                        	Table of slots
                                        	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots>`
                                        
                                        

                                        """

                                        _prefix = 'pfm-oper'
                                        _revision = '2017-03-28'

                                        def __init__(self):
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack, self).__init__()

                                            self.yang_name = "rack"
                                            self.yang_parent_name = "racks"

                                            self.rack = YLeaf(YType.int32, "rack")

                                            self.slots = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots()
                                            self.slots.parent = self
                                            self._children_name_map["slots"] = "slots"
                                            self._children_yang_names.add("slots")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("rack") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack, self).__setattr__(name, value)


                                        class Slots(Entity):
                                            """
                                            Table of slots
                                            
                                            .. attribute:: slot
                                            
                                            	Name
                                            	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot>`
                                            
                                            

                                            """

                                            _prefix = 'pfm-oper'
                                            _revision = '2017-03-28'

                                            def __init__(self):
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots, self).__init__()

                                                self.yang_name = "slots"
                                                self.yang_parent_name = "rack"

                                                self.slot = YList(self)

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in () and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots, self).__setattr__(name, value)


                                            class Slot(Entity):
                                                """
                                                Name
                                                
                                                .. attribute:: slot  <key>
                                                
                                                	Slot name
                                                	**type**\:  str
                                                
                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                
                                                .. attribute:: fault_summary
                                                
                                                	Table of Hardware Summary
                                                	**type**\:   :py:class:`FaultSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.FaultSummary>`
                                                
                                                .. attribute:: hardware_fault_devices
                                                
                                                	Table of Hardware Failure
                                                	**type**\:   :py:class:`HardwareFaultDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices>`
                                                
                                                

                                                """

                                                _prefix = 'pfm-oper'
                                                _revision = '2017-03-28'

                                                def __init__(self):
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot, self).__init__()

                                                    self.yang_name = "slot"
                                                    self.yang_parent_name = "slots"

                                                    self.slot = YLeaf(YType.str, "slot")

                                                    self.fault_summary = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.FaultSummary()
                                                    self.fault_summary.parent = self
                                                    self._children_name_map["fault_summary"] = "fault-summary"
                                                    self._children_yang_names.add("fault-summary")

                                                    self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                                    self.hardware_fault_devices.parent = self
                                                    self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                                    self._children_yang_names.add("hardware-fault-devices")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("slot") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot, self).__setattr__(name, value)


                                                class FaultSummary(Entity):
                                                    """
                                                    Table of Hardware Summary
                                                    
                                                    .. attribute:: severity_critical_count
                                                    
                                                    	Fault Severity Critical count
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: severity_emergency_or_alert_count
                                                    
                                                    	Fault Severity Emergency count
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: severity_error_count
                                                    
                                                    	Fault Severity Error count
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: total
                                                    
                                                    	Faulty Hardware total count
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'pfm-oper'
                                                    _revision = '2017-03-28'

                                                    def __init__(self):
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.FaultSummary, self).__init__()

                                                        self.yang_name = "fault-summary"
                                                        self.yang_parent_name = "slot"

                                                        self.severity_critical_count = YLeaf(YType.int32, "severity-critical-count")

                                                        self.severity_emergency_or_alert_count = YLeaf(YType.int32, "severity-emergency-or-alert-count")

                                                        self.severity_error_count = YLeaf(YType.int32, "severity-error-count")

                                                        self.total = YLeaf(YType.int32, "total")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("severity_critical_count",
                                                                        "severity_emergency_or_alert_count",
                                                                        "severity_error_count",
                                                                        "total") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.FaultSummary, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.FaultSummary, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.severity_critical_count.is_set or
                                                            self.severity_emergency_or_alert_count.is_set or
                                                            self.severity_error_count.is_set or
                                                            self.total.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.severity_critical_count.yfilter != YFilter.not_set or
                                                            self.severity_emergency_or_alert_count.yfilter != YFilter.not_set or
                                                            self.severity_error_count.yfilter != YFilter.not_set or
                                                            self.total.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "fault-summary" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.severity_critical_count.is_set or self.severity_critical_count.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.severity_critical_count.get_name_leafdata())
                                                        if (self.severity_emergency_or_alert_count.is_set or self.severity_emergency_or_alert_count.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.severity_emergency_or_alert_count.get_name_leafdata())
                                                        if (self.severity_error_count.is_set or self.severity_error_count.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.severity_error_count.get_name_leafdata())
                                                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.total.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "severity-critical-count" or name == "severity-emergency-or-alert-count" or name == "severity-error-count" or name == "total"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "severity-critical-count"):
                                                            self.severity_critical_count = value
                                                            self.severity_critical_count.value_namespace = name_space
                                                            self.severity_critical_count.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "severity-emergency-or-alert-count"):
                                                            self.severity_emergency_or_alert_count = value
                                                            self.severity_emergency_or_alert_count.value_namespace = name_space
                                                            self.severity_emergency_or_alert_count.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "severity-error-count"):
                                                            self.severity_error_count = value
                                                            self.severity_error_count.value_namespace = name_space
                                                            self.severity_error_count.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "total"):
                                                            self.total = value
                                                            self.total.value_namespace = name_space
                                                            self.total.value_namespace_prefix = name_space_prefix


                                                class HardwareFaultDevices(Entity):
                                                    """
                                                    Table of Hardware Failure
                                                    
                                                    .. attribute:: hardware_fault_device
                                                    
                                                    	Table of Hardware Failure Device
                                                    	**type**\: list of    :py:class:`HardwareFaultDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'pfm-oper'
                                                    _revision = '2017-03-28'

                                                    def __init__(self):
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__init__()

                                                        self.yang_name = "hardware-fault-devices"
                                                        self.yang_parent_name = "slot"

                                                        self.hardware_fault_device = YList(self)

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in () and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__setattr__(name, value)


                                                    class HardwareFaultDevice(Entity):
                                                        """
                                                        Table of Hardware Failure Device
                                                        
                                                        .. attribute:: hw_fault_device  <key>
                                                        
                                                        	hw fault device list
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                        
                                                        .. attribute:: hardware_fault_type
                                                        
                                                        	Table of Hardware Failure Type
                                                        	**type**\: list of    :py:class:`HardwareFaultType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'pfm-oper'
                                                        _revision = '2017-03-28'

                                                        def __init__(self):
                                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__init__()

                                                            self.yang_name = "hardware-fault-device"
                                                            self.yang_parent_name = "hardware-fault-devices"

                                                            self.hw_fault_device = YLeaf(YType.str, "hw-fault-device")

                                                            self.hardware_fault_type = YList(self)

                                                        def __setattr__(self, name, value):
                                                            self._check_monkey_patching_error(name, value)
                                                            with _handle_type_error():
                                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                        "Please use list append or extend method."
                                                                                        .format(value))
                                                                if isinstance(value, Enum.YLeaf):
                                                                    value = value.name
                                                                if name in ("hw_fault_device") and name in self.__dict__:
                                                                    if isinstance(value, YLeaf):
                                                                        self.__dict__[name].set(value.get())
                                                                    elif isinstance(value, YLeafList):
                                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__setattr__(name, value)
                                                                    else:
                                                                        self.__dict__[name].set(value)
                                                                else:
                                                                    if hasattr(value, "parent") and name != "parent":
                                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                            value.parent = self
                                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                            value.parent = self
                                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__setattr__(name, value)


                                                        class HardwareFaultType(Entity):
                                                            """
                                                            Table of Hardware Failure Type
                                                            
                                                            .. attribute:: hw_fault_type  <key>
                                                            
                                                            	hw fault type list
                                                            	**type**\:  str
                                                            
                                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                            
                                                            .. attribute:: condition_description
                                                            
                                                            	Faulty Hardware Condition Description
                                                            	**type**\:  str
                                                            
                                                            .. attribute:: condition_name
                                                            
                                                            	Faulty Hardware Condition Name
                                                            	**type**\:  str
                                                            
                                                            .. attribute:: condition_raised_timestamp
                                                            
                                                            	Fault Raised Timestamp
                                                            	**type**\:  str
                                                            
                                                            .. attribute:: condition_severity
                                                            
                                                            	Faulty Hardware Condition Severity
                                                            	**type**\:  str
                                                            
                                                            .. attribute:: device_description
                                                            
                                                            	Faulty Hardware Device Description
                                                            	**type**\:  str
                                                            
                                                            .. attribute:: device_key
                                                            
                                                            	Faulty Hardware Device Key
                                                            	**type**\:  str
                                                            
                                                            .. attribute:: device_version
                                                            
                                                            	Faulty Hardware Device Version
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: process_id
                                                            
                                                            	Faulty Hardware Process ID
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            

                                                            """

                                                            _prefix = 'pfm-oper'
                                                            _revision = '2017-03-28'

                                                            def __init__(self):
                                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__init__()

                                                                self.yang_name = "hardware-fault-type"
                                                                self.yang_parent_name = "hardware-fault-device"

                                                                self.hw_fault_type = YLeaf(YType.str, "hw-fault-type")

                                                                self.condition_description = YLeaf(YType.str, "condition-description")

                                                                self.condition_name = YLeaf(YType.str, "condition-name")

                                                                self.condition_raised_timestamp = YLeaf(YType.str, "condition-raised-timestamp")

                                                                self.condition_severity = YLeaf(YType.str, "condition-severity")

                                                                self.device_description = YLeaf(YType.str, "device-description")

                                                                self.device_key = YLeaf(YType.str, "device-key")

                                                                self.device_version = YLeaf(YType.int32, "device-version")

                                                                self.process_id = YLeaf(YType.int32, "process-id")

                                                            def __setattr__(self, name, value):
                                                                self._check_monkey_patching_error(name, value)
                                                                with _handle_type_error():
                                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                            "Please use list append or extend method."
                                                                                            .format(value))
                                                                    if isinstance(value, Enum.YLeaf):
                                                                        value = value.name
                                                                    if name in ("hw_fault_type",
                                                                                "condition_description",
                                                                                "condition_name",
                                                                                "condition_raised_timestamp",
                                                                                "condition_severity",
                                                                                "device_description",
                                                                                "device_key",
                                                                                "device_version",
                                                                                "process_id") and name in self.__dict__:
                                                                        if isinstance(value, YLeaf):
                                                                            self.__dict__[name].set(value.get())
                                                                        elif isinstance(value, YLeafList):
                                                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__setattr__(name, value)
                                                                        else:
                                                                            self.__dict__[name].set(value)
                                                                    else:
                                                                        if hasattr(value, "parent") and name != "parent":
                                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                                value.parent = self
                                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                                value.parent = self
                                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__setattr__(name, value)

                                                            def has_data(self):
                                                                return (
                                                                    self.hw_fault_type.is_set or
                                                                    self.condition_description.is_set or
                                                                    self.condition_name.is_set or
                                                                    self.condition_raised_timestamp.is_set or
                                                                    self.condition_severity.is_set or
                                                                    self.device_description.is_set or
                                                                    self.device_key.is_set or
                                                                    self.device_version.is_set or
                                                                    self.process_id.is_set)

                                                            def has_operation(self):
                                                                return (
                                                                    self.yfilter != YFilter.not_set or
                                                                    self.hw_fault_type.yfilter != YFilter.not_set or
                                                                    self.condition_description.yfilter != YFilter.not_set or
                                                                    self.condition_name.yfilter != YFilter.not_set or
                                                                    self.condition_raised_timestamp.yfilter != YFilter.not_set or
                                                                    self.condition_severity.yfilter != YFilter.not_set or
                                                                    self.device_description.yfilter != YFilter.not_set or
                                                                    self.device_key.yfilter != YFilter.not_set or
                                                                    self.device_version.yfilter != YFilter.not_set or
                                                                    self.process_id.yfilter != YFilter.not_set)

                                                            def get_segment_path(self):
                                                                path_buffer = ""
                                                                path_buffer = "hardware-fault-type" + "[hw-fault-type='" + self.hw_fault_type.get() + "']" + path_buffer

                                                                return path_buffer

                                                            def get_entity_path(self, ancestor):
                                                                path_buffer = ""
                                                                if (ancestor is None):
                                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                                else:
                                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                                leaf_name_data = LeafDataList()
                                                                if (self.hw_fault_type.is_set or self.hw_fault_type.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.hw_fault_type.get_name_leafdata())
                                                                if (self.condition_description.is_set or self.condition_description.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.condition_description.get_name_leafdata())
                                                                if (self.condition_name.is_set or self.condition_name.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.condition_name.get_name_leafdata())
                                                                if (self.condition_raised_timestamp.is_set or self.condition_raised_timestamp.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.condition_raised_timestamp.get_name_leafdata())
                                                                if (self.condition_severity.is_set or self.condition_severity.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.condition_severity.get_name_leafdata())
                                                                if (self.device_description.is_set or self.device_description.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.device_description.get_name_leafdata())
                                                                if (self.device_key.is_set or self.device_key.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.device_key.get_name_leafdata())
                                                                if (self.device_version.is_set or self.device_version.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.device_version.get_name_leafdata())
                                                                if (self.process_id.is_set or self.process_id.yfilter != YFilter.not_set):
                                                                    leaf_name_data.append(self.process_id.get_name_leafdata())

                                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                                return entity_path

                                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                                if child is not None:
                                                                    return child

                                                                return None

                                                            def has_leaf_or_child_of_name(self, name):
                                                                if(name == "hw-fault-type" or name == "condition-description" or name == "condition-name" or name == "condition-raised-timestamp" or name == "condition-severity" or name == "device-description" or name == "device-key" or name == "device-version" or name == "process-id"):
                                                                    return True
                                                                return False

                                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                                if(value_path == "hw-fault-type"):
                                                                    self.hw_fault_type = value
                                                                    self.hw_fault_type.value_namespace = name_space
                                                                    self.hw_fault_type.value_namespace_prefix = name_space_prefix
                                                                if(value_path == "condition-description"):
                                                                    self.condition_description = value
                                                                    self.condition_description.value_namespace = name_space
                                                                    self.condition_description.value_namespace_prefix = name_space_prefix
                                                                if(value_path == "condition-name"):
                                                                    self.condition_name = value
                                                                    self.condition_name.value_namespace = name_space
                                                                    self.condition_name.value_namespace_prefix = name_space_prefix
                                                                if(value_path == "condition-raised-timestamp"):
                                                                    self.condition_raised_timestamp = value
                                                                    self.condition_raised_timestamp.value_namespace = name_space
                                                                    self.condition_raised_timestamp.value_namespace_prefix = name_space_prefix
                                                                if(value_path == "condition-severity"):
                                                                    self.condition_severity = value
                                                                    self.condition_severity.value_namespace = name_space
                                                                    self.condition_severity.value_namespace_prefix = name_space_prefix
                                                                if(value_path == "device-description"):
                                                                    self.device_description = value
                                                                    self.device_description.value_namespace = name_space
                                                                    self.device_description.value_namespace_prefix = name_space_prefix
                                                                if(value_path == "device-key"):
                                                                    self.device_key = value
                                                                    self.device_key.value_namespace = name_space
                                                                    self.device_key.value_namespace_prefix = name_space_prefix
                                                                if(value_path == "device-version"):
                                                                    self.device_version = value
                                                                    self.device_version.value_namespace = name_space
                                                                    self.device_version.value_namespace_prefix = name_space_prefix
                                                                if(value_path == "process-id"):
                                                                    self.process_id = value
                                                                    self.process_id.value_namespace = name_space
                                                                    self.process_id.value_namespace_prefix = name_space_prefix

                                                        def has_data(self):
                                                            for c in self.hardware_fault_type:
                                                                if (c.has_data()):
                                                                    return True
                                                            return self.hw_fault_device.is_set

                                                        def has_operation(self):
                                                            for c in self.hardware_fault_type:
                                                                if (c.has_operation()):
                                                                    return True
                                                            return (
                                                                self.yfilter != YFilter.not_set or
                                                                self.hw_fault_device.yfilter != YFilter.not_set)

                                                        def get_segment_path(self):
                                                            path_buffer = ""
                                                            path_buffer = "hardware-fault-device" + "[hw-fault-device='" + self.hw_fault_device.get() + "']" + path_buffer

                                                            return path_buffer

                                                        def get_entity_path(self, ancestor):
                                                            path_buffer = ""
                                                            if (ancestor is None):
                                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                            else:
                                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                            leaf_name_data = LeafDataList()
                                                            if (self.hw_fault_device.is_set or self.hw_fault_device.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.hw_fault_device.get_name_leafdata())

                                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                                            return entity_path

                                                        def get_child_by_name(self, child_yang_name, segment_path):
                                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                            if child is not None:
                                                                return child

                                                            if (child_yang_name == "hardware-fault-type"):
                                                                for c in self.hardware_fault_type:
                                                                    segment = c.get_segment_path()
                                                                    if (segment_path == segment):
                                                                        return c
                                                                c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType()
                                                                c.parent = self
                                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                                self._local_refs[local_reference_key] = c
                                                                self.hardware_fault_type.append(c)
                                                                return c

                                                            return None

                                                        def has_leaf_or_child_of_name(self, name):
                                                            if(name == "hardware-fault-type" or name == "hw-fault-device"):
                                                                return True
                                                            return False

                                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                                            if(value_path == "hw-fault-device"):
                                                                self.hw_fault_device = value
                                                                self.hw_fault_device.value_namespace = name_space
                                                                self.hw_fault_device.value_namespace_prefix = name_space_prefix

                                                    def has_data(self):
                                                        for c in self.hardware_fault_device:
                                                            if (c.has_data()):
                                                                return True
                                                        return False

                                                    def has_operation(self):
                                                        for c in self.hardware_fault_device:
                                                            if (c.has_operation()):
                                                                return True
                                                        return self.yfilter != YFilter.not_set

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "hardware-fault-devices" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        if (child_yang_name == "hardware-fault-device"):
                                                            for c in self.hardware_fault_device:
                                                                segment = c.get_segment_path()
                                                                if (segment_path == segment):
                                                                    return c
                                                            c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice()
                                                            c.parent = self
                                                            local_reference_key = "ydk::seg::%s" % segment_path
                                                            self._local_refs[local_reference_key] = c
                                                            self.hardware_fault_device.append(c)
                                                            return c

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "hardware-fault-device"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        pass

                                                def has_data(self):
                                                    return (
                                                        self.slot.is_set or
                                                        (self.fault_summary is not None and self.fault_summary.has_data()) or
                                                        (self.hardware_fault_devices is not None and self.hardware_fault_devices.has_data()))

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.slot.yfilter != YFilter.not_set or
                                                        (self.fault_summary is not None and self.fault_summary.has_operation()) or
                                                        (self.hardware_fault_devices is not None and self.hardware_fault_devices.has_operation()))

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "slot" + "[slot='" + self.slot.get() + "']" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.slot.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "fault-summary"):
                                                        if (self.fault_summary is None):
                                                            self.fault_summary = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.FaultSummary()
                                                            self.fault_summary.parent = self
                                                            self._children_name_map["fault_summary"] = "fault-summary"
                                                        return self.fault_summary

                                                    if (child_yang_name == "hardware-fault-devices"):
                                                        if (self.hardware_fault_devices is None):
                                                            self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                                            self.hardware_fault_devices.parent = self
                                                            self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                                        return self.hardware_fault_devices

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "fault-summary" or name == "hardware-fault-devices" or name == "slot"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "slot"):
                                                        self.slot = value
                                                        self.slot.value_namespace = name_space
                                                        self.slot.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                for c in self.slot:
                                                    if (c.has_data()):
                                                        return True
                                                return False

                                            def has_operation(self):
                                                for c in self.slot:
                                                    if (c.has_operation()):
                                                        return True
                                                return self.yfilter != YFilter.not_set

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "slots" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "slot"):
                                                    for c in self.slot:
                                                        segment = c.get_segment_path()
                                                        if (segment_path == segment):
                                                            return c
                                                    c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots.Slot()
                                                    c.parent = self
                                                    local_reference_key = "ydk::seg::%s" % segment_path
                                                    self._local_refs[local_reference_key] = c
                                                    self.slot.append(c)
                                                    return c

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "slot"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass

                                        def has_data(self):
                                            return (
                                                self.rack.is_set or
                                                (self.slots is not None and self.slots.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.rack.yfilter != YFilter.not_set or
                                                (self.slots is not None and self.slots.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "rack" + "[rack='" + self.rack.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.rack.is_set or self.rack.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.rack.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "slots"):
                                                if (self.slots is None):
                                                    self.slots = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack.Slots()
                                                    self.slots.parent = self
                                                    self._children_name_map["slots"] = "slots"
                                                return self.slots

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "slots" or name == "rack"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "rack"):
                                                self.rack = value
                                                self.rack.value_namespace = name_space
                                                self.rack.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.rack:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.rack:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "racks" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "rack"):
                                            for c in self.rack:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks.Rack()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.rack.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "rack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.hw_fault_type3.is_set or
                                        (self.racks is not None and self.racks.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.hw_fault_type3.yfilter != YFilter.not_set or
                                        (self.racks is not None and self.racks.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "fault-type3" + "[hw-fault-type3='" + self.hw_fault_type3.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.hw_fault_type3.is_set or self.hw_fault_type3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hw_fault_type3.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "racks"):
                                        if (self.racks is None):
                                            self.racks = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3.Racks()
                                            self.racks.parent = self
                                            self._children_name_map["racks"] = "racks"
                                        return self.racks

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "racks" or name == "hw-fault-type3"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "hw-fault-type3"):
                                        self.hw_fault_type3 = value
                                        self.hw_fault_type3.value_namespace = name_space
                                        self.hw_fault_type3.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.fault_type3:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.fault_type3:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fault-type3s" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "fault-type3"):
                                    for c in self.fault_type3:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S.FaultType3()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.fault_type3.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fault-type3"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Racks(Entity):
                            """
                            Table of racks
                            
                            .. attribute:: rack
                            
                            	Number
                            	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack>`
                            
                            

                            """

                            _prefix = 'pfm-oper'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks, self).__init__()

                                self.yang_name = "racks"
                                self.yang_parent_name = "fault-type2"

                                self.rack = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks, self).__setattr__(name, value)


                            class Rack(Entity):
                                """
                                Number
                                
                                .. attribute:: rack  <key>
                                
                                	Rack number
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: slots
                                
                                	Table of slots
                                	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots>`
                                
                                

                                """

                                _prefix = 'pfm-oper'
                                _revision = '2017-03-28'

                                def __init__(self):
                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack, self).__init__()

                                    self.yang_name = "rack"
                                    self.yang_parent_name = "racks"

                                    self.rack = YLeaf(YType.int32, "rack")

                                    self.slots = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots()
                                    self.slots.parent = self
                                    self._children_name_map["slots"] = "slots"
                                    self._children_yang_names.add("slots")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("rack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack, self).__setattr__(name, value)


                                class Slots(Entity):
                                    """
                                    Table of slots
                                    
                                    .. attribute:: slot
                                    
                                    	Name
                                    	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot>`
                                    
                                    

                                    """

                                    _prefix = 'pfm-oper'
                                    _revision = '2017-03-28'

                                    def __init__(self):
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots, self).__init__()

                                        self.yang_name = "slots"
                                        self.yang_parent_name = "rack"

                                        self.slot = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in () and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots, self).__setattr__(name, value)


                                    class Slot(Entity):
                                        """
                                        Name
                                        
                                        .. attribute:: slot  <key>
                                        
                                        	Slot name
                                        	**type**\:  str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        .. attribute:: fault_summary
                                        
                                        	Table of Hardware Summary
                                        	**type**\:   :py:class:`FaultSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.FaultSummary>`
                                        
                                        .. attribute:: hardware_fault_devices
                                        
                                        	Table of Hardware Failure
                                        	**type**\:   :py:class:`HardwareFaultDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices>`
                                        
                                        

                                        """

                                        _prefix = 'pfm-oper'
                                        _revision = '2017-03-28'

                                        def __init__(self):
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot, self).__init__()

                                            self.yang_name = "slot"
                                            self.yang_parent_name = "slots"

                                            self.slot = YLeaf(YType.str, "slot")

                                            self.fault_summary = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.FaultSummary()
                                            self.fault_summary.parent = self
                                            self._children_name_map["fault_summary"] = "fault-summary"
                                            self._children_yang_names.add("fault-summary")

                                            self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                            self.hardware_fault_devices.parent = self
                                            self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                            self._children_yang_names.add("hardware-fault-devices")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("slot") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot, self).__setattr__(name, value)


                                        class FaultSummary(Entity):
                                            """
                                            Table of Hardware Summary
                                            
                                            .. attribute:: severity_critical_count
                                            
                                            	Fault Severity Critical count
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: severity_emergency_or_alert_count
                                            
                                            	Fault Severity Emergency count
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: severity_error_count
                                            
                                            	Fault Severity Error count
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: total
                                            
                                            	Faulty Hardware total count
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'pfm-oper'
                                            _revision = '2017-03-28'

                                            def __init__(self):
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.FaultSummary, self).__init__()

                                                self.yang_name = "fault-summary"
                                                self.yang_parent_name = "slot"

                                                self.severity_critical_count = YLeaf(YType.int32, "severity-critical-count")

                                                self.severity_emergency_or_alert_count = YLeaf(YType.int32, "severity-emergency-or-alert-count")

                                                self.severity_error_count = YLeaf(YType.int32, "severity-error-count")

                                                self.total = YLeaf(YType.int32, "total")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("severity_critical_count",
                                                                "severity_emergency_or_alert_count",
                                                                "severity_error_count",
                                                                "total") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.FaultSummary, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.FaultSummary, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.severity_critical_count.is_set or
                                                    self.severity_emergency_or_alert_count.is_set or
                                                    self.severity_error_count.is_set or
                                                    self.total.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.severity_critical_count.yfilter != YFilter.not_set or
                                                    self.severity_emergency_or_alert_count.yfilter != YFilter.not_set or
                                                    self.severity_error_count.yfilter != YFilter.not_set or
                                                    self.total.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "fault-summary" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.severity_critical_count.is_set or self.severity_critical_count.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.severity_critical_count.get_name_leafdata())
                                                if (self.severity_emergency_or_alert_count.is_set or self.severity_emergency_or_alert_count.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.severity_emergency_or_alert_count.get_name_leafdata())
                                                if (self.severity_error_count.is_set or self.severity_error_count.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.severity_error_count.get_name_leafdata())
                                                if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.total.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "severity-critical-count" or name == "severity-emergency-or-alert-count" or name == "severity-error-count" or name == "total"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "severity-critical-count"):
                                                    self.severity_critical_count = value
                                                    self.severity_critical_count.value_namespace = name_space
                                                    self.severity_critical_count.value_namespace_prefix = name_space_prefix
                                                if(value_path == "severity-emergency-or-alert-count"):
                                                    self.severity_emergency_or_alert_count = value
                                                    self.severity_emergency_or_alert_count.value_namespace = name_space
                                                    self.severity_emergency_or_alert_count.value_namespace_prefix = name_space_prefix
                                                if(value_path == "severity-error-count"):
                                                    self.severity_error_count = value
                                                    self.severity_error_count.value_namespace = name_space
                                                    self.severity_error_count.value_namespace_prefix = name_space_prefix
                                                if(value_path == "total"):
                                                    self.total = value
                                                    self.total.value_namespace = name_space
                                                    self.total.value_namespace_prefix = name_space_prefix


                                        class HardwareFaultDevices(Entity):
                                            """
                                            Table of Hardware Failure
                                            
                                            .. attribute:: hardware_fault_device
                                            
                                            	Table of Hardware Failure Device
                                            	**type**\: list of    :py:class:`HardwareFaultDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice>`
                                            
                                            

                                            """

                                            _prefix = 'pfm-oper'
                                            _revision = '2017-03-28'

                                            def __init__(self):
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__init__()

                                                self.yang_name = "hardware-fault-devices"
                                                self.yang_parent_name = "slot"

                                                self.hardware_fault_device = YList(self)

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in () and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__setattr__(name, value)


                                            class HardwareFaultDevice(Entity):
                                                """
                                                Table of Hardware Failure Device
                                                
                                                .. attribute:: hw_fault_device  <key>
                                                
                                                	hw fault device list
                                                	**type**\:  str
                                                
                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                
                                                .. attribute:: hardware_fault_type
                                                
                                                	Table of Hardware Failure Type
                                                	**type**\: list of    :py:class:`HardwareFaultType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType>`
                                                
                                                

                                                """

                                                _prefix = 'pfm-oper'
                                                _revision = '2017-03-28'

                                                def __init__(self):
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__init__()

                                                    self.yang_name = "hardware-fault-device"
                                                    self.yang_parent_name = "hardware-fault-devices"

                                                    self.hw_fault_device = YLeaf(YType.str, "hw-fault-device")

                                                    self.hardware_fault_type = YList(self)

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("hw_fault_device") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__setattr__(name, value)


                                                class HardwareFaultType(Entity):
                                                    """
                                                    Table of Hardware Failure Type
                                                    
                                                    .. attribute:: hw_fault_type  <key>
                                                    
                                                    	hw fault type list
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    .. attribute:: condition_description
                                                    
                                                    	Faulty Hardware Condition Description
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: condition_name
                                                    
                                                    	Faulty Hardware Condition Name
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: condition_raised_timestamp
                                                    
                                                    	Fault Raised Timestamp
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: condition_severity
                                                    
                                                    	Faulty Hardware Condition Severity
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: device_description
                                                    
                                                    	Faulty Hardware Device Description
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: device_key
                                                    
                                                    	Faulty Hardware Device Key
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: device_version
                                                    
                                                    	Faulty Hardware Device Version
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: process_id
                                                    
                                                    	Faulty Hardware Process ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'pfm-oper'
                                                    _revision = '2017-03-28'

                                                    def __init__(self):
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__init__()

                                                        self.yang_name = "hardware-fault-type"
                                                        self.yang_parent_name = "hardware-fault-device"

                                                        self.hw_fault_type = YLeaf(YType.str, "hw-fault-type")

                                                        self.condition_description = YLeaf(YType.str, "condition-description")

                                                        self.condition_name = YLeaf(YType.str, "condition-name")

                                                        self.condition_raised_timestamp = YLeaf(YType.str, "condition-raised-timestamp")

                                                        self.condition_severity = YLeaf(YType.str, "condition-severity")

                                                        self.device_description = YLeaf(YType.str, "device-description")

                                                        self.device_key = YLeaf(YType.str, "device-key")

                                                        self.device_version = YLeaf(YType.int32, "device-version")

                                                        self.process_id = YLeaf(YType.int32, "process-id")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("hw_fault_type",
                                                                        "condition_description",
                                                                        "condition_name",
                                                                        "condition_raised_timestamp",
                                                                        "condition_severity",
                                                                        "device_description",
                                                                        "device_key",
                                                                        "device_version",
                                                                        "process_id") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.hw_fault_type.is_set or
                                                            self.condition_description.is_set or
                                                            self.condition_name.is_set or
                                                            self.condition_raised_timestamp.is_set or
                                                            self.condition_severity.is_set or
                                                            self.device_description.is_set or
                                                            self.device_key.is_set or
                                                            self.device_version.is_set or
                                                            self.process_id.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.hw_fault_type.yfilter != YFilter.not_set or
                                                            self.condition_description.yfilter != YFilter.not_set or
                                                            self.condition_name.yfilter != YFilter.not_set or
                                                            self.condition_raised_timestamp.yfilter != YFilter.not_set or
                                                            self.condition_severity.yfilter != YFilter.not_set or
                                                            self.device_description.yfilter != YFilter.not_set or
                                                            self.device_key.yfilter != YFilter.not_set or
                                                            self.device_version.yfilter != YFilter.not_set or
                                                            self.process_id.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "hardware-fault-type" + "[hw-fault-type='" + self.hw_fault_type.get() + "']" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.hw_fault_type.is_set or self.hw_fault_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.hw_fault_type.get_name_leafdata())
                                                        if (self.condition_description.is_set or self.condition_description.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.condition_description.get_name_leafdata())
                                                        if (self.condition_name.is_set or self.condition_name.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.condition_name.get_name_leafdata())
                                                        if (self.condition_raised_timestamp.is_set or self.condition_raised_timestamp.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.condition_raised_timestamp.get_name_leafdata())
                                                        if (self.condition_severity.is_set or self.condition_severity.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.condition_severity.get_name_leafdata())
                                                        if (self.device_description.is_set or self.device_description.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.device_description.get_name_leafdata())
                                                        if (self.device_key.is_set or self.device_key.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.device_key.get_name_leafdata())
                                                        if (self.device_version.is_set or self.device_version.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.device_version.get_name_leafdata())
                                                        if (self.process_id.is_set or self.process_id.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.process_id.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "hw-fault-type" or name == "condition-description" or name == "condition-name" or name == "condition-raised-timestamp" or name == "condition-severity" or name == "device-description" or name == "device-key" or name == "device-version" or name == "process-id"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "hw-fault-type"):
                                                            self.hw_fault_type = value
                                                            self.hw_fault_type.value_namespace = name_space
                                                            self.hw_fault_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "condition-description"):
                                                            self.condition_description = value
                                                            self.condition_description.value_namespace = name_space
                                                            self.condition_description.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "condition-name"):
                                                            self.condition_name = value
                                                            self.condition_name.value_namespace = name_space
                                                            self.condition_name.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "condition-raised-timestamp"):
                                                            self.condition_raised_timestamp = value
                                                            self.condition_raised_timestamp.value_namespace = name_space
                                                            self.condition_raised_timestamp.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "condition-severity"):
                                                            self.condition_severity = value
                                                            self.condition_severity.value_namespace = name_space
                                                            self.condition_severity.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "device-description"):
                                                            self.device_description = value
                                                            self.device_description.value_namespace = name_space
                                                            self.device_description.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "device-key"):
                                                            self.device_key = value
                                                            self.device_key.value_namespace = name_space
                                                            self.device_key.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "device-version"):
                                                            self.device_version = value
                                                            self.device_version.value_namespace = name_space
                                                            self.device_version.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "process-id"):
                                                            self.process_id = value
                                                            self.process_id.value_namespace = name_space
                                                            self.process_id.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    for c in self.hardware_fault_type:
                                                        if (c.has_data()):
                                                            return True
                                                    return self.hw_fault_device.is_set

                                                def has_operation(self):
                                                    for c in self.hardware_fault_type:
                                                        if (c.has_operation()):
                                                            return True
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.hw_fault_device.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "hardware-fault-device" + "[hw-fault-device='" + self.hw_fault_device.get() + "']" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.hw_fault_device.is_set or self.hw_fault_device.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.hw_fault_device.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "hardware-fault-type"):
                                                        for c in self.hardware_fault_type:
                                                            segment = c.get_segment_path()
                                                            if (segment_path == segment):
                                                                return c
                                                        c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType()
                                                        c.parent = self
                                                        local_reference_key = "ydk::seg::%s" % segment_path
                                                        self._local_refs[local_reference_key] = c
                                                        self.hardware_fault_type.append(c)
                                                        return c

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "hardware-fault-type" or name == "hw-fault-device"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "hw-fault-device"):
                                                        self.hw_fault_device = value
                                                        self.hw_fault_device.value_namespace = name_space
                                                        self.hw_fault_device.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                for c in self.hardware_fault_device:
                                                    if (c.has_data()):
                                                        return True
                                                return False

                                            def has_operation(self):
                                                for c in self.hardware_fault_device:
                                                    if (c.has_operation()):
                                                        return True
                                                return self.yfilter != YFilter.not_set

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "hardware-fault-devices" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "hardware-fault-device"):
                                                    for c in self.hardware_fault_device:
                                                        segment = c.get_segment_path()
                                                        if (segment_path == segment):
                                                            return c
                                                    c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice()
                                                    c.parent = self
                                                    local_reference_key = "ydk::seg::%s" % segment_path
                                                    self._local_refs[local_reference_key] = c
                                                    self.hardware_fault_device.append(c)
                                                    return c

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "hardware-fault-device"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass

                                        def has_data(self):
                                            return (
                                                self.slot.is_set or
                                                (self.fault_summary is not None and self.fault_summary.has_data()) or
                                                (self.hardware_fault_devices is not None and self.hardware_fault_devices.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.slot.yfilter != YFilter.not_set or
                                                (self.fault_summary is not None and self.fault_summary.has_operation()) or
                                                (self.hardware_fault_devices is not None and self.hardware_fault_devices.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "slot" + "[slot='" + self.slot.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.slot.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "fault-summary"):
                                                if (self.fault_summary is None):
                                                    self.fault_summary = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.FaultSummary()
                                                    self.fault_summary.parent = self
                                                    self._children_name_map["fault_summary"] = "fault-summary"
                                                return self.fault_summary

                                            if (child_yang_name == "hardware-fault-devices"):
                                                if (self.hardware_fault_devices is None):
                                                    self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                                    self.hardware_fault_devices.parent = self
                                                    self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                                return self.hardware_fault_devices

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "fault-summary" or name == "hardware-fault-devices" or name == "slot"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "slot"):
                                                self.slot = value
                                                self.slot.value_namespace = name_space
                                                self.slot.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.slot:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.slot:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "slots" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "slot"):
                                            for c in self.slot:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots.Slot()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.slot.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "slot"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.rack.is_set or
                                        (self.slots is not None and self.slots.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.rack.yfilter != YFilter.not_set or
                                        (self.slots is not None and self.slots.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "rack" + "[rack='" + self.rack.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.rack.is_set or self.rack.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "slots"):
                                        if (self.slots is None):
                                            self.slots = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack.Slots()
                                            self.slots.parent = self
                                            self._children_name_map["slots"] = "slots"
                                        return self.slots

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "slots" or name == "rack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "rack"):
                                        self.rack = value
                                        self.rack.value_namespace = name_space
                                        self.rack.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.rack:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.rack:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "racks" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "rack"):
                                    for c in self.rack:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks.Rack()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.rack.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "rack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.hw_fault_type2.is_set or
                                (self.fault_type3s is not None and self.fault_type3s.has_data()) or
                                (self.racks is not None and self.racks.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.hw_fault_type2.yfilter != YFilter.not_set or
                                (self.fault_type3s is not None and self.fault_type3s.has_operation()) or
                                (self.racks is not None and self.racks.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "fault-type2" + "[hw-fault-type2='" + self.hw_fault_type2.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.hw_fault_type2.is_set or self.hw_fault_type2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hw_fault_type2.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "fault-type3s"):
                                if (self.fault_type3s is None):
                                    self.fault_type3s = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.FaultType3S()
                                    self.fault_type3s.parent = self
                                    self._children_name_map["fault_type3s"] = "fault-type3s"
                                return self.fault_type3s

                            if (child_yang_name == "racks"):
                                if (self.racks is None):
                                    self.racks = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2.Racks()
                                    self.racks.parent = self
                                    self._children_name_map["racks"] = "racks"
                                return self.racks

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "fault-type3s" or name == "racks" or name == "hw-fault-type2"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "hw-fault-type2"):
                                self.hw_fault_type2 = value
                                self.hw_fault_type2.value_namespace = name_space
                                self.hw_fault_type2.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.fault_type2:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.fault_type2:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fault-type2s" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "fault-type2"):
                            for c in self.fault_type2:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S.FaultType2()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.fault_type2.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "fault-type2"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Racks(Entity):
                    """
                    Table of racks
                    
                    .. attribute:: rack
                    
                    	Number
                    	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack>`
                    
                    

                    """

                    _prefix = 'pfm-oper'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks, self).__init__()

                        self.yang_name = "racks"
                        self.yang_parent_name = "fault-type1"

                        self.rack = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks, self).__setattr__(name, value)


                    class Rack(Entity):
                        """
                        Number
                        
                        .. attribute:: rack  <key>
                        
                        	Rack number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: slots
                        
                        	Table of slots
                        	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots>`
                        
                        

                        """

                        _prefix = 'pfm-oper'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack, self).__init__()

                            self.yang_name = "rack"
                            self.yang_parent_name = "racks"

                            self.rack = YLeaf(YType.int32, "rack")

                            self.slots = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots()
                            self.slots.parent = self
                            self._children_name_map["slots"] = "slots"
                            self._children_yang_names.add("slots")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("rack") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack, self).__setattr__(name, value)


                        class Slots(Entity):
                            """
                            Table of slots
                            
                            .. attribute:: slot
                            
                            	Name
                            	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot>`
                            
                            

                            """

                            _prefix = 'pfm-oper'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots, self).__init__()

                                self.yang_name = "slots"
                                self.yang_parent_name = "rack"

                                self.slot = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots, self).__setattr__(name, value)


                            class Slot(Entity):
                                """
                                Name
                                
                                .. attribute:: slot  <key>
                                
                                	Slot name
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: fault_summary
                                
                                	Table of Hardware Summary
                                	**type**\:   :py:class:`FaultSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.FaultSummary>`
                                
                                .. attribute:: hardware_fault_devices
                                
                                	Table of Hardware Failure
                                	**type**\:   :py:class:`HardwareFaultDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices>`
                                
                                

                                """

                                _prefix = 'pfm-oper'
                                _revision = '2017-03-28'

                                def __init__(self):
                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot, self).__init__()

                                    self.yang_name = "slot"
                                    self.yang_parent_name = "slots"

                                    self.slot = YLeaf(YType.str, "slot")

                                    self.fault_summary = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.FaultSummary()
                                    self.fault_summary.parent = self
                                    self._children_name_map["fault_summary"] = "fault-summary"
                                    self._children_yang_names.add("fault-summary")

                                    self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                    self.hardware_fault_devices.parent = self
                                    self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                    self._children_yang_names.add("hardware-fault-devices")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("slot") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot, self).__setattr__(name, value)


                                class FaultSummary(Entity):
                                    """
                                    Table of Hardware Summary
                                    
                                    .. attribute:: severity_critical_count
                                    
                                    	Fault Severity Critical count
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: severity_emergency_or_alert_count
                                    
                                    	Fault Severity Emergency count
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: severity_error_count
                                    
                                    	Fault Severity Error count
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: total
                                    
                                    	Faulty Hardware total count
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'pfm-oper'
                                    _revision = '2017-03-28'

                                    def __init__(self):
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.FaultSummary, self).__init__()

                                        self.yang_name = "fault-summary"
                                        self.yang_parent_name = "slot"

                                        self.severity_critical_count = YLeaf(YType.int32, "severity-critical-count")

                                        self.severity_emergency_or_alert_count = YLeaf(YType.int32, "severity-emergency-or-alert-count")

                                        self.severity_error_count = YLeaf(YType.int32, "severity-error-count")

                                        self.total = YLeaf(YType.int32, "total")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("severity_critical_count",
                                                        "severity_emergency_or_alert_count",
                                                        "severity_error_count",
                                                        "total") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.FaultSummary, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.FaultSummary, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.severity_critical_count.is_set or
                                            self.severity_emergency_or_alert_count.is_set or
                                            self.severity_error_count.is_set or
                                            self.total.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.severity_critical_count.yfilter != YFilter.not_set or
                                            self.severity_emergency_or_alert_count.yfilter != YFilter.not_set or
                                            self.severity_error_count.yfilter != YFilter.not_set or
                                            self.total.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "fault-summary" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.severity_critical_count.is_set or self.severity_critical_count.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.severity_critical_count.get_name_leafdata())
                                        if (self.severity_emergency_or_alert_count.is_set or self.severity_emergency_or_alert_count.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.severity_emergency_or_alert_count.get_name_leafdata())
                                        if (self.severity_error_count.is_set or self.severity_error_count.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.severity_error_count.get_name_leafdata())
                                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.total.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "severity-critical-count" or name == "severity-emergency-or-alert-count" or name == "severity-error-count" or name == "total"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "severity-critical-count"):
                                            self.severity_critical_count = value
                                            self.severity_critical_count.value_namespace = name_space
                                            self.severity_critical_count.value_namespace_prefix = name_space_prefix
                                        if(value_path == "severity-emergency-or-alert-count"):
                                            self.severity_emergency_or_alert_count = value
                                            self.severity_emergency_or_alert_count.value_namespace = name_space
                                            self.severity_emergency_or_alert_count.value_namespace_prefix = name_space_prefix
                                        if(value_path == "severity-error-count"):
                                            self.severity_error_count = value
                                            self.severity_error_count.value_namespace = name_space
                                            self.severity_error_count.value_namespace_prefix = name_space_prefix
                                        if(value_path == "total"):
                                            self.total = value
                                            self.total.value_namespace = name_space
                                            self.total.value_namespace_prefix = name_space_prefix


                                class HardwareFaultDevices(Entity):
                                    """
                                    Table of Hardware Failure
                                    
                                    .. attribute:: hardware_fault_device
                                    
                                    	Table of Hardware Failure Device
                                    	**type**\: list of    :py:class:`HardwareFaultDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice>`
                                    
                                    

                                    """

                                    _prefix = 'pfm-oper'
                                    _revision = '2017-03-28'

                                    def __init__(self):
                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__init__()

                                        self.yang_name = "hardware-fault-devices"
                                        self.yang_parent_name = "slot"

                                        self.hardware_fault_device = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in () and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__setattr__(name, value)


                                    class HardwareFaultDevice(Entity):
                                        """
                                        Table of Hardware Failure Device
                                        
                                        .. attribute:: hw_fault_device  <key>
                                        
                                        	hw fault device list
                                        	**type**\:  str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        .. attribute:: hardware_fault_type
                                        
                                        	Table of Hardware Failure Type
                                        	**type**\: list of    :py:class:`HardwareFaultType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType>`
                                        
                                        

                                        """

                                        _prefix = 'pfm-oper'
                                        _revision = '2017-03-28'

                                        def __init__(self):
                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__init__()

                                            self.yang_name = "hardware-fault-device"
                                            self.yang_parent_name = "hardware-fault-devices"

                                            self.hw_fault_device = YLeaf(YType.str, "hw-fault-device")

                                            self.hardware_fault_type = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("hw_fault_device") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__setattr__(name, value)


                                        class HardwareFaultType(Entity):
                                            """
                                            Table of Hardware Failure Type
                                            
                                            .. attribute:: hw_fault_type  <key>
                                            
                                            	hw fault type list
                                            	**type**\:  str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: condition_description
                                            
                                            	Faulty Hardware Condition Description
                                            	**type**\:  str
                                            
                                            .. attribute:: condition_name
                                            
                                            	Faulty Hardware Condition Name
                                            	**type**\:  str
                                            
                                            .. attribute:: condition_raised_timestamp
                                            
                                            	Fault Raised Timestamp
                                            	**type**\:  str
                                            
                                            .. attribute:: condition_severity
                                            
                                            	Faulty Hardware Condition Severity
                                            	**type**\:  str
                                            
                                            .. attribute:: device_description
                                            
                                            	Faulty Hardware Device Description
                                            	**type**\:  str
                                            
                                            .. attribute:: device_key
                                            
                                            	Faulty Hardware Device Key
                                            	**type**\:  str
                                            
                                            .. attribute:: device_version
                                            
                                            	Faulty Hardware Device Version
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: process_id
                                            
                                            	Faulty Hardware Process ID
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'pfm-oper'
                                            _revision = '2017-03-28'

                                            def __init__(self):
                                                super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__init__()

                                                self.yang_name = "hardware-fault-type"
                                                self.yang_parent_name = "hardware-fault-device"

                                                self.hw_fault_type = YLeaf(YType.str, "hw-fault-type")

                                                self.condition_description = YLeaf(YType.str, "condition-description")

                                                self.condition_name = YLeaf(YType.str, "condition-name")

                                                self.condition_raised_timestamp = YLeaf(YType.str, "condition-raised-timestamp")

                                                self.condition_severity = YLeaf(YType.str, "condition-severity")

                                                self.device_description = YLeaf(YType.str, "device-description")

                                                self.device_key = YLeaf(YType.str, "device-key")

                                                self.device_version = YLeaf(YType.int32, "device-version")

                                                self.process_id = YLeaf(YType.int32, "process-id")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("hw_fault_type",
                                                                "condition_description",
                                                                "condition_name",
                                                                "condition_raised_timestamp",
                                                                "condition_severity",
                                                                "device_description",
                                                                "device_key",
                                                                "device_version",
                                                                "process_id") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.hw_fault_type.is_set or
                                                    self.condition_description.is_set or
                                                    self.condition_name.is_set or
                                                    self.condition_raised_timestamp.is_set or
                                                    self.condition_severity.is_set or
                                                    self.device_description.is_set or
                                                    self.device_key.is_set or
                                                    self.device_version.is_set or
                                                    self.process_id.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.hw_fault_type.yfilter != YFilter.not_set or
                                                    self.condition_description.yfilter != YFilter.not_set or
                                                    self.condition_name.yfilter != YFilter.not_set or
                                                    self.condition_raised_timestamp.yfilter != YFilter.not_set or
                                                    self.condition_severity.yfilter != YFilter.not_set or
                                                    self.device_description.yfilter != YFilter.not_set or
                                                    self.device_key.yfilter != YFilter.not_set or
                                                    self.device_version.yfilter != YFilter.not_set or
                                                    self.process_id.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "hardware-fault-type" + "[hw-fault-type='" + self.hw_fault_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.hw_fault_type.is_set or self.hw_fault_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.hw_fault_type.get_name_leafdata())
                                                if (self.condition_description.is_set or self.condition_description.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.condition_description.get_name_leafdata())
                                                if (self.condition_name.is_set or self.condition_name.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.condition_name.get_name_leafdata())
                                                if (self.condition_raised_timestamp.is_set or self.condition_raised_timestamp.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.condition_raised_timestamp.get_name_leafdata())
                                                if (self.condition_severity.is_set or self.condition_severity.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.condition_severity.get_name_leafdata())
                                                if (self.device_description.is_set or self.device_description.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.device_description.get_name_leafdata())
                                                if (self.device_key.is_set or self.device_key.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.device_key.get_name_leafdata())
                                                if (self.device_version.is_set or self.device_version.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.device_version.get_name_leafdata())
                                                if (self.process_id.is_set or self.process_id.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.process_id.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "hw-fault-type" or name == "condition-description" or name == "condition-name" or name == "condition-raised-timestamp" or name == "condition-severity" or name == "device-description" or name == "device-key" or name == "device-version" or name == "process-id"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "hw-fault-type"):
                                                    self.hw_fault_type = value
                                                    self.hw_fault_type.value_namespace = name_space
                                                    self.hw_fault_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "condition-description"):
                                                    self.condition_description = value
                                                    self.condition_description.value_namespace = name_space
                                                    self.condition_description.value_namespace_prefix = name_space_prefix
                                                if(value_path == "condition-name"):
                                                    self.condition_name = value
                                                    self.condition_name.value_namespace = name_space
                                                    self.condition_name.value_namespace_prefix = name_space_prefix
                                                if(value_path == "condition-raised-timestamp"):
                                                    self.condition_raised_timestamp = value
                                                    self.condition_raised_timestamp.value_namespace = name_space
                                                    self.condition_raised_timestamp.value_namespace_prefix = name_space_prefix
                                                if(value_path == "condition-severity"):
                                                    self.condition_severity = value
                                                    self.condition_severity.value_namespace = name_space
                                                    self.condition_severity.value_namespace_prefix = name_space_prefix
                                                if(value_path == "device-description"):
                                                    self.device_description = value
                                                    self.device_description.value_namespace = name_space
                                                    self.device_description.value_namespace_prefix = name_space_prefix
                                                if(value_path == "device-key"):
                                                    self.device_key = value
                                                    self.device_key.value_namespace = name_space
                                                    self.device_key.value_namespace_prefix = name_space_prefix
                                                if(value_path == "device-version"):
                                                    self.device_version = value
                                                    self.device_version.value_namespace = name_space
                                                    self.device_version.value_namespace_prefix = name_space_prefix
                                                if(value_path == "process-id"):
                                                    self.process_id = value
                                                    self.process_id.value_namespace = name_space
                                                    self.process_id.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.hardware_fault_type:
                                                if (c.has_data()):
                                                    return True
                                            return self.hw_fault_device.is_set

                                        def has_operation(self):
                                            for c in self.hardware_fault_type:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.hw_fault_device.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "hardware-fault-device" + "[hw-fault-device='" + self.hw_fault_device.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.hw_fault_device.is_set or self.hw_fault_device.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.hw_fault_device.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "hardware-fault-type"):
                                                for c in self.hardware_fault_type:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.hardware_fault_type.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "hardware-fault-type" or name == "hw-fault-device"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "hw-fault-device"):
                                                self.hw_fault_device = value
                                                self.hw_fault_device.value_namespace = name_space
                                                self.hw_fault_device.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.hardware_fault_device:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.hardware_fault_device:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "hardware-fault-devices" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "hardware-fault-device"):
                                            for c in self.hardware_fault_device:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.hardware_fault_device.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "hardware-fault-device"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.slot.is_set or
                                        (self.fault_summary is not None and self.fault_summary.has_data()) or
                                        (self.hardware_fault_devices is not None and self.hardware_fault_devices.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.slot.yfilter != YFilter.not_set or
                                        (self.fault_summary is not None and self.fault_summary.has_operation()) or
                                        (self.hardware_fault_devices is not None and self.hardware_fault_devices.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "slot" + "[slot='" + self.slot.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.slot.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "fault-summary"):
                                        if (self.fault_summary is None):
                                            self.fault_summary = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.FaultSummary()
                                            self.fault_summary.parent = self
                                            self._children_name_map["fault_summary"] = "fault-summary"
                                        return self.fault_summary

                                    if (child_yang_name == "hardware-fault-devices"):
                                        if (self.hardware_fault_devices is None):
                                            self.hardware_fault_devices = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                            self.hardware_fault_devices.parent = self
                                            self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                                        return self.hardware_fault_devices

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "fault-summary" or name == "hardware-fault-devices" or name == "slot"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "slot"):
                                        self.slot = value
                                        self.slot.value_namespace = name_space
                                        self.slot.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.slot:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.slot:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "slots" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "slot"):
                                    for c in self.slot:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots.Slot()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.slot.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "slot"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.rack.is_set or
                                (self.slots is not None and self.slots.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.rack.yfilter != YFilter.not_set or
                                (self.slots is not None and self.slots.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rack" + "[rack='" + self.rack.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.rack.is_set or self.rack.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rack.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "slots"):
                                if (self.slots is None):
                                    self.slots = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack.Slots()
                                    self.slots.parent = self
                                    self._children_name_map["slots"] = "slots"
                                return self.slots

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "slots" or name == "rack"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "rack"):
                                self.rack = value
                                self.rack.value_namespace = name_space
                                self.rack.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.rack:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.rack:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "racks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "rack"):
                            for c in self.rack:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks.Rack()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.rack.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "rack"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.hw_fault_type1.is_set or
                        (self.fault_type2s is not None and self.fault_type2s.has_data()) or
                        (self.racks is not None and self.racks.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.hw_fault_type1.yfilter != YFilter.not_set or
                        (self.fault_type2s is not None and self.fault_type2s.has_operation()) or
                        (self.racks is not None and self.racks.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "fault-type1" + "[hw-fault-type1='" + self.hw_fault_type1.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-pfm-oper:platform-fault-manager/exclude/fault-type1s/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.hw_fault_type1.is_set or self.hw_fault_type1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hw_fault_type1.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "fault-type2s"):
                        if (self.fault_type2s is None):
                            self.fault_type2s = PlatformFaultManager.Exclude.FaultType1S.FaultType1.FaultType2S()
                            self.fault_type2s.parent = self
                            self._children_name_map["fault_type2s"] = "fault-type2s"
                        return self.fault_type2s

                    if (child_yang_name == "racks"):
                        if (self.racks is None):
                            self.racks = PlatformFaultManager.Exclude.FaultType1S.FaultType1.Racks()
                            self.racks.parent = self
                            self._children_name_map["racks"] = "racks"
                        return self.racks

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fault-type2s" or name == "racks" or name == "hw-fault-type1"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "hw-fault-type1"):
                        self.hw_fault_type1 = value
                        self.hw_fault_type1.value_namespace = name_space
                        self.hw_fault_type1.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.fault_type1:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.fault_type1:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "fault-type1s" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-pfm-oper:platform-fault-manager/exclude/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "fault-type1"):
                    for c in self.fault_type1:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = PlatformFaultManager.Exclude.FaultType1S.FaultType1()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.fault_type1.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "fault-type1"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.fault_type1s is not None and self.fault_type1s.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.fault_type1s is not None and self.fault_type1s.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "exclude" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-pfm-oper:platform-fault-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "fault-type1s"):
                if (self.fault_type1s is None):
                    self.fault_type1s = PlatformFaultManager.Exclude.FaultType1S()
                    self.fault_type1s.parent = self
                    self._children_name_map["fault_type1s"] = "fault-type1s"
                return self.fault_type1s

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "fault-type1s"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Number
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack>`
        
        

        """

        _prefix = 'pfm-oper'
        _revision = '2017-03-28'

        def __init__(self):
            super(PlatformFaultManager.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "platform-fault-manager"

            self.rack = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PlatformFaultManager.Racks, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PlatformFaultManager.Racks, self).__setattr__(name, value)


        class Rack(Entity):
            """
            Number
            
            .. attribute:: rack  <key>
            
            	Rack number
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'pfm-oper'
            _revision = '2017-03-28'

            def __init__(self):
                super(PlatformFaultManager.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"

                self.rack = YLeaf(YType.int32, "rack")

                self.slots = PlatformFaultManager.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._children_yang_names.add("slots")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rack") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PlatformFaultManager.Racks.Rack, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PlatformFaultManager.Racks.Rack, self).__setattr__(name, value)


            class Slots(Entity):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Name
                	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'pfm-oper'
                _revision = '2017-03-28'

                def __init__(self):
                    super(PlatformFaultManager.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"

                    self.slot = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PlatformFaultManager.Racks.Rack.Slots, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformFaultManager.Racks.Rack.Slots, self).__setattr__(name, value)


                class Slot(Entity):
                    """
                    Name
                    
                    .. attribute:: slot  <key>
                    
                    	Slot name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: fault_summary
                    
                    	Table of Hardware Summary
                    	**type**\:   :py:class:`FaultSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary>`
                    
                    .. attribute:: hardware_fault_devices
                    
                    	Table of Hardware Failure
                    	**type**\:   :py:class:`HardwareFaultDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices>`
                    
                    

                    """

                    _prefix = 'pfm-oper'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(PlatformFaultManager.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"

                        self.slot = YLeaf(YType.str, "slot")

                        self.fault_summary = PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary()
                        self.fault_summary.parent = self
                        self._children_name_map["fault_summary"] = "fault-summary"
                        self._children_yang_names.add("fault-summary")

                        self.hardware_fault_devices = PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                        self.hardware_fault_devices.parent = self
                        self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                        self._children_yang_names.add("hardware-fault-devices")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("slot") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformFaultManager.Racks.Rack.Slots.Slot, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformFaultManager.Racks.Rack.Slots.Slot, self).__setattr__(name, value)


                    class FaultSummary(Entity):
                        """
                        Table of Hardware Summary
                        
                        .. attribute:: severity_critical_count
                        
                        	Fault Severity Critical count
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: severity_emergency_or_alert_count
                        
                        	Fault Severity Emergency count
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: severity_error_count
                        
                        	Fault Severity Error count
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: total
                        
                        	Faulty Hardware total count
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'pfm-oper'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary, self).__init__()

                            self.yang_name = "fault-summary"
                            self.yang_parent_name = "slot"

                            self.severity_critical_count = YLeaf(YType.int32, "severity-critical-count")

                            self.severity_emergency_or_alert_count = YLeaf(YType.int32, "severity-emergency-or-alert-count")

                            self.severity_error_count = YLeaf(YType.int32, "severity-error-count")

                            self.total = YLeaf(YType.int32, "total")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("severity_critical_count",
                                            "severity_emergency_or_alert_count",
                                            "severity_error_count",
                                            "total") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.severity_critical_count.is_set or
                                self.severity_emergency_or_alert_count.is_set or
                                self.severity_error_count.is_set or
                                self.total.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.severity_critical_count.yfilter != YFilter.not_set or
                                self.severity_emergency_or_alert_count.yfilter != YFilter.not_set or
                                self.severity_error_count.yfilter != YFilter.not_set or
                                self.total.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "fault-summary" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.severity_critical_count.is_set or self.severity_critical_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.severity_critical_count.get_name_leafdata())
                            if (self.severity_emergency_or_alert_count.is_set or self.severity_emergency_or_alert_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.severity_emergency_or_alert_count.get_name_leafdata())
                            if (self.severity_error_count.is_set or self.severity_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.severity_error_count.get_name_leafdata())
                            if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "severity-critical-count" or name == "severity-emergency-or-alert-count" or name == "severity-error-count" or name == "total"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "severity-critical-count"):
                                self.severity_critical_count = value
                                self.severity_critical_count.value_namespace = name_space
                                self.severity_critical_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "severity-emergency-or-alert-count"):
                                self.severity_emergency_or_alert_count = value
                                self.severity_emergency_or_alert_count.value_namespace = name_space
                                self.severity_emergency_or_alert_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "severity-error-count"):
                                self.severity_error_count = value
                                self.severity_error_count.value_namespace = name_space
                                self.severity_error_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total"):
                                self.total = value
                                self.total.value_namespace = name_space
                                self.total.value_namespace_prefix = name_space_prefix


                    class HardwareFaultDevices(Entity):
                        """
                        Table of Hardware Failure
                        
                        .. attribute:: hardware_fault_device
                        
                        	Table of Hardware Failure Device
                        	**type**\: list of    :py:class:`HardwareFaultDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice>`
                        
                        

                        """

                        _prefix = 'pfm-oper'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__init__()

                            self.yang_name = "hardware-fault-devices"
                            self.yang_parent_name = "slot"

                            self.hardware_fault_device = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices, self).__setattr__(name, value)


                        class HardwareFaultDevice(Entity):
                            """
                            Table of Hardware Failure Device
                            
                            .. attribute:: hw_fault_device  <key>
                            
                            	hw fault device list
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: hardware_fault_type
                            
                            	Table of Hardware Failure Type
                            	**type**\: list of    :py:class:`HardwareFaultType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfm_oper.PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType>`
                            
                            

                            """

                            _prefix = 'pfm-oper'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__init__()

                                self.yang_name = "hardware-fault-device"
                                self.yang_parent_name = "hardware-fault-devices"

                                self.hw_fault_device = YLeaf(YType.str, "hw-fault-device")

                                self.hardware_fault_type = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("hw_fault_device") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice, self).__setattr__(name, value)


                            class HardwareFaultType(Entity):
                                """
                                Table of Hardware Failure Type
                                
                                .. attribute:: hw_fault_type  <key>
                                
                                	hw fault type list
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: condition_description
                                
                                	Faulty Hardware Condition Description
                                	**type**\:  str
                                
                                .. attribute:: condition_name
                                
                                	Faulty Hardware Condition Name
                                	**type**\:  str
                                
                                .. attribute:: condition_raised_timestamp
                                
                                	Fault Raised Timestamp
                                	**type**\:  str
                                
                                .. attribute:: condition_severity
                                
                                	Faulty Hardware Condition Severity
                                	**type**\:  str
                                
                                .. attribute:: device_description
                                
                                	Faulty Hardware Device Description
                                	**type**\:  str
                                
                                .. attribute:: device_key
                                
                                	Faulty Hardware Device Key
                                	**type**\:  str
                                
                                .. attribute:: device_version
                                
                                	Faulty Hardware Device Version
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: process_id
                                
                                	Faulty Hardware Process ID
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                

                                """

                                _prefix = 'pfm-oper'
                                _revision = '2017-03-28'

                                def __init__(self):
                                    super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__init__()

                                    self.yang_name = "hardware-fault-type"
                                    self.yang_parent_name = "hardware-fault-device"

                                    self.hw_fault_type = YLeaf(YType.str, "hw-fault-type")

                                    self.condition_description = YLeaf(YType.str, "condition-description")

                                    self.condition_name = YLeaf(YType.str, "condition-name")

                                    self.condition_raised_timestamp = YLeaf(YType.str, "condition-raised-timestamp")

                                    self.condition_severity = YLeaf(YType.str, "condition-severity")

                                    self.device_description = YLeaf(YType.str, "device-description")

                                    self.device_key = YLeaf(YType.str, "device-key")

                                    self.device_version = YLeaf(YType.int32, "device-version")

                                    self.process_id = YLeaf(YType.int32, "process-id")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("hw_fault_type",
                                                    "condition_description",
                                                    "condition_name",
                                                    "condition_raised_timestamp",
                                                    "condition_severity",
                                                    "device_description",
                                                    "device_key",
                                                    "device_version",
                                                    "process_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.hw_fault_type.is_set or
                                        self.condition_description.is_set or
                                        self.condition_name.is_set or
                                        self.condition_raised_timestamp.is_set or
                                        self.condition_severity.is_set or
                                        self.device_description.is_set or
                                        self.device_key.is_set or
                                        self.device_version.is_set or
                                        self.process_id.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.hw_fault_type.yfilter != YFilter.not_set or
                                        self.condition_description.yfilter != YFilter.not_set or
                                        self.condition_name.yfilter != YFilter.not_set or
                                        self.condition_raised_timestamp.yfilter != YFilter.not_set or
                                        self.condition_severity.yfilter != YFilter.not_set or
                                        self.device_description.yfilter != YFilter.not_set or
                                        self.device_key.yfilter != YFilter.not_set or
                                        self.device_version.yfilter != YFilter.not_set or
                                        self.process_id.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "hardware-fault-type" + "[hw-fault-type='" + self.hw_fault_type.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.hw_fault_type.is_set or self.hw_fault_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hw_fault_type.get_name_leafdata())
                                    if (self.condition_description.is_set or self.condition_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.condition_description.get_name_leafdata())
                                    if (self.condition_name.is_set or self.condition_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.condition_name.get_name_leafdata())
                                    if (self.condition_raised_timestamp.is_set or self.condition_raised_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.condition_raised_timestamp.get_name_leafdata())
                                    if (self.condition_severity.is_set or self.condition_severity.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.condition_severity.get_name_leafdata())
                                    if (self.device_description.is_set or self.device_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.device_description.get_name_leafdata())
                                    if (self.device_key.is_set or self.device_key.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.device_key.get_name_leafdata())
                                    if (self.device_version.is_set or self.device_version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.device_version.get_name_leafdata())
                                    if (self.process_id.is_set or self.process_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.process_id.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "hw-fault-type" or name == "condition-description" or name == "condition-name" or name == "condition-raised-timestamp" or name == "condition-severity" or name == "device-description" or name == "device-key" or name == "device-version" or name == "process-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "hw-fault-type"):
                                        self.hw_fault_type = value
                                        self.hw_fault_type.value_namespace = name_space
                                        self.hw_fault_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "condition-description"):
                                        self.condition_description = value
                                        self.condition_description.value_namespace = name_space
                                        self.condition_description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "condition-name"):
                                        self.condition_name = value
                                        self.condition_name.value_namespace = name_space
                                        self.condition_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "condition-raised-timestamp"):
                                        self.condition_raised_timestamp = value
                                        self.condition_raised_timestamp.value_namespace = name_space
                                        self.condition_raised_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "condition-severity"):
                                        self.condition_severity = value
                                        self.condition_severity.value_namespace = name_space
                                        self.condition_severity.value_namespace_prefix = name_space_prefix
                                    if(value_path == "device-description"):
                                        self.device_description = value
                                        self.device_description.value_namespace = name_space
                                        self.device_description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "device-key"):
                                        self.device_key = value
                                        self.device_key.value_namespace = name_space
                                        self.device_key.value_namespace_prefix = name_space_prefix
                                    if(value_path == "device-version"):
                                        self.device_version = value
                                        self.device_version.value_namespace = name_space
                                        self.device_version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "process-id"):
                                        self.process_id = value
                                        self.process_id.value_namespace = name_space
                                        self.process_id.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.hardware_fault_type:
                                    if (c.has_data()):
                                        return True
                                return self.hw_fault_device.is_set

                            def has_operation(self):
                                for c in self.hardware_fault_type:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.hw_fault_device.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "hardware-fault-device" + "[hw-fault-device='" + self.hw_fault_device.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.hw_fault_device.is_set or self.hw_fault_device.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hw_fault_device.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "hardware-fault-type"):
                                    for c in self.hardware_fault_type:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice.HardwareFaultType()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.hardware_fault_type.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "hardware-fault-type" or name == "hw-fault-device"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "hw-fault-device"):
                                    self.hw_fault_device = value
                                    self.hw_fault_device.value_namespace = name_space
                                    self.hw_fault_device.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.hardware_fault_device:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.hardware_fault_device:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "hardware-fault-devices" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "hardware-fault-device"):
                                for c in self.hardware_fault_device:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices.HardwareFaultDevice()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.hardware_fault_device.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "hardware-fault-device"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.slot.is_set or
                            (self.fault_summary is not None and self.fault_summary.has_data()) or
                            (self.hardware_fault_devices is not None and self.hardware_fault_devices.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.slot.yfilter != YFilter.not_set or
                            (self.fault_summary is not None and self.fault_summary.has_operation()) or
                            (self.hardware_fault_devices is not None and self.hardware_fault_devices.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slot" + "[slot='" + self.slot.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slot.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "fault-summary"):
                            if (self.fault_summary is None):
                                self.fault_summary = PlatformFaultManager.Racks.Rack.Slots.Slot.FaultSummary()
                                self.fault_summary.parent = self
                                self._children_name_map["fault_summary"] = "fault-summary"
                            return self.fault_summary

                        if (child_yang_name == "hardware-fault-devices"):
                            if (self.hardware_fault_devices is None):
                                self.hardware_fault_devices = PlatformFaultManager.Racks.Rack.Slots.Slot.HardwareFaultDevices()
                                self.hardware_fault_devices.parent = self
                                self._children_name_map["hardware_fault_devices"] = "hardware-fault-devices"
                            return self.hardware_fault_devices

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "fault-summary" or name == "hardware-fault-devices" or name == "slot"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "slot"):
                            self.slot = value
                            self.slot.value_namespace = name_space
                            self.slot.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.slot:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.slot:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "slots" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "slot"):
                        for c in self.slot:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PlatformFaultManager.Racks.Rack.Slots.Slot()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.slot.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slot"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.rack.is_set or
                    (self.slots is not None and self.slots.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rack.yfilter != YFilter.not_set or
                    (self.slots is not None and self.slots.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rack" + "[rack='" + self.rack.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-pfm-oper:platform-fault-manager/racks/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rack.is_set or self.rack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rack.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "slots"):
                    if (self.slots is None):
                        self.slots = PlatformFaultManager.Racks.Rack.Slots()
                        self.slots.parent = self
                        self._children_name_map["slots"] = "slots"
                    return self.slots

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "slots" or name == "rack"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rack"):
                    self.rack = value
                    self.rack.value_namespace = name_space
                    self.rack.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rack:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rack:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "racks" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-pfm-oper:platform-fault-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rack"):
                for c in self.rack:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PlatformFaultManager.Racks.Rack()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rack.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rack"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.exclude is not None and self.exclude.has_data()) or
            (self.racks is not None and self.racks.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.exclude is not None and self.exclude.has_operation()) or
            (self.racks is not None and self.racks.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-pfm-oper:platform-fault-manager" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "exclude"):
            if (self.exclude is None):
                self.exclude = PlatformFaultManager.Exclude()
                self.exclude.parent = self
                self._children_name_map["exclude"] = "exclude"
            return self.exclude

        if (child_yang_name == "racks"):
            if (self.racks is None):
                self.racks = PlatformFaultManager.Racks()
                self.racks.parent = self
                self._children_name_map["racks"] = "racks"
            return self.racks

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "exclude" or name == "racks"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PlatformFaultManager()
        return self._top_entity

