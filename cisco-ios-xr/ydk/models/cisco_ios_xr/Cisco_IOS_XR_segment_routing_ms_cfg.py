""" Cisco_IOS_XR_segment_routing_ms_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package configuration.

This module contains definitions
for the following management objects\:
  sr\: Segment Routing

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SrmsMiFlag(Enum):
    """
    SrmsMiFlag

    Srms mi flag

    .. data:: disable = 0

    	Disable flag

    .. data:: enable = 1

    	Enable flag

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")



class Sr(Entity):
    """
    Segment Routing
    
    .. attribute:: enable
    
    	enable SR
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: global_block
    
    	Global Block Segment Routing
    	**type**\:   :py:class:`GlobalBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.GlobalBlock>`
    
    	**presence node**\: True
    
    .. attribute:: local_block
    
    	Segment Routing Local Block of Labels
    	**type**\:   :py:class:`LocalBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.LocalBlock>`
    
    	**presence node**\: True
    
    .. attribute:: mappings
    
    	Mapping Server
    	**type**\:   :py:class:`Mappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Mappings>`
    
    

    """

    _prefix = 'segment-routing-ms-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sr, self).__init__()
        self._top_entity = None

        self.yang_name = "sr"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"global-block" : ("global_block", Sr.GlobalBlock), "local-block" : ("local_block", Sr.LocalBlock), "mappings" : ("mappings", Sr.Mappings)}
        self._child_list_classes = {}

        self.enable = YLeaf(YType.empty, "enable")

        self.global_block = None
        self._children_name_map["global_block"] = "global-block"
        self._children_yang_names.add("global-block")

        self.local_block = None
        self._children_name_map["local_block"] = "local-block"
        self._children_yang_names.add("local-block")

        self.mappings = Sr.Mappings()
        self.mappings.parent = self
        self._children_name_map["mappings"] = "mappings"
        self._children_yang_names.add("mappings")
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr"

    def __setattr__(self, name, value):
        self._perform_setattr(Sr, ['enable'], name, value)


    class GlobalBlock(Entity):
        """
        Global Block Segment Routing
        
        .. attribute:: lower_bound
        
        	SRGB Lower Bound
        	**type**\:  int
        
        	**range:** 16000..1048574
        
        	**mandatory**\: True
        
        .. attribute:: upper_bound
        
        	SRGB Upper Bound
        	**type**\:  int
        
        	**range:** 16001..1048575
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sr.GlobalBlock, self).__init__()

            self.yang_name = "global-block"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.lower_bound = YLeaf(YType.uint32, "lower-bound")

            self.upper_bound = YLeaf(YType.uint32, "upper-bound")
            self._segment_path = lambda: "global-block"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.GlobalBlock, ['lower_bound', 'upper_bound'], name, value)


    class LocalBlock(Entity):
        """
        Segment Routing Local Block of Labels
        
        .. attribute:: lower_bound
        
        	SRLB Lower Bound
        	**type**\:  int
        
        	**range:** 15000..1048574
        
        	**mandatory**\: True
        
        .. attribute:: upper_bound
        
        	SRLB Upper Bound
        	**type**\:  int
        
        	**range:** 15001..1048575
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sr.LocalBlock, self).__init__()

            self.yang_name = "local-block"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.lower_bound = YLeaf(YType.uint32, "lower-bound")

            self.upper_bound = YLeaf(YType.uint32, "upper-bound")
            self._segment_path = lambda: "local-block"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.LocalBlock, ['lower_bound', 'upper_bound'], name, value)


    class Mappings(Entity):
        """
        Mapping Server
        
        .. attribute:: mapping
        
        	IP prefix to SID mapping
        	**type**\: list of    :py:class:`Mapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Mappings.Mapping>`
        
        

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sr.Mappings, self).__init__()

            self.yang_name = "mappings"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"mapping" : ("mapping", Sr.Mappings.Mapping)}

            self.mapping = YList(self)
            self._segment_path = lambda: "mappings"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.Mappings, [], name, value)


        class Mapping(Entity):
            """
            IP prefix to SID mapping
            
            .. attribute:: af  <key>
            
            	Address Family
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ip  <key>
            
            	IP prefix
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: mask  <key>
            
            	Mask
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: flag_attached
            
            	Enable/Disable Attached flag
            	**type**\:   :py:class:`SrmsMiFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.SrmsMiFlag>`
            
            .. attribute:: sid_range
            
            	Range (number of SIDs)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sid_start
            
            	Start of SID index range
            	**type**\:  int
            
            	**range:** 0..1048575
            
            

            """

            _prefix = 'segment-routing-ms-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sr.Mappings.Mapping, self).__init__()

                self.yang_name = "mapping"
                self.yang_parent_name = "mappings"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.af = YLeaf(YType.str, "af")

                self.ip = YLeaf(YType.str, "ip")

                self.mask = YLeaf(YType.int32, "mask")

                self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                self.sid_range = YLeaf(YType.int32, "sid-range")

                self.sid_start = YLeaf(YType.uint32, "sid-start")
                self._segment_path = lambda: "mapping" + "[af='" + self.af.get() + "']" + "[ip='" + self.ip.get() + "']" + "[mask='" + self.mask.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/mappings/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.Mappings.Mapping, ['af', 'ip', 'mask', 'flag_attached', 'sid_range', 'sid_start'], name, value)

    def clone_ptr(self):
        self._top_entity = Sr()
        return self._top_entity

