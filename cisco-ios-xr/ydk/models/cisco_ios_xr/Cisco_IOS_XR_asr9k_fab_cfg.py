""" Cisco_IOS_XR_asr9k_fab_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-fab package configuration.

This module contains definitions
for the following management objects\:
  fab\-vqi\-config\: Configure Fabric Operation Mode

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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



class Asr9kFabMode(Enum):
    """
    Asr9kFabMode (Enum Class)

    Asr9k fab mode

    .. data:: highbandwidth = 1

    	High bandwidth mode

    .. data:: a99_highbandwidth = 2

    	A99 High bandwidth mode

    """

    highbandwidth = Enum.YLeaf(1, "highbandwidth")

    a99_highbandwidth = Enum.YLeaf(2, "a99-highbandwidth")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fab_cfg as meta
        return meta._meta_table['Asr9kFabMode']



class FabVqiConfig(_Entity_):
    """
    Configure Fabric Operation Mode
    
    .. attribute:: mode
    
    	Mode Type
    	**type**\:  :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg.FabVqiConfig.Mode>`
    
    

    """

    _prefix = 'asr9k-fab-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(FabVqiConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "fab-vqi-config"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-fab-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mode", ("mode", FabVqiConfig.Mode))])
        self._leafs = OrderedDict()

        self.mode = FabVqiConfig.Mode()
        self.mode.parent = self
        self._children_name_map["mode"] = "mode"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fab-cfg:fab-vqi-config"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FabVqiConfig, [], name, value)


    class Mode(_Entity_):
        """
        Mode Type
        
        .. attribute:: fab_mode_type_xr
        
        	Mode Type
        	**type**\:  :py:class:`Asr9kFabMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg.Asr9kFabMode>`
        
        .. attribute:: fab_mode_type
        
        	Mode Type
        	**type**\:  :py:class:`Asr9kFabMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg.Asr9kFabMode>`
        
        

        """

        _prefix = 'asr9k-fab-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(FabVqiConfig.Mode, self).__init__()

            self.yang_name = "mode"
            self.yang_parent_name = "fab-vqi-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('fab_mode_type_xr', (YLeaf(YType.enumeration, 'fab-mode-type-xr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg', 'Asr9kFabMode', '')])),
                ('fab_mode_type', (YLeaf(YType.enumeration, 'fab-mode-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg', 'Asr9kFabMode', '')])),
            ])
            self.fab_mode_type_xr = None
            self.fab_mode_type = None
            self._segment_path = lambda: "mode"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-fab-cfg:fab-vqi-config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FabVqiConfig.Mode, ['fab_mode_type_xr', 'fab_mode_type'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fab_cfg as meta
            return meta._meta_table['FabVqiConfig.Mode']['meta_info']

    def clone_ptr(self):
        self._top_entity = FabVqiConfig()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fab_cfg as meta
        return meta._meta_table['FabVqiConfig']['meta_info']


