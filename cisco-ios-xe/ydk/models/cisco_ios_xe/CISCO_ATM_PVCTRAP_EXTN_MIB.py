""" CISCO_ATM_PVCTRAP_EXTN_MIB 

This MIB Module is a supplement to the
CISCO\-IETF\-ATM2\-PVCTRAP\-MIB.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Catmoamfailuretype(Enum):
    """
    Catmoamfailuretype

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


class Catmoamrecoverytype(Enum):
    """
    Catmoamrecoverytype

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



class CiscoAtmPvctrapExtnMib(Entity):
    """
    
    
    .. attribute:: catmaisrdistatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to AIS/RDI failure in the same direction in the last corresponding PVC  notification
    	**type**\:   :py:class:`Catmaisrdistatuschpvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable>`
    
    .. attribute:: catmaisrdistatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and AISRDI OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:   :py:class:`Catmaisrdistatusuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable>`
    
    .. attribute:: catmcurstatchangepvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last corresponding PVC notification
    	**type**\:   :py:class:`Catmcurstatchangepvcltable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable>`
    
    .. attribute:: catmcurstatusuppvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed to UP in the last corresponding PVC notification 
    	**type**\:   :py:class:`Catmcurstatusuppvcltable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable>`
    
    .. attribute:: catmdownpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have detected as Down in the last corresponding PVC notification 
    	**type**\:   :py:class:`Catmdownpvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable>`
    
    .. attribute:: catmendccstatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to End CC failure in the same direction in the last PVC notification  interval
    	**type**\:   :py:class:`Catmendccstatuschpvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable>`
    
    .. attribute:: catmendccstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and End\-to\-End CC OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:   :py:class:`Catmendccstatusuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable>`
    
    .. attribute:: catmsegccstatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to segment CC  failure in the same direction in the last PVC  corresponding notification 
    	**type**\:   :py:class:`Catmsegccstatuschpvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable>`
    
    .. attribute:: catmsegccstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and Segment CC OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:   :py:class:`Catmsegccstatusuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable>`
    
    .. attribute:: catmstatuschangepvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the same direction in the last corresponding PVC notification 
    	**type**\:   :py:class:`Catmstatuschangepvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable>`
    
    .. attribute:: catmstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and loopback OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:   :py:class:`Catmstatusuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable>`
    
    .. attribute:: catmuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have detected as Up in the last corresponding PVC notification 
    	**type**\:   :py:class:`Catmuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmuppvclrangetable>`
    
    

    """

    _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
    _revision = '2003-01-20'

    def __init__(self):
        super(CiscoAtmPvctrapExtnMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
        self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

        self.catmaisrdistatuschpvclrangetable = CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable()
        self.catmaisrdistatuschpvclrangetable.parent = self
        self._children_name_map["catmaisrdistatuschpvclrangetable"] = "catmAISRDIStatusChPVclRangeTable"
        self._children_yang_names.add("catmAISRDIStatusChPVclRangeTable")

        self.catmaisrdistatusuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable()
        self.catmaisrdistatusuppvclrangetable.parent = self
        self._children_name_map["catmaisrdistatusuppvclrangetable"] = "catmAISRDIStatusUpPVclRangeTable"
        self._children_yang_names.add("catmAISRDIStatusUpPVclRangeTable")

        self.catmcurstatchangepvcltable = CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable()
        self.catmcurstatchangepvcltable.parent = self
        self._children_name_map["catmcurstatchangepvcltable"] = "catmCurStatChangePVclTable"
        self._children_yang_names.add("catmCurStatChangePVclTable")

        self.catmcurstatusuppvcltable = CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable()
        self.catmcurstatusuppvcltable.parent = self
        self._children_name_map["catmcurstatusuppvcltable"] = "catmCurStatusUpPVclTable"
        self._children_yang_names.add("catmCurStatusUpPVclTable")

        self.catmdownpvclrangetable = CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable()
        self.catmdownpvclrangetable.parent = self
        self._children_name_map["catmdownpvclrangetable"] = "catmDownPVclRangeTable"
        self._children_yang_names.add("catmDownPVclRangeTable")

        self.catmendccstatuschpvclrangetable = CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable()
        self.catmendccstatuschpvclrangetable.parent = self
        self._children_name_map["catmendccstatuschpvclrangetable"] = "catmEndCCStatusChPVclRangeTable"
        self._children_yang_names.add("catmEndCCStatusChPVclRangeTable")

        self.catmendccstatusuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable()
        self.catmendccstatusuppvclrangetable.parent = self
        self._children_name_map["catmendccstatusuppvclrangetable"] = "catmEndCCStatusUpPVclRangeTable"
        self._children_yang_names.add("catmEndCCStatusUpPVclRangeTable")

        self.catmsegccstatuschpvclrangetable = CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable()
        self.catmsegccstatuschpvclrangetable.parent = self
        self._children_name_map["catmsegccstatuschpvclrangetable"] = "catmSegCCStatusChPVclRangeTable"
        self._children_yang_names.add("catmSegCCStatusChPVclRangeTable")

        self.catmsegccstatusuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable()
        self.catmsegccstatusuppvclrangetable.parent = self
        self._children_name_map["catmsegccstatusuppvclrangetable"] = "catmSegCCStatusUpPVclRangeTable"
        self._children_yang_names.add("catmSegCCStatusUpPVclRangeTable")

        self.catmstatuschangepvclrangetable = CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable()
        self.catmstatuschangepvclrangetable.parent = self
        self._children_name_map["catmstatuschangepvclrangetable"] = "catmStatusChangePVclRangeTable"
        self._children_yang_names.add("catmStatusChangePVclRangeTable")

        self.catmstatusuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable()
        self.catmstatusuppvclrangetable.parent = self
        self._children_name_map["catmstatusuppvclrangetable"] = "catmStatusUpPVclRangeTable"
        self._children_yang_names.add("catmStatusUpPVclRangeTable")

        self.catmuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmuppvclrangetable()
        self.catmuppvclrangetable.parent = self
        self._children_name_map["catmuppvclrangetable"] = "catmUpPVclRangeTable"
        self._children_yang_names.add("catmUpPVclRangeTable")


    class Catmcurstatchangepvcltable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed in the
        last corresponding PVC notification.
        
        .. attribute:: catmcurstatchangepvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last corresponding PVC notification
        	**type**\: list of    :py:class:`Catmcurstatchangepvclentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable, self).__init__()

            self.yang_name = "catmCurStatChangePVclTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmcurstatchangepvclentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable, self).__setattr__(name, value)


        class Catmcurstatchangepvclentry(Entity):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed in the last corresponding PVC notification.
            
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
            
            .. attribute:: catmpvclaisrdistatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to AIS RDI OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to AIS RDI OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to AIS RDI OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclcurfailtime
            
            	The time stamp at which this PVCL changed state to DOWN last time in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to End CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to End CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to End CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclfailurereason
            
            	Type of OAM failure
            	**type**\:   :py:class:`Catmoamfailuretype <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.Catmoamfailuretype>`
            
            .. attribute:: catmpvclprevrecovertime
            
            	The time stamp at which this PVCL changed state to UP last time in the previous corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to Segment CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to Segment CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to Segment CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry, self).__init__()

                self.yang_name = "catmCurStatChangePVclEntry"
                self.yang_parent_name = "catmCurStatChangePVclTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.catmpvclaisrdistatuschangeend = YLeaf(YType.uint32, "catmPVclAISRDIStatusChangeEnd")

                self.catmpvclaisrdistatuschangestart = YLeaf(YType.uint32, "catmPVclAISRDIStatusChangeStart")

                self.catmpvclaisrdistatustransition = YLeaf(YType.uint32, "catmPVclAISRDIStatusTransition")

                self.catmpvclcurfailtime = YLeaf(YType.uint32, "catmPVclCurFailTime")

                self.catmpvclendccstatuschangeend = YLeaf(YType.uint32, "catmPVclEndCCStatusChangeEnd")

                self.catmpvclendccstatuschangestart = YLeaf(YType.uint32, "catmPVclEndCCStatusChangeStart")

                self.catmpvclendccstatustransition = YLeaf(YType.uint32, "catmPVclEndCCStatusTransition")

                self.catmpvclfailurereason = YLeaf(YType.enumeration, "catmPVclFailureReason")

                self.catmpvclprevrecovertime = YLeaf(YType.uint32, "catmPVclPrevRecoverTime")

                self.catmpvclsegccstatuschangeend = YLeaf(YType.uint32, "catmPVclSegCCStatusChangeEnd")

                self.catmpvclsegccstatuschangestart = YLeaf(YType.uint32, "catmPVclSegCCStatusChangeStart")

                self.catmpvclsegccstatustransition = YLeaf(YType.uint32, "catmPVclSegCCStatusTransition")

                self.catmpvclstatuschangeend = YLeaf(YType.uint32, "catmPVclStatusChangeEnd")

                self.catmpvclstatuschangestart = YLeaf(YType.uint32, "catmPVclStatusChangeStart")

                self.catmpvclstatustransition = YLeaf(YType.uint32, "catmPVclStatusTransition")

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
                                "catmpvclaisrdistatuschangeend",
                                "catmpvclaisrdistatuschangestart",
                                "catmpvclaisrdistatustransition",
                                "catmpvclcurfailtime",
                                "catmpvclendccstatuschangeend",
                                "catmpvclendccstatuschangestart",
                                "catmpvclendccstatustransition",
                                "catmpvclfailurereason",
                                "catmpvclprevrecovertime",
                                "catmpvclsegccstatuschangeend",
                                "catmpvclsegccstatuschangestart",
                                "catmpvclsegccstatustransition",
                                "catmpvclstatuschangeend",
                                "catmpvclstatuschangestart",
                                "catmpvclstatustransition") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.atmvclvci.is_set or
                    self.catmpvclaisrdistatuschangeend.is_set or
                    self.catmpvclaisrdistatuschangestart.is_set or
                    self.catmpvclaisrdistatustransition.is_set or
                    self.catmpvclcurfailtime.is_set or
                    self.catmpvclendccstatuschangeend.is_set or
                    self.catmpvclendccstatuschangestart.is_set or
                    self.catmpvclendccstatustransition.is_set or
                    self.catmpvclfailurereason.is_set or
                    self.catmpvclprevrecovertime.is_set or
                    self.catmpvclsegccstatuschangeend.is_set or
                    self.catmpvclsegccstatuschangestart.is_set or
                    self.catmpvclsegccstatustransition.is_set or
                    self.catmpvclstatuschangeend.is_set or
                    self.catmpvclstatuschangestart.is_set or
                    self.catmpvclstatustransition.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.atmvclvci.yfilter != YFilter.not_set or
                    self.catmpvclaisrdistatuschangeend.yfilter != YFilter.not_set or
                    self.catmpvclaisrdistatuschangestart.yfilter != YFilter.not_set or
                    self.catmpvclaisrdistatustransition.yfilter != YFilter.not_set or
                    self.catmpvclcurfailtime.yfilter != YFilter.not_set or
                    self.catmpvclendccstatuschangeend.yfilter != YFilter.not_set or
                    self.catmpvclendccstatuschangestart.yfilter != YFilter.not_set or
                    self.catmpvclendccstatustransition.yfilter != YFilter.not_set or
                    self.catmpvclfailurereason.yfilter != YFilter.not_set or
                    self.catmpvclprevrecovertime.yfilter != YFilter.not_set or
                    self.catmpvclsegccstatuschangeend.yfilter != YFilter.not_set or
                    self.catmpvclsegccstatuschangestart.yfilter != YFilter.not_set or
                    self.catmpvclsegccstatustransition.yfilter != YFilter.not_set or
                    self.catmpvclstatuschangeend.yfilter != YFilter.not_set or
                    self.catmpvclstatuschangestart.yfilter != YFilter.not_set or
                    self.catmpvclstatustransition.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmCurStatChangePVclEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmCurStatChangePVclTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.atmvclvci.is_set or self.atmvclvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvci.get_name_leafdata())
                if (self.catmpvclaisrdistatuschangeend.is_set or self.catmpvclaisrdistatuschangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdistatuschangeend.get_name_leafdata())
                if (self.catmpvclaisrdistatuschangestart.is_set or self.catmpvclaisrdistatuschangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdistatuschangestart.get_name_leafdata())
                if (self.catmpvclaisrdistatustransition.is_set or self.catmpvclaisrdistatustransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdistatustransition.get_name_leafdata())
                if (self.catmpvclcurfailtime.is_set or self.catmpvclcurfailtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclcurfailtime.get_name_leafdata())
                if (self.catmpvclendccstatuschangeend.is_set or self.catmpvclendccstatuschangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccstatuschangeend.get_name_leafdata())
                if (self.catmpvclendccstatuschangestart.is_set or self.catmpvclendccstatuschangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccstatuschangestart.get_name_leafdata())
                if (self.catmpvclendccstatustransition.is_set or self.catmpvclendccstatustransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccstatustransition.get_name_leafdata())
                if (self.catmpvclfailurereason.is_set or self.catmpvclfailurereason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclfailurereason.get_name_leafdata())
                if (self.catmpvclprevrecovertime.is_set or self.catmpvclprevrecovertime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclprevrecovertime.get_name_leafdata())
                if (self.catmpvclsegccstatuschangeend.is_set or self.catmpvclsegccstatuschangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccstatuschangeend.get_name_leafdata())
                if (self.catmpvclsegccstatuschangestart.is_set or self.catmpvclsegccstatuschangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccstatuschangestart.get_name_leafdata())
                if (self.catmpvclsegccstatustransition.is_set or self.catmpvclsegccstatustransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccstatustransition.get_name_leafdata())
                if (self.catmpvclstatuschangeend.is_set or self.catmpvclstatuschangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclstatuschangeend.get_name_leafdata())
                if (self.catmpvclstatuschangestart.is_set or self.catmpvclstatuschangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclstatuschangestart.get_name_leafdata())
                if (self.catmpvclstatustransition.is_set or self.catmpvclstatustransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclstatustransition.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "atmVclVci" or name == "catmPVclAISRDIStatusChangeEnd" or name == "catmPVclAISRDIStatusChangeStart" or name == "catmPVclAISRDIStatusTransition" or name == "catmPVclCurFailTime" or name == "catmPVclEndCCStatusChangeEnd" or name == "catmPVclEndCCStatusChangeStart" or name == "catmPVclEndCCStatusTransition" or name == "catmPVclFailureReason" or name == "catmPVclPrevRecoverTime" or name == "catmPVclSegCCStatusChangeEnd" or name == "catmPVclSegCCStatusChangeStart" or name == "catmPVclSegCCStatusTransition" or name == "catmPVclStatusChangeEnd" or name == "catmPVclStatusChangeStart" or name == "catmPVclStatusTransition"):
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
                if(value_path == "catmPVclAISRDIStatusChangeEnd"):
                    self.catmpvclaisrdistatuschangeend = value
                    self.catmpvclaisrdistatuschangeend.value_namespace = name_space
                    self.catmpvclaisrdistatuschangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIStatusChangeStart"):
                    self.catmpvclaisrdistatuschangestart = value
                    self.catmpvclaisrdistatuschangestart.value_namespace = name_space
                    self.catmpvclaisrdistatuschangestart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIStatusTransition"):
                    self.catmpvclaisrdistatustransition = value
                    self.catmpvclaisrdistatustransition.value_namespace = name_space
                    self.catmpvclaisrdistatustransition.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclCurFailTime"):
                    self.catmpvclcurfailtime = value
                    self.catmpvclcurfailtime.value_namespace = name_space
                    self.catmpvclcurfailtime.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCStatusChangeEnd"):
                    self.catmpvclendccstatuschangeend = value
                    self.catmpvclendccstatuschangeend.value_namespace = name_space
                    self.catmpvclendccstatuschangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCStatusChangeStart"):
                    self.catmpvclendccstatuschangestart = value
                    self.catmpvclendccstatuschangestart.value_namespace = name_space
                    self.catmpvclendccstatuschangestart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCStatusTransition"):
                    self.catmpvclendccstatustransition = value
                    self.catmpvclendccstatustransition.value_namespace = name_space
                    self.catmpvclendccstatustransition.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclFailureReason"):
                    self.catmpvclfailurereason = value
                    self.catmpvclfailurereason.value_namespace = name_space
                    self.catmpvclfailurereason.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclPrevRecoverTime"):
                    self.catmpvclprevrecovertime = value
                    self.catmpvclprevrecovertime.value_namespace = name_space
                    self.catmpvclprevrecovertime.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCStatusChangeEnd"):
                    self.catmpvclsegccstatuschangeend = value
                    self.catmpvclsegccstatuschangeend.value_namespace = name_space
                    self.catmpvclsegccstatuschangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCStatusChangeStart"):
                    self.catmpvclsegccstatuschangestart = value
                    self.catmpvclsegccstatuschangestart.value_namespace = name_space
                    self.catmpvclsegccstatuschangestart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCStatusTransition"):
                    self.catmpvclsegccstatustransition = value
                    self.catmpvclsegccstatustransition.value_namespace = name_space
                    self.catmpvclsegccstatustransition.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclStatusChangeEnd"):
                    self.catmpvclstatuschangeend = value
                    self.catmpvclstatuschangeend.value_namespace = name_space
                    self.catmpvclstatuschangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclStatusChangeStart"):
                    self.catmpvclstatuschangestart = value
                    self.catmpvclstatuschangestart.value_namespace = name_space
                    self.catmpvclstatuschangestart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclStatusTransition"):
                    self.catmpvclstatustransition = value
                    self.catmpvclstatustransition.value_namespace = name_space
                    self.catmpvclstatustransition.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmcurstatchangepvclentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmcurstatchangepvclentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmCurStatChangePVclTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmCurStatChangePVclEntry"):
                for c in self.catmcurstatchangepvclentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmcurstatchangepvclentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmCurStatChangePVclEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmstatuschangepvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed in the same
        direction in the last corresponding PVC notification .
        
        .. attribute:: catmstatuschangepvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed in the same direction in the last notification  interval
        	**type**\: list of    :py:class:`Catmstatuschangepvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable, self).__init__()

            self.yang_name = "catmStatusChangePVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmstatuschangepvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable, self).__setattr__(name, value)


        class Catmstatuschangepvclrangeentry(Entity):
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
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	Index to represent different ranges, the first range is indexed by value 0, the second by 1 and so on..
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: catmpvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to Loopback OAM failure
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to Loopback OAM failure
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclrangestatuschangeend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to Loopback OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangestatuschangestart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to Loopback OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry, self).__init__()

                self.yang_name = "catmStatusChangePVclRangeEntry"
                self.yang_parent_name = "catmStatusChangePVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.int32, "catmStatusChangePVclRangeIndex")

                self.catmpvclhigherrangevalue = YLeaf(YType.int32, "catmPVclHigherRangeValue")

                self.catmpvcllowerrangevalue = YLeaf(YType.int32, "catmPVclLowerRangeValue")

                self.catmpvclrangestatuschangeend = YLeaf(YType.uint32, "catmPVclRangeStatusChangeEnd")

                self.catmpvclrangestatuschangestart = YLeaf(YType.uint32, "catmPVclRangeStatusChangeStart")

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
                                "catmstatuschangepvclrangeindex",
                                "catmpvclhigherrangevalue",
                                "catmpvcllowerrangevalue",
                                "catmpvclrangestatuschangeend",
                                "catmpvclrangestatuschangestart") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmpvclhigherrangevalue.is_set or
                    self.catmpvcllowerrangevalue.is_set or
                    self.catmpvclrangestatuschangeend.is_set or
                    self.catmpvclrangestatuschangestart.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmpvclhigherrangevalue.yfilter != YFilter.not_set or
                    self.catmpvcllowerrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclrangestatuschangeend.yfilter != YFilter.not_set or
                    self.catmpvclrangestatuschangestart.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmStatusChangePVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmStatusChangePVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmpvclhigherrangevalue.is_set or self.catmpvclhigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclhigherrangevalue.get_name_leafdata())
                if (self.catmpvcllowerrangevalue.is_set or self.catmpvcllowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvcllowerrangevalue.get_name_leafdata())
                if (self.catmpvclrangestatuschangeend.is_set or self.catmpvclrangestatuschangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclrangestatuschangeend.get_name_leafdata())
                if (self.catmpvclrangestatuschangestart.is_set or self.catmpvclrangestatuschangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclrangestatuschangestart.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPVclHigherRangeValue" or name == "catmPVclLowerRangeValue" or name == "catmPVclRangeStatusChangeEnd" or name == "catmPVclRangeStatusChangeStart"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclHigherRangeValue"):
                    self.catmpvclhigherrangevalue = value
                    self.catmpvclhigherrangevalue.value_namespace = name_space
                    self.catmpvclhigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclLowerRangeValue"):
                    self.catmpvcllowerrangevalue = value
                    self.catmpvcllowerrangevalue.value_namespace = name_space
                    self.catmpvcllowerrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclRangeStatusChangeEnd"):
                    self.catmpvclrangestatuschangeend = value
                    self.catmpvclrangestatuschangeend.value_namespace = name_space
                    self.catmpvclrangestatuschangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclRangeStatusChangeStart"):
                    self.catmpvclrangestatuschangestart = value
                    self.catmpvclrangestatuschangestart.value_namespace = name_space
                    self.catmpvclrangestatuschangestart.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmstatuschangepvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmstatuschangepvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmStatusChangePVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmStatusChangePVclRangeEntry"):
                for c in self.catmstatuschangepvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmstatuschangepvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmStatusChangePVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmsegccstatuschpvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to segment CC 
        failure in the same direction in the last PVC 
        corresponding notification .
        
        .. attribute:: catmsegccstatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to segment CC failure in the same direction  in the last corresponding notification 
        	**type**\: list of    :py:class:`Catmsegccstatuschpvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable, self).__init__()

            self.yang_name = "catmSegCCStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmsegccstatuschpvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable, self).__setattr__(name, value)


        class Catmsegccstatuschpvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to segment CC failure in the same direction 
            in the last corresponding notification .
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclsegcchigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to Segment CC OAM failure
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegcclowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to Segment CC OAM failure
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccrangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to Segment CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccrangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to Segment CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry, self).__init__()

                self.yang_name = "catmSegCCStatusChPVclRangeEntry"
                self.yang_parent_name = "catmSegCCStatusChPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclsegcchigherrangevalue = YLeaf(YType.int32, "catmPVclSegCCHigherRangeValue")

                self.catmpvclsegcclowerrangevalue = YLeaf(YType.int32, "catmPVclSegCCLowerRangeValue")

                self.catmpvclsegccrangestatuschend = YLeaf(YType.uint32, "catmPVclSegCCRangeStatusChEnd")

                self.catmpvclsegccrangestatuschstart = YLeaf(YType.uint32, "catmPVclSegCCRangeStatusChStart")

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
                                "catmstatuschangepvclrangeindex",
                                "catmpvclsegcchigherrangevalue",
                                "catmpvclsegcclowerrangevalue",
                                "catmpvclsegccrangestatuschend",
                                "catmpvclsegccrangestatuschstart") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmpvclsegcchigherrangevalue.is_set or
                    self.catmpvclsegcclowerrangevalue.is_set or
                    self.catmpvclsegccrangestatuschend.is_set or
                    self.catmpvclsegccrangestatuschstart.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmpvclsegcchigherrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclsegcclowerrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclsegccrangestatuschend.yfilter != YFilter.not_set or
                    self.catmpvclsegccrangestatuschstart.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmSegCCStatusChPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmSegCCStatusChPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmpvclsegcchigherrangevalue.is_set or self.catmpvclsegcchigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegcchigherrangevalue.get_name_leafdata())
                if (self.catmpvclsegcclowerrangevalue.is_set or self.catmpvclsegcclowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegcclowerrangevalue.get_name_leafdata())
                if (self.catmpvclsegccrangestatuschend.is_set or self.catmpvclsegccrangestatuschend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccrangestatuschend.get_name_leafdata())
                if (self.catmpvclsegccrangestatuschstart.is_set or self.catmpvclsegccrangestatuschstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccrangestatuschstart.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPVclSegCCHigherRangeValue" or name == "catmPVclSegCCLowerRangeValue" or name == "catmPVclSegCCRangeStatusChEnd" or name == "catmPVclSegCCRangeStatusChStart"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCHigherRangeValue"):
                    self.catmpvclsegcchigherrangevalue = value
                    self.catmpvclsegcchigherrangevalue.value_namespace = name_space
                    self.catmpvclsegcchigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCLowerRangeValue"):
                    self.catmpvclsegcclowerrangevalue = value
                    self.catmpvclsegcclowerrangevalue.value_namespace = name_space
                    self.catmpvclsegcclowerrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCRangeStatusChEnd"):
                    self.catmpvclsegccrangestatuschend = value
                    self.catmpvclsegccrangestatuschend.value_namespace = name_space
                    self.catmpvclsegccrangestatuschend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCRangeStatusChStart"):
                    self.catmpvclsegccrangestatuschstart = value
                    self.catmpvclsegccrangestatuschstart.value_namespace = name_space
                    self.catmpvclsegccrangestatuschstart.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmsegccstatuschpvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmsegccstatuschpvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmSegCCStatusChPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmSegCCStatusChPVclRangeEntry"):
                for c in self.catmsegccstatuschpvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmsegccstatuschpvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmSegCCStatusChPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmendccstatuschpvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to End CC failure
        in the same direction in the last PVC notification 
        interval.
        
        .. attribute:: catmendccstatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to End CC failure in the same direction in the  last corresponding notification 
        	**type**\: list of    :py:class:`Catmendccstatuschpvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable, self).__init__()

            self.yang_name = "catmEndCCStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmendccstatuschpvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable, self).__setattr__(name, value)


        class Catmendccstatuschpvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to End CC failure in the same direction in the 
            last corresponding notification .
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclendcchigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to End CC OAM failure
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendcclowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to End CC OAM failure
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccrangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to End CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccrangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to End CC OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry, self).__init__()

                self.yang_name = "catmEndCCStatusChPVclRangeEntry"
                self.yang_parent_name = "catmEndCCStatusChPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclendcchigherrangevalue = YLeaf(YType.int32, "catmPVclEndCCHigherRangeValue")

                self.catmpvclendcclowerrangevalue = YLeaf(YType.int32, "catmPVclEndCCLowerRangeValue")

                self.catmpvclendccrangestatuschend = YLeaf(YType.uint32, "catmPVclEndCCRangeStatusChEnd")

                self.catmpvclendccrangestatuschstart = YLeaf(YType.uint32, "catmPVclEndCCRangeStatusChStart")

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
                                "catmstatuschangepvclrangeindex",
                                "catmpvclendcchigherrangevalue",
                                "catmpvclendcclowerrangevalue",
                                "catmpvclendccrangestatuschend",
                                "catmpvclendccrangestatuschstart") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmpvclendcchigherrangevalue.is_set or
                    self.catmpvclendcclowerrangevalue.is_set or
                    self.catmpvclendccrangestatuschend.is_set or
                    self.catmpvclendccrangestatuschstart.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmpvclendcchigherrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclendcclowerrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclendccrangestatuschend.yfilter != YFilter.not_set or
                    self.catmpvclendccrangestatuschstart.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmEndCCStatusChPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmEndCCStatusChPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmpvclendcchigherrangevalue.is_set or self.catmpvclendcchigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendcchigherrangevalue.get_name_leafdata())
                if (self.catmpvclendcclowerrangevalue.is_set or self.catmpvclendcclowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendcclowerrangevalue.get_name_leafdata())
                if (self.catmpvclendccrangestatuschend.is_set or self.catmpvclendccrangestatuschend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccrangestatuschend.get_name_leafdata())
                if (self.catmpvclendccrangestatuschstart.is_set or self.catmpvclendccrangestatuschstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccrangestatuschstart.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPVclEndCCHigherRangeValue" or name == "catmPVclEndCCLowerRangeValue" or name == "catmPVclEndCCRangeStatusChEnd" or name == "catmPVclEndCCRangeStatusChStart"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCHigherRangeValue"):
                    self.catmpvclendcchigherrangevalue = value
                    self.catmpvclendcchigherrangevalue.value_namespace = name_space
                    self.catmpvclendcchigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCLowerRangeValue"):
                    self.catmpvclendcclowerrangevalue = value
                    self.catmpvclendcclowerrangevalue.value_namespace = name_space
                    self.catmpvclendcclowerrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCRangeStatusChEnd"):
                    self.catmpvclendccrangestatuschend = value
                    self.catmpvclendccrangestatuschend.value_namespace = name_space
                    self.catmpvclendccrangestatuschend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCRangeStatusChStart"):
                    self.catmpvclendccrangestatuschstart = value
                    self.catmpvclendccrangestatuschstart.value_namespace = name_space
                    self.catmpvclendccrangestatuschstart.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmendccstatuschpvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmendccstatuschpvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmEndCCStatusChPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmEndCCStatusChPVclRangeEntry"):
                for c in self.catmendccstatuschpvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmendccstatuschpvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmEndCCStatusChPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmaisrdistatuschpvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to AIS/RDI failure
        in the same direction in the last corresponding PVC 
        notification.
        
        .. attribute:: catmaisrdistatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to AIS/RDI failure in the same direction in the  last corresponding notification 
        	**type**\: list of    :py:class:`Catmaisrdistatuschpvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable, self).__init__()

            self.yang_name = "catmAISRDIStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmaisrdistatuschpvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable, self).__setattr__(name, value)


        class Catmaisrdistatuschpvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to AIS/RDI failure in the same direction in the 
            last corresponding notification .
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclaisrdihigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to AISRDI OAM failure
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdilowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to AISRDI OAM failure
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdirangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to AISRDI OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdirangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to AISRDI OAM failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry, self).__init__()

                self.yang_name = "catmAISRDIStatusChPVclRangeEntry"
                self.yang_parent_name = "catmAISRDIStatusChPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclaisrdihigherrangevalue = YLeaf(YType.int32, "catmPVclAISRDIHigherRangeValue")

                self.catmpvclaisrdilowerrangevalue = YLeaf(YType.int32, "catmPVclAISRDILowerRangeValue")

                self.catmpvclaisrdirangestatuschend = YLeaf(YType.uint32, "catmPVclAISRDIRangeStatusChEnd")

                self.catmpvclaisrdirangestatuschstart = YLeaf(YType.uint32, "catmPVclAISRDIRangeStatusChStart")

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
                                "catmstatuschangepvclrangeindex",
                                "catmpvclaisrdihigherrangevalue",
                                "catmpvclaisrdilowerrangevalue",
                                "catmpvclaisrdirangestatuschend",
                                "catmpvclaisrdirangestatuschstart") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmpvclaisrdihigherrangevalue.is_set or
                    self.catmpvclaisrdilowerrangevalue.is_set or
                    self.catmpvclaisrdirangestatuschend.is_set or
                    self.catmpvclaisrdirangestatuschstart.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmpvclaisrdihigherrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclaisrdilowerrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclaisrdirangestatuschend.yfilter != YFilter.not_set or
                    self.catmpvclaisrdirangestatuschstart.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmAISRDIStatusChPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmAISRDIStatusChPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmpvclaisrdihigherrangevalue.is_set or self.catmpvclaisrdihigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdihigherrangevalue.get_name_leafdata())
                if (self.catmpvclaisrdilowerrangevalue.is_set or self.catmpvclaisrdilowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdilowerrangevalue.get_name_leafdata())
                if (self.catmpvclaisrdirangestatuschend.is_set or self.catmpvclaisrdirangestatuschend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdirangestatuschend.get_name_leafdata())
                if (self.catmpvclaisrdirangestatuschstart.is_set or self.catmpvclaisrdirangestatuschstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdirangestatuschstart.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPVclAISRDIHigherRangeValue" or name == "catmPVclAISRDILowerRangeValue" or name == "catmPVclAISRDIRangeStatusChEnd" or name == "catmPVclAISRDIRangeStatusChStart"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIHigherRangeValue"):
                    self.catmpvclaisrdihigherrangevalue = value
                    self.catmpvclaisrdihigherrangevalue.value_namespace = name_space
                    self.catmpvclaisrdihigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDILowerRangeValue"):
                    self.catmpvclaisrdilowerrangevalue = value
                    self.catmpvclaisrdilowerrangevalue.value_namespace = name_space
                    self.catmpvclaisrdilowerrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIRangeStatusChEnd"):
                    self.catmpvclaisrdirangestatuschend = value
                    self.catmpvclaisrdirangestatuschend.value_namespace = name_space
                    self.catmpvclaisrdirangestatuschend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIRangeStatusChStart"):
                    self.catmpvclaisrdirangestatuschstart = value
                    self.catmpvclaisrdirangestatuschstart.value_namespace = name_space
                    self.catmpvclaisrdirangestatuschstart.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmaisrdistatuschpvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmaisrdistatuschpvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmAISRDIStatusChPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmAISRDIStatusChPVclRangeEntry"):
                for c in self.catmaisrdistatuschpvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmaisrdistatuschpvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmAISRDIStatusChPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmdownpvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have detected as Down
        in the last corresponding PVC notification .
        
        .. attribute:: catmdownpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  atmVclOperStatus to  have detected as Down in the last notification  interval
        	**type**\: list of    :py:class:`Catmdownpvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable, self).__init__()

            self.yang_name = "catmDownPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmdownpvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable, self).__setattr__(name, value)


        class Catmdownpvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
            have detected as Down in the last notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmdownpvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Down in the  corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmdownpvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Down in the  corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmdownpvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Down on any of the PVCLs in the range in the corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmdownpvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Down on any of the PVCLs in the range in the corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevuppvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Up on any of the PVCLs in the range in the previous catmIntfPvcUp2Trap notification
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevuppvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Up on any of the PVCLs in the range in the previous catmIntfPvcUp2Trap notification
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangefailurereason
            
            	Type of OAM failure
            	**type**\:   :py:class:`Catmoamfailuretype <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.Catmoamfailuretype>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry, self).__init__()

                self.yang_name = "catmDownPVclRangeEntry"
                self.yang_parent_name = "catmDownPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmdownpvclhigherrangevalue = YLeaf(YType.int32, "catmDownPVclHigherRangeValue")

                self.catmdownpvcllowerrangevalue = YLeaf(YType.int32, "catmDownPVclLowerRangeValue")

                self.catmdownpvclrangeend = YLeaf(YType.uint32, "catmDownPVclRangeEnd")

                self.catmdownpvclrangestart = YLeaf(YType.uint32, "catmDownPVclRangeStart")

                self.catmprevuppvclrangeend = YLeaf(YType.uint32, "catmPrevUpPVclRangeEnd")

                self.catmprevuppvclrangestart = YLeaf(YType.uint32, "catmPrevUpPVclRangeStart")

                self.catmpvclrangefailurereason = YLeaf(YType.enumeration, "catmPVclRangeFailureReason")

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
                                "catmstatuschangepvclrangeindex",
                                "catmdownpvclhigherrangevalue",
                                "catmdownpvcllowerrangevalue",
                                "catmdownpvclrangeend",
                                "catmdownpvclrangestart",
                                "catmprevuppvclrangeend",
                                "catmprevuppvclrangestart",
                                "catmpvclrangefailurereason") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmdownpvclhigherrangevalue.is_set or
                    self.catmdownpvcllowerrangevalue.is_set or
                    self.catmdownpvclrangeend.is_set or
                    self.catmdownpvclrangestart.is_set or
                    self.catmprevuppvclrangeend.is_set or
                    self.catmprevuppvclrangestart.is_set or
                    self.catmpvclrangefailurereason.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmdownpvclhigherrangevalue.yfilter != YFilter.not_set or
                    self.catmdownpvcllowerrangevalue.yfilter != YFilter.not_set or
                    self.catmdownpvclrangeend.yfilter != YFilter.not_set or
                    self.catmdownpvclrangestart.yfilter != YFilter.not_set or
                    self.catmprevuppvclrangeend.yfilter != YFilter.not_set or
                    self.catmprevuppvclrangestart.yfilter != YFilter.not_set or
                    self.catmpvclrangefailurereason.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmDownPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmDownPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmdownpvclhigherrangevalue.is_set or self.catmdownpvclhigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmdownpvclhigherrangevalue.get_name_leafdata())
                if (self.catmdownpvcllowerrangevalue.is_set or self.catmdownpvcllowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmdownpvcllowerrangevalue.get_name_leafdata())
                if (self.catmdownpvclrangeend.is_set or self.catmdownpvclrangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmdownpvclrangeend.get_name_leafdata())
                if (self.catmdownpvclrangestart.is_set or self.catmdownpvclrangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmdownpvclrangestart.get_name_leafdata())
                if (self.catmprevuppvclrangeend.is_set or self.catmprevuppvclrangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmprevuppvclrangeend.get_name_leafdata())
                if (self.catmprevuppvclrangestart.is_set or self.catmprevuppvclrangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmprevuppvclrangestart.get_name_leafdata())
                if (self.catmpvclrangefailurereason.is_set or self.catmpvclrangefailurereason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclrangefailurereason.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmDownPVclHigherRangeValue" or name == "catmDownPVclLowerRangeValue" or name == "catmDownPVclRangeEnd" or name == "catmDownPVclRangeStart" or name == "catmPrevUpPVclRangeEnd" or name == "catmPrevUpPVclRangeStart" or name == "catmPVclRangeFailureReason"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmDownPVclHigherRangeValue"):
                    self.catmdownpvclhigherrangevalue = value
                    self.catmdownpvclhigherrangevalue.value_namespace = name_space
                    self.catmdownpvclhigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmDownPVclLowerRangeValue"):
                    self.catmdownpvcllowerrangevalue = value
                    self.catmdownpvcllowerrangevalue.value_namespace = name_space
                    self.catmdownpvcllowerrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmDownPVclRangeEnd"):
                    self.catmdownpvclrangeend = value
                    self.catmdownpvclrangeend.value_namespace = name_space
                    self.catmdownpvclrangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmDownPVclRangeStart"):
                    self.catmdownpvclrangestart = value
                    self.catmdownpvclrangestart.value_namespace = name_space
                    self.catmdownpvclrangestart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPrevUpPVclRangeEnd"):
                    self.catmprevuppvclrangeend = value
                    self.catmprevuppvclrangeend.value_namespace = name_space
                    self.catmprevuppvclrangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPrevUpPVclRangeStart"):
                    self.catmprevuppvclrangestart = value
                    self.catmprevuppvclrangestart.value_namespace = name_space
                    self.catmprevuppvclrangestart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclRangeFailureReason"):
                    self.catmpvclrangefailurereason = value
                    self.catmpvclrangefailurereason.value_namespace = name_space
                    self.catmpvclrangefailurereason.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmdownpvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmdownpvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmDownPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmDownPVclRangeEntry"):
                for c in self.catmdownpvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmdownpvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmDownPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmcurstatusuppvcltable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed to UP
        in the last corresponding PVC notification .
        
        .. attribute:: catmcurstatusuppvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed to UP in the last PVC notification  interval
        	**type**\: list of    :py:class:`Catmcurstatusuppvclentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable, self).__init__()

            self.yang_name = "catmCurStatusUpPVclTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmcurstatusuppvclentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable, self).__setattr__(name, value)


        class Catmcurstatusuppvclentry(Entity):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed to UP in the last PVC notification 
            interval.
            
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
            
            .. attribute:: catmpvclaisrdistatusupend
            
            	The time stamp at which this PVCL changed state to Up for the last time in the last corresponding notification  due to AIS/RDI OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusupstart
            
            	The time stamp at which this PVCL changed state to Up for the first time in the last corresponding notification  due to AIS/RDI OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusuptransition
            
            	The number of Down to Up state transitions that  has happened on this PVCL in the last notification  interval due to AIS RDI OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclcurrecovertime
            
            	The time stamp at which this PVCL changed state to UP last time in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusupend
            
            	The time stamp at which this PVCL changed state to Up for the last time in the last corresponding notification  due to End CC OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusupstart
            
            	The time stamp at which this PVCL changed state to Up for the first time in the last corresponding notification  due to End CC OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusuptransition
            
            	The number of Down to UP state transitions that has  happened on this PVCL in the last notification  interval due to End CC OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclprevfailtime
            
            	The time stamp at which this PVCL changed state to DOWN last time in the previous corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrecoveryreason
            
            	Type of OAM Recovered
            	**type**\:   :py:class:`Catmoamrecoverytype <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.Catmoamrecoverytype>`
            
            .. attribute:: catmpvclsegccstatusupend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to Segment CC  OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusupstart
            
            	The time stamp at which this PVCL changed state to Up for  the first time in the last corresponding notification due to Segment CC OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusuptransition
            
            	The number of Down to Up state transitions that has  happened on this PVCL in the last corresponding notification  due to Segment CC OAM recovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusupend
            
            	The time stamp at which this PVCL changed state to UP  for the last time due to OAM loopback recovery in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusupstart
            
            	The time stamp at which this PVCL changed state to UP  for the first time due to OAM loopback recovery in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusuptransition
            
            	The number of Down to Up state transitions due to OAM loopback recovery that has happened on this PVCL  in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry, self).__init__()

                self.yang_name = "catmCurStatusUpPVclEntry"
                self.yang_parent_name = "catmCurStatusUpPVclTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.catmpvclaisrdistatusupend = YLeaf(YType.uint32, "catmPVclAISRDIStatusUpEnd")

                self.catmpvclaisrdistatusupstart = YLeaf(YType.uint32, "catmPVclAISRDIStatusUpStart")

                self.catmpvclaisrdistatusuptransition = YLeaf(YType.uint32, "catmPVclAISRDIStatusUpTransition")

                self.catmpvclcurrecovertime = YLeaf(YType.uint32, "catmPVclCurRecoverTime")

                self.catmpvclendccstatusupend = YLeaf(YType.uint32, "catmPVclEndCCStatusUpEnd")

                self.catmpvclendccstatusupstart = YLeaf(YType.uint32, "catmPVclEndCCStatusUpStart")

                self.catmpvclendccstatusuptransition = YLeaf(YType.uint32, "catmPVclEndCCStatusUpTransition")

                self.catmpvclprevfailtime = YLeaf(YType.uint32, "catmPVclPrevFailTime")

                self.catmpvclrecoveryreason = YLeaf(YType.enumeration, "catmPVclRecoveryReason")

                self.catmpvclsegccstatusupend = YLeaf(YType.uint32, "catmPVclSegCCStatusUpEnd")

                self.catmpvclsegccstatusupstart = YLeaf(YType.uint32, "catmPVclSegCCStatusUpStart")

                self.catmpvclsegccstatusuptransition = YLeaf(YType.uint32, "catmPVclSegCCStatusUpTransition")

                self.catmpvclstatusupend = YLeaf(YType.uint32, "catmPVclStatusUpEnd")

                self.catmpvclstatusupstart = YLeaf(YType.uint32, "catmPVclStatusUpStart")

                self.catmpvclstatusuptransition = YLeaf(YType.uint32, "catmPVclStatusUpTransition")

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
                                "catmpvclaisrdistatusupend",
                                "catmpvclaisrdistatusupstart",
                                "catmpvclaisrdistatusuptransition",
                                "catmpvclcurrecovertime",
                                "catmpvclendccstatusupend",
                                "catmpvclendccstatusupstart",
                                "catmpvclendccstatusuptransition",
                                "catmpvclprevfailtime",
                                "catmpvclrecoveryreason",
                                "catmpvclsegccstatusupend",
                                "catmpvclsegccstatusupstart",
                                "catmpvclsegccstatusuptransition",
                                "catmpvclstatusupend",
                                "catmpvclstatusupstart",
                                "catmpvclstatusuptransition") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.atmvclvci.is_set or
                    self.catmpvclaisrdistatusupend.is_set or
                    self.catmpvclaisrdistatusupstart.is_set or
                    self.catmpvclaisrdistatusuptransition.is_set or
                    self.catmpvclcurrecovertime.is_set or
                    self.catmpvclendccstatusupend.is_set or
                    self.catmpvclendccstatusupstart.is_set or
                    self.catmpvclendccstatusuptransition.is_set or
                    self.catmpvclprevfailtime.is_set or
                    self.catmpvclrecoveryreason.is_set or
                    self.catmpvclsegccstatusupend.is_set or
                    self.catmpvclsegccstatusupstart.is_set or
                    self.catmpvclsegccstatusuptransition.is_set or
                    self.catmpvclstatusupend.is_set or
                    self.catmpvclstatusupstart.is_set or
                    self.catmpvclstatusuptransition.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.atmvclvci.yfilter != YFilter.not_set or
                    self.catmpvclaisrdistatusupend.yfilter != YFilter.not_set or
                    self.catmpvclaisrdistatusupstart.yfilter != YFilter.not_set or
                    self.catmpvclaisrdistatusuptransition.yfilter != YFilter.not_set or
                    self.catmpvclcurrecovertime.yfilter != YFilter.not_set or
                    self.catmpvclendccstatusupend.yfilter != YFilter.not_set or
                    self.catmpvclendccstatusupstart.yfilter != YFilter.not_set or
                    self.catmpvclendccstatusuptransition.yfilter != YFilter.not_set or
                    self.catmpvclprevfailtime.yfilter != YFilter.not_set or
                    self.catmpvclrecoveryreason.yfilter != YFilter.not_set or
                    self.catmpvclsegccstatusupend.yfilter != YFilter.not_set or
                    self.catmpvclsegccstatusupstart.yfilter != YFilter.not_set or
                    self.catmpvclsegccstatusuptransition.yfilter != YFilter.not_set or
                    self.catmpvclstatusupend.yfilter != YFilter.not_set or
                    self.catmpvclstatusupstart.yfilter != YFilter.not_set or
                    self.catmpvclstatusuptransition.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmCurStatusUpPVclEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmCurStatusUpPVclTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.atmvclvci.is_set or self.atmvclvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvci.get_name_leafdata())
                if (self.catmpvclaisrdistatusupend.is_set or self.catmpvclaisrdistatusupend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdistatusupend.get_name_leafdata())
                if (self.catmpvclaisrdistatusupstart.is_set or self.catmpvclaisrdistatusupstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdistatusupstart.get_name_leafdata())
                if (self.catmpvclaisrdistatusuptransition.is_set or self.catmpvclaisrdistatusuptransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdistatusuptransition.get_name_leafdata())
                if (self.catmpvclcurrecovertime.is_set or self.catmpvclcurrecovertime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclcurrecovertime.get_name_leafdata())
                if (self.catmpvclendccstatusupend.is_set or self.catmpvclendccstatusupend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccstatusupend.get_name_leafdata())
                if (self.catmpvclendccstatusupstart.is_set or self.catmpvclendccstatusupstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccstatusupstart.get_name_leafdata())
                if (self.catmpvclendccstatusuptransition.is_set or self.catmpvclendccstatusuptransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccstatusuptransition.get_name_leafdata())
                if (self.catmpvclprevfailtime.is_set or self.catmpvclprevfailtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclprevfailtime.get_name_leafdata())
                if (self.catmpvclrecoveryreason.is_set or self.catmpvclrecoveryreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclrecoveryreason.get_name_leafdata())
                if (self.catmpvclsegccstatusupend.is_set or self.catmpvclsegccstatusupend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccstatusupend.get_name_leafdata())
                if (self.catmpvclsegccstatusupstart.is_set or self.catmpvclsegccstatusupstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccstatusupstart.get_name_leafdata())
                if (self.catmpvclsegccstatusuptransition.is_set or self.catmpvclsegccstatusuptransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccstatusuptransition.get_name_leafdata())
                if (self.catmpvclstatusupend.is_set or self.catmpvclstatusupend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclstatusupend.get_name_leafdata())
                if (self.catmpvclstatusupstart.is_set or self.catmpvclstatusupstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclstatusupstart.get_name_leafdata())
                if (self.catmpvclstatusuptransition.is_set or self.catmpvclstatusuptransition.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclstatusuptransition.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "atmVclVci" or name == "catmPVclAISRDIStatusUpEnd" or name == "catmPVclAISRDIStatusUpStart" or name == "catmPVclAISRDIStatusUpTransition" or name == "catmPVclCurRecoverTime" or name == "catmPVclEndCCStatusUpEnd" or name == "catmPVclEndCCStatusUpStart" or name == "catmPVclEndCCStatusUpTransition" or name == "catmPVclPrevFailTime" or name == "catmPVclRecoveryReason" or name == "catmPVclSegCCStatusUpEnd" or name == "catmPVclSegCCStatusUpStart" or name == "catmPVclSegCCStatusUpTransition" or name == "catmPVclStatusUpEnd" or name == "catmPVclStatusUpStart" or name == "catmPVclStatusUpTransition"):
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
                if(value_path == "catmPVclAISRDIStatusUpEnd"):
                    self.catmpvclaisrdistatusupend = value
                    self.catmpvclaisrdistatusupend.value_namespace = name_space
                    self.catmpvclaisrdistatusupend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIStatusUpStart"):
                    self.catmpvclaisrdistatusupstart = value
                    self.catmpvclaisrdistatusupstart.value_namespace = name_space
                    self.catmpvclaisrdistatusupstart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIStatusUpTransition"):
                    self.catmpvclaisrdistatusuptransition = value
                    self.catmpvclaisrdistatusuptransition.value_namespace = name_space
                    self.catmpvclaisrdistatusuptransition.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclCurRecoverTime"):
                    self.catmpvclcurrecovertime = value
                    self.catmpvclcurrecovertime.value_namespace = name_space
                    self.catmpvclcurrecovertime.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCStatusUpEnd"):
                    self.catmpvclendccstatusupend = value
                    self.catmpvclendccstatusupend.value_namespace = name_space
                    self.catmpvclendccstatusupend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCStatusUpStart"):
                    self.catmpvclendccstatusupstart = value
                    self.catmpvclendccstatusupstart.value_namespace = name_space
                    self.catmpvclendccstatusupstart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCStatusUpTransition"):
                    self.catmpvclendccstatusuptransition = value
                    self.catmpvclendccstatusuptransition.value_namespace = name_space
                    self.catmpvclendccstatusuptransition.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclPrevFailTime"):
                    self.catmpvclprevfailtime = value
                    self.catmpvclprevfailtime.value_namespace = name_space
                    self.catmpvclprevfailtime.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclRecoveryReason"):
                    self.catmpvclrecoveryreason = value
                    self.catmpvclrecoveryreason.value_namespace = name_space
                    self.catmpvclrecoveryreason.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCStatusUpEnd"):
                    self.catmpvclsegccstatusupend = value
                    self.catmpvclsegccstatusupend.value_namespace = name_space
                    self.catmpvclsegccstatusupend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCStatusUpStart"):
                    self.catmpvclsegccstatusupstart = value
                    self.catmpvclsegccstatusupstart.value_namespace = name_space
                    self.catmpvclsegccstatusupstart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCStatusUpTransition"):
                    self.catmpvclsegccstatusuptransition = value
                    self.catmpvclsegccstatusuptransition.value_namespace = name_space
                    self.catmpvclsegccstatusuptransition.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclStatusUpEnd"):
                    self.catmpvclstatusupend = value
                    self.catmpvclstatusupend.value_namespace = name_space
                    self.catmpvclstatusupend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclStatusUpStart"):
                    self.catmpvclstatusupstart = value
                    self.catmpvclstatusupstart.value_namespace = name_space
                    self.catmpvclstatusupstart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclStatusUpTransition"):
                    self.catmpvclstatusuptransition = value
                    self.catmpvclstatusuptransition.value_namespace = name_space
                    self.catmpvclstatusuptransition.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmcurstatusuppvclentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmcurstatusuppvclentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmCurStatusUpPVclTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmCurStatusUpPVclEntry"):
                for c in self.catmcurstatusuppvclentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmcurstatusuppvclentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmCurStatusUpPVclEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmstatusuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and loopback OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  loopback OAM status to  have detected as recovered in the last notification  interval
        	**type**\: list of    :py:class:`Catmstatusuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable, self).__init__()

            self.yang_name = "catmStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmstatusuppvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable, self).__setattr__(name, value)


        class Catmstatusuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  loopback OAM status to 
            have detected as recovered in the last notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclrangestatusupend
            
            	The time stamp at which the last Loopback OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangestatusupstart
            
            	The time stamp at which the first Loopback OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvcluphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  Loopback OAM recovery has been detected in the last  corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvcluplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  Loopback OAM recovery has been detected in the last  corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry, self).__init__()

                self.yang_name = "catmStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmStatusUpPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclrangestatusupend = YLeaf(YType.uint32, "catmPVclRangeStatusUpEnd")

                self.catmpvclrangestatusupstart = YLeaf(YType.uint32, "catmPVclRangeStatusUpStart")

                self.catmpvcluphigherrangevalue = YLeaf(YType.int32, "catmPVclUpHigherRangeValue")

                self.catmpvcluplowerrangevalue = YLeaf(YType.int32, "catmPVclUpLowerRangeValue")

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
                                "catmstatuschangepvclrangeindex",
                                "catmpvclrangestatusupend",
                                "catmpvclrangestatusupstart",
                                "catmpvcluphigherrangevalue",
                                "catmpvcluplowerrangevalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmpvclrangestatusupend.is_set or
                    self.catmpvclrangestatusupstart.is_set or
                    self.catmpvcluphigherrangevalue.is_set or
                    self.catmpvcluplowerrangevalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmpvclrangestatusupend.yfilter != YFilter.not_set or
                    self.catmpvclrangestatusupstart.yfilter != YFilter.not_set or
                    self.catmpvcluphigherrangevalue.yfilter != YFilter.not_set or
                    self.catmpvcluplowerrangevalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmStatusUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmStatusUpPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmpvclrangestatusupend.is_set or self.catmpvclrangestatusupend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclrangestatusupend.get_name_leafdata())
                if (self.catmpvclrangestatusupstart.is_set or self.catmpvclrangestatusupstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclrangestatusupstart.get_name_leafdata())
                if (self.catmpvcluphigherrangevalue.is_set or self.catmpvcluphigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvcluphigherrangevalue.get_name_leafdata())
                if (self.catmpvcluplowerrangevalue.is_set or self.catmpvcluplowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvcluplowerrangevalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPVclRangeStatusUpEnd" or name == "catmPVclRangeStatusUpStart" or name == "catmPVclUpHigherRangeValue" or name == "catmPVclUpLowerRangeValue"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclRangeStatusUpEnd"):
                    self.catmpvclrangestatusupend = value
                    self.catmpvclrangestatusupend.value_namespace = name_space
                    self.catmpvclrangestatusupend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclRangeStatusUpStart"):
                    self.catmpvclrangestatusupstart = value
                    self.catmpvclrangestatusupstart.value_namespace = name_space
                    self.catmpvclrangestatusupstart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclUpHigherRangeValue"):
                    self.catmpvcluphigherrangevalue = value
                    self.catmpvcluphigherrangevalue.value_namespace = name_space
                    self.catmpvcluphigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclUpLowerRangeValue"):
                    self.catmpvcluplowerrangevalue = value
                    self.catmpvcluplowerrangevalue.value_namespace = name_space
                    self.catmpvcluplowerrangevalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmstatusuppvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmstatusuppvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmStatusUpPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmStatusUpPVclRangeEntry"):
                for c in self.catmstatusuppvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmstatusuppvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmStatusUpPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmsegccstatusuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and Segment CC OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmsegccstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and Segment CC OAM status to have detected as recovered in the last notification interval
        	**type**\: list of    :py:class:`Catmsegccstatusuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable, self).__init__()

            self.yang_name = "catmSegCCStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmsegccstatusuppvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable, self).__setattr__(name, value)


        class Catmsegccstatusuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and Segment CC OAM status to
            have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclsegccrangestatusupend
            
            	The time stamp at which the last Segment CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccrangestatusupstart
            
            	The time stamp at which the first Segment CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the Segment CC OAM recovery has been detected in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the Segment CC OAM recovery has been detected in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry, self).__init__()

                self.yang_name = "catmSegCCStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmSegCCStatusUpPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclsegccrangestatusupend = YLeaf(YType.uint32, "catmPVclSegCCRangeStatusUpEnd")

                self.catmpvclsegccrangestatusupstart = YLeaf(YType.uint32, "catmPVclSegCCRangeStatusUpStart")

                self.catmpvclsegccuphigherrangevalue = YLeaf(YType.int32, "catmPVclSegCCUpHigherRangeValue")

                self.catmpvclsegccuplowerrangevalue = YLeaf(YType.int32, "catmPVclSegCCUpLowerRangeValue")

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
                                "catmstatuschangepvclrangeindex",
                                "catmpvclsegccrangestatusupend",
                                "catmpvclsegccrangestatusupstart",
                                "catmpvclsegccuphigherrangevalue",
                                "catmpvclsegccuplowerrangevalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmpvclsegccrangestatusupend.is_set or
                    self.catmpvclsegccrangestatusupstart.is_set or
                    self.catmpvclsegccuphigherrangevalue.is_set or
                    self.catmpvclsegccuplowerrangevalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmpvclsegccrangestatusupend.yfilter != YFilter.not_set or
                    self.catmpvclsegccrangestatusupstart.yfilter != YFilter.not_set or
                    self.catmpvclsegccuphigherrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclsegccuplowerrangevalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmSegCCStatusUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmSegCCStatusUpPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmpvclsegccrangestatusupend.is_set or self.catmpvclsegccrangestatusupend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccrangestatusupend.get_name_leafdata())
                if (self.catmpvclsegccrangestatusupstart.is_set or self.catmpvclsegccrangestatusupstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccrangestatusupstart.get_name_leafdata())
                if (self.catmpvclsegccuphigherrangevalue.is_set or self.catmpvclsegccuphigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccuphigherrangevalue.get_name_leafdata())
                if (self.catmpvclsegccuplowerrangevalue.is_set or self.catmpvclsegccuplowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclsegccuplowerrangevalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPVclSegCCRangeStatusUpEnd" or name == "catmPVclSegCCRangeStatusUpStart" or name == "catmPVclSegCCUpHigherRangeValue" or name == "catmPVclSegCCUpLowerRangeValue"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCRangeStatusUpEnd"):
                    self.catmpvclsegccrangestatusupend = value
                    self.catmpvclsegccrangestatusupend.value_namespace = name_space
                    self.catmpvclsegccrangestatusupend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCRangeStatusUpStart"):
                    self.catmpvclsegccrangestatusupstart = value
                    self.catmpvclsegccrangestatusupstart.value_namespace = name_space
                    self.catmpvclsegccrangestatusupstart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCUpHigherRangeValue"):
                    self.catmpvclsegccuphigherrangevalue = value
                    self.catmpvclsegccuphigherrangevalue.value_namespace = name_space
                    self.catmpvclsegccuphigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclSegCCUpLowerRangeValue"):
                    self.catmpvclsegccuplowerrangevalue = value
                    self.catmpvclsegccuplowerrangevalue.value_namespace = name_space
                    self.catmpvclsegccuplowerrangevalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmsegccstatusuppvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmsegccstatusuppvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmSegCCStatusUpPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmSegCCStatusUpPVclRangeEntry"):
                for c in self.catmsegccstatusuppvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmsegccstatusuppvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmSegCCStatusUpPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmendccstatusuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and End\-to\-End CC OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmendccstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and End\-to\-End CC OAM status  to have detected as recovered in the last notification interval
        	**type**\: list of    :py:class:`Catmendccstatusuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable, self).__init__()

            self.yang_name = "catmEndCCStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmendccstatusuppvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable, self).__setattr__(name, value)


        class Catmendccstatusuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and End\-to\-End CC OAM status 
            to have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclendccrangestatusupend
            
            	The time stamp at which the last End\-to\-End CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccrangestatusupstart
            
            	The time stamp at which the first End\-to\-End CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the End\-to\-End CC OAM recovery has been detected in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the End\-to\-End CC OAM recovery has been detected in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry, self).__init__()

                self.yang_name = "catmEndCCStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmEndCCStatusUpPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclendccrangestatusupend = YLeaf(YType.uint32, "catmPVclEndCCRangeStatusUpEnd")

                self.catmpvclendccrangestatusupstart = YLeaf(YType.uint32, "catmPVclEndCCRangeStatusUpStart")

                self.catmpvclendccuphigherrangevalue = YLeaf(YType.int32, "catmPVclEndCCUpHigherRangeValue")

                self.catmpvclendccuplowerrangevalue = YLeaf(YType.int32, "catmPVclEndCCUpLowerRangeValue")

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
                                "catmstatuschangepvclrangeindex",
                                "catmpvclendccrangestatusupend",
                                "catmpvclendccrangestatusupstart",
                                "catmpvclendccuphigherrangevalue",
                                "catmpvclendccuplowerrangevalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmpvclendccrangestatusupend.is_set or
                    self.catmpvclendccrangestatusupstart.is_set or
                    self.catmpvclendccuphigherrangevalue.is_set or
                    self.catmpvclendccuplowerrangevalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmpvclendccrangestatusupend.yfilter != YFilter.not_set or
                    self.catmpvclendccrangestatusupstart.yfilter != YFilter.not_set or
                    self.catmpvclendccuphigherrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclendccuplowerrangevalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmEndCCStatusUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmEndCCStatusUpPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmpvclendccrangestatusupend.is_set or self.catmpvclendccrangestatusupend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccrangestatusupend.get_name_leafdata())
                if (self.catmpvclendccrangestatusupstart.is_set or self.catmpvclendccrangestatusupstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccrangestatusupstart.get_name_leafdata())
                if (self.catmpvclendccuphigherrangevalue.is_set or self.catmpvclendccuphigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccuphigherrangevalue.get_name_leafdata())
                if (self.catmpvclendccuplowerrangevalue.is_set or self.catmpvclendccuplowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclendccuplowerrangevalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPVclEndCCRangeStatusUpEnd" or name == "catmPVclEndCCRangeStatusUpStart" or name == "catmPVclEndCCUpHigherRangeValue" or name == "catmPVclEndCCUpLowerRangeValue"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCRangeStatusUpEnd"):
                    self.catmpvclendccrangestatusupend = value
                    self.catmpvclendccrangestatusupend.value_namespace = name_space
                    self.catmpvclendccrangestatusupend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCRangeStatusUpStart"):
                    self.catmpvclendccrangestatusupstart = value
                    self.catmpvclendccrangestatusupstart.value_namespace = name_space
                    self.catmpvclendccrangestatusupstart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCUpHigherRangeValue"):
                    self.catmpvclendccuphigherrangevalue = value
                    self.catmpvclendccuphigherrangevalue.value_namespace = name_space
                    self.catmpvclendccuphigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclEndCCUpLowerRangeValue"):
                    self.catmpvclendccuplowerrangevalue = value
                    self.catmpvclendccuplowerrangevalue.value_namespace = name_space
                    self.catmpvclendccuplowerrangevalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmendccstatusuppvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmendccstatusuppvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmEndCCStatusUpPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmEndCCStatusUpPVclRangeEntry"):
                for c in self.catmendccstatusuppvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmendccstatusuppvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmEndCCStatusUpPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmaisrdistatusuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and AISRDI OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmaisrdistatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and AISRDI OAM status  to have detected as recovered in the last notification interval
        	**type**\: list of    :py:class:`Catmaisrdistatusuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable, self).__init__()

            self.yang_name = "catmAISRDIStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmaisrdistatusuppvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable, self).__setattr__(name, value)


        class Catmaisrdistatusuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and AISRDI OAM status 
            to have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclaisrdirangestatusupend
            
            	The time stamp at which the last AISRDI OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdirangestatusupstart
            
            	The time stamp at which the first AISRDI OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdiuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the AISRDI OAM recovery has been detected in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdiuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the AISRDI OAM recovery has been detected in the last corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry, self).__init__()

                self.yang_name = "catmAISRDIStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmAISRDIStatusUpPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclaisrdirangestatusupend = YLeaf(YType.uint32, "catmPVclAISRDIRangeStatusUpEnd")

                self.catmpvclaisrdirangestatusupstart = YLeaf(YType.uint32, "catmPVclAISRDIRangeStatusUpStart")

                self.catmpvclaisrdiuphigherrangevalue = YLeaf(YType.int32, "catmPVclAISRDIUpHigherRangeValue")

                self.catmpvclaisrdiuplowerrangevalue = YLeaf(YType.int32, "catmPVclAISRDIUpLowerRangeValue")

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
                                "catmstatuschangepvclrangeindex",
                                "catmpvclaisrdirangestatusupend",
                                "catmpvclaisrdirangestatusupstart",
                                "catmpvclaisrdiuphigherrangevalue",
                                "catmpvclaisrdiuplowerrangevalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmpvclaisrdirangestatusupend.is_set or
                    self.catmpvclaisrdirangestatusupstart.is_set or
                    self.catmpvclaisrdiuphigherrangevalue.is_set or
                    self.catmpvclaisrdiuplowerrangevalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmpvclaisrdirangestatusupend.yfilter != YFilter.not_set or
                    self.catmpvclaisrdirangestatusupstart.yfilter != YFilter.not_set or
                    self.catmpvclaisrdiuphigherrangevalue.yfilter != YFilter.not_set or
                    self.catmpvclaisrdiuplowerrangevalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmAISRDIStatusUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmAISRDIStatusUpPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmpvclaisrdirangestatusupend.is_set or self.catmpvclaisrdirangestatusupend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdirangestatusupend.get_name_leafdata())
                if (self.catmpvclaisrdirangestatusupstart.is_set or self.catmpvclaisrdirangestatusupstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdirangestatusupstart.get_name_leafdata())
                if (self.catmpvclaisrdiuphigherrangevalue.is_set or self.catmpvclaisrdiuphigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdiuphigherrangevalue.get_name_leafdata())
                if (self.catmpvclaisrdiuplowerrangevalue.is_set or self.catmpvclaisrdiuplowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclaisrdiuplowerrangevalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPVclAISRDIRangeStatusUpEnd" or name == "catmPVclAISRDIRangeStatusUpStart" or name == "catmPVclAISRDIUpHigherRangeValue" or name == "catmPVclAISRDIUpLowerRangeValue"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIRangeStatusUpEnd"):
                    self.catmpvclaisrdirangestatusupend = value
                    self.catmpvclaisrdirangestatusupend.value_namespace = name_space
                    self.catmpvclaisrdirangestatusupend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIRangeStatusUpStart"):
                    self.catmpvclaisrdirangestatusupstart = value
                    self.catmpvclaisrdirangestatusupstart.value_namespace = name_space
                    self.catmpvclaisrdirangestatusupstart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIUpHigherRangeValue"):
                    self.catmpvclaisrdiuphigherrangevalue = value
                    self.catmpvclaisrdiuphigherrangevalue.value_namespace = name_space
                    self.catmpvclaisrdiuphigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclAISRDIUpLowerRangeValue"):
                    self.catmpvclaisrdiuplowerrangevalue = value
                    self.catmpvclaisrdiuplowerrangevalue.value_namespace = name_space
                    self.catmpvclaisrdiuplowerrangevalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmaisrdistatusuppvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmaisrdistatusuppvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmAISRDIStatusUpPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmAISRDIStatusUpPVclRangeEntry"):
                for c in self.catmaisrdistatusuppvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmaisrdistatusuppvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmAISRDIStatusUpPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Catmuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have detected as Up
        in the last corresponding PVC notification .
        
        .. attribute:: catmuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  atmVclOperStatus to  have detected as Up in the last notification  interval
        	**type**\: list of    :py:class:`Catmuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CiscoAtmPvctrapExtnMib.Catmuppvclrangetable, self).__init__()

            self.yang_name = "catmUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"

            self.catmuppvclrangeentry = YList(self)

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
                        super(CiscoAtmPvctrapExtnMib.Catmuppvclrangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmPvctrapExtnMib.Catmuppvclrangetable, self).__setattr__(name, value)


        class Catmuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
            have detected as Up in the last notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmprevdownpvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Down on any of the PVCLs in the range in the previous catmIntfPvcDownTrap notification
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevdownpvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Down on any of the PVCLs in the range in the previous catmIntfPvcDownTrap notification
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangerecoveryreason
            
            	Type of OAM Recovered
            	**type**\:   :py:class:`Catmoamrecoverytype <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.Catmoamrecoverytype>`
            
            .. attribute:: catmuppvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Up in the  corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmuppvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Up in the  corresponding notification 
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: catmuppvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Up on any of the PVCLs in the range in the corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmuppvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Up on any of the PVCLs in the range in the corresponding notification 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry, self).__init__()

                self.yang_name = "catmUpPVclRangeEntry"
                self.yang_parent_name = "catmUpPVclRangeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmprevdownpvclrangeend = YLeaf(YType.uint32, "catmPrevDownPVclRangeEnd")

                self.catmprevdownpvclrangestart = YLeaf(YType.uint32, "catmPrevDownPVclRangeStart")

                self.catmpvclrangerecoveryreason = YLeaf(YType.enumeration, "catmPVclRangeRecoveryReason")

                self.catmuppvclhigherrangevalue = YLeaf(YType.int32, "catmUpPVclHigherRangeValue")

                self.catmuppvcllowerrangevalue = YLeaf(YType.int32, "catmUpPVclLowerRangeValue")

                self.catmuppvclrangeend = YLeaf(YType.uint32, "catmUpPVclRangeEnd")

                self.catmuppvclrangestart = YLeaf(YType.uint32, "catmUpPVclRangeStart")

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
                                "catmstatuschangepvclrangeindex",
                                "catmprevdownpvclrangeend",
                                "catmprevdownpvclrangestart",
                                "catmpvclrangerecoveryreason",
                                "catmuppvclhigherrangevalue",
                                "catmuppvcllowerrangevalue",
                                "catmuppvclrangeend",
                                "catmuppvclrangestart") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.catmstatuschangepvclrangeindex.is_set or
                    self.catmprevdownpvclrangeend.is_set or
                    self.catmprevdownpvclrangestart.is_set or
                    self.catmpvclrangerecoveryreason.is_set or
                    self.catmuppvclhigherrangevalue.is_set or
                    self.catmuppvcllowerrangevalue.is_set or
                    self.catmuppvclrangeend.is_set or
                    self.catmuppvclrangestart.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set or
                    self.catmprevdownpvclrangeend.yfilter != YFilter.not_set or
                    self.catmprevdownpvclrangestart.yfilter != YFilter.not_set or
                    self.catmpvclrangerecoveryreason.yfilter != YFilter.not_set or
                    self.catmuppvclhigherrangevalue.yfilter != YFilter.not_set or
                    self.catmuppvcllowerrangevalue.yfilter != YFilter.not_set or
                    self.catmuppvclrangeend.yfilter != YFilter.not_set or
                    self.catmuppvclrangestart.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "catmUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmUpPVclRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.catmstatuschangepvclrangeindex.is_set or self.catmstatuschangepvclrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmstatuschangepvclrangeindex.get_name_leafdata())
                if (self.catmprevdownpvclrangeend.is_set or self.catmprevdownpvclrangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmprevdownpvclrangeend.get_name_leafdata())
                if (self.catmprevdownpvclrangestart.is_set or self.catmprevdownpvclrangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmprevdownpvclrangestart.get_name_leafdata())
                if (self.catmpvclrangerecoveryreason.is_set or self.catmpvclrangerecoveryreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmpvclrangerecoveryreason.get_name_leafdata())
                if (self.catmuppvclhigherrangevalue.is_set or self.catmuppvclhigherrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmuppvclhigherrangevalue.get_name_leafdata())
                if (self.catmuppvcllowerrangevalue.is_set or self.catmuppvcllowerrangevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmuppvcllowerrangevalue.get_name_leafdata())
                if (self.catmuppvclrangeend.is_set or self.catmuppvclrangeend.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmuppvclrangeend.get_name_leafdata())
                if (self.catmuppvclrangestart.is_set or self.catmuppvclrangestart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmuppvclrangestart.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "catmStatusChangePVclRangeIndex" or name == "catmPrevDownPVclRangeEnd" or name == "catmPrevDownPVclRangeStart" or name == "catmPVclRangeRecoveryReason" or name == "catmUpPVclHigherRangeValue" or name == "catmUpPVclLowerRangeValue" or name == "catmUpPVclRangeEnd" or name == "catmUpPVclRangeStart"):
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
                if(value_path == "catmStatusChangePVclRangeIndex"):
                    self.catmstatuschangepvclrangeindex = value
                    self.catmstatuschangepvclrangeindex.value_namespace = name_space
                    self.catmstatuschangepvclrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPrevDownPVclRangeEnd"):
                    self.catmprevdownpvclrangeend = value
                    self.catmprevdownpvclrangeend.value_namespace = name_space
                    self.catmprevdownpvclrangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPrevDownPVclRangeStart"):
                    self.catmprevdownpvclrangestart = value
                    self.catmprevdownpvclrangestart.value_namespace = name_space
                    self.catmprevdownpvclrangestart.value_namespace_prefix = name_space_prefix
                if(value_path == "catmPVclRangeRecoveryReason"):
                    self.catmpvclrangerecoveryreason = value
                    self.catmpvclrangerecoveryreason.value_namespace = name_space
                    self.catmpvclrangerecoveryreason.value_namespace_prefix = name_space_prefix
                if(value_path == "catmUpPVclHigherRangeValue"):
                    self.catmuppvclhigherrangevalue = value
                    self.catmuppvclhigherrangevalue.value_namespace = name_space
                    self.catmuppvclhigherrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmUpPVclLowerRangeValue"):
                    self.catmuppvcllowerrangevalue = value
                    self.catmuppvcllowerrangevalue.value_namespace = name_space
                    self.catmuppvcllowerrangevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "catmUpPVclRangeEnd"):
                    self.catmuppvclrangeend = value
                    self.catmuppvclrangeend.value_namespace = name_space
                    self.catmuppvclrangeend.value_namespace_prefix = name_space_prefix
                if(value_path == "catmUpPVclRangeStart"):
                    self.catmuppvclrangestart = value
                    self.catmuppvclrangestart.value_namespace = name_space
                    self.catmuppvclrangestart.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.catmuppvclrangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.catmuppvclrangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "catmUpPVclRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "catmUpPVclRangeEntry"):
                for c in self.catmuppvclrangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.catmuppvclrangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "catmUpPVclRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.catmaisrdistatuschpvclrangetable is not None and self.catmaisrdistatuschpvclrangetable.has_data()) or
            (self.catmaisrdistatusuppvclrangetable is not None and self.catmaisrdistatusuppvclrangetable.has_data()) or
            (self.catmcurstatchangepvcltable is not None and self.catmcurstatchangepvcltable.has_data()) or
            (self.catmcurstatusuppvcltable is not None and self.catmcurstatusuppvcltable.has_data()) or
            (self.catmdownpvclrangetable is not None and self.catmdownpvclrangetable.has_data()) or
            (self.catmendccstatuschpvclrangetable is not None and self.catmendccstatuschpvclrangetable.has_data()) or
            (self.catmendccstatusuppvclrangetable is not None and self.catmendccstatusuppvclrangetable.has_data()) or
            (self.catmsegccstatuschpvclrangetable is not None and self.catmsegccstatuschpvclrangetable.has_data()) or
            (self.catmsegccstatusuppvclrangetable is not None and self.catmsegccstatusuppvclrangetable.has_data()) or
            (self.catmstatuschangepvclrangetable is not None and self.catmstatuschangepvclrangetable.has_data()) or
            (self.catmstatusuppvclrangetable is not None and self.catmstatusuppvclrangetable.has_data()) or
            (self.catmuppvclrangetable is not None and self.catmuppvclrangetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.catmaisrdistatuschpvclrangetable is not None and self.catmaisrdistatuschpvclrangetable.has_operation()) or
            (self.catmaisrdistatusuppvclrangetable is not None and self.catmaisrdistatusuppvclrangetable.has_operation()) or
            (self.catmcurstatchangepvcltable is not None and self.catmcurstatchangepvcltable.has_operation()) or
            (self.catmcurstatusuppvcltable is not None and self.catmcurstatusuppvcltable.has_operation()) or
            (self.catmdownpvclrangetable is not None and self.catmdownpvclrangetable.has_operation()) or
            (self.catmendccstatuschpvclrangetable is not None and self.catmendccstatuschpvclrangetable.has_operation()) or
            (self.catmendccstatusuppvclrangetable is not None and self.catmendccstatusuppvclrangetable.has_operation()) or
            (self.catmsegccstatuschpvclrangetable is not None and self.catmsegccstatuschpvclrangetable.has_operation()) or
            (self.catmsegccstatusuppvclrangetable is not None and self.catmsegccstatusuppvclrangetable.has_operation()) or
            (self.catmstatuschangepvclrangetable is not None and self.catmstatuschangepvclrangetable.has_operation()) or
            (self.catmstatusuppvclrangetable is not None and self.catmstatusuppvclrangetable.has_operation()) or
            (self.catmuppvclrangetable is not None and self.catmuppvclrangetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB" + path_buffer

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

        if (child_yang_name == "catmAISRDIStatusChPVclRangeTable"):
            if (self.catmaisrdistatuschpvclrangetable is None):
                self.catmaisrdistatuschpvclrangetable = CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable()
                self.catmaisrdistatuschpvclrangetable.parent = self
                self._children_name_map["catmaisrdistatuschpvclrangetable"] = "catmAISRDIStatusChPVclRangeTable"
            return self.catmaisrdistatuschpvclrangetable

        if (child_yang_name == "catmAISRDIStatusUpPVclRangeTable"):
            if (self.catmaisrdistatusuppvclrangetable is None):
                self.catmaisrdistatusuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable()
                self.catmaisrdistatusuppvclrangetable.parent = self
                self._children_name_map["catmaisrdistatusuppvclrangetable"] = "catmAISRDIStatusUpPVclRangeTable"
            return self.catmaisrdistatusuppvclrangetable

        if (child_yang_name == "catmCurStatChangePVclTable"):
            if (self.catmcurstatchangepvcltable is None):
                self.catmcurstatchangepvcltable = CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable()
                self.catmcurstatchangepvcltable.parent = self
                self._children_name_map["catmcurstatchangepvcltable"] = "catmCurStatChangePVclTable"
            return self.catmcurstatchangepvcltable

        if (child_yang_name == "catmCurStatusUpPVclTable"):
            if (self.catmcurstatusuppvcltable is None):
                self.catmcurstatusuppvcltable = CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable()
                self.catmcurstatusuppvcltable.parent = self
                self._children_name_map["catmcurstatusuppvcltable"] = "catmCurStatusUpPVclTable"
            return self.catmcurstatusuppvcltable

        if (child_yang_name == "catmDownPVclRangeTable"):
            if (self.catmdownpvclrangetable is None):
                self.catmdownpvclrangetable = CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable()
                self.catmdownpvclrangetable.parent = self
                self._children_name_map["catmdownpvclrangetable"] = "catmDownPVclRangeTable"
            return self.catmdownpvclrangetable

        if (child_yang_name == "catmEndCCStatusChPVclRangeTable"):
            if (self.catmendccstatuschpvclrangetable is None):
                self.catmendccstatuschpvclrangetable = CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable()
                self.catmendccstatuschpvclrangetable.parent = self
                self._children_name_map["catmendccstatuschpvclrangetable"] = "catmEndCCStatusChPVclRangeTable"
            return self.catmendccstatuschpvclrangetable

        if (child_yang_name == "catmEndCCStatusUpPVclRangeTable"):
            if (self.catmendccstatusuppvclrangetable is None):
                self.catmendccstatusuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable()
                self.catmendccstatusuppvclrangetable.parent = self
                self._children_name_map["catmendccstatusuppvclrangetable"] = "catmEndCCStatusUpPVclRangeTable"
            return self.catmendccstatusuppvclrangetable

        if (child_yang_name == "catmSegCCStatusChPVclRangeTable"):
            if (self.catmsegccstatuschpvclrangetable is None):
                self.catmsegccstatuschpvclrangetable = CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable()
                self.catmsegccstatuschpvclrangetable.parent = self
                self._children_name_map["catmsegccstatuschpvclrangetable"] = "catmSegCCStatusChPVclRangeTable"
            return self.catmsegccstatuschpvclrangetable

        if (child_yang_name == "catmSegCCStatusUpPVclRangeTable"):
            if (self.catmsegccstatusuppvclrangetable is None):
                self.catmsegccstatusuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable()
                self.catmsegccstatusuppvclrangetable.parent = self
                self._children_name_map["catmsegccstatusuppvclrangetable"] = "catmSegCCStatusUpPVclRangeTable"
            return self.catmsegccstatusuppvclrangetable

        if (child_yang_name == "catmStatusChangePVclRangeTable"):
            if (self.catmstatuschangepvclrangetable is None):
                self.catmstatuschangepvclrangetable = CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable()
                self.catmstatuschangepvclrangetable.parent = self
                self._children_name_map["catmstatuschangepvclrangetable"] = "catmStatusChangePVclRangeTable"
            return self.catmstatuschangepvclrangetable

        if (child_yang_name == "catmStatusUpPVclRangeTable"):
            if (self.catmstatusuppvclrangetable is None):
                self.catmstatusuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable()
                self.catmstatusuppvclrangetable.parent = self
                self._children_name_map["catmstatusuppvclrangetable"] = "catmStatusUpPVclRangeTable"
            return self.catmstatusuppvclrangetable

        if (child_yang_name == "catmUpPVclRangeTable"):
            if (self.catmuppvclrangetable is None):
                self.catmuppvclrangetable = CiscoAtmPvctrapExtnMib.Catmuppvclrangetable()
                self.catmuppvclrangetable.parent = self
                self._children_name_map["catmuppvclrangetable"] = "catmUpPVclRangeTable"
            return self.catmuppvclrangetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "catmAISRDIStatusChPVclRangeTable" or name == "catmAISRDIStatusUpPVclRangeTable" or name == "catmCurStatChangePVclTable" or name == "catmCurStatusUpPVclTable" or name == "catmDownPVclRangeTable" or name == "catmEndCCStatusChPVclRangeTable" or name == "catmEndCCStatusUpPVclRangeTable" or name == "catmSegCCStatusChPVclRangeTable" or name == "catmSegCCStatusUpPVclRangeTable" or name == "catmStatusChangePVclRangeTable" or name == "catmStatusUpPVclRangeTable" or name == "catmUpPVclRangeTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoAtmPvctrapExtnMib()
        return self._top_entity

