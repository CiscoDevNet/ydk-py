""" Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5k\-fea\-pfilter\-nonatomic package configuration.

This module contains definitions
for the following management objects\:
  hardware\: Hardware

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AtomicDisableDfltActn(Enum):
    """
    AtomicDisableDfltActn (Enum Class)

    Atomic disable dflt actn

    .. data:: default_action_deny = 1

    	Drops traffic during modification

    .. data:: default_action_permit = 2

    	Forward traffic during modification

    """

    default_action_deny = Enum.YLeaf(1, "default-action-deny")

    default_action_permit = Enum.YLeaf(2, "default-action-permit")



class Hardware(Entity):
    """
    Hardware
    
    .. attribute:: access_list
    
    	Access\-list option
    	**type**\:  :py:class:`AccessList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg.Hardware.AccessList>`
    
    

    """

    _prefix = 'ncs5k-fea-pfilter-nonatomic-cfg'
    _revision = '2016-09-01'

    def __init__(self):
        super(Hardware, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware"
        self.yang_parent_name = "Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("access-list", ("access_list", Hardware.AccessList))])
        self._leafs = OrderedDict()

        self.access_list = Hardware.AccessList()
        self.access_list.parent = self
        self._children_name_map["access_list"] = "access-list"
        self._segment_path = lambda: "Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg:hardware"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Hardware, [], name, value)


    class AccessList(Entity):
        """
        Access\-list option
        
        .. attribute:: atomic_disable
        
        	Specify Option for Atomic disable
        	**type**\:  :py:class:`AtomicDisableDfltActn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg.AtomicDisableDfltActn>`
        
        

        """

        _prefix = 'ncs5k-fea-pfilter-nonatomic-cfg'
        _revision = '2016-09-01'

        def __init__(self):
            super(Hardware.AccessList, self).__init__()

            self.yang_name = "access-list"
            self.yang_parent_name = "hardware"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('atomic_disable', (YLeaf(YType.enumeration, 'atomic-disable'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg', 'AtomicDisableDfltActn', '')])),
            ])
            self.atomic_disable = None
            self._segment_path = lambda: "access-list"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg:hardware/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Hardware.AccessList, ['atomic_disable'], name, value)

    def clone_ptr(self):
        self._top_entity = Hardware()
        return self._top_entity

