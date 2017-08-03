""" Cisco_IOS_XR_segment_routing_ms_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package configuration.

This module contains definitions
for the following management objects\:
  sr\: Segment Routing

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.enable = YLeaf(YType.empty, "enable")

        self.global_block = None
        self._children_name_map["global_block"] = "global-block"
        self._children_yang_names.add("global-block")

        self.mappings = Sr.Mappings()
        self.mappings.parent = self
        self._children_name_map["mappings"] = "mappings"
        self._children_yang_names.add("mappings")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Sr, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Sr, self).__setattr__(name, value)


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
            self.is_presence_container = True

            self.lower_bound = YLeaf(YType.uint32, "lower-bound")

            self.upper_bound = YLeaf(YType.uint32, "upper-bound")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("lower_bound",
                            "upper_bound") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Sr.GlobalBlock, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Sr.GlobalBlock, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.lower_bound.is_set or
                self.upper_bound.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.lower_bound.yfilter != YFilter.not_set or
                self.upper_bound.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global-block" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.lower_bound.is_set or self.lower_bound.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lower_bound.get_name_leafdata())
            if (self.upper_bound.is_set or self.upper_bound.yfilter != YFilter.not_set):
                leaf_name_data.append(self.upper_bound.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lower-bound" or name == "upper-bound"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "lower-bound"):
                self.lower_bound = value
                self.lower_bound.value_namespace = name_space
                self.lower_bound.value_namespace_prefix = name_space_prefix
            if(value_path == "upper-bound"):
                self.upper_bound = value
                self.upper_bound.value_namespace = name_space
                self.upper_bound.value_namespace_prefix = name_space_prefix


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

            self.mapping = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Sr.Mappings, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Sr.Mappings, self).__setattr__(name, value)


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

                self.af = YLeaf(YType.str, "af")

                self.ip = YLeaf(YType.str, "ip")

                self.mask = YLeaf(YType.int32, "mask")

                self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                self.sid_range = YLeaf(YType.int32, "sid-range")

                self.sid_start = YLeaf(YType.uint32, "sid-start")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("af",
                                "ip",
                                "mask",
                                "flag_attached",
                                "sid_range",
                                "sid_start") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Sr.Mappings.Mapping, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sr.Mappings.Mapping, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.af.is_set or
                    self.ip.is_set or
                    self.mask.is_set or
                    self.flag_attached.is_set or
                    self.sid_range.is_set or
                    self.sid_start.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.af.yfilter != YFilter.not_set or
                    self.ip.yfilter != YFilter.not_set or
                    self.mask.yfilter != YFilter.not_set or
                    self.flag_attached.yfilter != YFilter.not_set or
                    self.sid_range.yfilter != YFilter.not_set or
                    self.sid_start.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mapping" + "[af='" + self.af.get() + "']" + "[ip='" + self.ip.get() + "']" + "[mask='" + self.mask.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-segment-routing-ms-cfg:sr/mappings/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.af.is_set or self.af.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.af.get_name_leafdata())
                if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip.get_name_leafdata())
                if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mask.get_name_leafdata())
                if (self.flag_attached.is_set or self.flag_attached.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flag_attached.get_name_leafdata())
                if (self.sid_range.is_set or self.sid_range.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sid_range.get_name_leafdata())
                if (self.sid_start.is_set or self.sid_start.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sid_start.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "af" or name == "ip" or name == "mask" or name == "flag-attached" or name == "sid-range" or name == "sid-start"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "af"):
                    self.af = value
                    self.af.value_namespace = name_space
                    self.af.value_namespace_prefix = name_space_prefix
                if(value_path == "ip"):
                    self.ip = value
                    self.ip.value_namespace = name_space
                    self.ip.value_namespace_prefix = name_space_prefix
                if(value_path == "mask"):
                    self.mask = value
                    self.mask.value_namespace = name_space
                    self.mask.value_namespace_prefix = name_space_prefix
                if(value_path == "flag-attached"):
                    self.flag_attached = value
                    self.flag_attached.value_namespace = name_space
                    self.flag_attached.value_namespace_prefix = name_space_prefix
                if(value_path == "sid-range"):
                    self.sid_range = value
                    self.sid_range.value_namespace = name_space
                    self.sid_range.value_namespace_prefix = name_space_prefix
                if(value_path == "sid-start"):
                    self.sid_start = value
                    self.sid_start.value_namespace = name_space
                    self.sid_start.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mapping:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mapping:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mappings" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mapping"):
                for c in self.mapping:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Sr.Mappings.Mapping()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mapping.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mapping"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.enable.is_set or
            (self.mappings is not None and self.mappings.has_data()) or
            (self.global_block is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            (self.global_block is not None and self.global_block.has_operation()) or
            (self.mappings is not None and self.mappings.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-segment-routing-ms-cfg:sr" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "global-block"):
            if (self.global_block is None):
                self.global_block = Sr.GlobalBlock()
                self.global_block.parent = self
                self._children_name_map["global_block"] = "global-block"
            return self.global_block

        if (child_yang_name == "mappings"):
            if (self.mappings is None):
                self.mappings = Sr.Mappings()
                self.mappings.parent = self
                self._children_name_map["mappings"] = "mappings"
            return self.mappings

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "global-block" or name == "mappings" or name == "enable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Sr()
        return self._top_entity

