""" CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN 

This MIB Module is a supplement to the
CISCO\-IETF\-ATM2\-PVCTRAP\-MIB.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIETFATM2PVCTRAPMIBEXTN(Entity):
    """
    
    
    .. attribute:: atmcurrentstatuschangepvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last PVC notification interval
    	**type**\:  :py:class:`Atmcurrentstatuschangepvcltable <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable>`
    
    .. attribute:: atmstatuschangepvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the same direction in the last PVC notification interval
    	**type**\:  :py:class:`Atmstatuschangepvclrangetable <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable>`
    
    

    """

    _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
    _revision = '2000-07-11'

    def __init__(self):
        super(CISCOIETFATM2PVCTRAPMIBEXTN, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"
        self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("atmCurrentStatusChangePVclTable", ("atmcurrentstatuschangepvcltable", CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable)), ("atmStatusChangePVclRangeTable", ("atmstatuschangepvclrangetable", CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.atmcurrentstatuschangepvcltable = CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable()
        self.atmcurrentstatuschangepvcltable.parent = self
        self._children_name_map["atmcurrentstatuschangepvcltable"] = "atmCurrentStatusChangePVclTable"
        self._children_yang_names.add("atmCurrentStatusChangePVclTable")

        self.atmstatuschangepvclrangetable = CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable()
        self.atmstatuschangepvclrangetable.parent = self
        self._children_name_map["atmstatuschangepvclrangetable"] = "atmStatusChangePVclRangeTable"
        self._children_yang_names.add("atmStatusChangePVclRangeTable")
        self._segment_path = lambda: "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"


    class Atmcurrentstatuschangepvcltable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed in the
        last PVC notification interval.
        
        .. attribute:: atmcurrentstatuschangepvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last PVC notification interval
        	**type**\: list of  		 :py:class:`Atmcurrentstatuschangepvclentry <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry>`
        
        

        """

        _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
        _revision = '2000-07-11'

        def __init__(self):
            super(CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable, self).__init__()

            self.yang_name = "atmCurrentStatusChangePVclTable"
            self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("atmCurrentStatusChangePVclEntry", ("atmcurrentstatuschangepvclentry", CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry))])
            self._leafs = OrderedDict()

            self.atmcurrentstatuschangepvclentry = YList(self)
            self._segment_path = lambda: "atmCurrentStatusChangePVclTable"
            self._absolute_path = lambda: "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable, [], name, value)


        class Atmcurrentstatuschangepvclentry(Entity):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed in the last PVC notification interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmpvclstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
            _revision = '2000-07-11'

            def __init__(self):
                super(CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry, self).__init__()

                self.yang_name = "atmCurrentStatusChangePVclEntry"
                self.yang_parent_name = "atmCurrentStatusChangePVclTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','atmvclvci']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('atmvclvpi', YLeaf(YType.str, 'atmVclVpi')),
                    ('atmvclvci', YLeaf(YType.str, 'atmVclVci')),
                    ('atmpvclstatustransition', YLeaf(YType.uint32, 'atmPVclStatusTransition')),
                    ('atmpvclstatuschangestart', YLeaf(YType.uint32, 'atmPVclStatusChangeStart')),
                    ('atmpvclstatuschangeend', YLeaf(YType.uint32, 'atmPVclStatusChangeEnd')),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.atmpvclstatustransition = None
                self.atmpvclstatuschangestart = None
                self.atmpvclstatuschangeend = None
                self._segment_path = lambda: "atmCurrentStatusChangePVclEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[atmVclVci='" + str(self.atmvclvci) + "']"
                self._absolute_path = lambda: "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/atmCurrentStatusChangePVclTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFATM2PVCTRAPMIBEXTN.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'atmpvclstatustransition', 'atmpvclstatuschangestart', 'atmpvclstatuschangeend'], name, value)


    class Atmstatuschangepvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed in the same
        direction in the last PVC notification interval.
        
        .. attribute:: atmstatuschangepvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed in the same direction in the last notification  interval
        	**type**\: list of  		 :py:class:`Atmstatuschangepvclrangeentry <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
        _revision = '2000-07-11'

        def __init__(self):
            super(CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable, self).__init__()

            self.yang_name = "atmStatusChangePVclRangeTable"
            self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("atmStatusChangePVclRangeEntry", ("atmstatuschangepvclrangeentry", CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry))])
            self._leafs = OrderedDict()

            self.atmstatuschangepvclrangeentry = YList(self)
            self._segment_path = lambda: "atmStatusChangePVclRangeTable"
            self._absolute_path = lambda: "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable, [], name, value)


        class Atmstatuschangepvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed in the same direction in the last notification 
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: rangeindex  (key)
            
            	Index to represent different ranges, the first range is  indexed by value 0, the second by 1 and so on..
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvcllowerrangevalue
            
            	The first PVCL in a range of PVcls for which the  atmVclOperStatus to have changed in the last  notification interval
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: atmpvclhigherrangevalue
            
            	The last PVCL in a range of PVcls for which the  atmOperStatus to have changed in the last  notification interval
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: atmpvclrangestatuschangestart
            
            	The time stamp at which the first PVCL in the range changed state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclrangestatuschangeend
            
            	The time stamp at which the last PVCL in the range changed state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'
            _revision = '2000-07-11'

            def __init__(self):
                super(CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry, self).__init__()

                self.yang_name = "atmStatusChangePVclRangeEntry"
                self.yang_parent_name = "atmStatusChangePVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','rangeindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('atmvclvpi', YLeaf(YType.str, 'atmVclVpi')),
                    ('rangeindex', YLeaf(YType.uint32, 'rangeIndex')),
                    ('atmpvcllowerrangevalue', YLeaf(YType.int32, 'atmPVclLowerRangeValue')),
                    ('atmpvclhigherrangevalue', YLeaf(YType.int32, 'atmPVclHigherRangeValue')),
                    ('atmpvclrangestatuschangestart', YLeaf(YType.uint32, 'atmPVclRangeStatusChangeStart')),
                    ('atmpvclrangestatuschangeend', YLeaf(YType.uint32, 'atmPVclRangeStatusChangeEnd')),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.rangeindex = None
                self.atmpvcllowerrangevalue = None
                self.atmpvclhigherrangevalue = None
                self.atmpvclrangestatuschangestart = None
                self.atmpvclrangestatuschangeend = None
                self._segment_path = lambda: "atmStatusChangePVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[rangeIndex='" + str(self.rangeindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/atmStatusChangePVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFATM2PVCTRAPMIBEXTN.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry, ['ifindex', 'atmvclvpi', 'rangeindex', 'atmpvcllowerrangevalue', 'atmpvclhigherrangevalue', 'atmpvclrangestatuschangestart', 'atmpvclrangestatuschangeend'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIETFATM2PVCTRAPMIBEXTN()
        return self._top_entity

