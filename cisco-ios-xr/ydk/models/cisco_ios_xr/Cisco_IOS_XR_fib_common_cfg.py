""" Cisco_IOS_XR_fib_common_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fib\-common package configuration.

This module contains definitions
for the following management objects\:
  fib\: CEF configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class FibPbtsFallback(Enum):
    """
    FibPbtsFallback

    Fib pbts fallback

    .. data:: list = 1

    	Fallback to class number list

    .. data:: any = 2

    	Fallback to any class

    .. data:: drop = 3

    	Fallback to drop

    """

    list = Enum.YLeaf(1, "list")

    any = Enum.YLeaf(2, "any")

    drop = Enum.YLeaf(3, "drop")


class FibPbtsForwardClass(Enum):
    """
    FibPbtsForwardClass

    Fib pbts forward class

    .. data:: any = 8

    	Any class

    """

    any = Enum.YLeaf(8, "any")



class Fib(Entity):
    """
    CEF configuration
    
    .. attribute:: pbts_forward_class_fallbacks
    
    	PBTS class configuration
    	**type**\:   :py:class:`PbtsForwardClassFallbacks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.PbtsForwardClassFallbacks>`
    
    .. attribute:: platform
    
    	FIB platform parameters
    	**type**\:   :py:class:`Platform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.Platform>`
    
    .. attribute:: prefer_aib_routes
    
    	Set options for adjacency routes overriding RIB routes
    	**type**\:  bool
    
    

    """

    _prefix = 'fib-common-cfg'
    _revision = '2017-01-20'

    def __init__(self):
        super(Fib, self).__init__()
        self._top_entity = None

        self.yang_name = "fib"
        self.yang_parent_name = "Cisco-IOS-XR-fib-common-cfg"

        self.prefer_aib_routes = YLeaf(YType.boolean, "prefer-aib-routes")

        self.pbts_forward_class_fallbacks = Fib.PbtsForwardClassFallbacks()
        self.pbts_forward_class_fallbacks.parent = self
        self._children_name_map["pbts_forward_class_fallbacks"] = "pbts-forward-class-fallbacks"
        self._children_yang_names.add("pbts-forward-class-fallbacks")

        self.platform = Fib.Platform()
        self.platform.parent = self
        self._children_name_map["platform"] = "platform"
        self._children_yang_names.add("platform")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("prefer_aib_routes") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Fib, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Fib, self).__setattr__(name, value)


    class PbtsForwardClassFallbacks(Entity):
        """
        PBTS class configuration
        
        .. attribute:: pbts_forward_class_fallback
        
        	Set PBTS class for fallback
        	**type**\: list of    :py:class:`PbtsForwardClassFallback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback>`
        
        

        """

        _prefix = 'fib-common-cfg'
        _revision = '2017-01-20'

        def __init__(self):
            super(Fib.PbtsForwardClassFallbacks, self).__init__()

            self.yang_name = "pbts-forward-class-fallbacks"
            self.yang_parent_name = "fib"

            self.pbts_forward_class_fallback = YList(self)

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
                        super(Fib.PbtsForwardClassFallbacks, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Fib.PbtsForwardClassFallbacks, self).__setattr__(name, value)


        class PbtsForwardClassFallback(Entity):
            """
            Set PBTS class for fallback
            
            .. attribute:: forward_class_number  <key>
            
            	PBTS forward class number
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`FibPbtsForwardClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.FibPbtsForwardClass>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..8
            
            
            ----
            .. attribute:: fallback_class_number_array
            
            	Set PBTS fallback class number array
            	**type**\:  list of int
            
            	**range:** 0..7
            
            .. attribute:: fallback_type
            
            	Set PBTS fallback type
            	**type**\:   :py:class:`FibPbtsFallback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.FibPbtsFallback>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'fib-common-cfg'
            _revision = '2017-01-20'

            def __init__(self):
                super(Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback, self).__init__()

                self.yang_name = "pbts-forward-class-fallback"
                self.yang_parent_name = "pbts-forward-class-fallbacks"

                self.forward_class_number = YLeaf(YType.str, "forward-class-number")

                self.fallback_class_number_array = YLeafList(YType.uint32, "fallback-class-number-array")

                self.fallback_type = YLeaf(YType.enumeration, "fallback-type")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("forward_class_number",
                                "fallback_class_number_array",
                                "fallback_type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.fallback_class_number_array.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.forward_class_number.is_set or
                    self.fallback_type.is_set)

            def has_operation(self):
                for leaf in self.fallback_class_number_array.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.forward_class_number.yfilter != YFilter.not_set or
                    self.fallback_class_number_array.yfilter != YFilter.not_set or
                    self.fallback_type.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pbts-forward-class-fallback" + "[forward-class-number='" + self.forward_class_number.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fib-common-cfg:fib/pbts-forward-class-fallbacks/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.forward_class_number.is_set or self.forward_class_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forward_class_number.get_name_leafdata())
                if (self.fallback_type.is_set or self.fallback_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fallback_type.get_name_leafdata())

                leaf_name_data.extend(self.fallback_class_number_array.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "forward-class-number" or name == "fallback-class-number-array" or name == "fallback-type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "forward-class-number"):
                    self.forward_class_number = value
                    self.forward_class_number.value_namespace = name_space
                    self.forward_class_number.value_namespace_prefix = name_space_prefix
                if(value_path == "fallback-class-number-array"):
                    self.fallback_class_number_array.append(value)
                if(value_path == "fallback-type"):
                    self.fallback_type = value
                    self.fallback_type.value_namespace = name_space
                    self.fallback_type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pbts_forward_class_fallback:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pbts_forward_class_fallback:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pbts-forward-class-fallbacks" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-fib-common-cfg:fib/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pbts-forward-class-fallback"):
                for c in self.pbts_forward_class_fallback:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pbts_forward_class_fallback.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pbts-forward-class-fallback"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Platform(Entity):
        """
        FIB platform parameters
        
        .. attribute:: label_switched_multicast
        
        	Options for label\-switched\-multicast parameters
        	**type**\:   :py:class:`LabelSwitchedMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.Platform.LabelSwitchedMulticast>`
        
        

        """

        _prefix = 'fib-common-cfg'
        _revision = '2017-01-20'

        def __init__(self):
            super(Fib.Platform, self).__init__()

            self.yang_name = "platform"
            self.yang_parent_name = "fib"

            self.label_switched_multicast = Fib.Platform.LabelSwitchedMulticast()
            self.label_switched_multicast.parent = self
            self._children_name_map["label_switched_multicast"] = "label-switched-multicast"
            self._children_yang_names.add("label-switched-multicast")


        class LabelSwitchedMulticast(Entity):
            """
            Options for label\-switched\-multicast parameters
            
            .. attribute:: frr_holdtime
            
            	Set time to keep FRR slots programmed post FRR
            	**type**\:  int
            
            	**range:** 3..180
            
            	**units**\: second
            
            

            """

            _prefix = 'fib-common-cfg'
            _revision = '2017-01-20'

            def __init__(self):
                super(Fib.Platform.LabelSwitchedMulticast, self).__init__()

                self.yang_name = "label-switched-multicast"
                self.yang_parent_name = "platform"

                self.frr_holdtime = YLeaf(YType.uint32, "frr-holdtime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("frr_holdtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Fib.Platform.LabelSwitchedMulticast, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Fib.Platform.LabelSwitchedMulticast, self).__setattr__(name, value)

            def has_data(self):
                return self.frr_holdtime.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.frr_holdtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "label-switched-multicast" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fib-common-cfg:fib/platform/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.frr_holdtime.is_set or self.frr_holdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frr_holdtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "frr-holdtime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "frr-holdtime"):
                    self.frr_holdtime = value
                    self.frr_holdtime.value_namespace = name_space
                    self.frr_holdtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.label_switched_multicast is not None and self.label_switched_multicast.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.label_switched_multicast is not None and self.label_switched_multicast.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "platform" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-fib-common-cfg:fib/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "label-switched-multicast"):
                if (self.label_switched_multicast is None):
                    self.label_switched_multicast = Fib.Platform.LabelSwitchedMulticast()
                    self.label_switched_multicast.parent = self
                    self._children_name_map["label_switched_multicast"] = "label-switched-multicast"
                return self.label_switched_multicast

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "label-switched-multicast"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.prefer_aib_routes.is_set or
            (self.pbts_forward_class_fallbacks is not None and self.pbts_forward_class_fallbacks.has_data()) or
            (self.platform is not None and self.platform.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.prefer_aib_routes.yfilter != YFilter.not_set or
            (self.pbts_forward_class_fallbacks is not None and self.pbts_forward_class_fallbacks.has_operation()) or
            (self.platform is not None and self.platform.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-fib-common-cfg:fib" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.prefer_aib_routes.is_set or self.prefer_aib_routes.yfilter != YFilter.not_set):
            leaf_name_data.append(self.prefer_aib_routes.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "pbts-forward-class-fallbacks"):
            if (self.pbts_forward_class_fallbacks is None):
                self.pbts_forward_class_fallbacks = Fib.PbtsForwardClassFallbacks()
                self.pbts_forward_class_fallbacks.parent = self
                self._children_name_map["pbts_forward_class_fallbacks"] = "pbts-forward-class-fallbacks"
            return self.pbts_forward_class_fallbacks

        if (child_yang_name == "platform"):
            if (self.platform is None):
                self.platform = Fib.Platform()
                self.platform.parent = self
                self._children_name_map["platform"] = "platform"
            return self.platform

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "pbts-forward-class-fallbacks" or name == "platform" or name == "prefer-aib-routes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "prefer-aib-routes"):
            self.prefer_aib_routes = value
            self.prefer_aib_routes.value_namespace = name_space
            self.prefer_aib_routes.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Fib()
        return self._top_entity

