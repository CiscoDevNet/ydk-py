""" Cisco_IOS_XR_man_ems_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package configuration.

This module contains definitions
for the following management objects\:
  grpc\: GRPC configruation

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Dscp(Enum):
    """
    Dscp (Enum Class)

    Dscp

    .. data:: default = 0

    	Default (DSCP 000000)

    .. data:: af11 = 10

    	AF11 (DSCP 001010)

    .. data:: af12 = 12

    	AF12 (DSCP 001100)

    .. data:: af13 = 14

    	AF13 (DSCP 001110)

    .. data:: af21 = 18

    	AF21 (DSCP 010010)

    .. data:: af22 = 20

    	AF22 (DSCP 010100)

    .. data:: af23 = 22

    	AF23 (DSCP 010110)

    .. data:: af31 = 26

    	AF31 (DSCP 011010)

    .. data:: af32 = 28

    	AF32 (DSCP 011100)

    .. data:: af33 = 30

    	AF33 (DSCP 011110)

    .. data:: af41 = 34

    	AF41 (DSCP 100010)

    .. data:: af42 = 36

    	AF42 (DSCP 100100)

    .. data:: af43 = 38

    	AF43 (DSCP 100110)

    .. data:: cs1 = 8

    	CS1 (Precedence 1) (DSCP 001000)

    .. data:: cs2 = 16

    	CS2 (Precedence 2) (DSCP 010000)

    .. data:: cs3 = 24

    	CS3 (Precedence 3) (DSCP 011000)

    .. data:: cs4 = 32

    	CS4 (Precedence 4) (DSCP 100000)

    .. data:: cs5 = 40

    	CS5 (Precedence 5) (DSCP 101000)

    .. data:: cs6 = 48

    	CS6 (Precedence 6) (DSCP 110000)

    .. data:: cs7 = 56

    	CS7 (Precedence 7) (DSCP 111000)

    .. data:: ef = 46

    	EF (DSCP 101110)

    """

    default = Enum.YLeaf(0, "default")

    af11 = Enum.YLeaf(10, "af11")

    af12 = Enum.YLeaf(12, "af12")

    af13 = Enum.YLeaf(14, "af13")

    af21 = Enum.YLeaf(18, "af21")

    af22 = Enum.YLeaf(20, "af22")

    af23 = Enum.YLeaf(22, "af23")

    af31 = Enum.YLeaf(26, "af31")

    af32 = Enum.YLeaf(28, "af32")

    af33 = Enum.YLeaf(30, "af33")

    af41 = Enum.YLeaf(34, "af41")

    af42 = Enum.YLeaf(36, "af42")

    af43 = Enum.YLeaf(38, "af43")

    cs1 = Enum.YLeaf(8, "cs1")

    cs2 = Enum.YLeaf(16, "cs2")

    cs3 = Enum.YLeaf(24, "cs3")

    cs4 = Enum.YLeaf(32, "cs4")

    cs5 = Enum.YLeaf(40, "cs5")

    cs6 = Enum.YLeaf(48, "cs6")

    cs7 = Enum.YLeaf(56, "cs7")

    ef = Enum.YLeaf(46, "ef")


class GrpCTlsCipherDefault(Enum):
    """
    GrpCTlsCipherDefault (Enum Class)

    Grp c tls cipher default

    .. data:: disable = 1

    	Default disable all ciphers

    .. data:: enable = 2

    	Default enable all ciphers

    """

    disable = Enum.YLeaf(1, "disable")

    enable = Enum.YLeaf(2, "enable")



class Grpc(Entity):
    """
    GRPC configruation
    
    .. attribute:: service_layer
    
    	Service Layer
    	**type**\:  :py:class:`ServiceLayer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Grpc.ServiceLayer>`
    
    .. attribute:: tls_cipher
    
    	TLS ciphers
    	**type**\:  :py:class:`TlsCipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Grpc.TlsCipher>`
    
    .. attribute:: port
    
    	Server listening port
    	**type**\: int
    
    	**range:** 10000..57999
    
    .. attribute:: vrf
    
    	Server vrf name
    	**type**\: str
    
    .. attribute:: max_streams
    
    	Maximum number of streaming gRPCs
    	**type**\: int
    
    	**range:** 1..128
    
    	**default value**\: 32
    
    .. attribute:: enable
    
    	Enable GRPC
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: max_streams_per_user
    
    	Maximum number of streaming gRPCs per user
    	**type**\: int
    
    	**range:** 1..128
    
    	**default value**\: 32
    
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
    
    .. attribute:: dscp
    
    	QoS marking DSCP to be set on transmitted gRPC
    	**type**\: union of the below types:
    
    		**type**\:  :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Dscp>`
    
    		**type**\: int
    
    			**range:** 0..63
    
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
    _revision = '2018-04-16'

    def __init__(self):
        super(Grpc, self).__init__()
        self._top_entity = None

        self.yang_name = "grpc"
        self.yang_parent_name = "Cisco-IOS-XR-man-ems-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("service-layer", ("service_layer", Grpc.ServiceLayer)), ("tls-cipher", ("tls_cipher", Grpc.TlsCipher))])
        self._leafs = OrderedDict([
            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
            ('max_streams', (YLeaf(YType.uint32, 'max-streams'), ['int'])),
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('max_streams_per_user', (YLeaf(YType.uint32, 'max-streams-per-user'), ['int'])),
            ('max_request_per_user', (YLeaf(YType.uint32, 'max-request-per-user'), ['int'])),
            ('no_tls', (YLeaf(YType.empty, 'no-tls'), ['Empty'])),
            ('tls_trustpoint', (YLeaf(YType.str, 'tls-trustpoint'), ['str'])),
            ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg', 'Dscp', ''),'int'])),
            ('address_family', (YLeaf(YType.str, 'address-family'), ['str'])),
            ('tls_mutual', (YLeaf(YType.empty, 'tls-mutual'), ['Empty'])),
            ('max_request_total', (YLeaf(YType.uint32, 'max-request-total'), ['int'])),
        ])
        self.port = None
        self.vrf = None
        self.max_streams = None
        self.enable = None
        self.max_streams_per_user = None
        self.max_request_per_user = None
        self.no_tls = None
        self.tls_trustpoint = None
        self.dscp = None
        self.address_family = None
        self.tls_mutual = None
        self.max_request_total = None

        self.service_layer = Grpc.ServiceLayer()
        self.service_layer.parent = self
        self._children_name_map["service_layer"] = "service-layer"

        self.tls_cipher = Grpc.TlsCipher()
        self.tls_cipher.parent = self
        self._children_name_map["tls_cipher"] = "tls-cipher"
        self._segment_path = lambda: "Cisco-IOS-XR-man-ems-cfg:grpc"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Grpc, ['port', 'vrf', 'max_streams', 'enable', 'max_streams_per_user', 'max_request_per_user', 'no_tls', 'tls_trustpoint', 'dscp', 'address_family', 'tls_mutual', 'max_request_total'], name, value)


    class ServiceLayer(Entity):
        """
        Service Layer
        
        .. attribute:: enable
        
        	Enable ServiceLayer
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2018-04-16'

        def __init__(self):
            super(Grpc.ServiceLayer, self).__init__()

            self.yang_name = "service-layer"
            self.yang_parent_name = "grpc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None
            self._segment_path = lambda: "service-layer"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-cfg:grpc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.ServiceLayer, ['enable'], name, value)


    class TlsCipher(Entity):
        """
        TLS ciphers
        
        .. attribute:: default
        
        	Default of all ciphers
        	**type**\:  :py:class:`GrpCTlsCipherDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.GrpCTlsCipherDefault>`
        
        .. attribute:: enable
        
        	Enable ciphers if default is disabled
        	**type**\: str
        
        .. attribute:: disable
        
        	Disable ciphers if default is enabled
        	**type**\: str
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2018-04-16'

        def __init__(self):
            super(Grpc.TlsCipher, self).__init__()

            self.yang_name = "tls-cipher"
            self.yang_parent_name = "grpc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('default', (YLeaf(YType.enumeration, 'default'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg', 'GrpCTlsCipherDefault', '')])),
                ('enable', (YLeaf(YType.str, 'enable'), ['str'])),
                ('disable', (YLeaf(YType.str, 'disable'), ['str'])),
            ])
            self.default = None
            self.enable = None
            self.disable = None
            self._segment_path = lambda: "tls-cipher"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-cfg:grpc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.TlsCipher, ['default', 'enable', 'disable'], name, value)

    def clone_ptr(self):
        self._top_entity = Grpc()
        return self._top_entity

