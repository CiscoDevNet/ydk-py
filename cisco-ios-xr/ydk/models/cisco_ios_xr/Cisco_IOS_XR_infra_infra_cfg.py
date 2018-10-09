""" Cisco_IOS_XR_infra_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra package configuration.

This module contains definitions
for the following management objects\:
  banners\: Schema for Banner configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Banner(Enum):
    """
    Banner (Enum Class)

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
    	**type**\: list of  		 :py:class:`Banner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg.Banners.Banner>`
    
    

    """

    _prefix = 'infra-infra-cfg'
    _revision = '2016-06-16'

    def __init__(self):
        super(Banners, self).__init__()
        self._top_entity = None

        self.yang_name = "banners"
        self.yang_parent_name = "Cisco-IOS-XR-infra-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("banner", ("banner", Banners.Banner))])
        self._leafs = OrderedDict()

        self.banner = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-infra-infra-cfg:banners"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Banners, [], name, value)


    class Banner(Entity):
        """
        Select a Banner Type
        
        .. attribute:: banner_name  (key)
        
        	Banner Type
        	**type**\:  :py:class:`Banner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg.Banner>`
        
        .. attribute:: banner_text
        
        	Banner text message
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'infra-infra-cfg'
        _revision = '2016-06-16'

        def __init__(self):
            super(Banners.Banner, self).__init__()

            self.yang_name = "banner"
            self.yang_parent_name = "banners"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['banner_name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('banner_name', (YLeaf(YType.enumeration, 'banner-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg', 'Banner', '')])),
                ('banner_text', (YLeaf(YType.str, 'banner-text'), ['str'])),
            ])
            self.banner_name = None
            self.banner_text = None
            self._segment_path = lambda: "banner" + "[banner-name='" + str(self.banner_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-infra-cfg:banners/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Banners.Banner, ['banner_name', 'banner_text'], name, value)

    def clone_ptr(self):
        self._top_entity = Banners()
        return self._top_entity

