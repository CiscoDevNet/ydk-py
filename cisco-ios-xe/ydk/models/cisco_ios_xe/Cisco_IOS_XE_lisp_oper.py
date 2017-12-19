""" Cisco_IOS_XE_lisp_oper 

This module contains a collection of YANG definitions for
LISP operational data.
Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LispAddressFamilyType(Enum):
    """
    LispAddressFamilyType

    Address\-family of a LISP address or prefix

    .. data:: ipv4_afi = 0

    	IANA IPv4 address family

    .. data:: ipv6_afi = 1

    	IANA IPv6 address family

    .. data:: mac_afi = 2

    	IANA MAC address family

    """

    ipv4_afi = Enum.YLeaf(0, "ipv4-afi")

    ipv6_afi = Enum.YLeaf(1, "ipv6-afi")

    mac_afi = Enum.YLeaf(2, "mac-afi")


class LispIaftypeType(Enum):
    """
    LispIaftypeType

    Type of service for an Address\-Family within a single

    LISP instance

    .. data:: iaf_ipv4 = 0

    	IPv4 instance service

    .. data:: iaf_ipv6 = 1

    	IPv6 instance service

    .. data:: iaf_mac = 2

    	MAC (L2) instance service

    .. data:: iaf_ar = 3

    	Address Resolution (L3 address-to-MAC) instance service

    .. data:: iaf_rar = 4

    	Reverse Address Resolution (MAC-to-L3 address)

    	instance service

    """

    iaf_ipv4 = Enum.YLeaf(0, "iaf-ipv4")

    iaf_ipv6 = Enum.YLeaf(1, "iaf-ipv6")

    iaf_mac = Enum.YLeaf(2, "iaf-mac")

    iaf_ar = Enum.YLeaf(3, "iaf-ar")

    iaf_rar = Enum.YLeaf(4, "iaf-rar")


class LispMapReplyActionType(Enum):
    """
    LispMapReplyActionType

    Defines the LISP map\-cache ACT type as described

    in the section 6.1.4 of RFC 6830. Valid only

    for negative map\-cache entries

    .. data:: no_action = 0

    	Mapping is kept alive and no encapsulation occurs

    .. data:: natively_forward = 1

    	Matching packets are forwarded without

    	LISP encapsulation

    .. data:: send_map_request = 2

    	Matching packets trigger sending Map-Requests

    .. data:: drop = 3

    	Matching packets are dropped

    """

    no_action = Enum.YLeaf(0, "no-action")

    natively_forward = Enum.YLeaf(1, "natively-forward")

    send_map_request = Enum.YLeaf(2, "send-map-request")

    drop = Enum.YLeaf(3, "drop")



class LispState(Entity):
    """
    Operational state of the LISP subsystem
    
    .. attribute:: lisp_routers
    
    	List of LISP routers
    	**type**\: list of  		 :py:class:`LispRouters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters>`
    
    

    """

    _prefix = 'lisp-ios-xe-oper'
    _revision = '2017-07-04'

    def __init__(self):
        super(LispState, self).__init__()
        self._top_entity = None

        self.yang_name = "lisp-state"
        self.yang_parent_name = "Cisco-IOS-XE-lisp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"lisp-routers" : ("lisp_routers", LispState.LispRouters)}

        self.lisp_routers = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-lisp-oper:lisp-state"

    def __setattr__(self, name, value):
        self._perform_setattr(LispState, [], name, value)


    class LispRouters(Entity):
        """
        List of LISP routers
        
        .. attribute:: top_id  <key>
        
        	ID number of the LISP router
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: site_id
        
        	Site\-ID common to all devices attached to the same site
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: xtr_id
        
        	xTR\-ID of the device
        	**type**\: list of int
        
        	**range:** 0..255
        
        .. attribute:: instances
        
        	List of LISP instances
        	**type**\: list of  		 :py:class:`Instances <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances>`
        
        

        """

        _prefix = 'lisp-ios-xe-oper'
        _revision = '2017-07-04'

        def __init__(self):
            super(LispState.LispRouters, self).__init__()

            self.yang_name = "lisp-routers"
            self.yang_parent_name = "lisp-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"instances" : ("instances", LispState.LispRouters.Instances)}

            self.top_id = YLeaf(YType.uint32, "top-id")

            self.site_id = YLeaf(YType.uint64, "site-id")

            self.xtr_id = YLeafList(YType.uint8, "xtr-id")

            self.instances = YList(self)
            self._segment_path = lambda: "lisp-routers" + "[top-id='" + self.top_id.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-lisp-oper:lisp-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LispState.LispRouters, ['top_id', 'site_id', 'xtr_id'], name, value)


        class Instances(Entity):
            """
            List of LISP instances
            
            .. attribute:: iid  <key>
            
            	LISP Instance ID
            	**type**\: int
            
            	**range:** 0..16777215
            
            .. attribute:: af
            
            	List of Address\-Families enabled in this LISP instance
            	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af>`
            
            

            """

            _prefix = 'lisp-ios-xe-oper'
            _revision = '2017-07-04'

            def __init__(self):
                super(LispState.LispRouters.Instances, self).__init__()

                self.yang_name = "instances"
                self.yang_parent_name = "lisp-routers"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"af" : ("af", LispState.LispRouters.Instances.Af)}

                self.iid = YLeaf(YType.uint32, "iid")

                self.af = YList(self)
                self._segment_path = lambda: "instances" + "[iid='" + self.iid.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(LispState.LispRouters.Instances, ['iid'], name, value)


            class Af(Entity):
                """
                List of Address\-Families enabled in this LISP instance
                
                .. attribute:: iaftype  <key>
                
                	Instance\-specific service type
                	**type**\:  :py:class:`LispIaftypeType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispIaftypeType>`
                
                .. attribute:: role
                
                	LISP device role for this service
                	**type**\:  :py:class:`Role <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.Role>`
                
                .. attribute:: map_cache
                
                	Map\-cache for this service instance
                	**type**\: list of  		 :py:class:`MapCache <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MapCache>`
                
                

                """

                _prefix = 'lisp-ios-xe-oper'
                _revision = '2017-07-04'

                def __init__(self):
                    super(LispState.LispRouters.Instances.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"role" : ("role", LispState.LispRouters.Instances.Af.Role)}
                    self._child_list_classes = {"map-cache" : ("map_cache", LispState.LispRouters.Instances.Af.MapCache)}

                    self.iaftype = YLeaf(YType.enumeration, "iaftype")

                    self.role = LispState.LispRouters.Instances.Af.Role()
                    self.role.parent = self
                    self._children_name_map["role"] = "role"
                    self._children_yang_names.add("role")

                    self.map_cache = YList(self)
                    self._segment_path = lambda: "af" + "[iaftype='" + self.iaftype.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(LispState.LispRouters.Instances.Af, ['iaftype'], name, value)


                class Role(Entity):
                    """
                    LISP device role for this service
                    
                    .. attribute:: is_ms
                    
                    	LISP Map\-Server
                    	**type**\: bool
                    
                    .. attribute:: is_mr
                    
                    	LISP Map\-Resolver
                    	**type**\: bool
                    
                    .. attribute:: is_itr
                    
                    	LISP ITR
                    	**type**\: bool
                    
                    .. attribute:: is_etr
                    
                    	LISP ETR
                    	**type**\: bool
                    
                    .. attribute:: is_pitr
                    
                    	LISP Proxy\-ITR
                    	**type**\: bool
                    
                    .. attribute:: is_petr
                    
                    	LISP Proxy\-ETR
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-07-04'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.Role, self).__init__()

                        self.yang_name = "role"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.is_ms = YLeaf(YType.boolean, "is-ms")

                        self.is_mr = YLeaf(YType.boolean, "is-mr")

                        self.is_itr = YLeaf(YType.boolean, "is-itr")

                        self.is_etr = YLeaf(YType.boolean, "is-etr")

                        self.is_pitr = YLeaf(YType.boolean, "is-pitr")

                        self.is_petr = YLeaf(YType.boolean, "is-petr")
                        self._segment_path = lambda: "role"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.Role, ['is_ms', 'is_mr', 'is_itr', 'is_etr', 'is_pitr', 'is_petr'], name, value)


                class MapCache(Entity):
                    """
                    Map\-cache for this service instance
                    
                    .. attribute:: afi  <key>
                    
                    	LISP Address\-Family of the prefix
                    	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                    
                    .. attribute:: prefix  <key>
                    
                    	LISP prefix. Format is defined by the AF
                    	**type**\: str
                    
                    .. attribute:: up_time
                    
                    	Time that this entry was created
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: last_modified_time
                    
                    	Last time that the RLOC information or the entry state were modified
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: last_update_time
                    
                    	Last time a mapping record for this entry was received
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: ttl
                    
                    	Mapping validity period (in milliseconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_authoritative
                    
                    	Indication if the mapping came from an authoritative source
                    	**type**\: bool
                    
                    .. attribute:: is_static
                    
                    	Indication if the mapping is static (i.e. configured)
                    	**type**\: bool
                    
                    .. attribute:: is_negative
                    
                    	Indication if the mapping is negative (i.e. provides no locators for LISP encapsulation)
                    	**type**\: bool
                    
                    .. attribute:: nmr_action
                    
                    	Forwarding action in case of negative entry
                    	**type**\:  :py:class:`LispMapReplyActionType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispMapReplyActionType>`
                    
                    .. attribute:: rloc
                    
                    	List of locators for positive mapping
                    	**type**\: list of  		 :py:class:`Rloc <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MapCache.Rloc>`
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-07-04'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.MapCache, self).__init__()

                        self.yang_name = "map-cache"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"rloc" : ("rloc", LispState.LispRouters.Instances.Af.MapCache.Rloc)}

                        self.afi = YLeaf(YType.enumeration, "afi")

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.up_time = YLeaf(YType.str, "up-time")

                        self.last_modified_time = YLeaf(YType.str, "last-modified-time")

                        self.last_update_time = YLeaf(YType.str, "last-update-time")

                        self.ttl = YLeaf(YType.uint32, "ttl")

                        self.is_authoritative = YLeaf(YType.boolean, "is-authoritative")

                        self.is_static = YLeaf(YType.boolean, "is-static")

                        self.is_negative = YLeaf(YType.boolean, "is-negative")

                        self.nmr_action = YLeaf(YType.enumeration, "nmr-action")

                        self.rloc = YList(self)
                        self._segment_path = lambda: "map-cache" + "[afi='" + self.afi.get() + "']" + "[prefix='" + self.prefix.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.MapCache, ['afi', 'prefix', 'up_time', 'last_modified_time', 'last_update_time', 'ttl', 'is_authoritative', 'is_static', 'is_negative', 'nmr_action'], name, value)


                    class Rloc(Entity):
                        """
                        List of locators for positive mapping
                        
                        .. attribute:: afi  <key>
                        
                        	LISP Address\-Family of the address
                        	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                        
                        .. attribute:: address  <key>
                        
                        	LISP address. Format is defined by the AF
                        	**type**\: str
                        
                        .. attribute:: params
                        
                        	Properties of the locator
                        	**type**\:  :py:class:`Params <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MapCache.Rloc.Params>`
                        
                        

                        """

                        _prefix = 'lisp-ios-xe-oper'
                        _revision = '2017-07-04'

                        def __init__(self):
                            super(LispState.LispRouters.Instances.Af.MapCache.Rloc, self).__init__()

                            self.yang_name = "rloc"
                            self.yang_parent_name = "map-cache"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"params" : ("params", LispState.LispRouters.Instances.Af.MapCache.Rloc.Params)}
                            self._child_list_classes = {}

                            self.afi = YLeaf(YType.enumeration, "afi")

                            self.address = YLeaf(YType.str, "address")

                            self.params = LispState.LispRouters.Instances.Af.MapCache.Rloc.Params()
                            self.params.parent = self
                            self._children_name_map["params"] = "params"
                            self._children_yang_names.add("params")
                            self._segment_path = lambda: "rloc" + "[afi='" + self.afi.get() + "']" + "[address='" + self.address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LispState.LispRouters.Instances.Af.MapCache.Rloc, ['afi', 'address'], name, value)


                        class Params(Entity):
                            """
                            Properties of the locator
                            
                            .. attribute:: priority
                            
                            	Locator priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: weight
                            
                            	Locator weight
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: mcast_priority
                            
                            	Locator's multicast priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: mcast_weight
                            
                            	Locator's multicast weight
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'lisp-ios-xe-oper'
                            _revision = '2017-07-04'

                            def __init__(self):
                                super(LispState.LispRouters.Instances.Af.MapCache.Rloc.Params, self).__init__()

                                self.yang_name = "params"
                                self.yang_parent_name = "rloc"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.priority = YLeaf(YType.uint8, "priority")

                                self.weight = YLeaf(YType.uint8, "weight")

                                self.mcast_priority = YLeaf(YType.uint8, "mcast-priority")

                                self.mcast_weight = YLeaf(YType.uint8, "mcast-weight")
                                self._segment_path = lambda: "params"

                            def __setattr__(self, name, value):
                                self._perform_setattr(LispState.LispRouters.Instances.Af.MapCache.Rloc.Params, ['priority', 'weight', 'mcast_priority', 'mcast_weight'], name, value)

    def clone_ptr(self):
        self._top_entity = LispState()
        return self._top_entity

