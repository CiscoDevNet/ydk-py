""" Cisco_IOS_XR_man_ems_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package configuration.

This module contains definitions
for the following management objects\:
  grpc\: GRPC configruation

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Grpc(Entity):
    """
    GRPC configruation
    
    .. attribute:: service_layer
    
    	Service Layer
    	**type**\:  :py:class:`ServiceLayer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Grpc.ServiceLayer>`
    
    .. attribute:: port
    
    	Server listening port
    	**type**\: int
    
    	**range:** 10000..57999
    
    .. attribute:: vrf
    
    	Server vrf name
    	**type**\: str
    
    .. attribute:: enable
    
    	Enable GRPC
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: max_request_per_user
    
    	Maximum concurrent requests per user
    	**type**\: int
    
    	**range:** 1..32
    
    .. attribute:: no_tls
    
    	No TLS
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: tls_trustpoint
    
    	Trustpoint Name
    	**type**\: str
    
    .. attribute:: address_family
    
    	Address family identifier type
    	**type**\: str
    
    .. attribute:: tls_mutual
    
    	TLS mutual authentication
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: max_request_total
    
    	Maximum concurrent requests in total
    	**type**\: int
    
    	**range:** 1..256
    
    

    """

    _prefix = 'man-ems-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Grpc, self).__init__()
        self._top_entity = None

        self.yang_name = "grpc"
        self.yang_parent_name = "Cisco-IOS-XR-man-ems-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("service-layer", ("service_layer", Grpc.ServiceLayer))])
        self._leafs = OrderedDict([
            ('port', YLeaf(YType.uint32, 'port')),
            ('vrf', YLeaf(YType.str, 'vrf')),
            ('enable', YLeaf(YType.empty, 'enable')),
            ('max_request_per_user', YLeaf(YType.uint32, 'max-request-per-user')),
            ('no_tls', YLeaf(YType.empty, 'no-tls')),
            ('tls_trustpoint', YLeaf(YType.str, 'tls-trustpoint')),
            ('address_family', YLeaf(YType.str, 'address-family')),
            ('tls_mutual', YLeaf(YType.empty, 'tls-mutual')),
            ('max_request_total', YLeaf(YType.uint32, 'max-request-total')),
        ])
        self.port = None
        self.vrf = None
        self.enable = None
        self.max_request_per_user = None
        self.no_tls = None
        self.tls_trustpoint = None
        self.address_family = None
        self.tls_mutual = None
        self.max_request_total = None

        self.service_layer = Grpc.ServiceLayer()
        self.service_layer.parent = self
        self._children_name_map["service_layer"] = "service-layer"
        self._segment_path = lambda: "Cisco-IOS-XR-man-ems-cfg:grpc"

    def __setattr__(self, name, value):
        self._perform_setattr(Grpc, ['port', 'vrf', 'enable', 'max_request_per_user', 'no_tls', 'tls_trustpoint', 'address_family', 'tls_mutual', 'max_request_total'], name, value)


    class ServiceLayer(Entity):
        """
        Service Layer
        
        .. attribute:: enable
        
        	Enable ServiceLayer
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.ServiceLayer, self).__init__()

            self.yang_name = "service-layer"
            self.yang_parent_name = "grpc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enable', YLeaf(YType.empty, 'enable')),
            ])
            self.enable = None
            self._segment_path = lambda: "service-layer"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-cfg:grpc/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.ServiceLayer, ['enable'], name, value)

    def clone_ptr(self):
        self._top_entity = Grpc()
        return self._top_entity

