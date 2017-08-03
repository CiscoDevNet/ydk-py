""" CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN 

This MIB Module is a supplement to the
CISCO\-IETF\-ATM2\-PVCTRAP\-MIB.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfAtm2PvctrapMibExtn(Entity):
    """
    
    
    .. attribute:: atmcurrentstatuschangepvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last PVC notification interval
    	**type**\:   :py:class:`Atmcurrentstatuschangepvcltable <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable>`
    
    .. attribute:: atmstatuschangepvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the same direction in the last PVC notification interval
    	**type**\:   :py:class:`Atmstatuschangepvclrangetable <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable>`
    
    

    """

    _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
    _revision = '2000-07-11'

    def __init__(self):
        super(CiscoIetfAtm2PvctrapMibExtn, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"
        self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"

        self.atmcurrentstatuschangepvcltable = CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable()
        self.atmcurrentstatuschangepvcltable.parent = self
        self._children_name_map["atmcurrentstatuschangepvcltable"] = "atmCurrentStatusChangePVclTable"
        self._children_yang_names.add("atmCurrentStatusChangePVclTable")

        self.atmstatuschangepvclrangetable = CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable()
        self.atmstatuschangepvclrangetable.parent = self
        self._children_name_map["atmstatuschangepvclrangetable"] = "atmStatusChangePVclRangeTable"
        self._children_yang_names.add("atmStatusChangePVclRangeTable")


    class Atmcurrentstatuschangepvcltable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed in the
        last PVC notification interval.
        
        .. attribute:: atmcurrentstatuschangepvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last PVC notification interval
        	**type**\: list of    :py:class:`Atmcurrentstatuschangepvclentry <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry>`
        
        

        """

        _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
        _revision = '2000-07-11'

        def __init__(self):
            super(CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable, self).__init__()

            self.yang_name = "atmCurrentStatusChangePVclTable"
            self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"

            self.atmcurrentstatuschangepvclentry = YList(self)

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
                        super(CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable, self).__setattr__(name, value)


        class Atmcurrentstatuschangepvclentry(Entity):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed in the last PVC notification interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmpvclstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
            _revision = '2000-07-11'

            def __init__(self):
                super(CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry, self).__init__()

                self.yang_name = "atmCurrentStatusChangePVclEntry"
                self.yang_parent_name = "atmCurrentStatusChangePVclTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.atmpvclstatuschangeend = YLeaf(YType.uint32, "atmPVclStatusChangeEnd")

                self.atmpvclstatuschangestart = YLeaf(YType.uint32, "atmPVclStatusChangeStart")

                self.atmpvclstatustransition = YLeaf(YType.uint32, "atmPVclStatusTransition")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "atmvclvpi",
                                "atmvclvci",
                                "atmpvclstatuschangeend",
                                "atmpvclstatuschangestart",
                                "atmpvclstatustransition") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.atmvclvci.is_set or
                    self.atmpvclstatuschangeend.is_set or
                    self.atmpvclstatuschangestart.is_set or
                    self.atmpvclstatustransition.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.atmvclvci.yfilter != YFilter.not_set or
                    self.atmpvclstatuschangeend.yfilter != YFilter.not_set or
                    self.atmpvclstatuschangestart.yfilter != YFilter.not_set or
                    self.atmpvclstatustransition.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmCurrentStatusChangePVclEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/atmCurrentStatusChangePVclTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.atmvclvci.is_set or self.atmvclvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvci.get_name_leafdata())
                if (self.atmpvclstatuschangeend.is_set or self.atmpvclstatuschangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpvclstatuschangeend.get_name_leafdata())
                if (self.atmpvclstatuschangestart.is_set or self.atmpvclstatuschangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpvclstatuschangestart.get_name_leafdata())
                if (self.atmpvclstatustransition.is_set or self.atmpvclstatustransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpvclstatustransition.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "atmVclVci" or name == "atmPVclStatusChangeEnd" or name == "atmPVclStatusChangeStart" or name == "atmPVclStatusTransition"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclVpi"):
                    self.atmvclvpi = value
                    self.atmvclvpi.value_namespace = name_space
                    self.atmvclvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclVci"):
                    self.atmvclvci = value
                    self.atmvclvci.value_namespace = name_space
                    self.atmvclvci.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPVclStatusChangeEnd"):
                    self.atmpvclstatuschangeend = value
                    self.atmpvclstatuschangeend.value_namespace = name_space
                    self.atmpvclstatuschangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPVclStatusChangeStart"):
                    self.atmpvclstatuschangestart = value
                    self.atmpvclstatuschangestart.value_namespace = name_space
                    self.atmpvclstatuschangestart.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPVclStatusTransition"):
                    self.atmpvclstatustransition = value
                    self.atmpvclstatustransition.value_namespace = name_space
                    self.atmpvclstatustransition.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atmcurrentstatuschangepvclentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atmcurrentstatuschangepvclentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmCurrentStatusChangePVclTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmCurrentStatusChangePVclEntry"):
                for c in self.atmcurrentstatuschangepvclentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atmcurrentstatuschangepvclentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmCurrentStatusChangePVclEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Atmstatuschangepvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed in the same
        direction in the last PVC notification interval.
        
        .. attribute:: atmstatuschangepvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed in the same direction in the last notification  interval
        	**type**\: list of    :py:class:`Atmstatuschangepvclrangeentry <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
        _revision = '2000-07-11'

        def __init__(self):
            super(CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable, self).__init__()

            self.yang_name = "atmStatusChangePVclRangeTable"
            self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"

            self.atmstatuschangepvclrangeentry = YList(self)

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
                        super(CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable, self).__setattr__(name, value)


        class Atmstatuschangepvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed in the same direction in the last notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: rangeindex  <key>
            
            	Index to represent different ranges, the first range is  indexed by value 0, the second by 1 and so on..
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclhigherrangevalue
            
            	The last PVCL in a range of PVcls for which the  atmOperStatus to have changed in the last  notification interval
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: atmpvcllowerrangevalue
            
            	The first PVCL in a range of PVcls for which the  atmVclOperStatus to have changed in the last  notification interval
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: atmpvclrangestatuschangeend
            
            	The time stamp at which the last PVCL in the range changed state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclrangestatuschangestart
            
            	The time stamp at which the first PVCL in the range changed state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
            _revision = '2000-07-11'

            def __init__(self):
                super(CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry, self).__init__()

                self.yang_name = "atmStatusChangePVclRangeEntry"
                self.yang_parent_name = "atmStatusChangePVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.rangeindex = YLeaf(YType.uint32, "rangeIndex")

                self.atmpvclhigherrangevalue = YLeaf(YType.int32, "atmPVclHigherRangeValue")

                self.atmpvcllowerrangevalue = YLeaf(YType.int32, "atmPVclLowerRangeValue")

                self.atmpvclrangestatuschangeend = YLeaf(YType.uint32, "atmPVclRangeStatusChangeEnd")

                self.atmpvclrangestatuschangestart = YLeaf(YType.uint32, "atmPVclRangeStatusChangeStart")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "atmvclvpi",
                                "rangeindex",
                                "atmpvclhigherrangevalue",
                                "atmpvcllowerrangevalue",
                                "atmpvclrangestatuschangeend",
                                "atmpvclrangestatuschangestart") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.rangeindex.is_set or
                    self.atmpvclhigherrangevalue.is_set or
                    self.atmpvcllowerrangevalue.is_set or
                    self.atmpvclrangestatuschangeend.is_set or
                    self.atmpvclrangestatuschangestart.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.rangeindex.yfilter != YFilter.not_set or
                    self.atmpvclhigherrangevalue.yfilter != YFilter.not_set or
                    self.atmpvcllowerrangevalue.yfilter != YFilter.not_set or
                    self.atmpvclrangestatuschangeend.yfilter != YFilter.not_set or
                    self.atmpvclrangestatuschangestart.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmStatusChangePVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[rangeIndex='" + self.rangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/atmStatusChangePVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.rangeindex.is_set or self.rangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rangeindex.get_name_leafdata())
                if (self.atmpvclhigherrangevalue.is_set or self.atmpvclhigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpvclhigherrangevalue.get_name_leafdata())
                if (self.atmpvcllowerrangevalue.is_set or self.atmpvcllowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpvcllowerrangevalue.get_name_leafdata())
                if (self.atmpvclrangestatuschangeend.is_set or self.atmpvclrangestatuschangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpvclrangestatuschangeend.get_name_leafdata())
                if (self.atmpvclrangestatuschangestart.is_set or self.atmpvclrangestatuschangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpvclrangestatuschangestart.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "rangeIndex" or name == "atmPVclHigherRangeValue" or name == "atmPVclLowerRangeValue" or name == "atmPVclRangeStatusChangeEnd" or name == "atmPVclRangeStatusChangeStart"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclVpi"):
                    self.atmvclvpi = value
                    self.atmvclvpi.value_namespace = name_space
                    self.atmvclvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "rangeIndex"):
                    self.rangeindex = value
                    self.rangeindex.value_namespace = name_space
                    self.rangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPVclHigherRangeValue"):
                    self.atmpvclhigherrangevalue = value
                    self.atmpvclhigherrangevalue.value_namespace = name_space
                    self.atmpvclhigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPVclLowerRangeValue"):
                    self.atmpvcllowerrangevalue = value
                    self.atmpvcllowerrangevalue.value_namespace = name_space
                    self.atmpvcllowerrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPVclRangeStatusChangeEnd"):
                    self.atmpvclrangestatuschangeend = value
                    self.atmpvclrangestatuschangeend.value_namespace = name_space
                    self.atmpvclrangestatuschangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPVclRangeStatusChangeStart"):
                    self.atmpvclrangestatuschangestart = value
                    self.atmpvclrangestatuschangestart.value_namespace = name_space
                    self.atmpvclrangestatuschangestart.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atmstatuschangepvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atmstatuschangepvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmStatusChangePVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmStatusChangePVclRangeEntry"):
                for c in self.atmstatuschangepvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atmstatuschangepvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmStatusChangePVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.atmcurrentstatuschangepvcltable is not None and self.atmcurrentstatuschangepvcltable.has_data()) or
            (self.atmstatuschangepvclrangetable is not None and self.atmstatuschangepvclrangetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.atmcurrentstatuschangepvcltable is not None and self.atmcurrentstatuschangepvcltable.has_operation()) or
            (self.atmstatuschangepvclrangetable is not None and self.atmstatuschangepvclrangetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN" + path_buffer

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

        if (child_yang_name == "atmCurrentStatusChangePVclTable"):
            if (self.atmcurrentstatuschangepvcltable is None):
                self.atmcurrentstatuschangepvcltable = CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable()
                self.atmcurrentstatuschangepvcltable.parent = self
                self._children_name_map["atmcurrentstatuschangepvcltable"] = "atmCurrentStatusChangePVclTable"
            return self.atmcurrentstatuschangepvcltable

        if (child_yang_name == "atmStatusChangePVclRangeTable"):
            if (self.atmstatuschangepvclrangetable is None):
                self.atmstatuschangepvclrangetable = CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable()
                self.atmstatuschangepvclrangetable.parent = self
                self._children_name_map["atmstatuschangepvclrangetable"] = "atmStatusChangePVclRangeTable"
            return self.atmstatuschangepvclrangetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "atmCurrentStatusChangePVclTable" or name == "atmStatusChangePVclRangeTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfAtm2PvctrapMibExtn()
        return self._top_entity

