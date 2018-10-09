""" Cisco_IOS_XR_pbr_bng_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr\-bng package configuration.

This module contains definitions
for the following management objects\:
  bng\-pbr\: Subscriber PBR configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BngPbrHttpEnrichmentParams(Enum):
    """
    BngPbrHttpEnrichmentParams (Enum Class)

    Bng pbr http enrichment params

    .. data:: subscriber_mac = 1

    	Subscriber Mac

    .. data:: subscriber_ip = 2

    	Subscriber IPv4/IPv6 address

    .. data:: host_name = 4

    	Bng Router Hostname

    .. data:: bng_identifier_interface = 8

    	Bng Identifier interface

    """

    subscriber_mac = Enum.YLeaf(1, "subscriber-mac")

    subscriber_ip = Enum.YLeaf(2, "subscriber-ip")

    host_name = Enum.YLeaf(4, "host-name")

    bng_identifier_interface = Enum.YLeaf(8, "bng-identifier-interface")



class BngPbr(Entity):
    """
    Subscriber PBR configuration
    
    .. attribute:: http_enrichment
    
    	HTTP Enrichment
    	**type**\:  :py:class:`HttpEnrichment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg.BngPbr.HttpEnrichment>`
    
    .. attribute:: bng_interface
    
    	Interface for source address
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
    
    

    """

    _prefix = 'pbr-bng-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(BngPbr, self).__init__()
        self._top_entity = None

        self.yang_name = "bng-pbr"
        self.yang_parent_name = "Cisco-IOS-XR-pbr-bng-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("http-enrichment", ("http_enrichment", BngPbr.HttpEnrichment))])
        self._leafs = OrderedDict([
            ('bng_interface', (YLeaf(YType.str, 'bng-interface'), ['str'])),
        ])
        self.bng_interface = None

        self.http_enrichment = BngPbr.HttpEnrichment()
        self.http_enrichment.parent = self
        self._children_name_map["http_enrichment"] = "http-enrichment"
        self._segment_path = lambda: "Cisco-IOS-XR-pbr-bng-cfg:bng-pbr"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(BngPbr, ['bng_interface'], name, value)


    class HttpEnrichment(Entity):
        """
        HTTP Enrichment
        
        .. attribute:: parameters
        
        	HTTP Enrichment parameters
        	**type**\:  :py:class:`Parameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg.BngPbr.HttpEnrichment.Parameters>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'pbr-bng-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(BngPbr.HttpEnrichment, self).__init__()

            self.yang_name = "http-enrichment"
            self.yang_parent_name = "bng-pbr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("parameters", ("parameters", BngPbr.HttpEnrichment.Parameters))])
            self._leafs = OrderedDict()

            self.parameters = None
            self._children_name_map["parameters"] = "parameters"
            self._segment_path = lambda: "http-enrichment"
            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-bng-cfg:bng-pbr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(BngPbr.HttpEnrichment, [], name, value)


        class Parameters(Entity):
            """
            HTTP Enrichment parameters
            
            .. attribute:: arg1
            
            	first argument 
            	**type**\:  :py:class:`BngPbrHttpEnrichmentParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg.BngPbrHttpEnrichmentParams>`
            
            	**mandatory**\: True
            
            .. attribute:: arg2
            
            	second argument 
            	**type**\:  :py:class:`BngPbrHttpEnrichmentParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg.BngPbrHttpEnrichmentParams>`
            
            .. attribute:: arg3
            
            	Third argument 
            	**type**\:  :py:class:`BngPbrHttpEnrichmentParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg.BngPbrHttpEnrichmentParams>`
            
            .. attribute:: arg4
            
            	Fourth argument 
            	**type**\:  :py:class:`BngPbrHttpEnrichmentParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg.BngPbrHttpEnrichmentParams>`
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'pbr-bng-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(BngPbr.HttpEnrichment.Parameters, self).__init__()

                self.yang_name = "parameters"
                self.yang_parent_name = "http-enrichment"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('arg1', (YLeaf(YType.enumeration, 'arg1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams', '')])),
                    ('arg2', (YLeaf(YType.enumeration, 'arg2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams', '')])),
                    ('arg3', (YLeaf(YType.enumeration, 'arg3'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams', '')])),
                    ('arg4', (YLeaf(YType.enumeration, 'arg4'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams', '')])),
                ])
                self.arg1 = None
                self.arg2 = None
                self.arg3 = None
                self.arg4 = None
                self._segment_path = lambda: "parameters"
                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-bng-cfg:bng-pbr/http-enrichment/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(BngPbr.HttpEnrichment.Parameters, ['arg1', 'arg2', 'arg3', 'arg4'], name, value)

    def clone_ptr(self):
        self._top_entity = BngPbr()
        return self._top_entity

