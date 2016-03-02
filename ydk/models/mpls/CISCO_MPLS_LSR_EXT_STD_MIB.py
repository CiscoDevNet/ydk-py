""" CISCO_MPLS_LSR_EXT_STD_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.

This MIB module contains generic object definitions for


MPLS LSR in transport networks.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOMPLSLSREXTSTDMIB(object):
    """
    
    
    .. attribute:: cmplsxcexttable
    
    	This table sparse augments the mplsXCTable of MPLS\-LSR\-STD\-MIB [RFC3813] to provide MPLS\-TP specific information about associated tunnel information
    	**type**\: :py:class:`CmplsXCExtTable <ydk.models.mpls.CISCO_MPLS_LSR_EXT_STD_MIB.CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable>`
    
    

    """

    _prefix = 'cisco-mpls'
    _revision = '2012-04-30'

    def __init__(self):
        self.cmplsxcexttable = CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable()
        self.cmplsxcexttable.parent = self


    class CmplsXCExtTable(object):
        """
        This table sparse augments the mplsXCTable of
        MPLS\-LSR\-STD\-MIB [RFC3813] to provide MPLS\-TP specific
        information about associated tunnel information
        
        .. attribute:: cmplsxcextentry
        
        	An entry in this table extends the cross connect information represented by an entry in the mplsXCTable in MPLS\-LSR\-STD\-MIB [RFC3813] through a sparse augmentation.  An entry can be created by a network administrator via SNMP SET commands, or in response to signaling protocol events
        	**type**\: list of :py:class:`CmplsXCExtEntry <ydk.models.mpls.CISCO_MPLS_LSR_EXT_STD_MIB.CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry>`
        
        

        """

        _prefix = 'cisco-mpls'
        _revision = '2012-04-30'

        def __init__(self):
            self.parent = None
            self.cmplsxcextentry = YList()
            self.cmplsxcextentry.parent = self
            self.cmplsxcextentry.name = 'cmplsxcextentry'


        class CmplsXCExtEntry(object):
            """
            An entry in this table extends the cross connect
            information represented by an entry in
            the mplsXCTable in MPLS\-LSR\-STD\-MIB [RFC3813] through
            a sparse augmentation.  An entry can be created by
            a network administrator via SNMP SET commands, or in
            response to signaling protocol events.
            
            .. attribute:: mplsxcindex
            
            	
            	**type**\: str
            
            	**range:** 1..24
            
            .. attribute:: mplsxcinsegmentindex
            
            	
            	**type**\: str
            
            	**range:** 1..24
            
            .. attribute:: mplsxcoutsegmentindex
            
            	
            	**type**\: str
            
            	**range:** 1..24
            
            .. attribute:: cmplsxcexttunnelpointer
            
            	This object indicates the back pointer to the tunnel entry segment.  This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cmplsxcoppositedirxcptr
            
            	This object indicates the pointer to the opposite direction XC entry.  This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'cisco-mpls'
            _revision = '2012-04-30'

            def __init__(self):
                self.parent = None
                self.mplsxcindex = None
                self.mplsxcinsegmentindex = None
                self.mplsxcoutsegmentindex = None
                self.cmplsxcexttunnelpointer = None
                self.cmplsxcoppositedirxcptr = None

            @property
            def _common_path(self):
                if self.mplsxcindex is None:
                    raise YPYDataValidationError('Key property mplsxcindex is None')
                if self.mplsxcinsegmentindex is None:
                    raise YPYDataValidationError('Key property mplsxcinsegmentindex is None')
                if self.mplsxcoutsegmentindex is None:
                    raise YPYDataValidationError('Key property mplsxcoutsegmentindex is None')

                return '/CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB/CISCO-MPLS-LSR-EXT-STD-MIB:cmplsXCExtTable/CISCO-MPLS-LSR-EXT-STD-MIB:cmplsXCExtEntry[CISCO-MPLS-LSR-EXT-STD-MIB:mplsXCIndex = ' + str(self.mplsxcindex) + '][CISCO-MPLS-LSR-EXT-STD-MIB:mplsXCInSegmentIndex = ' + str(self.mplsxcinsegmentindex) + '][CISCO-MPLS-LSR-EXT-STD-MIB:mplsXCOutSegmentIndex = ' + str(self.mplsxcoutsegmentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsxcindex is not None:
                    return True

                if self.mplsxcinsegmentindex is not None:
                    return True

                if self.mplsxcoutsegmentindex is not None:
                    return True

                if self.cmplsxcexttunnelpointer is not None:
                    return True

                if self.cmplsxcoppositedirxcptr is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _CISCO_MPLS_LSR_EXT_STD_MIB as meta
                return meta._meta_table['CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB/CISCO-MPLS-LSR-EXT-STD-MIB:cmplsXCExtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmplsxcextentry is not None:
                for child_ref in self.cmplsxcextentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _CISCO_MPLS_LSR_EXT_STD_MIB as meta
            return meta._meta_table['CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cmplsxcexttable is not None and self.cmplsxcexttable._has_data():
            return True

        if self.cmplsxcexttable is not None and self.cmplsxcexttable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _CISCO_MPLS_LSR_EXT_STD_MIB as meta
        return meta._meta_table['CISCOMPLSLSREXTSTDMIB']['meta_info']


