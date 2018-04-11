""" CISCO_IETF_ATM2_PVCTRAP_MIB 

This MIB Module is a supplement to the
ATM\-MIB.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIETFATM2PVCTRAPMIB(Entity):
    """
    
    
    .. attribute:: atmcurrentlyfailingpvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and an atmVclOperStatus with a value other than `up'
    	**type**\:  :py:class:`Atmcurrentlyfailingpvcltable <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB.CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable>`
    
    

    """

    _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
    _revision = '1998-02-03'

    def __init__(self):
        super(CISCOIETFATM2PVCTRAPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-ATM2-PVCTRAP-MIB"
        self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("atmCurrentlyFailingPVclTable", ("atmcurrentlyfailingpvcltable", CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.atmcurrentlyfailingpvcltable = CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable()
        self.atmcurrentlyfailingpvcltable.parent = self
        self._children_name_map["atmcurrentlyfailingpvcltable"] = "atmCurrentlyFailingPVclTable"
        self._children_yang_names.add("atmCurrentlyFailingPVclTable")
        self._segment_path = lambda: "CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB"


    class Atmcurrentlyfailingpvcltable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and an atmVclOperStatus with a value
        other than `up'.
        
        .. attribute:: atmcurrentlyfailingpvclentry
        
        	Each entry in this table represents a VCL for which the atmVclRowStatus is `active', the atmVclConnKind is `pvc', and the atmVclOperStatus is other than `up'
        	**type**\: list of  		 :py:class:`Atmcurrentlyfailingpvclentry <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB.CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry>`
        
        

        """

        _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
        _revision = '1998-02-03'

        def __init__(self):
            super(CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable, self).__init__()

            self.yang_name = "atmCurrentlyFailingPVclTable"
            self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("atmCurrentlyFailingPVclEntry", ("atmcurrentlyfailingpvclentry", CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry))])
            self._leafs = OrderedDict()

            self.atmcurrentlyfailingpvclentry = YList(self)
            self._segment_path = lambda: "atmCurrentlyFailingPVclTable"
            self._absolute_path = lambda: "CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable, [], name, value)


        class Atmcurrentlyfailingpvclentry(Entity):
            """
            Each entry in this table represents a VCL for which
            the atmVclRowStatus is `active', the atmVclConnKind is
            `pvc', and the atmVclOperStatus is other than `up'.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmcurrentlyfailingpvcltimestamp
            
            	The time at which this PVCL began to fail
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpreviouslyfailedpvcltimestamp
            
            	The time at which this PVCL began to fail during the PVC Notification interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
            _revision = '1998-02-03'

            def __init__(self):
                super(CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry, self).__init__()

                self.yang_name = "atmCurrentlyFailingPVclEntry"
                self.yang_parent_name = "atmCurrentlyFailingPVclTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','atmvclvci']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('atmvclvpi', YLeaf(YType.str, 'atmVclVpi')),
                    ('atmvclvci', YLeaf(YType.str, 'atmVclVci')),
                    ('atmcurrentlyfailingpvcltimestamp', YLeaf(YType.uint32, 'atmCurrentlyFailingPVclTimeStamp')),
                    ('atmpreviouslyfailedpvcltimestamp', YLeaf(YType.uint32, 'atmPreviouslyFailedPVclTimeStamp')),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.atmcurrentlyfailingpvcltimestamp = None
                self.atmpreviouslyfailedpvcltimestamp = None
                self._segment_path = lambda: "atmCurrentlyFailingPVclEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[atmVclVci='" + str(self.atmvclvci) + "']"
                self._absolute_path = lambda: "CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB/atmCurrentlyFailingPVclTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFATM2PVCTRAPMIB.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'atmcurrentlyfailingpvcltimestamp', 'atmpreviouslyfailedpvcltimestamp'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIETFATM2PVCTRAPMIB()
        return self._top_entity

