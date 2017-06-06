""" Cisco_IOS_XR_mpls_oam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-oam package configuration.

This module contains definitions
for the following management objects\:
  mpls\-oam\: MPLS LSP verification configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MplsOam(object):
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
        self.disable_vendor_extension = None
        self.enable_oam = None
        self.reply_mode = MplsOam.ReplyMode()
        self.reply_mode.parent = self


    class ReplyMode(object):
        """
        Echo request reply mode attributes
        
        .. attribute:: control_channel
        
        	Configure control channel reply mode
        	**type**\:   :py:class:`ControlChannel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg.MplsOam.ReplyMode.ControlChannel>`
        
        

        """

        _prefix = 'mpls-oam-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.control_channel = MplsOam.ReplyMode.ControlChannel()
            self.control_channel.parent = self


        class ControlChannel(object):
            """
            Configure control channel reply mode
            
            .. attribute:: allow_reverse_lsp
            
            	Use Reverse LSP as the control channel
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.allow_reverse_lsp = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-cfg:mpls-oam/Cisco-IOS-XR-mpls-oam-cfg:reply-mode/Cisco-IOS-XR-mpls-oam-cfg:control-channel'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.allow_reverse_lsp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_cfg as meta
                return meta._meta_table['MplsOam.ReplyMode.ControlChannel']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-oam-cfg:mpls-oam/Cisco-IOS-XR-mpls-oam-cfg:reply-mode'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.control_channel is not None and self.control_channel._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_cfg as meta
            return meta._meta_table['MplsOam.ReplyMode']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-oam-cfg:mpls-oam'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.disable_vendor_extension is not None:
            return True

        if self.enable_oam is not None:
            return True

        if self.reply_mode is not None and self.reply_mode._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_cfg as meta
        return meta._meta_table['MplsOam']['meta_info']


