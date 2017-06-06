""" CISCO_IETF_MPLS_ID_STD_03_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.

This MIB module contains generic object definitions for
MPLS Traffic Engineering in transport networks. This module is a
cisco\-ized version of the IETF draft\:
draft\-ietf\-mpls\-tp\-te\-mib\-03.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIetfMplsIdStd03Mib(object):
    """
    
    
    .. attribute:: cmplsidobjects
    
    	
    	**type**\:   :py:class:`Cmplsidobjects <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_ID_STD_03_MIB.CiscoIetfMplsIdStd03Mib.Cmplsidobjects>`
    
    

    """

    _prefix = 'CISCO-IETF-MPLS-ID-STD-03-MIB'
    _revision = '2012-06-07'

    def __init__(self):
        self.cmplsidobjects = CiscoIetfMplsIdStd03Mib.Cmplsidobjects()
        self.cmplsidobjects.parent = self


    class Cmplsidobjects(object):
        """
        
        
        .. attribute:: cmplsglobalid
        
        	This object allows the administrator to assign a unique operator identifier also called MPLS\-TP Global\_ID
        	**type**\:  str
        
        	**length:** 4
        
        .. attribute:: cmplsicc
        
        	This object allows the operator or service provider to assign a unique MPLS\-TP ITU\-T Carrier Code (ICC) to a network
        	**type**\:  str
        
        	**length:** 1..6
        
        .. attribute:: cmplsnodeid
        
        	This object allows the operator or service provider to assign a unique MPLS\-TP Node\_ID.  The Node\_ID is assigned within the scope of the Global\_ID
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-ID-STD-03-MIB'
        _revision = '2012-06-07'

        def __init__(self):
            self.parent = None
            self.cmplsglobalid = None
            self.cmplsicc = None
            self.cmplsnodeid = None

        @property
        def _common_path(self):

            return '/CISCO-IETF-MPLS-ID-STD-03-MIB:CISCO-IETF-MPLS-ID-STD-03-MIB/CISCO-IETF-MPLS-ID-STD-03-MIB:cmplsIdObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cmplsglobalid is not None:
                return True

            if self.cmplsicc is not None:
                return True

            if self.cmplsnodeid is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_MPLS_ID_STD_03_MIB as meta
            return meta._meta_table['CiscoIetfMplsIdStd03Mib.Cmplsidobjects']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-MPLS-ID-STD-03-MIB:CISCO-IETF-MPLS-ID-STD-03-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cmplsidobjects is not None and self.cmplsidobjects._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_MPLS_ID_STD_03_MIB as meta
        return meta._meta_table['CiscoIetfMplsIdStd03Mib']['meta_info']


