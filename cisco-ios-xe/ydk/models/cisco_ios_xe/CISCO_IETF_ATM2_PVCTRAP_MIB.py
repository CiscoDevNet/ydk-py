""" CISCO_IETF_ATM2_PVCTRAP_MIB 

This MIB Module is a supplement to the
ATM\-MIB.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIetfAtm2PvctrapMib(object):
    """
    
    
    .. attribute:: atmcurrentlyfailingpvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and an atmVclOperStatus with a value other than `up'
    	**type**\:   :py:class:`Atmcurrentlyfailingpvcltable <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB.CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable>`
    
    

    """

    _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
    _revision = '1998-02-03'

    def __init__(self):
        self.atmcurrentlyfailingpvcltable = CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable()
        self.atmcurrentlyfailingpvcltable.parent = self


    class Atmcurrentlyfailingpvcltable(object):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and an atmVclOperStatus with a value
        other than `up'.
        
        .. attribute:: atmcurrentlyfailingpvclentry
        
        	Each entry in this table represents a VCL for which the atmVclRowStatus is `active', the atmVclConnKind is `pvc', and the atmVclOperStatus is other than `up'
        	**type**\: list of    :py:class:`Atmcurrentlyfailingpvclentry <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB.CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry>`
        
        

        """

        _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
        _revision = '1998-02-03'

        def __init__(self):
            self.parent = None
            self.atmcurrentlyfailingpvclentry = YList()
            self.atmcurrentlyfailingpvclentry.parent = self
            self.atmcurrentlyfailingpvclentry.name = 'atmcurrentlyfailingpvclentry'


        class Atmcurrentlyfailingpvclentry(object):
            """
            Each entry in this table represents a VCL for which
            the atmVclRowStatus is `active', the atmVclConnKind is
            `pvc', and the atmVclOperStatus is other than `up'.
            
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
            
            .. attribute:: atmcurrentlyfailingpvcltimestamp
            
            	The time at which this PVCL began to fail
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpreviouslyfailedpvcltimestamp
            
            	The time at which this PVCL began to fail during the PVC Notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
            _revision = '1998-02-03'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.atmcurrentlyfailingpvcltimestamp = None
                self.atmpreviouslyfailedpvcltimestamp = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.atmvclvpi is None:
                    raise YPYModelError('Key property atmvclvpi is None')
                if self.atmvclvci is None:
                    raise YPYModelError('Key property atmvclvci is None')

                return '/CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB/CISCO-IETF-ATM2-PVCTRAP-MIB:atmCurrentlyFailingPVclTable/CISCO-IETF-ATM2-PVCTRAP-MIB:atmCurrentlyFailingPVclEntry[CISCO-IETF-ATM2-PVCTRAP-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-IETF-ATM2-PVCTRAP-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-IETF-ATM2-PVCTRAP-MIB:atmVclVci = ' + str(self.atmvclvci) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atmvclvpi is not None:
                    return True

                if self.atmvclvci is not None:
                    return True

                if self.atmcurrentlyfailingpvcltimestamp is not None:
                    return True

                if self.atmpreviouslyfailedpvcltimestamp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB as meta
                return meta._meta_table['CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB/CISCO-IETF-ATM2-PVCTRAP-MIB:atmCurrentlyFailingPVclTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atmcurrentlyfailingpvclentry is not None:
                for child_ref in self.atmcurrentlyfailingpvclentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB as meta
            return meta._meta_table['CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.atmcurrentlyfailingpvcltable is not None and self.atmcurrentlyfailingpvcltable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_ATM2_PVCTRAP_MIB as meta
        return meta._meta_table['CiscoIetfAtm2PvctrapMib']['meta_info']


