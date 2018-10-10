""" Cisco_IOS_XR_ipv4_telnet_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-telnet package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-telnet\: IPv6 telnet configuration
  ipv4\-telnet\: ipv4 telnet

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ipv6Telnet(Entity):
    """
    IPv6 telnet configuration
    
    .. attribute:: client
    
    	Telnet client configuration
    	**type**\:  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg.Ipv6Telnet.Client>`
    
    

    """

    _prefix = 'ipv4-telnet-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv6Telnet, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-telnet"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-telnet-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("client", ("client", Ipv6Telnet.Client))])
        self._leafs = OrderedDict()

        self.client = Ipv6Telnet.Client()
        self.client.parent = self
        self._children_name_map["client"] = "client"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-telnet-cfg:ipv6-telnet"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6Telnet, [], name, value)


    class Client(Entity):
        """
        Telnet client configuration
        
        .. attribute:: source_interface
        
        	Source interface for telnet sessions
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        

        """

        _prefix = 'ipv4-telnet-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv6Telnet.Client, self).__init__()

            self.yang_name = "client"
            self.yang_parent_name = "ipv6-telnet"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
            ])
            self.source_interface = None
            self._segment_path = lambda: "client"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-telnet-cfg:ipv6-telnet/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Telnet.Client, ['source_interface'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6Telnet()
        return self._top_entity

class Ipv4Telnet(Entity):
    """
    ipv4 telnet
    
    .. attribute:: client
    
    	Telnet client configuration
    	**type**\:  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg.Ipv4Telnet.Client>`
    
    

    """

    _prefix = 'ipv4-telnet-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv4Telnet, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-telnet"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-telnet-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("client", ("client", Ipv4Telnet.Client))])
        self._leafs = OrderedDict()

        self.client = Ipv4Telnet.Client()
        self.client.parent = self
        self._children_name_map["client"] = "client"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-telnet-cfg:ipv4-telnet"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4Telnet, [], name, value)


    class Client(Entity):
        """
        Telnet client configuration
        
        .. attribute:: source_interface
        
        	Source interface for telnet sessions
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        

        """

        _prefix = 'ipv4-telnet-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Telnet.Client, self).__init__()

            self.yang_name = "client"
            self.yang_parent_name = "ipv4-telnet"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
            ])
            self.source_interface = None
            self._segment_path = lambda: "client"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-telnet-cfg:ipv4-telnet/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Telnet.Client, ['source_interface'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4Telnet()
        return self._top_entity

