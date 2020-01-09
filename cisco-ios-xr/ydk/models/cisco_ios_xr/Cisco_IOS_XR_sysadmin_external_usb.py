""" Cisco_IOS_XR_sysadmin_external_usb 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the top level container for
all 'external\-usb' commands for Sysadmin.

Copyright(c) 2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ExternalUsb(_Entity_):
    """
    
    
    .. attribute:: config
    
    	
    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_external_usb.ExternalUsb.Config>`
    
    

    """

    _prefix = 'extusbconf'
    _revision = '2017-04-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ExternalUsb, self).__init__()
        self._top_entity = None

        self.yang_name = "external-usb"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-external-usb"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", ExternalUsb.Config))])
        self._leafs = OrderedDict()

        self.config = ExternalUsb.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-external-usb:external-usb"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ExternalUsb, [], name, value)


    class Config(_Entity_):
        """
        
        
        .. attribute:: disable
        
        	
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'extusbconf'
        _revision = '2017-04-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ExternalUsb.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "external-usb"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
            ])
            self.disable = None
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-external-usb:external-usb/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ExternalUsb.Config, ['disable'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_external_usb as meta
            return meta._meta_table['ExternalUsb.Config']['meta_info']

    def clone_ptr(self):
        self._top_entity = ExternalUsb()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_external_usb as meta
        return meta._meta_table['ExternalUsb']['meta_info']


