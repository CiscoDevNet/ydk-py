""" CISCO_ATM_PVCTRAP_EXTN_MIB 

This MIB Module is a supplement to the
CISCO\-IETF\-ATM2\-PVCTRAP\-MIB.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CatmOAMFailureType(Enum):
    """
    CatmOAMFailureType (Enum Class)

    Enums to indicate different types of OAM recoveries .

    catmLoopbackOAMFailure  \- The object in query is Loopback OAM

                              type of failure.

    catmSegmentCCOAMFailure \- The object in query is Segment CC

                              OAM type of failure.

    catmEndCCOAMFailure     \- The object in query is End\-to\-End 

                              CC OAM type of failure.

    catmAISRDIOAMFailure    \- The object in query is AISRDI OAM

                              type of failure.

    .. data:: catmLoopbackOAMFailure = 1

    .. data:: catmSegmentCCOAMFailure = 2

    .. data:: catmEndCCOAMFailure = 4

    .. data:: catmAISRDIOAMFailure = 8

    """

    catmLoopbackOAMFailure = Enum.YLeaf(1, "catmLoopbackOAMFailure")

    catmSegmentCCOAMFailure = Enum.YLeaf(2, "catmSegmentCCOAMFailure")

    catmEndCCOAMFailure = Enum.YLeaf(4, "catmEndCCOAMFailure")

    catmAISRDIOAMFailure = Enum.YLeaf(8, "catmAISRDIOAMFailure")


class CatmOAMRecoveryType(Enum):
    """
    CatmOAMRecoveryType (Enum Class)

    Enums to indicate different types of OAM recoveries .

    catmLoopbackOAMRecover  \- The object in query is Loopback OAM

                              type of recovery.

    catmSegmentCCOAMRecover \- The object in query is Segment CC

                              OAM type of recovery.

    catmEndCCOAMRecover     \- The object in query is End\-to\-End 

                              CC OAM type of recovery.

    catmAISRDIOAMRecover    \- The object in query is AISRDI OAM

                              type of recovery.

    .. data:: catmLoopbackOAMRecover = 1

    .. data:: catmSegmentCCOAMRecover = 2

    .. data:: catmEndCCOAMRecover = 4

    .. data:: catmAISRDIOAMRecover = 8

    """

    catmLoopbackOAMRecover = Enum.YLeaf(1, "catmLoopbackOAMRecover")

    catmSegmentCCOAMRecover = Enum.YLeaf(2, "catmSegmentCCOAMRecover")

    catmEndCCOAMRecover = Enum.YLeaf(4, "catmEndCCOAMRecover")

    catmAISRDIOAMRecover = Enum.YLeaf(8, "catmAISRDIOAMRecover")



class CISCOATMPVCTRAPEXTNMIB(Entity):
    """
    
    
    .. attribute:: catmcurstatchangepvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last corresponding PVC notification
    	**type**\:  :py:class:`CatmCurStatChangePVclTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable>`
    
    .. attribute:: catmstatuschangepvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the same direction in the last corresponding PVC notification 
    	**type**\:  :py:class:`CatmStatusChangePVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable>`
    
    .. attribute:: catmsegccstatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to segment CC  failure in the same direction in the last PVC  corresponding notification 
    	**type**\:  :py:class:`CatmSegCCStatusChPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable>`
    
    .. attribute:: catmendccstatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to End CC failure in the same direction in the last PVC notification  interval
    	**type**\:  :py:class:`CatmEndCCStatusChPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable>`
    
    .. attribute:: catmaisrdistatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to AIS/RDI failure in the same direction in the last corresponding PVC  notification
    	**type**\:  :py:class:`CatmAISRDIStatusChPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable>`
    
    .. attribute:: catmdownpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have detected as Down in the last corresponding PVC notification 
    	**type**\:  :py:class:`CatmDownPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable>`
    
    .. attribute:: catmcurstatusuppvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed to UP in the last corresponding PVC notification 
    	**type**\:  :py:class:`CatmCurStatusUpPVclTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable>`
    
    .. attribute:: catmstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and loopback OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:  :py:class:`CatmStatusUpPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable>`
    
    .. attribute:: catmsegccstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and Segment CC OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:  :py:class:`CatmSegCCStatusUpPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable>`
    
    .. attribute:: catmendccstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and End\-to\-End CC OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:  :py:class:`CatmEndCCStatusUpPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable>`
    
    .. attribute:: catmaisrdistatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and AISRDI OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:  :py:class:`CatmAISRDIStatusUpPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable>`
    
    .. attribute:: catmuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have detected as Up in the last corresponding PVC notification 
    	**type**\:  :py:class:`CatmUpPVclRangeTable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable>`
    
    

    """

    _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
    _revision = '2003-01-20'

    def __init__(self):
        super(CISCOATMPVCTRAPEXTNMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
        self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("catmCurStatChangePVclTable", ("catmcurstatchangepvcltable", CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable)), ("catmStatusChangePVclRangeTable", ("catmstatuschangepvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable)), ("catmSegCCStatusChPVclRangeTable", ("catmsegccstatuschpvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable)), ("catmEndCCStatusChPVclRangeTable", ("catmendccstatuschpvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable)), ("catmAISRDIStatusChPVclRangeTable", ("catmaisrdistatuschpvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable)), ("catmDownPVclRangeTable", ("catmdownpvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable)), ("catmCurStatusUpPVclTable", ("catmcurstatusuppvcltable", CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable)), ("catmStatusUpPVclRangeTable", ("catmstatusuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable)), ("catmSegCCStatusUpPVclRangeTable", ("catmsegccstatusuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable)), ("catmEndCCStatusUpPVclRangeTable", ("catmendccstatusuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable)), ("catmAISRDIStatusUpPVclRangeTable", ("catmaisrdistatusuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable)), ("catmUpPVclRangeTable", ("catmuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable))])
        self._leafs = OrderedDict()

        self.catmcurstatchangepvcltable = CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable()
        self.catmcurstatchangepvcltable.parent = self
        self._children_name_map["catmcurstatchangepvcltable"] = "catmCurStatChangePVclTable"

        self.catmstatuschangepvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable()
        self.catmstatuschangepvclrangetable.parent = self
        self._children_name_map["catmstatuschangepvclrangetable"] = "catmStatusChangePVclRangeTable"

        self.catmsegccstatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable()
        self.catmsegccstatuschpvclrangetable.parent = self
        self._children_name_map["catmsegccstatuschpvclrangetable"] = "catmSegCCStatusChPVclRangeTable"

        self.catmendccstatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable()
        self.catmendccstatuschpvclrangetable.parent = self
        self._children_name_map["catmendccstatuschpvclrangetable"] = "catmEndCCStatusChPVclRangeTable"

        self.catmaisrdistatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable()
        self.catmaisrdistatuschpvclrangetable.parent = self
        self._children_name_map["catmaisrdistatuschpvclrangetable"] = "catmAISRDIStatusChPVclRangeTable"

        self.catmdownpvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable()
        self.catmdownpvclrangetable.parent = self
        self._children_name_map["catmdownpvclrangetable"] = "catmDownPVclRangeTable"

        self.catmcurstatusuppvcltable = CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable()
        self.catmcurstatusuppvcltable.parent = self
        self._children_name_map["catmcurstatusuppvcltable"] = "catmCurStatusUpPVclTable"

        self.catmstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable()
        self.catmstatusuppvclrangetable.parent = self
        self._children_name_map["catmstatusuppvclrangetable"] = "catmStatusUpPVclRangeTable"

        self.catmsegccstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable()
        self.catmsegccstatusuppvclrangetable.parent = self
        self._children_name_map["catmsegccstatusuppvclrangetable"] = "catmSegCCStatusUpPVclRangeTable"

        self.catmendccstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable()
        self.catmendccstatusuppvclrangetable.parent = self
        self._children_name_map["catmendccstatusuppvclrangetable"] = "catmEndCCStatusUpPVclRangeTable"

        self.catmaisrdistatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable()
        self.catmaisrdistatusuppvclrangetable.parent = self
        self._children_name_map["catmaisrdistatusuppvclrangetable"] = "catmAISRDIStatusUpPVclRangeTable"

        self.catmuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable()
        self.catmuppvclrangetable.parent = self
        self._children_name_map["catmuppvclrangetable"] = "catmUpPVclRangeTable"
        self._segment_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOATMPVCTRAPEXTNMIB, [], name, value)


    class CatmCurStatChangePVclTable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed in the
        last corresponding PVC notification.
        
        .. attribute:: catmcurstatchangepvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last corresponding PVC notification
        	**type**\: list of  		 :py:class:`CatmCurStatChangePVclEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable, self).__init__()

            self.yang_name = "catmCurStatChangePVclTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmCurStatChangePVclEntry", ("catmcurstatchangepvclentry", CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry))])
            self._leafs = OrderedDict()

            self.catmcurstatchangepvclentry = YList(self)
            self._segment_path = lambda: "catmCurStatChangePVclTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable, [], name, value)


        class CatmCurStatChangePVclEntry(Entity):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed in the last corresponding PVC notification.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: atmvclvci  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmpvclstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclcurfailtime
            
            	The time stamp at which this PVCL changed state to DOWN last time in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclprevrecovertime
            
            	The time stamp at which this PVCL changed state to UP last time in the previous corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclfailurereason
            
            	Type of OAM failure
            	**type**\:  :py:class:`CatmOAMFailureType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMFailureType>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry, self).__init__()

                self.yang_name = "catmCurStatChangePVclEntry"
                self.yang_parent_name = "catmCurStatChangePVclTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','atmvclvci']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('atmvclvci', (YLeaf(YType.str, 'atmVclVci'), ['int'])),
                    ('catmpvclstatustransition', (YLeaf(YType.uint32, 'catmPVclStatusTransition'), ['int'])),
                    ('catmpvclstatuschangestart', (YLeaf(YType.uint32, 'catmPVclStatusChangeStart'), ['int'])),
                    ('catmpvclstatuschangeend', (YLeaf(YType.uint32, 'catmPVclStatusChangeEnd'), ['int'])),
                    ('catmpvclsegccstatustransition', (YLeaf(YType.uint32, 'catmPVclSegCCStatusTransition'), ['int'])),
                    ('catmpvclsegccstatuschangestart', (YLeaf(YType.uint32, 'catmPVclSegCCStatusChangeStart'), ['int'])),
                    ('catmpvclsegccstatuschangeend', (YLeaf(YType.uint32, 'catmPVclSegCCStatusChangeEnd'), ['int'])),
                    ('catmpvclendccstatustransition', (YLeaf(YType.uint32, 'catmPVclEndCCStatusTransition'), ['int'])),
                    ('catmpvclendccstatuschangestart', (YLeaf(YType.uint32, 'catmPVclEndCCStatusChangeStart'), ['int'])),
                    ('catmpvclendccstatuschangeend', (YLeaf(YType.uint32, 'catmPVclEndCCStatusChangeEnd'), ['int'])),
                    ('catmpvclaisrdistatustransition', (YLeaf(YType.uint32, 'catmPVclAISRDIStatusTransition'), ['int'])),
                    ('catmpvclaisrdistatuschangestart', (YLeaf(YType.uint32, 'catmPVclAISRDIStatusChangeStart'), ['int'])),
                    ('catmpvclaisrdistatuschangeend', (YLeaf(YType.uint32, 'catmPVclAISRDIStatusChangeEnd'), ['int'])),
                    ('catmpvclcurfailtime', (YLeaf(YType.uint32, 'catmPVclCurFailTime'), ['int'])),
                    ('catmpvclprevrecovertime', (YLeaf(YType.uint32, 'catmPVclPrevRecoverTime'), ['int'])),
                    ('catmpvclfailurereason', (YLeaf(YType.enumeration, 'catmPVclFailureReason'), [('ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMFailureType', '')])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.catmpvclstatustransition = None
                self.catmpvclstatuschangestart = None
                self.catmpvclstatuschangeend = None
                self.catmpvclsegccstatustransition = None
                self.catmpvclsegccstatuschangestart = None
                self.catmpvclsegccstatuschangeend = None
                self.catmpvclendccstatustransition = None
                self.catmpvclendccstatuschangestart = None
                self.catmpvclendccstatuschangeend = None
                self.catmpvclaisrdistatustransition = None
                self.catmpvclaisrdistatuschangestart = None
                self.catmpvclaisrdistatuschangeend = None
                self.catmpvclcurfailtime = None
                self.catmpvclprevrecovertime = None
                self.catmpvclfailurereason = None
                self._segment_path = lambda: "catmCurStatChangePVclEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[atmVclVci='" + str(self.atmvclvci) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmCurStatChangePVclTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'catmpvclstatustransition', 'catmpvclstatuschangestart', 'catmpvclstatuschangeend', 'catmpvclsegccstatustransition', 'catmpvclsegccstatuschangestart', 'catmpvclsegccstatuschangeend', 'catmpvclendccstatustransition', 'catmpvclendccstatuschangestart', 'catmpvclendccstatuschangeend', 'catmpvclaisrdistatustransition', 'catmpvclaisrdistatuschangestart', 'catmpvclaisrdistatuschangeend', 'catmpvclcurfailtime', 'catmpvclprevrecovertime', 'catmpvclfailurereason'], name, value)


    class CatmStatusChangePVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed in the same
        direction in the last corresponding PVC notification .
        
        .. attribute:: catmstatuschangepvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed in the same direction in the last notification  interval
        	**type**\: list of  		 :py:class:`CatmStatusChangePVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable, self).__init__()

            self.yang_name = "catmStatusChangePVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmStatusChangePVclRangeEntry", ("catmstatuschangepvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmstatuschangepvclrangeentry = YList(self)
            self._segment_path = lambda: "catmStatusChangePVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable, [], name, value)


        class CatmStatusChangePVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed in the same direction in the last notification 
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	Index to represent different ranges, the first range is indexed by value 0, the second by 1 and so on..
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: catmpvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclrangestatuschangestart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangestatuschangeend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry, self).__init__()

                self.yang_name = "catmStatusChangePVclRangeEntry"
                self.yang_parent_name = "catmStatusChangePVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.int32, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmpvcllowerrangevalue', (YLeaf(YType.int32, 'catmPVclLowerRangeValue'), ['int'])),
                    ('catmpvclhigherrangevalue', (YLeaf(YType.int32, 'catmPVclHigherRangeValue'), ['int'])),
                    ('catmpvclrangestatuschangestart', (YLeaf(YType.uint32, 'catmPVclRangeStatusChangeStart'), ['int'])),
                    ('catmpvclrangestatuschangeend', (YLeaf(YType.uint32, 'catmPVclRangeStatusChangeEnd'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmpvcllowerrangevalue = None
                self.catmpvclhigherrangevalue = None
                self.catmpvclrangestatuschangestart = None
                self.catmpvclrangestatuschangeend = None
                self._segment_path = lambda: "catmStatusChangePVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmStatusChangePVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvcllowerrangevalue', 'catmpvclhigherrangevalue', 'catmpvclrangestatuschangestart', 'catmpvclrangestatuschangeend'], name, value)


    class CatmSegCCStatusChPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to segment CC 
        failure in the same direction in the last PVC 
        corresponding notification .
        
        .. attribute:: catmsegccstatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to segment CC failure in the same direction  in the last corresponding notification 
        	**type**\: list of  		 :py:class:`CatmSegCCStatusChPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable, self).__init__()

            self.yang_name = "catmSegCCStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmSegCCStatusChPVclRangeEntry", ("catmsegccstatuschpvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmsegccstatuschpvclrangeentry = YList(self)
            self._segment_path = lambda: "catmSegCCStatusChPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable, [], name, value)


        class CatmSegCCStatusChPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to segment CC failure in the same direction 
            in the last corresponding notification .
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmpvclsegcclowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegcchigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccrangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccrangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry, self).__init__()

                self.yang_name = "catmSegCCStatusChPVclRangeEntry"
                self.yang_parent_name = "catmSegCCStatusChPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmpvclsegcclowerrangevalue', (YLeaf(YType.int32, 'catmPVclSegCCLowerRangeValue'), ['int'])),
                    ('catmpvclsegcchigherrangevalue', (YLeaf(YType.int32, 'catmPVclSegCCHigherRangeValue'), ['int'])),
                    ('catmpvclsegccrangestatuschstart', (YLeaf(YType.uint32, 'catmPVclSegCCRangeStatusChStart'), ['int'])),
                    ('catmpvclsegccrangestatuschend', (YLeaf(YType.uint32, 'catmPVclSegCCRangeStatusChEnd'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmpvclsegcclowerrangevalue = None
                self.catmpvclsegcchigherrangevalue = None
                self.catmpvclsegccrangestatuschstart = None
                self.catmpvclsegccrangestatuschend = None
                self._segment_path = lambda: "catmSegCCStatusChPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmSegCCStatusChPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclsegcclowerrangevalue', 'catmpvclsegcchigherrangevalue', 'catmpvclsegccrangestatuschstart', 'catmpvclsegccrangestatuschend'], name, value)


    class CatmEndCCStatusChPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to End CC failure
        in the same direction in the last PVC notification 
        interval.
        
        .. attribute:: catmendccstatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to End CC failure in the same direction in the  last corresponding notification 
        	**type**\: list of  		 :py:class:`CatmEndCCStatusChPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable, self).__init__()

            self.yang_name = "catmEndCCStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmEndCCStatusChPVclRangeEntry", ("catmendccstatuschpvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmendccstatuschpvclrangeentry = YList(self)
            self._segment_path = lambda: "catmEndCCStatusChPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable, [], name, value)


        class CatmEndCCStatusChPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to End CC failure in the same direction in the 
            last corresponding notification .
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmpvclendcclowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendcchigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccrangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccrangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry, self).__init__()

                self.yang_name = "catmEndCCStatusChPVclRangeEntry"
                self.yang_parent_name = "catmEndCCStatusChPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmpvclendcclowerrangevalue', (YLeaf(YType.int32, 'catmPVclEndCCLowerRangeValue'), ['int'])),
                    ('catmpvclendcchigherrangevalue', (YLeaf(YType.int32, 'catmPVclEndCCHigherRangeValue'), ['int'])),
                    ('catmpvclendccrangestatuschstart', (YLeaf(YType.uint32, 'catmPVclEndCCRangeStatusChStart'), ['int'])),
                    ('catmpvclendccrangestatuschend', (YLeaf(YType.uint32, 'catmPVclEndCCRangeStatusChEnd'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmpvclendcclowerrangevalue = None
                self.catmpvclendcchigherrangevalue = None
                self.catmpvclendccrangestatuschstart = None
                self.catmpvclendccrangestatuschend = None
                self._segment_path = lambda: "catmEndCCStatusChPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmEndCCStatusChPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclendcclowerrangevalue', 'catmpvclendcchigherrangevalue', 'catmpvclendccrangestatuschstart', 'catmpvclendccrangestatuschend'], name, value)


    class CatmAISRDIStatusChPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to AIS/RDI failure
        in the same direction in the last corresponding PVC 
        notification.
        
        .. attribute:: catmaisrdistatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to AIS/RDI failure in the same direction in the  last corresponding notification 
        	**type**\: list of  		 :py:class:`CatmAISRDIStatusChPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable, self).__init__()

            self.yang_name = "catmAISRDIStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmAISRDIStatusChPVclRangeEntry", ("catmaisrdistatuschpvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmaisrdistatuschpvclrangeentry = YList(self)
            self._segment_path = lambda: "catmAISRDIStatusChPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable, [], name, value)


        class CatmAISRDIStatusChPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to AIS/RDI failure in the same direction in the 
            last corresponding notification .
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmpvclaisrdilowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdihigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdirangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdirangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry, self).__init__()

                self.yang_name = "catmAISRDIStatusChPVclRangeEntry"
                self.yang_parent_name = "catmAISRDIStatusChPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmpvclaisrdilowerrangevalue', (YLeaf(YType.int32, 'catmPVclAISRDILowerRangeValue'), ['int'])),
                    ('catmpvclaisrdihigherrangevalue', (YLeaf(YType.int32, 'catmPVclAISRDIHigherRangeValue'), ['int'])),
                    ('catmpvclaisrdirangestatuschstart', (YLeaf(YType.uint32, 'catmPVclAISRDIRangeStatusChStart'), ['int'])),
                    ('catmpvclaisrdirangestatuschend', (YLeaf(YType.uint32, 'catmPVclAISRDIRangeStatusChEnd'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmpvclaisrdilowerrangevalue = None
                self.catmpvclaisrdihigherrangevalue = None
                self.catmpvclaisrdirangestatuschstart = None
                self.catmpvclaisrdirangestatuschend = None
                self._segment_path = lambda: "catmAISRDIStatusChPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmAISRDIStatusChPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclaisrdilowerrangevalue', 'catmpvclaisrdihigherrangevalue', 'catmpvclaisrdirangestatuschstart', 'catmpvclaisrdirangestatuschend'], name, value)


    class CatmDownPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have detected as Down
        in the last corresponding PVC notification .
        
        .. attribute:: catmdownpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  atmVclOperStatus to  have detected as Down in the last notification  interval
        	**type**\: list of  		 :py:class:`CatmDownPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable, self).__init__()

            self.yang_name = "catmDownPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmDownPVclRangeEntry", ("catmdownpvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmdownpvclrangeentry = YList(self)
            self._segment_path = lambda: "catmDownPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable, [], name, value)


        class CatmDownPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
            have detected as Down in the last notification 
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmdownpvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Down in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmdownpvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Down in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmdownpvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Down on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmdownpvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Down on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevuppvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Up on any of the PVCLs in the range in the previous catmIntfPvcUp2Trap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevuppvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Up on any of the PVCLs in the range in the previous catmIntfPvcUp2Trap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangefailurereason
            
            	Type of OAM failure
            	**type**\:  :py:class:`CatmOAMFailureType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMFailureType>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry, self).__init__()

                self.yang_name = "catmDownPVclRangeEntry"
                self.yang_parent_name = "catmDownPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmdownpvcllowerrangevalue', (YLeaf(YType.int32, 'catmDownPVclLowerRangeValue'), ['int'])),
                    ('catmdownpvclhigherrangevalue', (YLeaf(YType.int32, 'catmDownPVclHigherRangeValue'), ['int'])),
                    ('catmdownpvclrangestart', (YLeaf(YType.uint32, 'catmDownPVclRangeStart'), ['int'])),
                    ('catmdownpvclrangeend', (YLeaf(YType.uint32, 'catmDownPVclRangeEnd'), ['int'])),
                    ('catmprevuppvclrangestart', (YLeaf(YType.uint32, 'catmPrevUpPVclRangeStart'), ['int'])),
                    ('catmprevuppvclrangeend', (YLeaf(YType.uint32, 'catmPrevUpPVclRangeEnd'), ['int'])),
                    ('catmpvclrangefailurereason', (YLeaf(YType.enumeration, 'catmPVclRangeFailureReason'), [('ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMFailureType', '')])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmdownpvcllowerrangevalue = None
                self.catmdownpvclhigherrangevalue = None
                self.catmdownpvclrangestart = None
                self.catmdownpvclrangeend = None
                self.catmprevuppvclrangestart = None
                self.catmprevuppvclrangeend = None
                self.catmpvclrangefailurereason = None
                self._segment_path = lambda: "catmDownPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmDownPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmdownpvcllowerrangevalue', 'catmdownpvclhigherrangevalue', 'catmdownpvclrangestart', 'catmdownpvclrangeend', 'catmprevuppvclrangestart', 'catmprevuppvclrangeend', 'catmpvclrangefailurereason'], name, value)


    class CatmCurStatusUpPVclTable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed to UP
        in the last corresponding PVC notification .
        
        .. attribute:: catmcurstatusuppvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed to UP in the last PVC notification  interval
        	**type**\: list of  		 :py:class:`CatmCurStatusUpPVclEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable, self).__init__()

            self.yang_name = "catmCurStatusUpPVclTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmCurStatusUpPVclEntry", ("catmcurstatusuppvclentry", CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry))])
            self._leafs = OrderedDict()

            self.catmcurstatusuppvclentry = YList(self)
            self._segment_path = lambda: "catmCurStatusUpPVclTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable, [], name, value)


        class CatmCurStatusUpPVclEntry(Entity):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed to UP in the last PVC notification 
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: atmvclvci  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmpvclstatusuptransition
            
            	The number of Down to Up state transitions due to OAM loopback recovery that has happened on this PVCL  in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusupstart
            
            	The time stamp at which this PVCL changed state to UP  for the first time due to OAM loopback recovery in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusupend
            
            	The time stamp at which this PVCL changed state to UP  for the last time due to OAM loopback recovery in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusuptransition
            
            	The number of Down to Up state transitions that has  happened on this PVCL in the last corresponding notification  due to Segment CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusupstart
            
            	The time stamp at which this PVCL changed state to Up for  the first time in the last corresponding notification due to Segment CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusupend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to Segment CC  OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusuptransition
            
            	The number of Down to UP state transitions that has  happened on this PVCL in the last notification  interval due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusupstart
            
            	The time stamp at which this PVCL changed state to Up for the first time in the last corresponding notification  due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusupend
            
            	The time stamp at which this PVCL changed state to Up for the last time in the last corresponding notification  due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusuptransition
            
            	The number of Down to Up state transitions that  has happened on this PVCL in the last notification  interval due to AIS RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusupstart
            
            	The time stamp at which this PVCL changed state to Up for the first time in the last corresponding notification  due to AIS/RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusupend
            
            	The time stamp at which this PVCL changed state to Up for the last time in the last corresponding notification  due to AIS/RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclcurrecovertime
            
            	The time stamp at which this PVCL changed state to UP last time in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclprevfailtime
            
            	The time stamp at which this PVCL changed state to DOWN last time in the previous corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrecoveryreason
            
            	Type of OAM Recovered
            	**type**\:  :py:class:`CatmOAMRecoveryType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMRecoveryType>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry, self).__init__()

                self.yang_name = "catmCurStatusUpPVclEntry"
                self.yang_parent_name = "catmCurStatusUpPVclTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','atmvclvci']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('atmvclvci', (YLeaf(YType.str, 'atmVclVci'), ['int'])),
                    ('catmpvclstatusuptransition', (YLeaf(YType.uint32, 'catmPVclStatusUpTransition'), ['int'])),
                    ('catmpvclstatusupstart', (YLeaf(YType.uint32, 'catmPVclStatusUpStart'), ['int'])),
                    ('catmpvclstatusupend', (YLeaf(YType.uint32, 'catmPVclStatusUpEnd'), ['int'])),
                    ('catmpvclsegccstatusuptransition', (YLeaf(YType.uint32, 'catmPVclSegCCStatusUpTransition'), ['int'])),
                    ('catmpvclsegccstatusupstart', (YLeaf(YType.uint32, 'catmPVclSegCCStatusUpStart'), ['int'])),
                    ('catmpvclsegccstatusupend', (YLeaf(YType.uint32, 'catmPVclSegCCStatusUpEnd'), ['int'])),
                    ('catmpvclendccstatusuptransition', (YLeaf(YType.uint32, 'catmPVclEndCCStatusUpTransition'), ['int'])),
                    ('catmpvclendccstatusupstart', (YLeaf(YType.uint32, 'catmPVclEndCCStatusUpStart'), ['int'])),
                    ('catmpvclendccstatusupend', (YLeaf(YType.uint32, 'catmPVclEndCCStatusUpEnd'), ['int'])),
                    ('catmpvclaisrdistatusuptransition', (YLeaf(YType.uint32, 'catmPVclAISRDIStatusUpTransition'), ['int'])),
                    ('catmpvclaisrdistatusupstart', (YLeaf(YType.uint32, 'catmPVclAISRDIStatusUpStart'), ['int'])),
                    ('catmpvclaisrdistatusupend', (YLeaf(YType.uint32, 'catmPVclAISRDIStatusUpEnd'), ['int'])),
                    ('catmpvclcurrecovertime', (YLeaf(YType.uint32, 'catmPVclCurRecoverTime'), ['int'])),
                    ('catmpvclprevfailtime', (YLeaf(YType.uint32, 'catmPVclPrevFailTime'), ['int'])),
                    ('catmpvclrecoveryreason', (YLeaf(YType.enumeration, 'catmPVclRecoveryReason'), [('ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMRecoveryType', '')])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.catmpvclstatusuptransition = None
                self.catmpvclstatusupstart = None
                self.catmpvclstatusupend = None
                self.catmpvclsegccstatusuptransition = None
                self.catmpvclsegccstatusupstart = None
                self.catmpvclsegccstatusupend = None
                self.catmpvclendccstatusuptransition = None
                self.catmpvclendccstatusupstart = None
                self.catmpvclendccstatusupend = None
                self.catmpvclaisrdistatusuptransition = None
                self.catmpvclaisrdistatusupstart = None
                self.catmpvclaisrdistatusupend = None
                self.catmpvclcurrecovertime = None
                self.catmpvclprevfailtime = None
                self.catmpvclrecoveryreason = None
                self._segment_path = lambda: "catmCurStatusUpPVclEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[atmVclVci='" + str(self.atmvclvci) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmCurStatusUpPVclTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'catmpvclstatusuptransition', 'catmpvclstatusupstart', 'catmpvclstatusupend', 'catmpvclsegccstatusuptransition', 'catmpvclsegccstatusupstart', 'catmpvclsegccstatusupend', 'catmpvclendccstatusuptransition', 'catmpvclendccstatusupstart', 'catmpvclendccstatusupend', 'catmpvclaisrdistatusuptransition', 'catmpvclaisrdistatusupstart', 'catmpvclaisrdistatusupend', 'catmpvclcurrecovertime', 'catmpvclprevfailtime', 'catmpvclrecoveryreason'], name, value)


    class CatmStatusUpPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and loopback OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  loopback OAM status to  have detected as recovered in the last notification  interval
        	**type**\: list of  		 :py:class:`CatmStatusUpPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable, self).__init__()

            self.yang_name = "catmStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmStatusUpPVclRangeEntry", ("catmstatusuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmstatusuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmStatusUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable, [], name, value)


        class CatmStatusUpPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  loopback OAM status to 
            have detected as recovered in the last notification 
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmpvcluplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  Loopback OAM recovery has been detected in the last  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvcluphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  Loopback OAM recovery has been detected in the last  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclrangestatusupstart
            
            	The time stamp at which the first Loopback OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangestatusupend
            
            	The time stamp at which the last Loopback OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry, self).__init__()

                self.yang_name = "catmStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmStatusUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmpvcluplowerrangevalue', (YLeaf(YType.int32, 'catmPVclUpLowerRangeValue'), ['int'])),
                    ('catmpvcluphigherrangevalue', (YLeaf(YType.int32, 'catmPVclUpHigherRangeValue'), ['int'])),
                    ('catmpvclrangestatusupstart', (YLeaf(YType.uint32, 'catmPVclRangeStatusUpStart'), ['int'])),
                    ('catmpvclrangestatusupend', (YLeaf(YType.uint32, 'catmPVclRangeStatusUpEnd'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmpvcluplowerrangevalue = None
                self.catmpvcluphigherrangevalue = None
                self.catmpvclrangestatusupstart = None
                self.catmpvclrangestatusupend = None
                self._segment_path = lambda: "catmStatusUpPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmStatusUpPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvcluplowerrangevalue', 'catmpvcluphigherrangevalue', 'catmpvclrangestatusupstart', 'catmpvclrangestatusupend'], name, value)


    class CatmSegCCStatusUpPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and Segment CC OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmsegccstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and Segment CC OAM status to have detected as recovered in the last notification interval
        	**type**\: list of  		 :py:class:`CatmSegCCStatusUpPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable, self).__init__()

            self.yang_name = "catmSegCCStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmSegCCStatusUpPVclRangeEntry", ("catmsegccstatusuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmsegccstatusuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmSegCCStatusUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable, [], name, value)


        class CatmSegCCStatusUpPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and Segment CC OAM status to
            have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmpvclsegccuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the Segment CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the Segment CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccrangestatusupstart
            
            	The time stamp at which the first Segment CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccrangestatusupend
            
            	The time stamp at which the last Segment CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry, self).__init__()

                self.yang_name = "catmSegCCStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmSegCCStatusUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmpvclsegccuplowerrangevalue', (YLeaf(YType.int32, 'catmPVclSegCCUpLowerRangeValue'), ['int'])),
                    ('catmpvclsegccuphigherrangevalue', (YLeaf(YType.int32, 'catmPVclSegCCUpHigherRangeValue'), ['int'])),
                    ('catmpvclsegccrangestatusupstart', (YLeaf(YType.uint32, 'catmPVclSegCCRangeStatusUpStart'), ['int'])),
                    ('catmpvclsegccrangestatusupend', (YLeaf(YType.uint32, 'catmPVclSegCCRangeStatusUpEnd'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmpvclsegccuplowerrangevalue = None
                self.catmpvclsegccuphigherrangevalue = None
                self.catmpvclsegccrangestatusupstart = None
                self.catmpvclsegccrangestatusupend = None
                self._segment_path = lambda: "catmSegCCStatusUpPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmSegCCStatusUpPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclsegccuplowerrangevalue', 'catmpvclsegccuphigherrangevalue', 'catmpvclsegccrangestatusupstart', 'catmpvclsegccrangestatusupend'], name, value)


    class CatmEndCCStatusUpPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and End\-to\-End CC OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmendccstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and End\-to\-End CC OAM status  to have detected as recovered in the last notification interval
        	**type**\: list of  		 :py:class:`CatmEndCCStatusUpPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable, self).__init__()

            self.yang_name = "catmEndCCStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmEndCCStatusUpPVclRangeEntry", ("catmendccstatusuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmendccstatusuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmEndCCStatusUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable, [], name, value)


        class CatmEndCCStatusUpPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and End\-to\-End CC OAM status 
            to have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmpvclendccuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the End\-to\-End CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the End\-to\-End CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccrangestatusupstart
            
            	The time stamp at which the first End\-to\-End CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccrangestatusupend
            
            	The time stamp at which the last End\-to\-End CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry, self).__init__()

                self.yang_name = "catmEndCCStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmEndCCStatusUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmpvclendccuplowerrangevalue', (YLeaf(YType.int32, 'catmPVclEndCCUpLowerRangeValue'), ['int'])),
                    ('catmpvclendccuphigherrangevalue', (YLeaf(YType.int32, 'catmPVclEndCCUpHigherRangeValue'), ['int'])),
                    ('catmpvclendccrangestatusupstart', (YLeaf(YType.uint32, 'catmPVclEndCCRangeStatusUpStart'), ['int'])),
                    ('catmpvclendccrangestatusupend', (YLeaf(YType.uint32, 'catmPVclEndCCRangeStatusUpEnd'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmpvclendccuplowerrangevalue = None
                self.catmpvclendccuphigherrangevalue = None
                self.catmpvclendccrangestatusupstart = None
                self.catmpvclendccrangestatusupend = None
                self._segment_path = lambda: "catmEndCCStatusUpPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmEndCCStatusUpPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclendccuplowerrangevalue', 'catmpvclendccuphigherrangevalue', 'catmpvclendccrangestatusupstart', 'catmpvclendccrangestatusupend'], name, value)


    class CatmAISRDIStatusUpPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and AISRDI OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmaisrdistatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and AISRDI OAM status  to have detected as recovered in the last notification interval
        	**type**\: list of  		 :py:class:`CatmAISRDIStatusUpPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable, self).__init__()

            self.yang_name = "catmAISRDIStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmAISRDIStatusUpPVclRangeEntry", ("catmaisrdistatusuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmaisrdistatusuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmAISRDIStatusUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable, [], name, value)


        class CatmAISRDIStatusUpPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and AISRDI OAM status 
            to have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmpvclaisrdiuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the AISRDI OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdiuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the AISRDI OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdirangestatusupstart
            
            	The time stamp at which the first AISRDI OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdirangestatusupend
            
            	The time stamp at which the last AISRDI OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry, self).__init__()

                self.yang_name = "catmAISRDIStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmAISRDIStatusUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmpvclaisrdiuplowerrangevalue', (YLeaf(YType.int32, 'catmPVclAISRDIUpLowerRangeValue'), ['int'])),
                    ('catmpvclaisrdiuphigherrangevalue', (YLeaf(YType.int32, 'catmPVclAISRDIUpHigherRangeValue'), ['int'])),
                    ('catmpvclaisrdirangestatusupstart', (YLeaf(YType.uint32, 'catmPVclAISRDIRangeStatusUpStart'), ['int'])),
                    ('catmpvclaisrdirangestatusupend', (YLeaf(YType.uint32, 'catmPVclAISRDIRangeStatusUpEnd'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmpvclaisrdiuplowerrangevalue = None
                self.catmpvclaisrdiuphigherrangevalue = None
                self.catmpvclaisrdirangestatusupstart = None
                self.catmpvclaisrdirangestatusupend = None
                self._segment_path = lambda: "catmAISRDIStatusUpPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmAISRDIStatusUpPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclaisrdiuplowerrangevalue', 'catmpvclaisrdiuphigherrangevalue', 'catmpvclaisrdirangestatusupstart', 'catmpvclaisrdirangestatusupend'], name, value)


    class CatmUpPVclRangeTable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have detected as Up
        in the last corresponding PVC notification .
        
        .. attribute:: catmuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  atmVclOperStatus to  have detected as Up in the last notification  interval
        	**type**\: list of  		 :py:class:`CatmUpPVclRangeEntry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable, self).__init__()

            self.yang_name = "catmUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("catmUpPVclRangeEntry", ("catmuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry))])
            self._leafs = OrderedDict()

            self.catmuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable, [], name, value)


        class CatmUpPVclRangeEntry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
            have detected as Up in the last notification 
            interval.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
            
            .. attribute:: catmuppvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Up in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmuppvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Up in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmuppvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Up on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmuppvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Up on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevdownpvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Down on any of the PVCLs in the range in the previous catmIntfPvcDownTrap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevdownpvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Down on any of the PVCLs in the range in the previous catmIntfPvcDownTrap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangerecoveryreason
            
            	Type of OAM Recovered
            	**type**\:  :py:class:`CatmOAMRecoveryType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMRecoveryType>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry, self).__init__()

                self.yang_name = "catmUpPVclRangeEntry"
                self.yang_parent_name = "catmUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','catmstatuschangepvclrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('catmstatuschangepvclrangeindex', (YLeaf(YType.str, 'catmStatusChangePVclRangeIndex'), ['int'])),
                    ('catmuppvcllowerrangevalue', (YLeaf(YType.int32, 'catmUpPVclLowerRangeValue'), ['int'])),
                    ('catmuppvclhigherrangevalue', (YLeaf(YType.int32, 'catmUpPVclHigherRangeValue'), ['int'])),
                    ('catmuppvclrangestart', (YLeaf(YType.uint32, 'catmUpPVclRangeStart'), ['int'])),
                    ('catmuppvclrangeend', (YLeaf(YType.uint32, 'catmUpPVclRangeEnd'), ['int'])),
                    ('catmprevdownpvclrangestart', (YLeaf(YType.uint32, 'catmPrevDownPVclRangeStart'), ['int'])),
                    ('catmprevdownpvclrangeend', (YLeaf(YType.uint32, 'catmPrevDownPVclRangeEnd'), ['int'])),
                    ('catmpvclrangerecoveryreason', (YLeaf(YType.enumeration, 'catmPVclRangeRecoveryReason'), [('ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMRecoveryType', '')])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.catmuppvcllowerrangevalue = None
                self.catmuppvclhigherrangevalue = None
                self.catmuppvclrangestart = None
                self.catmuppvclrangeend = None
                self.catmprevdownpvclrangestart = None
                self.catmprevdownpvclrangeend = None
                self.catmpvclrangerecoveryreason = None
                self._segment_path = lambda: "catmUpPVclRangeEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[catmStatusChangePVclRangeIndex='" + str(self.catmstatuschangepvclrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmUpPVclRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmuppvcllowerrangevalue', 'catmuppvclhigherrangevalue', 'catmuppvclrangestart', 'catmuppvclrangeend', 'catmprevdownpvclrangestart', 'catmprevdownpvclrangeend', 'catmpvclrangerecoveryreason'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOATMPVCTRAPEXTNMIB()
        return self._top_entity

