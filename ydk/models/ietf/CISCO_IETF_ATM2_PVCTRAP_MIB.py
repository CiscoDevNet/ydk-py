""" CISCO_IETF_ATM2_PVCTRAP_MIB 

This MIB Module is a supplement to the
ATM\-MIB.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOIETFATM2PVCTRAPMIB(object):
    """
    
    
    .. attribute:: atmcurrentlyfailingpvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and an atmVclOperStatus with a value other than `up'
    	**type**\: :py:class:`AtmCurrentlyFailingPVclTable <ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB.CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable>`
    
    

    """

    _prefix = 'cisco-ietf'
    _revision = '1998-02-03'

    def __init__(self):
        self.atmcurrentlyfailingpvcltable = CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable()
        self.atmcurrentlyfailingpvcltable.parent = self


    class AtmCurrentlyFailingPVclTable(object):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and an atmVclOperStatus with a value
        other than `up'.
        
        .. attribute:: atmcurrentlyfailingpvclentry
        
        	Each entry in this table represents a VCL for which the atmVclRowStatus is `active', the atmVclConnKind is `pvc', and the atmVclOperStatus is other than `up'
        	**type**\: list of :py:class:`AtmCurrentlyFailingPVclEntry <ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB.CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable.AtmCurrentlyFailingPVclEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '1998-02-03'

        def __init__(self):
            self.parent = None
            self.atmcurrentlyfailingpvclentry = YList()
            self.atmcurrentlyfailingpvclentry.parent = self
            self.atmcurrentlyfailingpvclentry.name = 'atmcurrentlyfailingpvclentry'


        class AtmCurrentlyFailingPVclEntry(object):
            """
            Each entry in this table represents a VCL for which
            the atmVclRowStatus is `active', the atmVclConnKind is
            `pvc', and the atmVclOperStatus is other than `up'.
            
            .. attribute:: atmvclvci
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmcurrentlyfailingpvcltimestamp
            
            	The time at which this PVCL began to fail
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpreviouslyfailedpvcltimestamp
            
            	The time at which this PVCL began to fail during the PVC Notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '1998-02-03'

            def __init__(self):
                self.parent = None
                self.atmvclvci = None
                self.atmvclvpi = None
                self.ifindex = None
                self.atmcurrentlyfailingpvcltimestamp = None
                self.atmpreviouslyfailedpvcltimestamp = None

            @property
            def _common_path(self):
                if self.atmvclvci is None:
                    raise YPYDataValidationError('Key property atmvclvci is None')
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB/CISCO-IETF-ATM2-PVCTRAP-MIB:atmCurrentlyFailingPVclTable/CISCO-IETF-ATM2-PVCTRAP-MIB:atmCurrentlyFailingPVclEntry[CISCO-IETF-ATM2-PVCTRAP-MIB:atmVclVci = ' + str(self.atmvclvci) + '][CISCO-IETF-ATM2-PVCTRAP-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-IETF-ATM2-PVCTRAP-MIB:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.atmcurrentlyfailingpvcltimestamp is not None:
                    return True

                if self.atmpreviouslyfailedpvcltimestamp is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB as meta
                return meta._meta_table['CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable.AtmCurrentlyFailingPVclEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB/CISCO-IETF-ATM2-PVCTRAP-MIB:atmCurrentlyFailingPVclTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.atmcurrentlyfailingpvclentry is not None:
                for child_ref in self.atmcurrentlyfailingpvclentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB as meta
            return meta._meta_table['CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.atmcurrentlyfailingpvcltable is not None and self.atmcurrentlyfailingpvcltable._has_data():
            return True

        if self.atmcurrentlyfailingpvcltable is not None and self.atmcurrentlyfailingpvcltable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB as meta
        return meta._meta_table['CISCOIETFATM2PVCTRAPMIB']['meta_info']


