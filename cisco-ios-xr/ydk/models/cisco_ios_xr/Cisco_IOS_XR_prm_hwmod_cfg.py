""" Cisco_IOS_XR_prm_hwmod_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR prm\-hwmod package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: HardwareModule

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



class UrpfConfig(Enum):
    """
    UrpfConfig (Enum Class)

    Urpf config

    .. data:: disable = 0

    	Urpf Disable

    .. data:: enable = 1

    	Urpf Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_hwmod_cfg as meta
        return meta._meta_table['UrpfConfig']



class HardwareModule(_Entity_):
    """
    HardwareModule
    
    .. attribute:: loadbalancing
    
    	Loadbalance option
    	**type**\:  :py:class:`Loadbalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg.HardwareModule.Loadbalancing>`
    
    .. attribute:: urpf
    
    	Enabled Disabled
    	**type**\:  :py:class:`UrpfConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg.UrpfConfig>`
    
    

    """

    _prefix = 'prm-hwmod-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-prm-hwmod-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("loadbalancing", ("loadbalancing", HardwareModule.Loadbalancing))])
        self._leafs = OrderedDict([
            ('urpf', (YLeaf(YType.enumeration, 'urpf'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg', 'UrpfConfig', '')])),
        ])
        self.urpf = None

        self.loadbalancing = HardwareModule.Loadbalancing()
        self.loadbalancing.parent = self
        self._children_name_map["loadbalancing"] = "loadbalancing"
        self._segment_path = lambda: "Cisco-IOS-XR-prm-hwmod-cfg:hardware-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModule, ['urpf'], name, value)


    class Loadbalancing(_Entity_):
        """
        Loadbalance option
        
        .. attribute:: bgp3107
        
        	BGP LU
        	**type**\:  :py:class:`Bgp3107 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg.HardwareModule.Loadbalancing.Bgp3107>`
        
        

        """

        _prefix = 'prm-hwmod-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(HardwareModule.Loadbalancing, self).__init__()

            self.yang_name = "loadbalancing"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("bgp3107", ("bgp3107", HardwareModule.Loadbalancing.Bgp3107))])
            self._leafs = OrderedDict()

            self.bgp3107 = HardwareModule.Loadbalancing.Bgp3107()
            self.bgp3107.parent = self
            self._children_name_map["bgp3107"] = "bgp3107"
            self._segment_path = lambda: "loadbalancing"
            self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-cfg:hardware-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModule.Loadbalancing, [], name, value)


        class Bgp3107(_Entity_):
            """
            BGP LU
            
            .. attribute:: ecmp
            
            	ECMP 
            	**type**\:  :py:class:`Ecmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg.HardwareModule.Loadbalancing.Bgp3107.Ecmp>`
            
            

            """

            _prefix = 'prm-hwmod-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(HardwareModule.Loadbalancing.Bgp3107, self).__init__()

                self.yang_name = "bgp3107"
                self.yang_parent_name = "loadbalancing"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ecmp", ("ecmp", HardwareModule.Loadbalancing.Bgp3107.Ecmp))])
                self._leafs = OrderedDict()

                self.ecmp = HardwareModule.Loadbalancing.Bgp3107.Ecmp()
                self.ecmp.parent = self
                self._children_name_map["ecmp"] = "ecmp"
                self._segment_path = lambda: "bgp3107"
                self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-cfg:hardware-module/loadbalancing/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModule.Loadbalancing.Bgp3107, [], name, value)


            class Ecmp(_Entity_):
                """
                ECMP 
                
                .. attribute:: enable
                
                	Enable Option
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'prm-hwmod-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(HardwareModule.Loadbalancing.Bgp3107.Ecmp, self).__init__()

                    self.yang_name = "ecmp"
                    self.yang_parent_name = "bgp3107"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None
                    self._segment_path = lambda: "ecmp"
                    self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-cfg:hardware-module/loadbalancing/bgp3107/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Loadbalancing.Bgp3107.Ecmp, ['enable'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_hwmod_cfg as meta
                    return meta._meta_table['HardwareModule.Loadbalancing.Bgp3107.Ecmp']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_hwmod_cfg as meta
                return meta._meta_table['HardwareModule.Loadbalancing.Bgp3107']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_hwmod_cfg as meta
            return meta._meta_table['HardwareModule.Loadbalancing']['meta_info']

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_hwmod_cfg as meta
        return meta._meta_table['HardwareModule']['meta_info']


