""" CISCO_MPLS_LSR_EXT_STD_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.

This MIB module contains generic object definitions for


MPLS LSR in transport networks.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoMplsLsrExtStdMib(object):
    """
    
    
    .. attribute:: cmplsxcexttable
    
    	This table sparse augments the mplsXCTable of MPLS\-LSR\-STD\-MIB [RFC3813] to provide MPLS\-TP specific information about associated tunnel information
    	**type**\:   :py:class:`Cmplsxcexttable <ydk.models.cisco_ios_xe.CISCO_MPLS_LSR_EXT_STD_MIB.CiscoMplsLsrExtStdMib.Cmplsxcexttable>`
    
    

    """

    _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
    _revision = '2012-04-30'

    def __init__(self):
        self.cmplsxcexttable = CiscoMplsLsrExtStdMib.Cmplsxcexttable()
        self.cmplsxcexttable.parent = self


    class Cmplsxcexttable(object):
        """
        This table sparse augments the mplsXCTable of
        MPLS\-LSR\-STD\-MIB [RFC3813] to provide MPLS\-TP specific
        information about associated tunnel information
        
        .. attribute:: cmplsxcextentry
        
        	An entry in this table extends the cross connect information represented by an entry in the mplsXCTable in MPLS\-LSR\-STD\-MIB [RFC3813] through a sparse augmentation.  An entry can be created by a network administrator via SNMP SET commands, or in response to signaling protocol events
        	**type**\: list of    :py:class:`Cmplsxcextentry <ydk.models.cisco_ios_xe.CISCO_MPLS_LSR_EXT_STD_MIB.CiscoMplsLsrExtStdMib.Cmplsxcexttable.Cmplsxcextentry>`
        
        

        """

        _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
        _revision = '2012-04-30'

        def __init__(self):
            self.parent = None
            self.cmplsxcextentry = YList()
            self.cmplsxcextentry.parent = self
            self.cmplsxcextentry.name = 'cmplsxcextentry'


        class Cmplsxcextentry(object):
            """
            An entry in this table extends the cross connect
            information represented by an entry in
            the mplsXCTable in MPLS\-LSR\-STD\-MIB [RFC3813] through
            a sparse augmentation.  An entry can be created by
            a network administrator via SNMP SET commands, or in
            response to signaling protocol events.
            
            .. attribute:: mplsxcindex  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry>`
            
            .. attribute:: mplsxcinsegmentindex  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcinsegmentindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry>`
            
            .. attribute:: mplsxcoutsegmentindex  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcoutsegmentindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry>`
            
            .. attribute:: cmplsxcexttunnelpointer
            
            	This object indicates the back pointer to the tunnel entry segment.  This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cmplsxcoppositedirxcptr
            
            	This object indicates the pointer to the opposite direction XC entry.  This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
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
                    raise YPYModelError('Key property mplsxcindex is None')
                if self.mplsxcinsegmentindex is None:
                    raise YPYModelError('Key property mplsxcinsegmentindex is None')
                if self.mplsxcoutsegmentindex is None:
                    raise YPYModelError('Key property mplsxcoutsegmentindex is None')

                return '/CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB/CISCO-MPLS-LSR-EXT-STD-MIB:cmplsXCExtTable/CISCO-MPLS-LSR-EXT-STD-MIB:cmplsXCExtEntry[CISCO-MPLS-LSR-EXT-STD-MIB:mplsXCIndex = ' + str(self.mplsxcindex) + '][CISCO-MPLS-LSR-EXT-STD-MIB:mplsXCInSegmentIndex = ' + str(self.mplsxcinsegmentindex) + '][CISCO-MPLS-LSR-EXT-STD-MIB:mplsXCOutSegmentIndex = ' + str(self.mplsxcoutsegmentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_MPLS_LSR_EXT_STD_MIB as meta
                return meta._meta_table['CiscoMplsLsrExtStdMib.Cmplsxcexttable.Cmplsxcextentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB/CISCO-MPLS-LSR-EXT-STD-MIB:cmplsXCExtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cmplsxcextentry is not None:
                for child_ref in self.cmplsxcextentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_MPLS_LSR_EXT_STD_MIB as meta
            return meta._meta_table['CiscoMplsLsrExtStdMib.Cmplsxcexttable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cmplsxcexttable is not None and self.cmplsxcexttable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_MPLS_LSR_EXT_STD_MIB as meta
        return meta._meta_table['CiscoMplsLsrExtStdMib']['meta_info']


