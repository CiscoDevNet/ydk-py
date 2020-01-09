""" Cisco_IOS_XR_hwmod_bcc_disable_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR hwmod\-bcc\-disable package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\-bcc\-disable\: HW module BCC Disable config

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




class HardwareModuleBccDisable(_Entity_):
    """
    HW module BCC Disable config
    
    .. attribute:: bcc
    
    	bundle configuration
    	**type**\:  :py:class:`Bcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg.HardwareModuleBccDisable.Bcc>`
    
    

    """

    _prefix = 'hwmod-bcc-disable-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(HardwareModuleBccDisable, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-bcc-disable"
        self.yang_parent_name = "Cisco-IOS-XR-hwmod-bcc-disable-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("bcc", ("bcc", HardwareModuleBccDisable.Bcc))])
        self._leafs = OrderedDict()

        self.bcc = HardwareModuleBccDisable.Bcc()
        self.bcc.parent = self
        self._children_name_map["bcc"] = "bcc"
        self._segment_path = lambda: "Cisco-IOS-XR-hwmod-bcc-disable-cfg:hardware-module-bcc-disable"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModuleBccDisable, [], name, value)


    class Bcc(_Entity_):
        """
        bundle configuration
        
        .. attribute:: node
        
        	Node
        	**type**\:  :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg.HardwareModuleBccDisable.Bcc.Node>`
        
        

        """

        _prefix = 'hwmod-bcc-disable-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(HardwareModuleBccDisable.Bcc, self).__init__()

            self.yang_name = "bcc"
            self.yang_parent_name = "hardware-module-bcc-disable"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", HardwareModuleBccDisable.Bcc.Node))])
            self._leafs = OrderedDict()

            self.node = HardwareModuleBccDisable.Bcc.Node()
            self.node.parent = self
            self._children_name_map["node"] = "node"
            self._segment_path = lambda: "bcc"
            self._absolute_path = lambda: "Cisco-IOS-XR-hwmod-bcc-disable-cfg:hardware-module-bcc-disable/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModuleBccDisable.Bcc, [], name, value)


        class Node(_Entity_):
            """
            Node
            
            .. attribute:: all
            
            	all node configuration
            	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg.HardwareModuleBccDisable.Bcc.Node.All>`
            
            

            """

            _prefix = 'hwmod-bcc-disable-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(HardwareModuleBccDisable.Bcc.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "bcc"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("all", ("all", HardwareModuleBccDisable.Bcc.Node.All))])
                self._leafs = OrderedDict()

                self.all = HardwareModuleBccDisable.Bcc.Node.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"
                self._segment_path = lambda: "node"
                self._absolute_path = lambda: "Cisco-IOS-XR-hwmod-bcc-disable-cfg:hardware-module-bcc-disable/bcc/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleBccDisable.Bcc.Node, [], name, value)


            class All(_Entity_):
                """
                all node configuration
                
                .. attribute:: disable
                
                	bcc disable config
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'hwmod-bcc-disable-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(HardwareModuleBccDisable.Bcc.Node.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                    ])
                    self.disable = None
                    self._segment_path = lambda: "all"
                    self._absolute_path = lambda: "Cisco-IOS-XR-hwmod-bcc-disable-cfg:hardware-module-bcc-disable/bcc/node/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleBccDisable.Bcc.Node.All, ['disable'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_hwmod_bcc_disable_cfg as meta
                    return meta._meta_table['HardwareModuleBccDisable.Bcc.Node.All']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_hwmod_bcc_disable_cfg as meta
                return meta._meta_table['HardwareModuleBccDisable.Bcc.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_hwmod_bcc_disable_cfg as meta
            return meta._meta_table['HardwareModuleBccDisable.Bcc']['meta_info']

    def clone_ptr(self):
        self._top_entity = HardwareModuleBccDisable()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_hwmod_bcc_disable_cfg as meta
        return meta._meta_table['HardwareModuleBccDisable']['meta_info']


