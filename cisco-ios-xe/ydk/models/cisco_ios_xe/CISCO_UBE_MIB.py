""" CISCO_UBE_MIB 

This MIB describes objects used for managing Cisco
Unified Border Element (CUBE).

The Cisco Unified Border Element (CUBE) is a Cisco 
IOS Session Border Controller (SBC) that interconnects
independent voice over IP (VoIP) and video over IP 
networks for data, voice, and video transport

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOUBEMIB(Entity):
    """
    
    
    .. attribute:: ciscoubemibobjects
    
    	
    	**type**\:  :py:class:`Ciscoubemibobjects <ydk.models.cisco_ios_xe.CISCO_UBE_MIB.CISCOUBEMIB.Ciscoubemibobjects>`
    
    

    """

    _prefix = 'CISCO-UBE-MIB'
    _revision = '2010-11-29'

    def __init__(self):
        super(CISCOUBEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-UBE-MIB"
        self.yang_parent_name = "CISCO-UBE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ciscoUbeMIBObjects", ("ciscoubemibobjects", CISCOUBEMIB.Ciscoubemibobjects))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ciscoubemibobjects = CISCOUBEMIB.Ciscoubemibobjects()
        self.ciscoubemibobjects.parent = self
        self._children_name_map["ciscoubemibobjects"] = "ciscoUbeMIBObjects"
        self._children_yang_names.add("ciscoUbeMIBObjects")
        self._segment_path = lambda: "CISCO-UBE-MIB:CISCO-UBE-MIB"


    class Ciscoubemibobjects(Entity):
        """
        
        
        .. attribute:: cubeenabled
        
        	This object represents, whether the Cisco Unified Border Element (CUBE) is enabled  on the device or not.  The value 'true' means that the CUBE feature  is enabled on the device.  The value 'false' means that the CUBE feature  is disabled
        	**type**\: bool
        
        .. attribute:: cubeversion
        
        	This object represents the version of Cisco Unified Border Element on the device
        	**type**\: str
        
        .. attribute:: cubetotalsessionallowed
        
        	This object provides the total number of CUBE session allowed on the device. The value zero  means no sessions are allowed with CUBE
        	**type**\: int
        
        	**range:** 0..999999
        
        	**units**\: session
        
        

        """

        _prefix = 'CISCO-UBE-MIB'
        _revision = '2010-11-29'

        def __init__(self):
            super(CISCOUBEMIB.Ciscoubemibobjects, self).__init__()

            self.yang_name = "ciscoUbeMIBObjects"
            self.yang_parent_name = "CISCO-UBE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cubeenabled', YLeaf(YType.boolean, 'cubeEnabled')),
                ('cubeversion', YLeaf(YType.str, 'cubeVersion')),
                ('cubetotalsessionallowed', YLeaf(YType.uint32, 'cubeTotalSessionAllowed')),
            ])
            self.cubeenabled = None
            self.cubeversion = None
            self.cubetotalsessionallowed = None
            self._segment_path = lambda: "ciscoUbeMIBObjects"
            self._absolute_path = lambda: "CISCO-UBE-MIB:CISCO-UBE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOUBEMIB.Ciscoubemibobjects, ['cubeenabled', 'cubeversion', 'cubetotalsessionallowed'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOUBEMIB()
        return self._top_entity

