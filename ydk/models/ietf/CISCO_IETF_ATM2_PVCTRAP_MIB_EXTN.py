""" CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN 

This MIB Module is a supplement to the
CISCO\-IETF\-ATM2\-PVCTRAP\-MIB.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOIETFATM2PVCTRAPMIBEXTN(object):
    """
    
    
    .. attribute:: atmcurrentstatuschangepvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last PVC notification interval
    	**type**\: :py:class:`AtmCurrentStatusChangePVclTable <ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CISCOIETFATM2PVCTRAPMIBEXTN.AtmCurrentStatusChangePVclTable>`
    
    .. attribute:: atmstatuschangepvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the same direction in the last PVC notification interval
    	**type**\: :py:class:`AtmStatusChangePVclRangeTable <ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CISCOIETFATM2PVCTRAPMIBEXTN.AtmStatusChangePVclRangeTable>`
    
    

    """

    _prefix = 'cisco-ietf'
    _revision = '2000-07-11'

    def __init__(self):
        self.atmcurrentstatuschangepvcltable = CISCOIETFATM2PVCTRAPMIBEXTN.AtmCurrentStatusChangePVclTable()
        self.atmcurrentstatuschangepvcltable.parent = self
        self.atmstatuschangepvclrangetable = CISCOIETFATM2PVCTRAPMIBEXTN.AtmStatusChangePVclRangeTable()
        self.atmstatuschangepvclrangetable.parent = self


    class AtmCurrentStatusChangePVclTable(object):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed in the
        last PVC notification interval.
        
        .. attribute:: atmcurrentstatuschangepvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last PVC notification interval
        	**type**\: list of :py:class:`AtmCurrentStatusChangePVclEntry <ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CISCOIETFATM2PVCTRAPMIBEXTN.AtmCurrentStatusChangePVclTable.AtmCurrentStatusChangePVclEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2000-07-11'

        def __init__(self):
            self.parent = None
            self.atmcurrentstatuschangepvclentry = YList()
            self.atmcurrentstatuschangepvclentry.parent = self
            self.atmcurrentstatuschangepvclentry.name = 'atmcurrentstatuschangepvclentry'


        class AtmCurrentStatusChangePVclEntry(object):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed in the last PVC notification interval.
            
            .. attribute:: atmvclvci
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmpvclstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2000-07-11'

            def __init__(self):
                self.parent = None
                self.atmvclvci = None
                self.atmvclvpi = None
                self.ifindex = None
                self.atmpvclstatuschangeend = None
                self.atmpvclstatuschangestart = None
                self.atmpvclstatustransition = None

            @property
            def _common_path(self):
                if self.atmvclvci is None:
                    raise YPYDataValidationError('Key property atmvclvci is None')
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmCurrentStatusChangePVclTable/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmCurrentStatusChangePVclEntry[CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmVclVci = ' + str(self.atmvclvci) + '][CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.atmpvclstatuschangeend is not None:
                    return True

                if self.atmpvclstatuschangestart is not None:
                    return True

                if self.atmpvclstatustransition is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN as meta
                return meta._meta_table['CISCOIETFATM2PVCTRAPMIBEXTN.AtmCurrentStatusChangePVclTable.AtmCurrentStatusChangePVclEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmCurrentStatusChangePVclTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.atmcurrentstatuschangepvclentry is not None:
                for child_ref in self.atmcurrentstatuschangepvclentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN as meta
            return meta._meta_table['CISCOIETFATM2PVCTRAPMIBEXTN.AtmCurrentStatusChangePVclTable']['meta_info']


    class AtmStatusChangePVclRangeTable(object):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed in the same
        direction in the last PVC notification interval.
        
        .. attribute:: atmstatuschangepvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed in the same direction in the last notification  interval
        	**type**\: list of :py:class:`AtmStatusChangePVclRangeEntry <ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN.CISCOIETFATM2PVCTRAPMIBEXTN.AtmStatusChangePVclRangeTable.AtmStatusChangePVclRangeEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2000-07-11'

        def __init__(self):
            self.parent = None
            self.atmstatuschangepvclrangeentry = YList()
            self.atmstatuschangepvclrangeentry.parent = self
            self.atmstatuschangepvclrangeentry.name = 'atmstatuschangepvclrangeentry'


        class AtmStatusChangePVclRangeEntry(object):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed in the same direction in the last notification 
            interval.
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rangeindex
            
            	Index to represent different ranges, the first range is  indexed by value 0, the second by 1 and so on..
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclhigherrangevalue
            
            	The last PVCL in a range of PVcls for which the  atmOperStatus to have changed in the last  notification interval
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: atmpvcllowerrangevalue
            
            	The first PVCL in a range of PVcls for which the  atmVclOperStatus to have changed in the last  notification interval
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: atmpvclrangestatuschangeend
            
            	The time stamp at which the last PVCL in the range changed state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpvclrangestatuschangestart
            
            	The time stamp at which the first PVCL in the range changed state in the last notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2000-07-11'

            def __init__(self):
                self.parent = None
                self.atmvclvpi = None
                self.ifindex = None
                self.rangeindex = None
                self.atmpvclhigherrangevalue = None
                self.atmpvcllowerrangevalue = None
                self.atmpvclrangestatuschangeend = None
                self.atmpvclrangestatuschangestart = None

            @property
            def _common_path(self):
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.rangeindex is None:
                    raise YPYDataValidationError('Key property rangeindex is None')

                return '/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmStatusChangePVclRangeTable/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmStatusChangePVclRangeEntry[CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:ifIndex = ' + str(self.ifindex) + '][CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:rangeIndex = ' + str(self.rangeindex) + ']'

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

                if self.ifindex is not None:
                    return True

                if self.rangeindex is not None:
                    return True

                if self.atmpvclhigherrangevalue is not None:
                    return True

                if self.atmpvcllowerrangevalue is not None:
                    return True

                if self.atmpvclrangestatuschangeend is not None:
                    return True

                if self.atmpvclrangestatuschangestart is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN as meta
                return meta._meta_table['CISCOIETFATM2PVCTRAPMIBEXTN.AtmStatusChangePVclRangeTable.AtmStatusChangePVclRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmStatusChangePVclRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.atmstatuschangepvclrangeentry is not None:
                for child_ref in self.atmstatuschangepvclrangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN as meta
            return meta._meta_table['CISCOIETFATM2PVCTRAPMIBEXTN.AtmStatusChangePVclRangeTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.atmcurrentstatuschangepvcltable is not None and self.atmcurrentstatuschangepvcltable._has_data():
            return True

        if self.atmcurrentstatuschangepvcltable is not None and self.atmcurrentstatuschangepvcltable.is_presence():
            return True

        if self.atmstatuschangepvclrangetable is not None and self.atmstatuschangepvclrangetable._has_data():
            return True

        if self.atmstatuschangepvclrangetable is not None and self.atmstatuschangepvclrangetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN as meta
        return meta._meta_table['CISCOIETFATM2PVCTRAPMIBEXTN']['meta_info']


