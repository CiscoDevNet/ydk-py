""" Cisco_IOS_XR_segment_routing_ms_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package operational data.

This module contains definitions
for the following management objects\:
  srms\: Segment Routing Mapping Server operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SrmsMiAfEB(Enum):
    """
    SrmsMiAfEB

    Srms mi af e b

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    none = Enum.YLeaf(0, "none")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class SrmsMiFlagEB(Enum):
    """
    SrmsMiFlagEB

    Srms mi flag e b

    .. data:: false = 0

    	False

    .. data:: true = 1

    	True

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(1, "true")


class SrmsMiSrcEB(Enum):
    """
    SrmsMiSrcEB

    Srms mi src e b

    .. data:: none = 0

    	None

    .. data:: local = 1

    	Local

    .. data:: remote = 2

    	Remote

    """

    none = Enum.YLeaf(0, "none")

    local = Enum.YLeaf(1, "local")

    remote = Enum.YLeaf(2, "remote")



class Srms(Entity):
    """
    Segment Routing Mapping Server operational data
    
    .. attribute:: mapping
    
    	IP prefix to SID mappings
    	**type**\:   :py:class:`Mapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping>`
    
    .. attribute:: policy
    
    	Policy operational data
    	**type**\:   :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy>`
    
    

    """

    _prefix = 'segment-routing-ms-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Srms, self).__init__()
        self._top_entity = None

        self.yang_name = "srms"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"mapping" : ("mapping", Srms.Mapping), "policy" : ("policy", Srms.Policy)}
        self._child_list_classes = {}

        self.mapping = Srms.Mapping()
        self.mapping.parent = self
        self._children_name_map["mapping"] = "mapping"
        self._children_yang_names.add("mapping")

        self.policy = Srms.Policy()
        self.policy.parent = self
        self._children_name_map["policy"] = "policy"
        self._children_yang_names.add("policy")
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms"


    class Mapping(Entity):
        """
        IP prefix to SID mappings
        
        .. attribute:: mapping_ipv4
        
        	IPv4 prefix to SID mappings
        	**type**\:   :py:class:`MappingIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4>`
        
        .. attribute:: mapping_ipv6
        
        	IPv6 prefix to SID mappings
        	**type**\:   :py:class:`MappingIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6>`
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Srms.Mapping, self).__init__()

            self.yang_name = "mapping"
            self.yang_parent_name = "srms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"mapping-ipv4" : ("mapping_ipv4", Srms.Mapping.MappingIpv4), "mapping-ipv6" : ("mapping_ipv6", Srms.Mapping.MappingIpv6)}
            self._child_list_classes = {}

            self.mapping_ipv4 = Srms.Mapping.MappingIpv4()
            self.mapping_ipv4.parent = self
            self._children_name_map["mapping_ipv4"] = "mapping-ipv4"
            self._children_yang_names.add("mapping-ipv4")

            self.mapping_ipv6 = Srms.Mapping.MappingIpv6()
            self.mapping_ipv6.parent = self
            self._children_name_map["mapping_ipv6"] = "mapping-ipv6"
            self._children_yang_names.add("mapping-ipv6")
            self._segment_path = lambda: "mapping"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/%s" % self._segment_path()


        class MappingIpv4(Entity):
            """
            IPv4 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of    :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4.MappingMi>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Srms.Mapping.MappingIpv4, self).__init__()

                self.yang_name = "mapping-ipv4"
                self.yang_parent_name = "mapping"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"mapping-mi" : ("mapping_mi", Srms.Mapping.MappingIpv4.MappingMi)}

                self.mapping_mi = YList(self)
                self._segment_path = lambda: "mapping-ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srms.Mapping.MappingIpv4, [], name, value)


            class MappingMi(Entity):
                """
                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                
                .. attribute:: addr
                
                	addr
                	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4.MappingMi.Addr>`
                
                .. attribute:: area
                
                	Area (OSPF) or Level (ISIS)
                	**type**\:  str
                
                	**length:** 0..30
                
                .. attribute:: flag_attached
                
                	Attached flag
                	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                
                .. attribute:: ip
                
                	IP
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: last_prefix
                
                	Last IP Prefix
                	**type**\:  str
                
                	**length:** 0..50
                
                .. attribute:: last_sid_index
                
                	Last SID Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: prefix_xr
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: router
                
                	Router ID
                	**type**\:  str
                
                	**length:** 0..30
                
                .. attribute:: sid_count
                
                	SID range
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sid_start
                
                	Starting SID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: src
                
                	src
                	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Mapping.MappingIpv4.MappingMi, self).__init__()

                    self.yang_name = "mapping-mi"
                    self.yang_parent_name = "mapping-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"addr" : ("addr", Srms.Mapping.MappingIpv4.MappingMi.Addr)}
                    self._child_list_classes = {}

                    self.area = YLeaf(YType.str, "area")

                    self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                    self.ip = YLeaf(YType.str, "ip")

                    self.last_prefix = YLeaf(YType.str, "last-prefix")

                    self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                    self.prefix = YLeaf(YType.int32, "prefix")

                    self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                    self.router = YLeaf(YType.str, "router")

                    self.sid_count = YLeaf(YType.uint32, "sid-count")

                    self.sid_start = YLeaf(YType.uint32, "sid-start")

                    self.src = YLeaf(YType.enumeration, "src")

                    self.addr = Srms.Mapping.MappingIpv4.MappingMi.Addr()
                    self.addr.parent = self
                    self._children_name_map["addr"] = "addr"
                    self._children_yang_names.add("addr")
                    self._segment_path = lambda: "mapping-mi"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv4/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Mapping.MappingIpv4.MappingMi, ['area', 'flag_attached', 'ip', 'last_prefix', 'last_sid_index', 'prefix', 'prefix_xr', 'router', 'sid_count', 'sid_start', 'src'], name, value)


                class Addr(Entity):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Mapping.MappingIpv4.MappingMi.Addr, self).__init__()

                        self.yang_name = "addr"
                        self.yang_parent_name = "mapping-mi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.af = YLeaf(YType.enumeration, "af")

                        self.ipv4 = YLeaf(YType.str, "ipv4")

                        self.ipv6 = YLeaf(YType.str, "ipv6")
                        self._segment_path = lambda: "addr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv4/mapping-mi/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Mapping.MappingIpv4.MappingMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)


        class MappingIpv6(Entity):
            """
            IPv6 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of    :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6.MappingMi>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Srms.Mapping.MappingIpv6, self).__init__()

                self.yang_name = "mapping-ipv6"
                self.yang_parent_name = "mapping"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"mapping-mi" : ("mapping_mi", Srms.Mapping.MappingIpv6.MappingMi)}

                self.mapping_mi = YList(self)
                self._segment_path = lambda: "mapping-ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srms.Mapping.MappingIpv6, [], name, value)


            class MappingMi(Entity):
                """
                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                
                .. attribute:: addr
                
                	addr
                	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6.MappingMi.Addr>`
                
                .. attribute:: area
                
                	Area (OSPF) or Level (ISIS)
                	**type**\:  str
                
                	**length:** 0..30
                
                .. attribute:: flag_attached
                
                	Attached flag
                	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                
                .. attribute:: ip
                
                	IP
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: last_prefix
                
                	Last IP Prefix
                	**type**\:  str
                
                	**length:** 0..50
                
                .. attribute:: last_sid_index
                
                	Last SID Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: prefix_xr
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: router
                
                	Router ID
                	**type**\:  str
                
                	**length:** 0..30
                
                .. attribute:: sid_count
                
                	SID range
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sid_start
                
                	Starting SID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: src
                
                	src
                	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Mapping.MappingIpv6.MappingMi, self).__init__()

                    self.yang_name = "mapping-mi"
                    self.yang_parent_name = "mapping-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"addr" : ("addr", Srms.Mapping.MappingIpv6.MappingMi.Addr)}
                    self._child_list_classes = {}

                    self.area = YLeaf(YType.str, "area")

                    self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                    self.ip = YLeaf(YType.str, "ip")

                    self.last_prefix = YLeaf(YType.str, "last-prefix")

                    self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                    self.prefix = YLeaf(YType.int32, "prefix")

                    self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                    self.router = YLeaf(YType.str, "router")

                    self.sid_count = YLeaf(YType.uint32, "sid-count")

                    self.sid_start = YLeaf(YType.uint32, "sid-start")

                    self.src = YLeaf(YType.enumeration, "src")

                    self.addr = Srms.Mapping.MappingIpv6.MappingMi.Addr()
                    self.addr.parent = self
                    self._children_name_map["addr"] = "addr"
                    self._children_yang_names.add("addr")
                    self._segment_path = lambda: "mapping-mi"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv6/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Mapping.MappingIpv6.MappingMi, ['area', 'flag_attached', 'ip', 'last_prefix', 'last_sid_index', 'prefix', 'prefix_xr', 'router', 'sid_count', 'sid_start', 'src'], name, value)


                class Addr(Entity):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Mapping.MappingIpv6.MappingMi.Addr, self).__init__()

                        self.yang_name = "addr"
                        self.yang_parent_name = "mapping-mi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.af = YLeaf(YType.enumeration, "af")

                        self.ipv4 = YLeaf(YType.str, "ipv4")

                        self.ipv6 = YLeaf(YType.str, "ipv6")
                        self._segment_path = lambda: "addr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv6/mapping-mi/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Mapping.MappingIpv6.MappingMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)


    class Policy(Entity):
        """
        Policy operational data
        
        .. attribute:: policy_ipv4
        
        	IPv4 policy operational data
        	**type**\:   :py:class:`PolicyIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4>`
        
        .. attribute:: policy_ipv6
        
        	IPv6 policy operational data
        	**type**\:   :py:class:`PolicyIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6>`
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Srms.Policy, self).__init__()

            self.yang_name = "policy"
            self.yang_parent_name = "srms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"policy-ipv4" : ("policy_ipv4", Srms.Policy.PolicyIpv4), "policy-ipv6" : ("policy_ipv6", Srms.Policy.PolicyIpv6)}
            self._child_list_classes = {}

            self.policy_ipv4 = Srms.Policy.PolicyIpv4()
            self.policy_ipv4.parent = self
            self._children_name_map["policy_ipv4"] = "policy-ipv4"
            self._children_yang_names.add("policy-ipv4")

            self.policy_ipv6 = Srms.Policy.PolicyIpv6()
            self.policy_ipv6.parent = self
            self._children_name_map["policy_ipv6"] = "policy-ipv6"
            self._children_yang_names.add("policy-ipv6")
            self._segment_path = lambda: "policy"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/%s" % self._segment_path()


        class PolicyIpv4(Entity):
            """
            IPv4 policy operational data
            
            .. attribute:: policy_ipv4_active
            
            	IPv4 active policy operational data
            	**type**\:   :py:class:`PolicyIpv4Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active>`
            
            .. attribute:: policy_ipv4_backup
            
            	IPv4 backup policy operational data
            	**type**\:   :py:class:`PolicyIpv4Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Srms.Policy.PolicyIpv4, self).__init__()

                self.yang_name = "policy-ipv4"
                self.yang_parent_name = "policy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"policy-ipv4-active" : ("policy_ipv4_active", Srms.Policy.PolicyIpv4.PolicyIpv4Active), "policy-ipv4-backup" : ("policy_ipv4_backup", Srms.Policy.PolicyIpv4.PolicyIpv4Backup)}
                self._child_list_classes = {}

                self.policy_ipv4_active = Srms.Policy.PolicyIpv4.PolicyIpv4Active()
                self.policy_ipv4_active.parent = self
                self._children_name_map["policy_ipv4_active"] = "policy-ipv4-active"
                self._children_yang_names.add("policy-ipv4-active")

                self.policy_ipv4_backup = Srms.Policy.PolicyIpv4.PolicyIpv4Backup()
                self.policy_ipv4_backup.parent = self
                self._children_name_map["policy_ipv4_backup"] = "policy-ipv4-backup"
                self._children_yang_names.add("policy-ipv4-backup")
                self._segment_path = lambda: "policy-ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/%s" % self._segment_path()


            class PolicyIpv4Active(Entity):
                """
                IPv4 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Policy.PolicyIpv4.PolicyIpv4Active, self).__init__()

                    self.yang_name = "policy-ipv4-active"
                    self.yang_parent_name = "policy-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"policy-mi" : ("policy_mi", Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi)}

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv4-active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Active, [], name, value)


                class PolicyMi(Entity):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  <key>
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr>`
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv4-active"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"addr" : ("addr", Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr)}
                        self._child_list_classes = {}

                        self.mi_id = YLeaf(YType.str, "mi-id")

                        self.area = YLeaf(YType.str, "area")

                        self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                        self.last_prefix = YLeaf(YType.str, "last-prefix")

                        self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                        self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                        self.router = YLeaf(YType.str, "router")

                        self.sid_count = YLeaf(YType.uint32, "sid-count")

                        self.sid_start = YLeaf(YType.uint32, "sid-start")

                        self.src = YLeaf(YType.enumeration, "src")

                        self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._children_yang_names.add("addr")
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + self.mi_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/policy-ipv4-active/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, ['mi_id', 'area', 'flag_attached', 'last_prefix', 'last_sid_index', 'prefix_xr', 'router', 'sid_count', 'sid_start', 'src'], name, value)


                    class Addr(Entity):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af = YLeaf(YType.enumeration, "af")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "addr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)


            class PolicyIpv4Backup(Entity):
                """
                IPv4 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup, self).__init__()

                    self.yang_name = "policy-ipv4-backup"
                    self.yang_parent_name = "policy-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"policy-mi" : ("policy_mi", Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi)}

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv4-backup"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Backup, [], name, value)


                class PolicyMi(Entity):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  <key>
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr>`
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv4-backup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"addr" : ("addr", Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr)}
                        self._child_list_classes = {}

                        self.mi_id = YLeaf(YType.str, "mi-id")

                        self.area = YLeaf(YType.str, "area")

                        self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                        self.last_prefix = YLeaf(YType.str, "last-prefix")

                        self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                        self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                        self.router = YLeaf(YType.str, "router")

                        self.sid_count = YLeaf(YType.uint32, "sid-count")

                        self.sid_start = YLeaf(YType.uint32, "sid-start")

                        self.src = YLeaf(YType.enumeration, "src")

                        self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._children_yang_names.add("addr")
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + self.mi_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/policy-ipv4-backup/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, ['mi_id', 'area', 'flag_attached', 'last_prefix', 'last_sid_index', 'prefix_xr', 'router', 'sid_count', 'sid_start', 'src'], name, value)


                    class Addr(Entity):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af = YLeaf(YType.enumeration, "af")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "addr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)


        class PolicyIpv6(Entity):
            """
            IPv6 policy operational data
            
            .. attribute:: policy_ipv6_active
            
            	IPv6 active policy operational data
            	**type**\:   :py:class:`PolicyIpv6Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active>`
            
            .. attribute:: policy_ipv6_backup
            
            	IPv6 backup policy operational data
            	**type**\:   :py:class:`PolicyIpv6Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Srms.Policy.PolicyIpv6, self).__init__()

                self.yang_name = "policy-ipv6"
                self.yang_parent_name = "policy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"policy-ipv6-active" : ("policy_ipv6_active", Srms.Policy.PolicyIpv6.PolicyIpv6Active), "policy-ipv6-backup" : ("policy_ipv6_backup", Srms.Policy.PolicyIpv6.PolicyIpv6Backup)}
                self._child_list_classes = {}

                self.policy_ipv6_active = Srms.Policy.PolicyIpv6.PolicyIpv6Active()
                self.policy_ipv6_active.parent = self
                self._children_name_map["policy_ipv6_active"] = "policy-ipv6-active"
                self._children_yang_names.add("policy-ipv6-active")

                self.policy_ipv6_backup = Srms.Policy.PolicyIpv6.PolicyIpv6Backup()
                self.policy_ipv6_backup.parent = self
                self._children_name_map["policy_ipv6_backup"] = "policy-ipv6-backup"
                self._children_yang_names.add("policy-ipv6-backup")
                self._segment_path = lambda: "policy-ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/%s" % self._segment_path()


            class PolicyIpv6Active(Entity):
                """
                IPv6 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Policy.PolicyIpv6.PolicyIpv6Active, self).__init__()

                    self.yang_name = "policy-ipv6-active"
                    self.yang_parent_name = "policy-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"policy-mi" : ("policy_mi", Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi)}

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv6-active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Active, [], name, value)


                class PolicyMi(Entity):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  <key>
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr>`
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv6-active"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"addr" : ("addr", Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr)}
                        self._child_list_classes = {}

                        self.mi_id = YLeaf(YType.str, "mi-id")

                        self.area = YLeaf(YType.str, "area")

                        self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                        self.last_prefix = YLeaf(YType.str, "last-prefix")

                        self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                        self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                        self.router = YLeaf(YType.str, "router")

                        self.sid_count = YLeaf(YType.uint32, "sid-count")

                        self.sid_start = YLeaf(YType.uint32, "sid-start")

                        self.src = YLeaf(YType.enumeration, "src")

                        self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._children_yang_names.add("addr")
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + self.mi_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/policy-ipv6-active/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, ['mi_id', 'area', 'flag_attached', 'last_prefix', 'last_sid_index', 'prefix_xr', 'router', 'sid_count', 'sid_start', 'src'], name, value)


                    class Addr(Entity):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af = YLeaf(YType.enumeration, "af")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "addr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)


            class PolicyIpv6Backup(Entity):
                """
                IPv6 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup, self).__init__()

                    self.yang_name = "policy-ipv6-backup"
                    self.yang_parent_name = "policy-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"policy-mi" : ("policy_mi", Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi)}

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv6-backup"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Backup, [], name, value)


                class PolicyMi(Entity):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  <key>
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr>`
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv6-backup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"addr" : ("addr", Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr)}
                        self._child_list_classes = {}

                        self.mi_id = YLeaf(YType.str, "mi-id")

                        self.area = YLeaf(YType.str, "area")

                        self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                        self.last_prefix = YLeaf(YType.str, "last-prefix")

                        self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                        self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                        self.router = YLeaf(YType.str, "router")

                        self.sid_count = YLeaf(YType.uint32, "sid-count")

                        self.sid_start = YLeaf(YType.uint32, "sid-start")

                        self.src = YLeaf(YType.enumeration, "src")

                        self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._children_yang_names.add("addr")
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + self.mi_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/policy-ipv6-backup/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, ['mi_id', 'area', 'flag_attached', 'last_prefix', 'last_sid_index', 'prefix_xr', 'router', 'sid_count', 'sid_start', 'src'], name, value)


                    class Addr(Entity):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af = YLeaf(YType.enumeration, "af")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "addr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

    def clone_ptr(self):
        self._top_entity = Srms()
        return self._top_entity

