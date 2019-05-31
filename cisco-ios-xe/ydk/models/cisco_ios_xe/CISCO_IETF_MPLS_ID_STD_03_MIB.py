""" CISCO_IETF_MPLS_ID_STD_03_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.

This MIB module contains generic object definitions for
MPLS Traffic Engineering in transport networks. This module is a
cisco\-ized version of the IETF draft\:
draft\-ietf\-mpls\-tp\-te\-mib\-03.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIETFMPLSIDSTD03MIB(Entity):
    """
    
    
    .. attribute:: cmplsidobjects
    
    	
    	**type**\:  :py:class:`CmplsIdObjects <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_ID_STD_03_MIB.CISCOIETFMPLSIDSTD03MIB.CmplsIdObjects>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-IETF-MPLS-ID-STD-03-MIB'
    _revision = '2012-06-07'

    def __init__(self):
        super(CISCOIETFMPLSIDSTD03MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-MPLS-ID-STD-03-MIB"
        self.yang_parent_name = "CISCO-IETF-MPLS-ID-STD-03-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cmplsIdObjects", ("cmplsidobjects", CISCOIETFMPLSIDSTD03MIB.CmplsIdObjects))])
        self._leafs = OrderedDict()

        self.cmplsidobjects = CISCOIETFMPLSIDSTD03MIB.CmplsIdObjects()
        self.cmplsidobjects.parent = self
        self._children_name_map["cmplsidobjects"] = "cmplsIdObjects"
        self._segment_path = lambda: "CISCO-IETF-MPLS-ID-STD-03-MIB:CISCO-IETF-MPLS-ID-STD-03-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIETFMPLSIDSTD03MIB, [], name, value)


    class CmplsIdObjects(Entity):
        """
        
        
        .. attribute:: cmplsglobalid
        
        	This object allows the administrator to assign a unique operator identifier also called MPLS\-TP Global\_ID
        	**type**\: str
        
        	**length:** 4..4
        
        	**config**\: False
        
        .. attribute:: cmplsicc
        
        	This object allows the operator or service provider to assign a unique MPLS\-TP ITU\-T Carrier Code (ICC) to a network
        	**type**\: str
        
        	**length:** 1..6
        
        	**config**\: False
        
        .. attribute:: cmplsnodeid
        
        	This object allows the operator or service provider to assign a unique MPLS\-TP Node\_ID.  The Node\_ID is assigned within the scope of the Global\_ID
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-ID-STD-03-MIB'
        _revision = '2012-06-07'

        def __init__(self):
            super(CISCOIETFMPLSIDSTD03MIB.CmplsIdObjects, self).__init__()

            self.yang_name = "cmplsIdObjects"
            self.yang_parent_name = "CISCO-IETF-MPLS-ID-STD-03-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cmplsglobalid', (YLeaf(YType.str, 'cmplsGlobalId'), ['str'])),
                ('cmplsicc', (YLeaf(YType.str, 'cmplsIcc'), ['str'])),
                ('cmplsnodeid', (YLeaf(YType.uint32, 'cmplsNodeId'), ['int'])),
            ])
            self.cmplsglobalid = None
            self.cmplsicc = None
            self.cmplsnodeid = None
            self._segment_path = lambda: "cmplsIdObjects"
            self._absolute_path = lambda: "CISCO-IETF-MPLS-ID-STD-03-MIB:CISCO-IETF-MPLS-ID-STD-03-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFMPLSIDSTD03MIB.CmplsIdObjects, ['cmplsglobalid', 'cmplsicc', 'cmplsnodeid'], name, value)


    def clone_ptr(self):
        self._top_entity = CISCOIETFMPLSIDSTD03MIB()
        return self._top_entity



