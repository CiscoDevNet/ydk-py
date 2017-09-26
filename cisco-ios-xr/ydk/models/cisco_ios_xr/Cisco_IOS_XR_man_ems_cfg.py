""" Cisco_IOS_XR_man_ems_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package configuration.

This module contains definitions
for the following management objects\:
  grpc\: GRPC configruation

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Grpc(Entity):
    """
    GRPC configruation
    
    .. attribute:: address_family
    
    	Address family identifier type
    	**type**\:  str
    
    .. attribute:: enable
    
    	Enable GRPC
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: max_request_per_user
    
    	Maximum concurrent requests per user
    	**type**\:  int
    
    	**range:** 1..32
    
    .. attribute:: max_request_total
    
    	Maximum concurrent requests in total
    	**type**\:  int
    
    	**range:** 1..256
    
    .. attribute:: port
    
    	Server listening port
    	**type**\:  int
    
    	**range:** 10000..57999
    
    .. attribute:: service_layer
    
    	Service Layer
    	**type**\:   :py:class:`ServiceLayer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Grpc.ServiceLayer>`
    
    .. attribute:: tls
    
    	Transport Layer Security (TLS)
    	**type**\:   :py:class:`Tls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Grpc.Tls>`
    
    .. attribute:: vrf
    
    	Server vrf name
    	**type**\:  str
    
    

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
        self._child_container_classes = {"service-layer" : ("service_layer", Grpc.ServiceLayer), "tls" : ("tls", Grpc.Tls)}
        self._child_list_classes = {}

        self.address_family = YLeaf(YType.str, "address-family")

        self.enable = YLeaf(YType.empty, "enable")

        self.max_request_per_user = YLeaf(YType.uint32, "max-request-per-user")

        self.max_request_total = YLeaf(YType.uint32, "max-request-total")

        self.port = YLeaf(YType.uint32, "port")

        self.vrf = YLeaf(YType.str, "vrf")

        self.service_layer = Grpc.ServiceLayer()
        self.service_layer.parent = self
        self._children_name_map["service_layer"] = "service-layer"
        self._children_yang_names.add("service-layer")

        self.tls = Grpc.Tls()
        self.tls.parent = self
        self._children_name_map["tls"] = "tls"
        self._children_yang_names.add("tls")
        self._segment_path = lambda: "Cisco-IOS-XR-man-ems-cfg:grpc"

    def __setattr__(self, name, value):
        self._perform_setattr(Grpc, ['address_family', 'enable', 'max_request_per_user', 'max_request_total', 'port', 'vrf'], name, value)


    class ServiceLayer(Entity):
        """
        Service Layer
        
        .. attribute:: enable
        
        	Enable ServiceLayer
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.ServiceLayer, self).__init__()

            self.yang_name = "service-layer"
            self.yang_parent_name = "grpc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.enable = YLeaf(YType.empty, "enable")
            self._segment_path = lambda: "service-layer"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-cfg:grpc/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.ServiceLayer, ['enable'], name, value)


    class Tls(Entity):
        """
        Transport Layer Security (TLS)
        
        .. attribute:: enable
        
        	Enable TLS
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: trustpoint
        
        	Trustpoint Name
        	**type**\:  str
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.Tls, self).__init__()

            self.yang_name = "tls"
            self.yang_parent_name = "grpc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.enable = YLeaf(YType.empty, "enable")

            self.trustpoint = YLeaf(YType.str, "trustpoint")
            self._segment_path = lambda: "tls"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-cfg:grpc/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.Tls, ['enable', 'trustpoint'], name, value)

    def clone_ptr(self):
        self._top_entity = Grpc()
        return self._top_entity

