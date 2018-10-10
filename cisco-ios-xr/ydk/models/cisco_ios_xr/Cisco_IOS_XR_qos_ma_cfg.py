""" Cisco_IOS_XR_qos_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR qos package configuration.

This module contains definitions
for the following management objects\:
  qos\: Global QOS configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg,
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class QosFieldNotSupported(Enum):
    """
    QosFieldNotSupported (Enum Class)

    Qos field not supported

    .. data:: not_supported = 0

    	Dummy data type leave unspecified

    """

    not_supported = Enum.YLeaf(0, "not-supported")


class QosPolicyAccount(Enum):
    """
    QosPolicyAccount (Enum Class)

    Qos policy account

    .. data:: layer1 = 8

    	Turn on Layer 1 accounting

    .. data:: layer2 = 1

    	Turn on Layer 2 accounting

    .. data:: nolayer2 = 2

    	Turn on Layer 2 accounting

    .. data:: user_defined = 4

    	User defined accounting

    """

    layer1 = Enum.YLeaf(8, "layer1")

    layer2 = Enum.YLeaf(1, "layer2")

    nolayer2 = Enum.YLeaf(2, "nolayer2")

    user_defined = Enum.YLeaf(4, "user-defined")



class Qos(Entity):
    """
    Global QOS configuration.
    
    .. attribute:: fabric_service_policy
    
    	Name of the fabric service policy
    	**type**\: str
    
    	**length:** 0..63
    
    

    """

    _prefix = 'qos-ma-cfg'
    _revision = '2018-02-27'

    def __init__(self):
        super(Qos, self).__init__()
        self._top_entity = None

        self.yang_name = "qos"
        self.yang_parent_name = "Cisco-IOS-XR-qos-ma-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('fabric_service_policy', (YLeaf(YType.str, 'fabric-service-policy'), ['str'])),
        ])
        self.fabric_service_policy = None
        self._segment_path = lambda: "Cisco-IOS-XR-qos-ma-cfg:qos"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Qos, ['fabric_service_policy'], name, value)

    def clone_ptr(self):
        self._top_entity = Qos()
        return self._top_entity

