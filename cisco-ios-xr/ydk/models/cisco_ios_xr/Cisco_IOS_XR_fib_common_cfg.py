""" Cisco_IOS_XR_fib_common_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fib\-common package configuration.

This module contains definitions
for the following management objects\:
  fib\: CEF configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FibPbtsFallback(Enum):
    """
    FibPbtsFallback (Enum Class)

    Fib pbts fallback

    .. data:: list = 1

    	Fallback to class number list

    .. data:: any = 2

    	Fallback to any class

    .. data:: drop = 3

    	Fallback to drop

    """

    list = Enum.YLeaf(1, "list")

    any = Enum.YLeaf(2, "any")

    drop = Enum.YLeaf(3, "drop")


class FibPbtsForwardClass(Enum):
    """
    FibPbtsForwardClass (Enum Class)

    Fib pbts forward class

    .. data:: any = 8

    	Any class

    """

    any = Enum.YLeaf(8, "any")



class Fib(Entity):
    """
    CEF configuration
    
    .. attribute:: pbts_forward_class_fallbacks
    
    	PBTS class configuration
    	**type**\:  :py:class:`PbtsForwardClassFallbacks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.PbtsForwardClassFallbacks>`
    
    .. attribute:: platform
    
    	FIB platform parameters
    	**type**\:  :py:class:`Platform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.Platform>`
    
    .. attribute:: auto_hash_recover
    
    	Set option for automatcially recovering consistent\-hashing state on interface up
    	**type**\: bool
    
    .. attribute:: prefer_aib_routes
    
    	Set options for adjacency routes overriding RIB routes
    	**type**\: bool
    
    .. attribute:: encap_sharing_disable
    
    	Set true to disable encapsulation sharing
    	**type**\: bool
    
    .. attribute:: frr_follow_bgp_pic
    
    	Set option for fast\-reroute to follow BGP PIC update, not to wait for timeout
    	**type**\: bool
    
    

    """

    _prefix = 'fib-common-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Fib, self).__init__()
        self._top_entity = None

        self.yang_name = "fib"
        self.yang_parent_name = "Cisco-IOS-XR-fib-common-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("pbts-forward-class-fallbacks", ("pbts_forward_class_fallbacks", Fib.PbtsForwardClassFallbacks)), ("platform", ("platform", Fib.Platform))])
        self._leafs = OrderedDict([
            ('auto_hash_recover', (YLeaf(YType.boolean, 'auto-hash-recover'), ['bool'])),
            ('prefer_aib_routes', (YLeaf(YType.boolean, 'prefer-aib-routes'), ['bool'])),
            ('encap_sharing_disable', (YLeaf(YType.boolean, 'encap-sharing-disable'), ['bool'])),
            ('frr_follow_bgp_pic', (YLeaf(YType.boolean, 'frr-follow-bgp-pic'), ['bool'])),
        ])
        self.auto_hash_recover = None
        self.prefer_aib_routes = None
        self.encap_sharing_disable = None
        self.frr_follow_bgp_pic = None

        self.pbts_forward_class_fallbacks = Fib.PbtsForwardClassFallbacks()
        self.pbts_forward_class_fallbacks.parent = self
        self._children_name_map["pbts_forward_class_fallbacks"] = "pbts-forward-class-fallbacks"

        self.platform = Fib.Platform()
        self.platform.parent = self
        self._children_name_map["platform"] = "platform"
        self._segment_path = lambda: "Cisco-IOS-XR-fib-common-cfg:fib"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Fib, ['auto_hash_recover', 'prefer_aib_routes', 'encap_sharing_disable', 'frr_follow_bgp_pic'], name, value)


    class PbtsForwardClassFallbacks(Entity):
        """
        PBTS class configuration
        
        .. attribute:: pbts_forward_class_fallback
        
        	Set PBTS class for fallback
        	**type**\: list of  		 :py:class:`PbtsForwardClassFallback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback>`
        
        

        """

        _prefix = 'fib-common-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Fib.PbtsForwardClassFallbacks, self).__init__()

            self.yang_name = "pbts-forward-class-fallbacks"
            self.yang_parent_name = "fib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pbts-forward-class-fallback", ("pbts_forward_class_fallback", Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback))])
            self._leafs = OrderedDict()

            self.pbts_forward_class_fallback = YList(self)
            self._segment_path = lambda: "pbts-forward-class-fallbacks"
            self._absolute_path = lambda: "Cisco-IOS-XR-fib-common-cfg:fib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Fib.PbtsForwardClassFallbacks, [], name, value)


        class PbtsForwardClassFallback(Entity):
            """
            Set PBTS class for fallback
            
            .. attribute:: forward_class_number  (key)
            
            	PBTS forward class number
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`FibPbtsForwardClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.FibPbtsForwardClass>`
            
            		**type**\: int
            
            			**range:** 0..8
            
            .. attribute:: fallback_type
            
            	Set PBTS fallback type
            	**type**\:  :py:class:`FibPbtsFallback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.FibPbtsFallback>`
            
            	**mandatory**\: True
            
            .. attribute:: fallback_class_number_array
            
            	Set PBTS fallback class number array
            	**type**\: list of int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'fib-common-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback, self).__init__()

                self.yang_name = "pbts-forward-class-fallback"
                self.yang_parent_name = "pbts-forward-class-fallbacks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['forward_class_number']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('forward_class_number', (YLeaf(YType.str, 'forward-class-number'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'FibPbtsForwardClass', ''),'int'])),
                    ('fallback_type', (YLeaf(YType.enumeration, 'fallback-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'FibPbtsFallback', '')])),
                    ('fallback_class_number_array', (YLeafList(YType.uint32, 'fallback-class-number-array'), ['int'])),
                ])
                self.forward_class_number = None
                self.fallback_type = None
                self.fallback_class_number_array = []
                self._segment_path = lambda: "pbts-forward-class-fallback" + "[forward-class-number='" + str(self.forward_class_number) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-fib-common-cfg:fib/pbts-forward-class-fallbacks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback, ['forward_class_number', 'fallback_type', 'fallback_class_number_array'], name, value)


    class Platform(Entity):
        """
        FIB platform parameters
        
        .. attribute:: label_switched_multicast
        
        	Options for label\-switched\-multicast parameters
        	**type**\:  :py:class:`LabelSwitchedMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg.Fib.Platform.LabelSwitchedMulticast>`
        
        

        """

        _prefix = 'fib-common-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Fib.Platform, self).__init__()

            self.yang_name = "platform"
            self.yang_parent_name = "fib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("label-switched-multicast", ("label_switched_multicast", Fib.Platform.LabelSwitchedMulticast))])
            self._leafs = OrderedDict()

            self.label_switched_multicast = Fib.Platform.LabelSwitchedMulticast()
            self.label_switched_multicast.parent = self
            self._children_name_map["label_switched_multicast"] = "label-switched-multicast"
            self._segment_path = lambda: "platform"
            self._absolute_path = lambda: "Cisco-IOS-XR-fib-common-cfg:fib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Fib.Platform, [], name, value)


        class LabelSwitchedMulticast(Entity):
            """
            Options for label\-switched\-multicast parameters
            
            .. attribute:: frr_holdtime
            
            	Set time to keep FRR slots programmed post FRR
            	**type**\: int
            
            	**range:** 3..180
            
            	**units**\: second
            
            

            """

            _prefix = 'fib-common-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Fib.Platform.LabelSwitchedMulticast, self).__init__()

                self.yang_name = "label-switched-multicast"
                self.yang_parent_name = "platform"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('frr_holdtime', (YLeaf(YType.uint32, 'frr-holdtime'), ['int'])),
                ])
                self.frr_holdtime = None
                self._segment_path = lambda: "label-switched-multicast"
                self._absolute_path = lambda: "Cisco-IOS-XR-fib-common-cfg:fib/platform/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fib.Platform.LabelSwitchedMulticast, ['frr_holdtime'], name, value)

    def clone_ptr(self):
        self._top_entity = Fib()
        return self._top_entity

