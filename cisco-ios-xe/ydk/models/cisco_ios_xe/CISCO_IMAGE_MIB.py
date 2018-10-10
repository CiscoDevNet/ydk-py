""" CISCO_IMAGE_MIB 

Router image MIB which identify the capabilities
and characteristics of the image

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIMAGEMIB(Entity):
    """
    
    
    .. attribute:: ciscoimagetable
    
    	A table provides content information describing the executing IOS image
    	**type**\:  :py:class:`CiscoImageTable <ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB.CISCOIMAGEMIB.CiscoImageTable>`
    
    

    """

    _prefix = 'CISCO-IMAGE-MIB'
    _revision = '1995-08-15'

    def __init__(self):
        super(CISCOIMAGEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IMAGE-MIB"
        self.yang_parent_name = "CISCO-IMAGE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ciscoImageTable", ("ciscoimagetable", CISCOIMAGEMIB.CiscoImageTable))])
        self._leafs = OrderedDict()

        self.ciscoimagetable = CISCOIMAGEMIB.CiscoImageTable()
        self.ciscoimagetable.parent = self
        self._children_name_map["ciscoimagetable"] = "ciscoImageTable"
        self._segment_path = lambda: "CISCO-IMAGE-MIB:CISCO-IMAGE-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIMAGEMIB, [], name, value)


    class CiscoImageTable(Entity):
        """
        A table provides content information describing the
        executing IOS image.
        
        .. attribute:: ciscoimageentry
        
        	A image characteristic string entry
        	**type**\: list of  		 :py:class:`CiscoImageEntry <ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB.CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry>`
        
        

        """

        _prefix = 'CISCO-IMAGE-MIB'
        _revision = '1995-08-15'

        def __init__(self):
            super(CISCOIMAGEMIB.CiscoImageTable, self).__init__()

            self.yang_name = "ciscoImageTable"
            self.yang_parent_name = "CISCO-IMAGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ciscoImageEntry", ("ciscoimageentry", CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry))])
            self._leafs = OrderedDict()

            self.ciscoimageentry = YList(self)
            self._segment_path = lambda: "ciscoImageTable"
            self._absolute_path = lambda: "CISCO-IMAGE-MIB:CISCO-IMAGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIMAGEMIB.CiscoImageTable, [], name, value)


        class CiscoImageEntry(Entity):
            """
            A image characteristic string entry.
            
            .. attribute:: ciscoimageindex  (key)
            
            	A sequence number for each string stored in the IOS image
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoimagestring
            
            	The string of this entry
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-IMAGE-MIB'
            _revision = '1995-08-15'

            def __init__(self):
                super(CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry, self).__init__()

                self.yang_name = "ciscoImageEntry"
                self.yang_parent_name = "ciscoImageTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoimageindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoimageindex', (YLeaf(YType.int32, 'ciscoImageIndex'), ['int'])),
                    ('ciscoimagestring', (YLeaf(YType.str, 'ciscoImageString'), ['str'])),
                ])
                self.ciscoimageindex = None
                self.ciscoimagestring = None
                self._segment_path = lambda: "ciscoImageEntry" + "[ciscoImageIndex='" + str(self.ciscoimageindex) + "']"
                self._absolute_path = lambda: "CISCO-IMAGE-MIB:CISCO-IMAGE-MIB/ciscoImageTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry, ['ciscoimageindex', 'ciscoimagestring'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIMAGEMIB()
        return self._top_entity

