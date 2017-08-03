""" Cisco_IOS_XR_mpls_oam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-oam package configuration.

This module contains definitions
for the following management objects\:
  mpls\-oam\: MPLS LSP verification configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsOam(Entity):
    """
    MPLS LSP verification configuration
    
    .. attribute:: disable_vendor_extension
    
    	Disable vendor extension
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable_oam
    
    	Enable/Disable MPLS OAM globally.Without creating this object the MPLS OAM feature will not be enabled. Deleting this object will stop the MPLS OAM feature
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: reply_mode
    
    	Echo request reply mode attributes
    	**type**\:   :py:class:`ReplyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg.MplsOam.ReplyMode>`
    
    

    """

    _prefix = 'mpls-oam-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsOam, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-oam"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-oam-cfg"

        self.disable_vendor_extension = YLeaf(YType.empty, "disable-vendor-extension")

        self.enable_oam = YLeaf(YType.empty, "enable-oam")

        self.reply_mode = MplsOam.ReplyMode()
        self.reply_mode.parent = self
        self._children_name_map["reply_mode"] = "reply-mode"
        self._children_yang_names.add("reply-mode")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("disable_vendor_extension",
                        "enable_oam") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(MplsOam, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MplsOam, self).__setattr__(name, value)


    class ReplyMode(Entity):
        """
        Echo request reply mode attributes
        
        .. attribute:: control_channel
        
        	Configure control channel reply mode
        	**type**\:   :py:class:`ControlChannel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg.MplsOam.ReplyMode.ControlChannel>`
        
        

        """

        _prefix = 'mpls-oam-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsOam.ReplyMode, self).__init__()

            self.yang_name = "reply-mode"
            self.yang_parent_name = "mpls-oam"

            self.control_channel = MplsOam.ReplyMode.ControlChannel()
            self.control_channel.parent = self
            self._children_name_map["control_channel"] = "control-channel"
            self._children_yang_names.add("control-channel")


        class ControlChannel(Entity):
            """
            Configure control channel reply mode
            
            .. attribute:: allow_reverse_lsp
            
            	Use Reverse LSP as the control channel
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.ReplyMode.ControlChannel, self).__init__()

                self.yang_name = "control-channel"
                self.yang_parent_name = "reply-mode"

                self.allow_reverse_lsp = YLeaf(YType.empty, "allow-reverse-lsp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("allow_reverse_lsp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsOam.ReplyMode.ControlChannel, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsOam.ReplyMode.ControlChannel, self).__setattr__(name, value)

            def has_data(self):
                return self.allow_reverse_lsp.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.allow_reverse_lsp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "control-channel" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-cfg:mpls-oam/reply-mode/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.allow_reverse_lsp.is_set or self.allow_reverse_lsp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.allow_reverse_lsp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "allow-reverse-lsp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "allow-reverse-lsp"):
                    self.allow_reverse_lsp = value
                    self.allow_reverse_lsp.value_namespace = name_space
                    self.allow_reverse_lsp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.control_channel is not None and self.control_channel.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.control_channel is not None and self.control_channel.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "reply-mode" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-oam-cfg:mpls-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "control-channel"):
                if (self.control_channel is None):
                    self.control_channel = MplsOam.ReplyMode.ControlChannel()
                    self.control_channel.parent = self
                    self._children_name_map["control_channel"] = "control-channel"
                return self.control_channel

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "control-channel"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.disable_vendor_extension.is_set or
            self.enable_oam.is_set or
            (self.reply_mode is not None and self.reply_mode.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.disable_vendor_extension.yfilter != YFilter.not_set or
            self.enable_oam.yfilter != YFilter.not_set or
            (self.reply_mode is not None and self.reply_mode.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-mpls-oam-cfg:mpls-oam" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.disable_vendor_extension.is_set or self.disable_vendor_extension.yfilter != YFilter.not_set):
            leaf_name_data.append(self.disable_vendor_extension.get_name_leafdata())
        if (self.enable_oam.is_set or self.enable_oam.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable_oam.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "reply-mode"):
            if (self.reply_mode is None):
                self.reply_mode = MplsOam.ReplyMode()
                self.reply_mode.parent = self
                self._children_name_map["reply_mode"] = "reply-mode"
            return self.reply_mode

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "reply-mode" or name == "disable-vendor-extension" or name == "enable-oam"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "disable-vendor-extension"):
            self.disable_vendor_extension = value
            self.disable_vendor_extension.value_namespace = name_space
            self.disable_vendor_extension.value_namespace_prefix = name_space_prefix
        if(value_path == "enable-oam"):
            self.enable_oam = value
            self.enable_oam.value_namespace = name_space
            self.enable_oam.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = MplsOam()
        return self._top_entity

