""" CISCO_ATM_PVCTRAP_EXTN_MIB 

This MIB Module is a supplement to the
CISCO\-IETF\-ATM2\-PVCTRAP\-MIB.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CatmOAMFailureType_Enum(Enum):
    """
    CatmOAMFailureType_Enum

    Enums to indicate different types of OAM recoveries .
    catmLoopbackOAMFailure  \- The object in query is Loopback OAM
                              type of failure.
    catmSegmentCCOAMFailure \- The object in query is Segment CC
                              OAM type of failure.
    catmEndCCOAMFailure     \- The object in query is End\-to\-End 
                              CC OAM type of failure.
    catmAISRDIOAMFailure    \- The object in query is AISRDI OAM
                              type of failure.

    """

    CATMLOOPBACKOAMFAILURE = 1

    CATMSEGMENTCCOAMFAILURE = 2

    CATMENDCCOAMFAILURE = 4

    CATMAISRDIOAMFAILURE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
        return meta._meta_table['CatmOAMFailureType_Enum']


class CatmOAMRecoveryType_Enum(Enum):
    """
    CatmOAMRecoveryType_Enum

    Enums to indicate different types of OAM recoveries .
    catmLoopbackOAMRecover  \- The object in query is Loopback OAM
                              type of recovery.
    catmSegmentCCOAMRecover \- The object in query is Segment CC
                              OAM type of recovery.
    catmEndCCOAMRecover     \- The object in query is End\-to\-End 
                              CC OAM type of recovery.
    catmAISRDIOAMRecover    \- The object in query is AISRDI OAM
                              type of recovery.

    """

    CATMLOOPBACKOAMRECOVER = 1

    CATMSEGMENTCCOAMRECOVER = 2

    CATMENDCCOAMRECOVER = 4

    CATMAISRDIOAMRECOVER = 8


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
        return meta._meta_table['CatmOAMRecoveryType_Enum']



class CISCOATMPVCTRAPEXTNMIB(object):
    """
    
    
    .. attribute:: catmaisrdistatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to AIS/RDI failure in the same direction in the last corresponding PVC  notification
    	**type**\: :py:class:`CatmAISRDIStatusChPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable>`
    
    .. attribute:: catmaisrdistatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and AISRDI OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\: :py:class:`CatmAISRDIStatusUpPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable>`
    
    .. attribute:: catmcurstatchangepvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last corresponding PVC notification
    	**type**\: :py:class:`CatmCurStatChangePVclTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable>`
    
    .. attribute:: catmcurstatusuppvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed to UP in the last corresponding PVC notification 
    	**type**\: :py:class:`CatmCurStatusUpPVclTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable>`
    
    .. attribute:: catmdownpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have detected as Down in the last corresponding PVC notification 
    	**type**\: :py:class:`CatmDownPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable>`
    
    .. attribute:: catmendccstatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to End CC failure in the same direction in the last PVC notification  interval
    	**type**\: :py:class:`CatmEndCCStatusChPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable>`
    
    .. attribute:: catmendccstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and End\-to\-End CC OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\: :py:class:`CatmEndCCStatusUpPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable>`
    
    .. attribute:: catmsegccstatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to segment CC  failure in the same direction in the last PVC  corresponding notification 
    	**type**\: :py:class:`CatmSegCCStatusChPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable>`
    
    .. attribute:: catmsegccstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and Segment CC OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\: :py:class:`CatmSegCCStatusUpPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable>`
    
    .. attribute:: catmstatuschangepvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the same direction in the last corresponding PVC notification 
    	**type**\: :py:class:`CatmStatusChangePVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable>`
    
    .. attribute:: catmstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and loopback OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\: :py:class:`CatmStatusUpPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable>`
    
    .. attribute:: catmuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have detected as Up in the last corresponding PVC notification 
    	**type**\: :py:class:`CatmUpPVclRangeTable <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable>`
    
    

    """

    _prefix = 'cisco-atm'
    _revision = '2003-01-20'

    def __init__(self):
        self.catmaisrdistatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable()
        self.catmaisrdistatuschpvclrangetable.parent = self
        self.catmaisrdistatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable()
        self.catmaisrdistatusuppvclrangetable.parent = self
        self.catmcurstatchangepvcltable = CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable()
        self.catmcurstatchangepvcltable.parent = self
        self.catmcurstatusuppvcltable = CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable()
        self.catmcurstatusuppvcltable.parent = self
        self.catmdownpvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable()
        self.catmdownpvclrangetable.parent = self
        self.catmendccstatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable()
        self.catmendccstatuschpvclrangetable.parent = self
        self.catmendccstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable()
        self.catmendccstatusuppvclrangetable.parent = self
        self.catmsegccstatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable()
        self.catmsegccstatuschpvclrangetable.parent = self
        self.catmsegccstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable()
        self.catmsegccstatusuppvclrangetable.parent = self
        self.catmstatuschangepvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable()
        self.catmstatuschangepvclrangetable.parent = self
        self.catmstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable()
        self.catmstatusuppvclrangetable.parent = self
        self.catmuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable()
        self.catmuppvclrangetable.parent = self


    class CatmAISRDIStatusChPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to AIS/RDI failure
        in the same direction in the last corresponding PVC 
        notification.
        
        .. attribute:: catmaisrdistatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to AIS/RDI failure in the same direction in the  last corresponding notification 
        	**type**\: list of :py:class:`CatmAISRDIStatusChPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmaisrdistatuschpvclrangeentry = YList()
            self.catmaisrdistatuschpvclrangeentry.parent = self
            self.catmaisrdistatuschpvclrangeentry.name = 'catmaisrdistatuschpvclrangeentry'


        class CatmAISRDIStatusChPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to AIS/RDI failure in the same direction in the 
            last corresponding notification .
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclaisrdihigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdilowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdirangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdirangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmpvclaisrdihigherrangevalue = None
                self.catmpvclaisrdilowerrangevalue = None
                self.catmpvclaisrdirangestatuschend = None
                self.catmpvclaisrdirangestatuschstart = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmAISRDIStatusChPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmAISRDIStatusChPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclaisrdihigherrangevalue is not None:
                    return True

                if self.catmpvclaisrdilowerrangevalue is not None:
                    return True

                if self.catmpvclaisrdirangestatuschend is not None:
                    return True

                if self.catmpvclaisrdirangestatuschstart is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmAISRDIStatusChPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmaisrdistatuschpvclrangeentry is not None:
                for child_ref in self.catmaisrdistatuschpvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable']['meta_info']


    class CatmAISRDIStatusUpPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and AISRDI OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmaisrdistatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and AISRDI OAM status  to have detected as recovered in the last notification interval
        	**type**\: list of :py:class:`CatmAISRDIStatusUpPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmaisrdistatusuppvclrangeentry = YList()
            self.catmaisrdistatusuppvclrangeentry.parent = self
            self.catmaisrdistatusuppvclrangeentry.name = 'catmaisrdistatusuppvclrangeentry'


        class CatmAISRDIStatusUpPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and AISRDI OAM status 
            to have detected as recovered in the last notification
            interval.
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclaisrdirangestatusupend
            
            	The time stamp at which the last AISRDI OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdirangestatusupstart
            
            	The time stamp at which the first AISRDI OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdiuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the AISRDI OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdiuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the AISRDI OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmpvclaisrdirangestatusupend = None
                self.catmpvclaisrdirangestatusupstart = None
                self.catmpvclaisrdiuphigherrangevalue = None
                self.catmpvclaisrdiuplowerrangevalue = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmAISRDIStatusUpPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmAISRDIStatusUpPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclaisrdirangestatusupend is not None:
                    return True

                if self.catmpvclaisrdirangestatusupstart is not None:
                    return True

                if self.catmpvclaisrdiuphigherrangevalue is not None:
                    return True

                if self.catmpvclaisrdiuplowerrangevalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmAISRDIStatusUpPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmaisrdistatusuppvclrangeentry is not None:
                for child_ref in self.catmaisrdistatusuppvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable']['meta_info']


    class CatmCurStatChangePVclTable(object):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed in the
        last corresponding PVC notification.
        
        .. attribute:: catmcurstatchangepvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last corresponding PVC notification
        	**type**\: list of :py:class:`CatmCurStatChangePVclEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmcurstatchangepvclentry = YList()
            self.catmcurstatchangepvclentry.parent = self
            self.catmcurstatchangepvclentry.name = 'catmcurstatchangepvclentry'


        class CatmCurStatChangePVclEntry(object):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed in the last corresponding PVC notification.
            
            .. attribute:: atmvclvci
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclaisrdistatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclcurfailtime
            
            	The time stamp at which this PVCL changed state to DOWN last time in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclfailurereason
            
            	Type of OAM failure
            	**type**\: :py:class:`CatmOAMFailureType_Enum <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMFailureType_Enum>`
            
            .. attribute:: catmpvclprevrecovertime
            
            	The time stamp at which this PVCL changed state to UP last time in the previous corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvci = None
                self.atmvclvpi = None
                self.ifindex = None
                self.catmpvclaisrdistatuschangeend = None
                self.catmpvclaisrdistatuschangestart = None
                self.catmpvclaisrdistatustransition = None
                self.catmpvclcurfailtime = None
                self.catmpvclendccstatuschangeend = None
                self.catmpvclendccstatuschangestart = None
                self.catmpvclendccstatustransition = None
                self.catmpvclfailurereason = None
                self.catmpvclprevrecovertime = None
                self.catmpvclsegccstatuschangeend = None
                self.catmpvclsegccstatuschangestart = None
                self.catmpvclsegccstatustransition = None
                self.catmpvclstatuschangeend = None
                self.catmpvclstatuschangestart = None
                self.catmpvclstatustransition = None

            @property
            def _common_path(self):
                if self.atmvclvci is None:
                    raise YPYDataValidationError('Key property atmvclvci is None')
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmCurStatChangePVclTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmCurStatChangePVclEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVci = ' + str(self.atmvclvci) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvci is not None:
                    return True

                if self.atmvclvpi is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclaisrdistatuschangeend is not None:
                    return True

                if self.catmpvclaisrdistatuschangestart is not None:
                    return True

                if self.catmpvclaisrdistatustransition is not None:
                    return True

                if self.catmpvclcurfailtime is not None:
                    return True

                if self.catmpvclendccstatuschangeend is not None:
                    return True

                if self.catmpvclendccstatuschangestart is not None:
                    return True

                if self.catmpvclendccstatustransition is not None:
                    return True

                if self.catmpvclfailurereason is not None:
                    return True

                if self.catmpvclprevrecovertime is not None:
                    return True

                if self.catmpvclsegccstatuschangeend is not None:
                    return True

                if self.catmpvclsegccstatuschangestart is not None:
                    return True

                if self.catmpvclsegccstatustransition is not None:
                    return True

                if self.catmpvclstatuschangeend is not None:
                    return True

                if self.catmpvclstatuschangestart is not None:
                    return True

                if self.catmpvclstatustransition is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmCurStatChangePVclTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmcurstatchangepvclentry is not None:
                for child_ref in self.catmcurstatchangepvclentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable']['meta_info']


    class CatmCurStatusUpPVclTable(object):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed to UP
        in the last corresponding PVC notification .
        
        .. attribute:: catmcurstatusuppvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed to UP in the last PVC notification  interval
        	**type**\: list of :py:class:`CatmCurStatusUpPVclEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmcurstatusuppvclentry = YList()
            self.catmcurstatusuppvclentry.parent = self
            self.catmcurstatusuppvclentry.name = 'catmcurstatusuppvclentry'


        class CatmCurStatusUpPVclEntry(object):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed to UP in the last PVC notification 
            interval.
            
            .. attribute:: atmvclvci
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclaisrdistatusupend
            
            	The time stamp at which this PVCL changed state to Up for the last time in the last corresponding notification  due to AIS/RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusupstart
            
            	The time stamp at which this PVCL changed state to Up for the first time in the last corresponding notification  due to AIS/RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusuptransition
            
            	The number of Down to Up state transitions that  has happened on this PVCL in the last notification  interval due to AIS RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclcurrecovertime
            
            	The time stamp at which this PVCL changed state to UP last time in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusupend
            
            	The time stamp at which this PVCL changed state to Up for the last time in the last corresponding notification  due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusupstart
            
            	The time stamp at which this PVCL changed state to Up for the first time in the last corresponding notification  due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusuptransition
            
            	The number of Down to UP state transitions that has  happened on this PVCL in the last notification  interval due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclprevfailtime
            
            	The time stamp at which this PVCL changed state to DOWN last time in the previous corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrecoveryreason
            
            	Type of OAM Recovered
            	**type**\: :py:class:`CatmOAMRecoveryType_Enum <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMRecoveryType_Enum>`
            
            .. attribute:: catmpvclsegccstatusupend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to Segment CC  OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusupstart
            
            	The time stamp at which this PVCL changed state to Up for  the first time in the last corresponding notification due to Segment CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusuptransition
            
            	The number of Down to Up state transitions that has  happened on this PVCL in the last corresponding notification  due to Segment CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusupend
            
            	The time stamp at which this PVCL changed state to UP  for the last time due to OAM loopback recovery in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusupstart
            
            	The time stamp at which this PVCL changed state to UP  for the first time due to OAM loopback recovery in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusuptransition
            
            	The number of Down to Up state transitions due to OAM loopback recovery that has happened on this PVCL  in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvci = None
                self.atmvclvpi = None
                self.ifindex = None
                self.catmpvclaisrdistatusupend = None
                self.catmpvclaisrdistatusupstart = None
                self.catmpvclaisrdistatusuptransition = None
                self.catmpvclcurrecovertime = None
                self.catmpvclendccstatusupend = None
                self.catmpvclendccstatusupstart = None
                self.catmpvclendccstatusuptransition = None
                self.catmpvclprevfailtime = None
                self.catmpvclrecoveryreason = None
                self.catmpvclsegccstatusupend = None
                self.catmpvclsegccstatusupstart = None
                self.catmpvclsegccstatusuptransition = None
                self.catmpvclstatusupend = None
                self.catmpvclstatusupstart = None
                self.catmpvclstatusuptransition = None

            @property
            def _common_path(self):
                if self.atmvclvci is None:
                    raise YPYDataValidationError('Key property atmvclvci is None')
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmCurStatusUpPVclTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmCurStatusUpPVclEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVci = ' + str(self.atmvclvci) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvci is not None:
                    return True

                if self.atmvclvpi is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclaisrdistatusupend is not None:
                    return True

                if self.catmpvclaisrdistatusupstart is not None:
                    return True

                if self.catmpvclaisrdistatusuptransition is not None:
                    return True

                if self.catmpvclcurrecovertime is not None:
                    return True

                if self.catmpvclendccstatusupend is not None:
                    return True

                if self.catmpvclendccstatusupstart is not None:
                    return True

                if self.catmpvclendccstatusuptransition is not None:
                    return True

                if self.catmpvclprevfailtime is not None:
                    return True

                if self.catmpvclrecoveryreason is not None:
                    return True

                if self.catmpvclsegccstatusupend is not None:
                    return True

                if self.catmpvclsegccstatusupstart is not None:
                    return True

                if self.catmpvclsegccstatusuptransition is not None:
                    return True

                if self.catmpvclstatusupend is not None:
                    return True

                if self.catmpvclstatusupstart is not None:
                    return True

                if self.catmpvclstatusuptransition is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmCurStatusUpPVclTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmcurstatusuppvclentry is not None:
                for child_ref in self.catmcurstatusuppvclentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable']['meta_info']


    class CatmDownPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have detected as Down
        in the last corresponding PVC notification .
        
        .. attribute:: catmdownpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  atmVclOperStatus to  have detected as Down in the last notification  interval
        	**type**\: list of :py:class:`CatmDownPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmdownpvclrangeentry = YList()
            self.catmdownpvclrangeentry.parent = self
            self.catmdownpvclrangeentry.name = 'catmdownpvclrangeentry'


        class CatmDownPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
            have detected as Down in the last notification 
            interval.
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmdownpvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Down in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmdownpvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Down in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmdownpvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Down on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmdownpvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Down on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevuppvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Up on any of the PVCLs in the range in the previous catmIntfPvcUp2Trap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevuppvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Up on any of the PVCLs in the range in the previous catmIntfPvcUp2Trap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangefailurereason
            
            	Type of OAM failure
            	**type**\: :py:class:`CatmOAMFailureType_Enum <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMFailureType_Enum>`
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmdownpvclhigherrangevalue = None
                self.catmdownpvcllowerrangevalue = None
                self.catmdownpvclrangeend = None
                self.catmdownpvclrangestart = None
                self.catmprevuppvclrangeend = None
                self.catmprevuppvclrangestart = None
                self.catmpvclrangefailurereason = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmDownPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmDownPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmdownpvclhigherrangevalue is not None:
                    return True

                if self.catmdownpvcllowerrangevalue is not None:
                    return True

                if self.catmdownpvclrangeend is not None:
                    return True

                if self.catmdownpvclrangestart is not None:
                    return True

                if self.catmprevuppvclrangeend is not None:
                    return True

                if self.catmprevuppvclrangestart is not None:
                    return True

                if self.catmpvclrangefailurereason is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmDownPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmdownpvclrangeentry is not None:
                for child_ref in self.catmdownpvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable']['meta_info']


    class CatmEndCCStatusChPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to End CC failure
        in the same direction in the last PVC notification 
        interval.
        
        .. attribute:: catmendccstatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to End CC failure in the same direction in the  last corresponding notification 
        	**type**\: list of :py:class:`CatmEndCCStatusChPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmendccstatuschpvclrangeentry = YList()
            self.catmendccstatuschpvclrangeentry.parent = self
            self.catmendccstatuschpvclrangeentry.name = 'catmendccstatuschpvclrangeentry'


        class CatmEndCCStatusChPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to End CC failure in the same direction in the 
            last corresponding notification .
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclendcchigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendcclowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccrangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccrangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmpvclendcchigherrangevalue = None
                self.catmpvclendcclowerrangevalue = None
                self.catmpvclendccrangestatuschend = None
                self.catmpvclendccrangestatuschstart = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmEndCCStatusChPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmEndCCStatusChPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclendcchigherrangevalue is not None:
                    return True

                if self.catmpvclendcclowerrangevalue is not None:
                    return True

                if self.catmpvclendccrangestatuschend is not None:
                    return True

                if self.catmpvclendccrangestatuschstart is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmEndCCStatusChPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmendccstatuschpvclrangeentry is not None:
                for child_ref in self.catmendccstatuschpvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable']['meta_info']


    class CatmEndCCStatusUpPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and End\-to\-End CC OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmendccstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and End\-to\-End CC OAM status  to have detected as recovered in the last notification interval
        	**type**\: list of :py:class:`CatmEndCCStatusUpPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmendccstatusuppvclrangeentry = YList()
            self.catmendccstatusuppvclrangeentry.parent = self
            self.catmendccstatusuppvclrangeentry.name = 'catmendccstatusuppvclrangeentry'


        class CatmEndCCStatusUpPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and End\-to\-End CC OAM status 
            to have detected as recovered in the last notification
            interval.
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclendccrangestatusupend
            
            	The time stamp at which the last End\-to\-End CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccrangestatusupstart
            
            	The time stamp at which the first End\-to\-End CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the End\-to\-End CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the End\-to\-End CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmpvclendccrangestatusupend = None
                self.catmpvclendccrangestatusupstart = None
                self.catmpvclendccuphigherrangevalue = None
                self.catmpvclendccuplowerrangevalue = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmEndCCStatusUpPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmEndCCStatusUpPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclendccrangestatusupend is not None:
                    return True

                if self.catmpvclendccrangestatusupstart is not None:
                    return True

                if self.catmpvclendccuphigherrangevalue is not None:
                    return True

                if self.catmpvclendccuplowerrangevalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmEndCCStatusUpPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmendccstatusuppvclrangeentry is not None:
                for child_ref in self.catmendccstatusuppvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable']['meta_info']


    class CatmSegCCStatusChPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to segment CC 
        failure in the same direction in the last PVC 
        corresponding notification .
        
        .. attribute:: catmsegccstatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to segment CC failure in the same direction  in the last corresponding notification 
        	**type**\: list of :py:class:`CatmSegCCStatusChPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmsegccstatuschpvclrangeentry = YList()
            self.catmsegccstatuschpvclrangeentry.parent = self
            self.catmsegccstatuschpvclrangeentry.name = 'catmsegccstatuschpvclrangeentry'


        class CatmSegCCStatusChPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to segment CC failure in the same direction 
            in the last corresponding notification .
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclsegcchigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegcclowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccrangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccrangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmpvclsegcchigherrangevalue = None
                self.catmpvclsegcclowerrangevalue = None
                self.catmpvclsegccrangestatuschend = None
                self.catmpvclsegccrangestatuschstart = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmSegCCStatusChPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmSegCCStatusChPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclsegcchigherrangevalue is not None:
                    return True

                if self.catmpvclsegcclowerrangevalue is not None:
                    return True

                if self.catmpvclsegccrangestatuschend is not None:
                    return True

                if self.catmpvclsegccrangestatuschstart is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmSegCCStatusChPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmsegccstatuschpvclrangeentry is not None:
                for child_ref in self.catmsegccstatuschpvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable']['meta_info']


    class CatmSegCCStatusUpPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and Segment CC OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmsegccstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and Segment CC OAM status to have detected as recovered in the last notification interval
        	**type**\: list of :py:class:`CatmSegCCStatusUpPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmsegccstatusuppvclrangeentry = YList()
            self.catmsegccstatusuppvclrangeentry.parent = self
            self.catmsegccstatusuppvclrangeentry.name = 'catmsegccstatusuppvclrangeentry'


        class CatmSegCCStatusUpPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and Segment CC OAM status to
            have detected as recovered in the last notification
            interval.
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclsegccrangestatusupend
            
            	The time stamp at which the last Segment CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccrangestatusupstart
            
            	The time stamp at which the first Segment CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the Segment CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the Segment CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmpvclsegccrangestatusupend = None
                self.catmpvclsegccrangestatusupstart = None
                self.catmpvclsegccuphigherrangevalue = None
                self.catmpvclsegccuplowerrangevalue = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmSegCCStatusUpPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmSegCCStatusUpPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclsegccrangestatusupend is not None:
                    return True

                if self.catmpvclsegccrangestatusupstart is not None:
                    return True

                if self.catmpvclsegccuphigherrangevalue is not None:
                    return True

                if self.catmpvclsegccuplowerrangevalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmSegCCStatusUpPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmsegccstatusuppvclrangeentry is not None:
                for child_ref in self.catmsegccstatusuppvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable']['meta_info']


    class CatmStatusChangePVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed in the same
        direction in the last corresponding PVC notification .
        
        .. attribute:: catmstatuschangepvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed in the same direction in the last notification  interval
        	**type**\: list of :py:class:`CatmStatusChangePVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmstatuschangepvclrangeentry = YList()
            self.catmstatuschangepvclrangeentry.parent = self
            self.catmstatuschangepvclrangeentry.name = 'catmstatuschangepvclrangeentry'


        class CatmStatusChangePVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed in the same direction in the last notification 
            interval.
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	Index to represent different ranges, the first range is indexed by value 0, the second by 1 and so on..
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclrangestatuschangeend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangestatuschangestart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmpvclhigherrangevalue = None
                self.catmpvcllowerrangevalue = None
                self.catmpvclrangestatuschangeend = None
                self.catmpvclrangestatuschangestart = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclhigherrangevalue is not None:
                    return True

                if self.catmpvcllowerrangevalue is not None:
                    return True

                if self.catmpvclrangestatuschangeend is not None:
                    return True

                if self.catmpvclrangestatuschangestart is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmstatuschangepvclrangeentry is not None:
                for child_ref in self.catmstatuschangepvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable']['meta_info']


    class CatmStatusUpPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and loopback OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  loopback OAM status to  have detected as recovered in the last notification  interval
        	**type**\: list of :py:class:`CatmStatusUpPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmstatusuppvclrangeentry = YList()
            self.catmstatusuppvclrangeentry.parent = self
            self.catmstatusuppvclrangeentry.name = 'catmstatusuppvclrangeentry'


        class CatmStatusUpPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  loopback OAM status to 
            have detected as recovered in the last notification 
            interval.
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmpvclrangestatusupend
            
            	The time stamp at which the last Loopback OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangestatusupstart
            
            	The time stamp at which the first Loopback OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvcluphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  Loopback OAM recovery has been detected in the last  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvcluplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  Loopback OAM recovery has been detected in the last  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmpvclrangestatusupend = None
                self.catmpvclrangestatusupstart = None
                self.catmpvcluphigherrangevalue = None
                self.catmpvcluplowerrangevalue = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusUpPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusUpPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmpvclrangestatusupend is not None:
                    return True

                if self.catmpvclrangestatusupstart is not None:
                    return True

                if self.catmpvcluphigherrangevalue is not None:
                    return True

                if self.catmpvcluplowerrangevalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusUpPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmstatusuppvclrangeentry is not None:
                for child_ref in self.catmstatusuppvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable']['meta_info']


    class CatmUpPVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have detected as Up
        in the last corresponding PVC notification .
        
        .. attribute:: catmuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  atmVclOperStatus to  have detected as Up in the last notification  interval
        	**type**\: list of :py:class:`CatmUpPVclRangeEntry <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-atm'
        _revision = '2003-01-20'

        def __init__(self):
            self.parent = None
            self.catmuppvclrangeentry = YList()
            self.catmuppvclrangeentry.parent = self
            self.catmuppvclrangeentry.name = 'catmuppvclrangeentry'


        class CatmUpPVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
            have detected as Up in the last notification 
            interval.
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: catmstatuschangepvclrangeindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: catmprevdownpvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Down on any of the PVCLs in the range in the previous catmIntfPvcDownTrap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevdownpvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Down on any of the PVCLs in the range in the previous catmIntfPvcDownTrap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangerecoveryreason
            
            	Type of OAM Recovered
            	**type**\: :py:class:`CatmOAMRecoveryType_Enum <ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMRecoveryType_Enum>`
            
            .. attribute:: catmuppvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Up in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmuppvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Up in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmuppvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Up on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmuppvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Up on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-atm'
            _revision = '2003-01-20'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.catmstatuschangepvclrangeindex = None
                self.ifindex = None
                self.catmprevdownpvclrangeend = None
                self.catmprevdownpvclrangestart = None
                self.catmpvclrangerecoveryreason = None
                self.catmuppvclhigherrangevalue = None
                self.catmuppvcllowerrangevalue = None
                self.catmuppvclrangeend = None
                self.catmuppvclrangestart = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.catmstatuschangepvclrangeindex is None:
                    raise YPYDataValidationError('Key property catmstatuschangepvclrangeindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmUpPVclRangeTable/CISCO-ATM-PVCTRAP-EXTN-MIB:catmUpPVclRangeEntry[CISCO-ATM-PVCTRAP-EXTN-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:catmStatusChangePVclRangeIndex = ' + str(self.catmstatuschangepvclrangeindex) + '][CISCO-ATM-PVCTRAP-EXTN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvpi is not None:
                    return True

                if self.catmstatuschangepvclrangeindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.catmprevdownpvclrangeend is not None:
                    return True

                if self.catmprevdownpvclrangestart is not None:
                    return True

                if self.catmpvclrangerecoveryreason is not None:
                    return True

                if self.catmuppvclhigherrangevalue is not None:
                    return True

                if self.catmuppvcllowerrangevalue is not None:
                    return True

                if self.catmuppvclrangeend is not None:
                    return True

                if self.catmuppvclrangestart is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
                return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/CISCO-ATM-PVCTRAP-EXTN-MIB:catmUpPVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.catmuppvclrangeentry is not None:
                for child_ref in self.catmuppvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
            return meta._meta_table['CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.catmaisrdistatuschpvclrangetable is not None and self.catmaisrdistatuschpvclrangetable._has_data():
            return True

        if self.catmaisrdistatuschpvclrangetable is not None and self.catmaisrdistatuschpvclrangetable.is_presence():
            return True

        if self.catmaisrdistatusuppvclrangetable is not None and self.catmaisrdistatusuppvclrangetable._has_data():
            return True

        if self.catmaisrdistatusuppvclrangetable is not None and self.catmaisrdistatusuppvclrangetable.is_presence():
            return True

        if self.catmcurstatchangepvcltable is not None and self.catmcurstatchangepvcltable._has_data():
            return True

        if self.catmcurstatchangepvcltable is not None and self.catmcurstatchangepvcltable.is_presence():
            return True

        if self.catmcurstatusuppvcltable is not None and self.catmcurstatusuppvcltable._has_data():
            return True

        if self.catmcurstatusuppvcltable is not None and self.catmcurstatusuppvcltable.is_presence():
            return True

        if self.catmdownpvclrangetable is not None and self.catmdownpvclrangetable._has_data():
            return True

        if self.catmdownpvclrangetable is not None and self.catmdownpvclrangetable.is_presence():
            return True

        if self.catmendccstatuschpvclrangetable is not None and self.catmendccstatuschpvclrangetable._has_data():
            return True

        if self.catmendccstatuschpvclrangetable is not None and self.catmendccstatuschpvclrangetable.is_presence():
            return True

        if self.catmendccstatusuppvclrangetable is not None and self.catmendccstatusuppvclrangetable._has_data():
            return True

        if self.catmendccstatusuppvclrangetable is not None and self.catmendccstatusuppvclrangetable.is_presence():
            return True

        if self.catmsegccstatuschpvclrangetable is not None and self.catmsegccstatuschpvclrangetable._has_data():
            return True

        if self.catmsegccstatuschpvclrangetable is not None and self.catmsegccstatuschpvclrangetable.is_presence():
            return True

        if self.catmsegccstatusuppvclrangetable is not None and self.catmsegccstatusuppvclrangetable._has_data():
            return True

        if self.catmsegccstatusuppvclrangetable is not None and self.catmsegccstatusuppvclrangetable.is_presence():
            return True

        if self.catmstatuschangepvclrangetable is not None and self.catmstatuschangepvclrangetable._has_data():
            return True

        if self.catmstatuschangepvclrangetable is not None and self.catmstatuschangepvclrangetable.is_presence():
            return True

        if self.catmstatusuppvclrangetable is not None and self.catmstatusuppvclrangetable._has_data():
            return True

        if self.catmstatusuppvclrangetable is not None and self.catmstatusuppvclrangetable.is_presence():
            return True

        if self.catmuppvclrangetable is not None and self.catmuppvclrangetable._has_data():
            return True

        if self.catmuppvclrangetable is not None and self.catmuppvclrangetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _CISCO_ATM_PVCTRAP_EXTN_MIB as meta
        return meta._meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']


