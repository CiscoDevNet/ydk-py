""" CISCO_MPLS_LSR_EXT_STD_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.

This MIB module contains generic object definitions for


MPLS LSR in transport networks.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOMPLSLSREXTSTDMIB(Entity):
    """
    
    
    .. attribute:: cmplsxcexttable
    
    	This table sparse augments the mplsXCTable of MPLS\-LSR\-STD\-MIB [RFC3813] to provide MPLS\-TP specific information about associated tunnel information
    	**type**\:  :py:class:`CmplsXCExtTable <ydk.models.cisco_ios_xe.CISCO_MPLS_LSR_EXT_STD_MIB.CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
    _revision = '2012-04-30'

    def __init__(self):
        super(CISCOMPLSLSREXTSTDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-MPLS-LSR-EXT-STD-MIB"
        self.yang_parent_name = "CISCO-MPLS-LSR-EXT-STD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cmplsXCExtTable", ("cmplsxcexttable", CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable))])
        self._leafs = OrderedDict()

        self.cmplsxcexttable = CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable()
        self.cmplsxcexttable.parent = self
        self._children_name_map["cmplsxcexttable"] = "cmplsXCExtTable"
        self._segment_path = lambda: "CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOMPLSLSREXTSTDMIB, [], name, value)


    class CmplsXCExtTable(Entity):
        """
        This table sparse augments the mplsXCTable of
        MPLS\-LSR\-STD\-MIB [RFC3813] to provide MPLS\-TP specific
        information about associated tunnel information
        
        .. attribute:: cmplsxcextentry
        
        	An entry in this table extends the cross connect information represented by an entry in the mplsXCTable in MPLS\-LSR\-STD\-MIB [RFC3813] through a sparse augmentation.  An entry can be created by a network administrator via SNMP SET commands, or in response to signaling protocol events
        	**type**\: list of  		 :py:class:`CmplsXCExtEntry <ydk.models.cisco_ios_xe.CISCO_MPLS_LSR_EXT_STD_MIB.CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
        _revision = '2012-04-30'

        def __init__(self):
            super(CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable, self).__init__()

            self.yang_name = "cmplsXCExtTable"
            self.yang_parent_name = "CISCO-MPLS-LSR-EXT-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cmplsXCExtEntry", ("cmplsxcextentry", CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry))])
            self._leafs = OrderedDict()

            self.cmplsxcextentry = YList(self)
            self._segment_path = lambda: "cmplsXCExtTable"
            self._absolute_path = lambda: "CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable, [], name, value)


        class CmplsXCExtEntry(Entity):
            """
            An entry in this table extends the cross connect
            information represented by an entry in
            the mplsXCTable in MPLS\-LSR\-STD\-MIB [RFC3813] through
            a sparse augmentation.  An entry can be created by
            a network administrator via SNMP SET commands, or in
            response to signaling protocol events.
            
            .. attribute:: mplsxcindex  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsxcinsegmentindex  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcinsegmentindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsxcoutsegmentindex  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcoutsegmentindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry>`
            
            	**config**\: False
            
            .. attribute:: cmplsxcexttunnelpointer
            
            	This object indicates the back pointer to the tunnel entry segment.  This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cmplsxcoppositedirxcptr
            
            	This object indicates the pointer to the opposite direction XC entry.  This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
            _revision = '2012-04-30'

            def __init__(self):
                super(CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry, self).__init__()

                self.yang_name = "cmplsXCExtEntry"
                self.yang_parent_name = "cmplsXCExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsxcindex','mplsxcinsegmentindex','mplsxcoutsegmentindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsxcindex', (YLeaf(YType.str, 'mplsXCIndex'), ['str'])),
                    ('mplsxcinsegmentindex', (YLeaf(YType.str, 'mplsXCInSegmentIndex'), ['str'])),
                    ('mplsxcoutsegmentindex', (YLeaf(YType.str, 'mplsXCOutSegmentIndex'), ['str'])),
                    ('cmplsxcexttunnelpointer', (YLeaf(YType.str, 'cmplsXCExtTunnelPointer'), ['str'])),
                    ('cmplsxcoppositedirxcptr', (YLeaf(YType.str, 'cmplsXCOppositeDirXCPtr'), ['str'])),
                ])
                self.mplsxcindex = None
                self.mplsxcinsegmentindex = None
                self.mplsxcoutsegmentindex = None
                self.cmplsxcexttunnelpointer = None
                self.cmplsxcoppositedirxcptr = None
                self._segment_path = lambda: "cmplsXCExtEntry" + "[mplsXCIndex='" + str(self.mplsxcindex) + "']" + "[mplsXCInSegmentIndex='" + str(self.mplsxcinsegmentindex) + "']" + "[mplsXCOutSegmentIndex='" + str(self.mplsxcoutsegmentindex) + "']"
                self._absolute_path = lambda: "CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB/cmplsXCExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry, ['mplsxcindex', 'mplsxcinsegmentindex', 'mplsxcoutsegmentindex', 'cmplsxcexttunnelpointer', 'cmplsxcoppositedirxcptr'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOMPLSLSREXTSTDMIB()
        return self._top_entity



