""" Cisco_IOS_XR_ip_icmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-icmp package configuration.

This module contains definitions
for the following management objects\:
  icmp\: IP ICMP configuration data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SourcePolicy(Enum):
    """
    SourcePolicy (Enum Class)

    Source policy

    .. data:: vrf = 1

    	Set Source Selection Policy to vrf

    .. data:: rfc = 2

    	Set Source Selection Policy to rfc

    """

    vrf = Enum.YLeaf(1, "vrf")

    rfc = Enum.YLeaf(2, "rfc")



class Icmp(Entity):
    """
    IP ICMP configuration data
    
    .. attribute:: ipv6
    
    	IP Protocol Type
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.Ipv6>`
    
    .. attribute:: ipv4
    
    	IP Protocol Type
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.Ipv4>`
    
    

    """

    _prefix = 'ip-icmp-cfg'
    _revision = '2017-06-08'

    def __init__(self):
        super(Icmp, self).__init__()
        self._top_entity = None

        self.yang_name = "icmp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-icmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ipv6", ("ipv6", Icmp.Ipv6)), ("ipv4", ("ipv4", Icmp.Ipv4))])
        self._leafs = OrderedDict()

        self.ipv6 = Icmp.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"

        self.ipv4 = Icmp.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Icmp, [], name, value)


    class Ipv6(Entity):
        """
        IP Protocol Type
        
        .. attribute:: rate_limit
        
        	Set ratelimit of ICMP packets
        	**type**\:  :py:class:`RateLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.Ipv6.RateLimit>`
        
        .. attribute:: source
        
        	IP ICMP Source Address Selection Policy
        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.Ipv6.Source>`
        
        

        """

        _prefix = 'ip-icmp-cfg'
        _revision = '2017-06-08'

        def __init__(self):
            super(Icmp.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "icmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rate-limit", ("rate_limit", Icmp.Ipv6.RateLimit)), ("source", ("source", Icmp.Ipv6.Source))])
            self._leafs = OrderedDict()

            self.rate_limit = Icmp.Ipv6.RateLimit()
            self.rate_limit.parent = self
            self._children_name_map["rate_limit"] = "rate-limit"

            self.source = Icmp.Ipv6.Source()
            self.source.parent = self
            self._children_name_map["source"] = "source"
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Icmp.Ipv6, [], name, value)


        class RateLimit(Entity):
            """
            Set ratelimit of ICMP packets
            
            .. attribute:: unreachable
            
            	Set unreachable ICMP packets ratelimit
            	**type**\:  :py:class:`Unreachable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.Ipv6.RateLimit.Unreachable>`
            
            

            """

            _prefix = 'ip-icmp-cfg'
            _revision = '2017-06-08'

            def __init__(self):
                super(Icmp.Ipv6.RateLimit, self).__init__()

                self.yang_name = "rate-limit"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("unreachable", ("unreachable", Icmp.Ipv6.RateLimit.Unreachable))])
                self._leafs = OrderedDict()

                self.unreachable = Icmp.Ipv6.RateLimit.Unreachable()
                self.unreachable.parent = self
                self._children_name_map["unreachable"] = "unreachable"
                self._segment_path = lambda: "rate-limit"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Icmp.Ipv6.RateLimit, [], name, value)


            class Unreachable(Entity):
                """
                Set unreachable ICMP packets ratelimit
                
                .. attribute:: rate
                
                	Rate Limit of Unreachable ICMP packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: fragmentation
                
                	Rate Limit of Unreachable DF packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-icmp-cfg'
                _revision = '2017-06-08'

                def __init__(self):
                    super(Icmp.Ipv6.RateLimit.Unreachable, self).__init__()

                    self.yang_name = "unreachable"
                    self.yang_parent_name = "rate-limit"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                        ('fragmentation', (YLeaf(YType.uint32, 'fragmentation'), ['int'])),
                    ])
                    self.rate = None
                    self.fragmentation = None
                    self._segment_path = lambda: "unreachable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp/ipv6/rate-limit/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Icmp.Ipv6.RateLimit.Unreachable, ['rate', 'fragmentation'], name, value)


        class Source(Entity):
            """
            IP ICMP Source Address Selection Policy
            
            .. attribute:: source_address_policy
            
            	Configure Source Address Policy
            	**type**\:  :py:class:`SourcePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.SourcePolicy>`
            
            

            """

            _prefix = 'ip-icmp-cfg'
            _revision = '2017-06-08'

            def __init__(self):
                super(Icmp.Ipv6.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('source_address_policy', (YLeaf(YType.enumeration, 'source-address-policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'SourcePolicy', '')])),
                ])
                self.source_address_policy = None
                self._segment_path = lambda: "source"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Icmp.Ipv6.Source, ['source_address_policy'], name, value)


    class Ipv4(Entity):
        """
        IP Protocol Type
        
        .. attribute:: rate_limit
        
        	Set ratelimit of ICMP packets
        	**type**\:  :py:class:`RateLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.Ipv4.RateLimit>`
        
        .. attribute:: source
        
        	IP ICMP Source Address Selection Policy
        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.Ipv4.Source>`
        
        

        """

        _prefix = 'ip-icmp-cfg'
        _revision = '2017-06-08'

        def __init__(self):
            super(Icmp.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "icmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rate-limit", ("rate_limit", Icmp.Ipv4.RateLimit)), ("source", ("source", Icmp.Ipv4.Source))])
            self._leafs = OrderedDict()

            self.rate_limit = Icmp.Ipv4.RateLimit()
            self.rate_limit.parent = self
            self._children_name_map["rate_limit"] = "rate-limit"

            self.source = Icmp.Ipv4.Source()
            self.source.parent = self
            self._children_name_map["source"] = "source"
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Icmp.Ipv4, [], name, value)


        class RateLimit(Entity):
            """
            Set ratelimit of ICMP packets
            
            .. attribute:: unreachable
            
            	Set unreachable ICMP packets ratelimit
            	**type**\:  :py:class:`Unreachable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.Ipv4.RateLimit.Unreachable>`
            
            

            """

            _prefix = 'ip-icmp-cfg'
            _revision = '2017-06-08'

            def __init__(self):
                super(Icmp.Ipv4.RateLimit, self).__init__()

                self.yang_name = "rate-limit"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("unreachable", ("unreachable", Icmp.Ipv4.RateLimit.Unreachable))])
                self._leafs = OrderedDict()

                self.unreachable = Icmp.Ipv4.RateLimit.Unreachable()
                self.unreachable.parent = self
                self._children_name_map["unreachable"] = "unreachable"
                self._segment_path = lambda: "rate-limit"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Icmp.Ipv4.RateLimit, [], name, value)


            class Unreachable(Entity):
                """
                Set unreachable ICMP packets ratelimit
                
                .. attribute:: rate
                
                	Rate Limit of Unreachable ICMP packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: fragmentation
                
                	Rate Limit of Unreachable DF packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-icmp-cfg'
                _revision = '2017-06-08'

                def __init__(self):
                    super(Icmp.Ipv4.RateLimit.Unreachable, self).__init__()

                    self.yang_name = "unreachable"
                    self.yang_parent_name = "rate-limit"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                        ('fragmentation', (YLeaf(YType.uint32, 'fragmentation'), ['int'])),
                    ])
                    self.rate = None
                    self.fragmentation = None
                    self._segment_path = lambda: "unreachable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp/ipv4/rate-limit/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Icmp.Ipv4.RateLimit.Unreachable, ['rate', 'fragmentation'], name, value)


        class Source(Entity):
            """
            IP ICMP Source Address Selection Policy
            
            .. attribute:: source_address_policy
            
            	Configure Source Address Policy
            	**type**\:  :py:class:`SourcePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.SourcePolicy>`
            
            

            """

            _prefix = 'ip-icmp-cfg'
            _revision = '2017-06-08'

            def __init__(self):
                super(Icmp.Ipv4.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('source_address_policy', (YLeaf(YType.enumeration, 'source-address-policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'SourcePolicy', '')])),
                ])
                self.source_address_policy = None
                self._segment_path = lambda: "source"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-icmp-cfg:icmp/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Icmp.Ipv4.Source, ['source_address_policy'], name, value)

    def clone_ptr(self):
        self._top_entity = Icmp()
        return self._top_entity

