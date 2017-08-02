""" Cisco_IOS_XR_infra_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra package configuration.

This module contains definitions
for the following management objects\:
  banners\: Schema for Banner configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Banner(Enum):
    """
    Banner

    Banner

    .. data:: exec_ = 0

    	Set EXEC process creation banner

    .. data:: incoming = 1

    	Set incoming terminal line banner

    .. data:: motd = 2

    	Set Message of the Day banner

    .. data:: login = 3

    	Set login banner

    .. data:: slip_ppp = 4

    	Set Message for SLIP/PPP

    .. data:: prompt_timeout = 5

    	Set Message for login authentication timeout

    """

    exec_ = Enum.YLeaf(0, "exec")

    incoming = Enum.YLeaf(1, "incoming")

    motd = Enum.YLeaf(2, "motd")

    login = Enum.YLeaf(3, "login")

    slip_ppp = Enum.YLeaf(4, "slip-ppp")

    prompt_timeout = Enum.YLeaf(5, "prompt-timeout")



class Banners(Entity):
    """
    Schema for Banner configuration commands
    
    .. attribute:: banner
    
    	Select a Banner Type
    	**type**\: list of    :py:class:`Banner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg.Banners.Banner>`
    
    

    """

    _prefix = 'infra-infra-cfg'
    _revision = '2016-06-16'

    def __init__(self):
        super(Banners, self).__init__()
        self._top_entity = None

        self.yang_name = "banners"
        self.yang_parent_name = "Cisco-IOS-XR-infra-infra-cfg"

        self.banner = YList(self)

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
                    super(Banners, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Banners, self).__setattr__(name, value)


    class Banner(Entity):
        """
        Select a Banner Type
        
        .. attribute:: banner_name  <key>
        
        	Banner Type
        	**type**\:   :py:class:`Banner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg.Banner>`
        
        .. attribute:: banner_text
        
        	Banner text message
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'infra-infra-cfg'
        _revision = '2016-06-16'

        def __init__(self):
            super(Banners.Banner, self).__init__()

            self.yang_name = "banner"
            self.yang_parent_name = "banners"

            self.banner_name = YLeaf(YType.enumeration, "banner-name")

            self.banner_text = YLeaf(YType.str, "banner-text")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("banner_name",
                            "banner_text") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Banners.Banner, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Banners.Banner, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.banner_name.is_set or
                self.banner_text.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.banner_name.yfilter != YFilter.not_set or
                self.banner_text.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "banner" + "[banner-name='" + self.banner_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-infra-cfg:banners/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.banner_name.is_set or self.banner_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.banner_name.get_name_leafdata())
            if (self.banner_text.is_set or self.banner_text.yfilter != YFilter.not_set):
                leaf_name_data.append(self.banner_text.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "banner-name" or name == "banner-text"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "banner-name"):
                self.banner_name = value
                self.banner_name.value_namespace = name_space
                self.banner_name.value_namespace_prefix = name_space_prefix
            if(value_path == "banner-text"):
                self.banner_text = value
                self.banner_text.value_namespace = name_space
                self.banner_text.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.banner:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.banner:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-infra-cfg:banners" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "banner"):
            for c in self.banner:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Banners.Banner()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.banner.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "banner"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Banners()
        return self._top_entity

