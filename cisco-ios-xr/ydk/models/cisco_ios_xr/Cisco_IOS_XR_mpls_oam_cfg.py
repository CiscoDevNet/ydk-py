""" Cisco_IOS_XR_mpls_oam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-oam package configuration.

This module contains definitions
for the following management objects\:
  mpls\-oam\: MPLS LSP verification configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class MplsOam(Entity):
    """
    MPLS LSP verification configuration
    
    .. attribute:: reply_mode
    
    	Echo request reply mode attributes
    	**type**\:  :py:class:`ReplyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg.MplsOam.ReplyMode>`
    
    .. attribute:: enable_oam
    
    	Enable/Disable MPLS OAM globally.Without creating this object the MPLS OAM feature will not be enabled. Deleting this object will stop the MPLS OAM feature
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: disable_vendor_extension
    
    	Disable vendor extension
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'mpls-oam-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsOam, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-oam"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-oam-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("reply-mode", ("reply_mode", MplsOam.ReplyMode))])
        self._leafs = OrderedDict([
            ('enable_oam', (YLeaf(YType.empty, 'enable-oam'), ['Empty'])),
            ('disable_vendor_extension', (YLeaf(YType.empty, 'disable-vendor-extension'), ['Empty'])),
        ])
        self.enable_oam = None
        self.disable_vendor_extension = None

        self.reply_mode = MplsOam.ReplyMode()
        self.reply_mode.parent = self
        self._children_name_map["reply_mode"] = "reply-mode"
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-oam-cfg:mpls-oam"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsOam, ['enable_oam', 'disable_vendor_extension'], name, value)


    class ReplyMode(Entity):
        """
        Echo request reply mode attributes
        
        .. attribute:: control_channel
        
        	Configure control channel reply mode
        	**type**\:  :py:class:`ControlChannel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg.MplsOam.ReplyMode.ControlChannel>`
        
        

        """

        _prefix = 'mpls-oam-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsOam.ReplyMode, self).__init__()

            self.yang_name = "reply-mode"
            self.yang_parent_name = "mpls-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("control-channel", ("control_channel", MplsOam.ReplyMode.ControlChannel))])
            self._leafs = OrderedDict()

            self.control_channel = MplsOam.ReplyMode.ControlChannel()
            self.control_channel.parent = self
            self._children_name_map["control_channel"] = "control-channel"
            self._segment_path = lambda: "reply-mode"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-cfg:mpls-oam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsOam.ReplyMode, [], name, value)


        class ControlChannel(Entity):
            """
            Configure control channel reply mode
            
            .. attribute:: allow_reverse_lsp
            
            	Use Reverse LSP as the control channel
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.ReplyMode.ControlChannel, self).__init__()

                self.yang_name = "control-channel"
                self.yang_parent_name = "reply-mode"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('allow_reverse_lsp', (YLeaf(YType.empty, 'allow-reverse-lsp'), ['Empty'])),
                ])
                self.allow_reverse_lsp = None
                self._segment_path = lambda: "control-channel"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-cfg:mpls-oam/reply-mode/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.ReplyMode.ControlChannel, ['allow_reverse_lsp'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsOam()
        return self._top_entity

