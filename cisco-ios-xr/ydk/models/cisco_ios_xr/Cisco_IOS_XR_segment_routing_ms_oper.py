""" Cisco_IOS_XR_segment_routing_ms_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package operational data.

This module contains definitions
for the following management objects\:
  standby\-srms\: Standby Segment Routing Mapping Server
    operational data
  srms\: srms
  srlb\: srlb

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SidTypeEnum(Enum):
    """
    SidTypeEnum (Enum Class)

    Sid type enum

    .. data:: absolute = 1

    	Absolute SID

    .. data:: index = 2

    	Index SID

    """

    absolute = Enum.YLeaf(1, "absolute")

    index = Enum.YLeaf(2, "index")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['SidTypeEnum']


class SrmsAf(Enum):
    """
    SrmsAf (Enum Class)

    Srms af

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['SrmsAf']


class SrmsMiAfEB(Enum):
    """
    SrmsMiAfEB (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['SrmsMiAfEB']


class SrmsMiFlagEB(Enum):
    """
    SrmsMiFlagEB (Enum Class)

    Srms mi flag e b

    .. data:: false = 0

    	False

    .. data:: true = 1

    	True

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(1, "true")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['SrmsMiFlagEB']


class SrmsMiSrcEB(Enum):
    """
    SrmsMiSrcEB (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['SrmsMiSrcEB']



class StandbySrms(_Entity_):
    """
    Standby Segment Routing Mapping Server
    operational data
    
    .. attribute:: mapping
    
    	IP prefix to SID mappings
    	**type**\:  :py:class:`Mapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Mapping>`
    
    	**config**\: False
    
    .. attribute:: policy
    
    	Policy operational data
    	**type**\:  :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy>`
    
    	**config**\: False
    
    

    """

    _prefix = 'segment-routing-ms-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(StandbySrms, self).__init__()
        self._top_entity = None

        self.yang_name = "standby-srms"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mapping", ("mapping", StandbySrms.Mapping)), ("policy", ("policy", StandbySrms.Policy))])
        self._leafs = OrderedDict()

        self.mapping = StandbySrms.Mapping()
        self.mapping.parent = self
        self._children_name_map["mapping"] = "mapping"

        self.policy = StandbySrms.Policy()
        self.policy.parent = self
        self._children_name_map["policy"] = "policy"
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(StandbySrms, [], name, value)


    class Mapping(_Entity_):
        """
        IP prefix to SID mappings
        
        .. attribute:: mapping_ipv4
        
        	IPv4 prefix to SID mappings
        	**type**\:  :py:class:`MappingIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Mapping.MappingIpv4>`
        
        	**config**\: False
        
        .. attribute:: mapping_ipv6
        
        	IPv6 prefix to SID mappings
        	**type**\:  :py:class:`MappingIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Mapping.MappingIpv6>`
        
        	**config**\: False
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(StandbySrms.Mapping, self).__init__()

            self.yang_name = "mapping"
            self.yang_parent_name = "standby-srms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mapping-ipv4", ("mapping_ipv4", StandbySrms.Mapping.MappingIpv4)), ("mapping-ipv6", ("mapping_ipv6", StandbySrms.Mapping.MappingIpv6))])
            self._leafs = OrderedDict()

            self.mapping_ipv4 = StandbySrms.Mapping.MappingIpv4()
            self.mapping_ipv4.parent = self
            self._children_name_map["mapping_ipv4"] = "mapping-ipv4"

            self.mapping_ipv6 = StandbySrms.Mapping.MappingIpv6()
            self.mapping_ipv6.parent = self
            self._children_name_map["mapping_ipv6"] = "mapping-ipv6"
            self._segment_path = lambda: "mapping"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(StandbySrms.Mapping, [], name, value)


        class MappingIpv4(_Entity_):
            """
            IPv4 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of  		 :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Mapping.MappingIpv4.MappingMi>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(StandbySrms.Mapping.MappingIpv4, self).__init__()

                self.yang_name = "mapping-ipv4"
                self.yang_parent_name = "mapping"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mapping-mi", ("mapping_mi", StandbySrms.Mapping.MappingIpv4.MappingMi))])
                self._leafs = OrderedDict()

                self.mapping_mi = YList(self)
                self._segment_path = lambda: "mapping-ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/mapping/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(StandbySrms.Mapping.MappingIpv4, [], name, value)


            class MappingMi(_Entity_):
                """
                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                
                .. attribute:: ip
                
                	IP
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: addr
                
                	addr
                	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Mapping.MappingIpv4.MappingMi.Addr>`
                
                	**config**\: False
                
                .. attribute:: src
                
                	src
                	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                
                	**config**\: False
                
                .. attribute:: router
                
                	Router ID
                	**type**\: str
                
                	**length:** 0..30
                
                	**config**\: False
                
                .. attribute:: area
                
                	Area (OSPF) or Level (ISIS)
                	**type**\: str
                
                	**length:** 0..30
                
                	**config**\: False
                
                .. attribute:: prefix_xr
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: sid_start
                
                	Starting SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_count
                
                	SID range
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: last_prefix
                
                	Last IP Prefix
                	**type**\: str
                
                	**length:** 0..50
                
                	**config**\: False
                
                .. attribute:: last_sid_index
                
                	Last SID Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flag_attached
                
                	Attached flag
                	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(StandbySrms.Mapping.MappingIpv4.MappingMi, self).__init__()

                    self.yang_name = "mapping-mi"
                    self.yang_parent_name = "mapping-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("addr", ("addr", StandbySrms.Mapping.MappingIpv4.MappingMi.Addr))])
                    self._leafs = OrderedDict([
                        ('ip', (YLeaf(YType.str, 'ip'), ['str'])),
                        ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                        ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                        ('router', (YLeaf(YType.str, 'router'), ['str'])),
                        ('area', (YLeaf(YType.str, 'area'), ['str'])),
                        ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                        ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                        ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                        ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                        ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                        ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                    ])
                    self.ip = None
                    self.prefix = None
                    self.src = None
                    self.router = None
                    self.area = None
                    self.prefix_xr = None
                    self.sid_start = None
                    self.sid_count = None
                    self.last_prefix = None
                    self.last_sid_index = None
                    self.flag_attached = None

                    self.addr = StandbySrms.Mapping.MappingIpv4.MappingMi.Addr()
                    self.addr.parent = self
                    self._children_name_map["addr"] = "addr"
                    self._segment_path = lambda: "mapping-mi"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/mapping/mapping-ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(StandbySrms.Mapping.MappingIpv4.MappingMi, ['ip', 'prefix', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                class Addr(_Entity_):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4
                    
                    	IPv4
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(StandbySrms.Mapping.MappingIpv4.MappingMi.Addr, self).__init__()

                        self.yang_name = "addr"
                        self.yang_parent_name = "mapping-mi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "addr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/mapping/mapping-ipv4/mapping-mi/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(StandbySrms.Mapping.MappingIpv4.MappingMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['StandbySrms.Mapping.MappingIpv4.MappingMi.Addr']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['StandbySrms.Mapping.MappingIpv4.MappingMi']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['StandbySrms.Mapping.MappingIpv4']['meta_info']


        class MappingIpv6(_Entity_):
            """
            IPv6 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of  		 :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Mapping.MappingIpv6.MappingMi>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(StandbySrms.Mapping.MappingIpv6, self).__init__()

                self.yang_name = "mapping-ipv6"
                self.yang_parent_name = "mapping"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mapping-mi", ("mapping_mi", StandbySrms.Mapping.MappingIpv6.MappingMi))])
                self._leafs = OrderedDict()

                self.mapping_mi = YList(self)
                self._segment_path = lambda: "mapping-ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/mapping/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(StandbySrms.Mapping.MappingIpv6, [], name, value)


            class MappingMi(_Entity_):
                """
                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                
                .. attribute:: ip
                
                	IP
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: addr
                
                	addr
                	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Mapping.MappingIpv6.MappingMi.Addr>`
                
                	**config**\: False
                
                .. attribute:: src
                
                	src
                	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                
                	**config**\: False
                
                .. attribute:: router
                
                	Router ID
                	**type**\: str
                
                	**length:** 0..30
                
                	**config**\: False
                
                .. attribute:: area
                
                	Area (OSPF) or Level (ISIS)
                	**type**\: str
                
                	**length:** 0..30
                
                	**config**\: False
                
                .. attribute:: prefix_xr
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: sid_start
                
                	Starting SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_count
                
                	SID range
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: last_prefix
                
                	Last IP Prefix
                	**type**\: str
                
                	**length:** 0..50
                
                	**config**\: False
                
                .. attribute:: last_sid_index
                
                	Last SID Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flag_attached
                
                	Attached flag
                	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(StandbySrms.Mapping.MappingIpv6.MappingMi, self).__init__()

                    self.yang_name = "mapping-mi"
                    self.yang_parent_name = "mapping-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("addr", ("addr", StandbySrms.Mapping.MappingIpv6.MappingMi.Addr))])
                    self._leafs = OrderedDict([
                        ('ip', (YLeaf(YType.str, 'ip'), ['str'])),
                        ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                        ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                        ('router', (YLeaf(YType.str, 'router'), ['str'])),
                        ('area', (YLeaf(YType.str, 'area'), ['str'])),
                        ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                        ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                        ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                        ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                        ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                        ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                    ])
                    self.ip = None
                    self.prefix = None
                    self.src = None
                    self.router = None
                    self.area = None
                    self.prefix_xr = None
                    self.sid_start = None
                    self.sid_count = None
                    self.last_prefix = None
                    self.last_sid_index = None
                    self.flag_attached = None

                    self.addr = StandbySrms.Mapping.MappingIpv6.MappingMi.Addr()
                    self.addr.parent = self
                    self._children_name_map["addr"] = "addr"
                    self._segment_path = lambda: "mapping-mi"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/mapping/mapping-ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(StandbySrms.Mapping.MappingIpv6.MappingMi, ['ip', 'prefix', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                class Addr(_Entity_):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4
                    
                    	IPv4
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(StandbySrms.Mapping.MappingIpv6.MappingMi.Addr, self).__init__()

                        self.yang_name = "addr"
                        self.yang_parent_name = "mapping-mi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "addr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/mapping/mapping-ipv6/mapping-mi/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(StandbySrms.Mapping.MappingIpv6.MappingMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['StandbySrms.Mapping.MappingIpv6.MappingMi.Addr']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['StandbySrms.Mapping.MappingIpv6.MappingMi']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['StandbySrms.Mapping.MappingIpv6']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
            return meta._meta_table['StandbySrms.Mapping']['meta_info']


    class Policy(_Entity_):
        """
        Policy operational data
        
        .. attribute:: policy_ipv4
        
        	IPv4 policy operational data
        	**type**\:  :py:class:`PolicyIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv4>`
        
        	**config**\: False
        
        .. attribute:: policy_ipv6
        
        	IPv6 policy operational data
        	**type**\:  :py:class:`PolicyIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv6>`
        
        	**config**\: False
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(StandbySrms.Policy, self).__init__()

            self.yang_name = "policy"
            self.yang_parent_name = "standby-srms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-ipv4", ("policy_ipv4", StandbySrms.Policy.PolicyIpv4)), ("policy-ipv6", ("policy_ipv6", StandbySrms.Policy.PolicyIpv6))])
            self._leafs = OrderedDict()

            self.policy_ipv4 = StandbySrms.Policy.PolicyIpv4()
            self.policy_ipv4.parent = self
            self._children_name_map["policy_ipv4"] = "policy-ipv4"

            self.policy_ipv6 = StandbySrms.Policy.PolicyIpv6()
            self.policy_ipv6.parent = self
            self._children_name_map["policy_ipv6"] = "policy-ipv6"
            self._segment_path = lambda: "policy"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(StandbySrms.Policy, [], name, value)


        class PolicyIpv4(_Entity_):
            """
            IPv4 policy operational data
            
            .. attribute:: policy_ipv4_backup
            
            	IPv4 backup policy operational data
            	**type**\:  :py:class:`PolicyIpv4Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup>`
            
            	**config**\: False
            
            .. attribute:: policy_ipv4_active
            
            	IPv4 active policy operational data
            	**type**\:  :py:class:`PolicyIpv4Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(StandbySrms.Policy.PolicyIpv4, self).__init__()

                self.yang_name = "policy-ipv4"
                self.yang_parent_name = "policy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policy-ipv4-backup", ("policy_ipv4_backup", StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup)), ("policy-ipv4-active", ("policy_ipv4_active", StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active))])
                self._leafs = OrderedDict()

                self.policy_ipv4_backup = StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup()
                self.policy_ipv4_backup.parent = self
                self._children_name_map["policy_ipv4_backup"] = "policy-ipv4-backup"

                self.policy_ipv4_active = StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active()
                self.policy_ipv4_active.parent = self
                self._children_name_map["policy_ipv4_active"] = "policy-ipv4-active"
                self._segment_path = lambda: "policy-ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(StandbySrms.Policy.PolicyIpv4, [], name, value)


            class PolicyIpv4Backup(_Entity_):
                """
                IPv4 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of  		 :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup, self).__init__()

                    self.yang_name = "policy-ipv4-backup"
                    self.yang_parent_name = "policy-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy-mi", ("policy_mi", StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi))])
                    self._leafs = OrderedDict()

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv4-backup"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/policy-ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup, [], name, value)


                class PolicyMi(_Entity_):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  (key)
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr>`
                    
                    	**config**\: False
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv4-backup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mi_id']
                        self._child_classes = OrderedDict([("addr", ("addr", StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr))])
                        self._leafs = OrderedDict([
                            ('mi_id', (YLeaf(YType.str, 'mi-id'), ['str'])),
                            ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                            ('router', (YLeaf(YType.str, 'router'), ['str'])),
                            ('area', (YLeaf(YType.str, 'area'), ['str'])),
                            ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                            ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                            ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                            ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                            ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                            ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                        ])
                        self.mi_id = None
                        self.src = None
                        self.router = None
                        self.area = None
                        self.prefix_xr = None
                        self.sid_start = None
                        self.sid_count = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.flag_attached = None

                        self.addr = StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + str(self.mi_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/policy-ipv4/policy-ipv4-backup/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, ['mi_id', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                    class Addr(_Entity_):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "addr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['StandbySrms.Policy.PolicyIpv4.PolicyIpv4Backup']['meta_info']


            class PolicyIpv4Active(_Entity_):
                """
                IPv4 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of  		 :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active, self).__init__()

                    self.yang_name = "policy-ipv4-active"
                    self.yang_parent_name = "policy-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy-mi", ("policy_mi", StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi))])
                    self._leafs = OrderedDict()

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv4-active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/policy-ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active, [], name, value)


                class PolicyMi(_Entity_):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  (key)
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr>`
                    
                    	**config**\: False
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv4-active"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mi_id']
                        self._child_classes = OrderedDict([("addr", ("addr", StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr))])
                        self._leafs = OrderedDict([
                            ('mi_id', (YLeaf(YType.str, 'mi-id'), ['str'])),
                            ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                            ('router', (YLeaf(YType.str, 'router'), ['str'])),
                            ('area', (YLeaf(YType.str, 'area'), ['str'])),
                            ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                            ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                            ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                            ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                            ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                            ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                        ])
                        self.mi_id = None
                        self.src = None
                        self.router = None
                        self.area = None
                        self.prefix_xr = None
                        self.sid_start = None
                        self.sid_count = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.flag_attached = None

                        self.addr = StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + str(self.mi_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/policy-ipv4/policy-ipv4-active/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, ['mi_id', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                    class Addr(_Entity_):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "addr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['StandbySrms.Policy.PolicyIpv4.PolicyIpv4Active']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['StandbySrms.Policy.PolicyIpv4']['meta_info']


        class PolicyIpv6(_Entity_):
            """
            IPv6 policy operational data
            
            .. attribute:: policy_ipv6_backup
            
            	IPv6 backup policy operational data
            	**type**\:  :py:class:`PolicyIpv6Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup>`
            
            	**config**\: False
            
            .. attribute:: policy_ipv6_active
            
            	IPv6 active policy operational data
            	**type**\:  :py:class:`PolicyIpv6Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(StandbySrms.Policy.PolicyIpv6, self).__init__()

                self.yang_name = "policy-ipv6"
                self.yang_parent_name = "policy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policy-ipv6-backup", ("policy_ipv6_backup", StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup)), ("policy-ipv6-active", ("policy_ipv6_active", StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active))])
                self._leafs = OrderedDict()

                self.policy_ipv6_backup = StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup()
                self.policy_ipv6_backup.parent = self
                self._children_name_map["policy_ipv6_backup"] = "policy-ipv6-backup"

                self.policy_ipv6_active = StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active()
                self.policy_ipv6_active.parent = self
                self._children_name_map["policy_ipv6_active"] = "policy-ipv6-active"
                self._segment_path = lambda: "policy-ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(StandbySrms.Policy.PolicyIpv6, [], name, value)


            class PolicyIpv6Backup(_Entity_):
                """
                IPv6 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of  		 :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup, self).__init__()

                    self.yang_name = "policy-ipv6-backup"
                    self.yang_parent_name = "policy-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy-mi", ("policy_mi", StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi))])
                    self._leafs = OrderedDict()

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv6-backup"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/policy-ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup, [], name, value)


                class PolicyMi(_Entity_):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  (key)
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr>`
                    
                    	**config**\: False
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv6-backup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mi_id']
                        self._child_classes = OrderedDict([("addr", ("addr", StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr))])
                        self._leafs = OrderedDict([
                            ('mi_id', (YLeaf(YType.str, 'mi-id'), ['str'])),
                            ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                            ('router', (YLeaf(YType.str, 'router'), ['str'])),
                            ('area', (YLeaf(YType.str, 'area'), ['str'])),
                            ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                            ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                            ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                            ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                            ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                            ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                        ])
                        self.mi_id = None
                        self.src = None
                        self.router = None
                        self.area = None
                        self.prefix_xr = None
                        self.sid_start = None
                        self.sid_count = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.flag_attached = None

                        self.addr = StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + str(self.mi_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/policy-ipv6/policy-ipv6-backup/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, ['mi_id', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                    class Addr(_Entity_):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "addr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['StandbySrms.Policy.PolicyIpv6.PolicyIpv6Backup']['meta_info']


            class PolicyIpv6Active(_Entity_):
                """
                IPv6 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of  		 :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active, self).__init__()

                    self.yang_name = "policy-ipv6-active"
                    self.yang_parent_name = "policy-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy-mi", ("policy_mi", StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi))])
                    self._leafs = OrderedDict()

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv6-active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/policy-ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active, [], name, value)


                class PolicyMi(_Entity_):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  (key)
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr>`
                    
                    	**config**\: False
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv6-active"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mi_id']
                        self._child_classes = OrderedDict([("addr", ("addr", StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr))])
                        self._leafs = OrderedDict([
                            ('mi_id', (YLeaf(YType.str, 'mi-id'), ['str'])),
                            ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                            ('router', (YLeaf(YType.str, 'router'), ['str'])),
                            ('area', (YLeaf(YType.str, 'area'), ['str'])),
                            ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                            ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                            ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                            ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                            ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                            ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                        ])
                        self.mi_id = None
                        self.src = None
                        self.router = None
                        self.area = None
                        self.prefix_xr = None
                        self.sid_start = None
                        self.sid_count = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.flag_attached = None

                        self.addr = StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + str(self.mi_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:standby-srms/policy/policy-ipv6/policy-ipv6-active/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, ['mi_id', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                    class Addr(_Entity_):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "addr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['StandbySrms.Policy.PolicyIpv6.PolicyIpv6Active']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['StandbySrms.Policy.PolicyIpv6']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
            return meta._meta_table['StandbySrms.Policy']['meta_info']

    def clone_ptr(self):
        self._top_entity = StandbySrms()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['StandbySrms']['meta_info']


class Srms(_Entity_):
    """
    srms
    
    .. attribute:: adjacency_sid
    
    	Adjacency SID
    	**type**\:  :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid>`
    
    	**config**\: False
    
    .. attribute:: mapping
    
    	IP prefix to SID mappings
    	**type**\:  :py:class:`Mapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping>`
    
    	**config**\: False
    
    .. attribute:: policy
    
    	Policy operational data
    	**type**\:  :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy>`
    
    	**config**\: False
    
    

    """

    _prefix = 'segment-routing-ms-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Srms, self).__init__()
        self._top_entity = None

        self.yang_name = "srms"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("adjacency-sid", ("adjacency_sid", Srms.AdjacencySid)), ("mapping", ("mapping", Srms.Mapping)), ("policy", ("policy", Srms.Policy))])
        self._leafs = OrderedDict()

        self.adjacency_sid = Srms.AdjacencySid()
        self.adjacency_sid.parent = self
        self._children_name_map["adjacency_sid"] = "adjacency-sid"

        self.mapping = Srms.Mapping()
        self.mapping.parent = self
        self._children_name_map["mapping"] = "mapping"

        self.policy = Srms.Policy()
        self.policy.parent = self
        self._children_name_map["policy"] = "policy"
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Srms, [], name, value)


    class AdjacencySid(_Entity_):
        """
        Adjacency SID
        
        .. attribute:: l2_adjacency
        
        	L2 Adjacency Option
        	**type**\:  :py:class:`L2Adjacency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency>`
        
        	**config**\: False
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srms.AdjacencySid, self).__init__()

            self.yang_name = "adjacency-sid"
            self.yang_parent_name = "srms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("l2-adjacency", ("l2_adjacency", Srms.AdjacencySid.L2Adjacency))])
            self._leafs = OrderedDict()

            self.l2_adjacency = Srms.AdjacencySid.L2Adjacency()
            self.l2_adjacency.parent = self
            self._children_name_map["l2_adjacency"] = "l2-adjacency"
            self._segment_path = lambda: "adjacency-sid"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srms.AdjacencySid, [], name, value)


        class L2Adjacency(_Entity_):
            """
            L2 Adjacency Option
            
            .. attribute:: interfaces
            
            	Interface directory
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srms.AdjacencySid.L2Adjacency, self).__init__()

                self.yang_name = "l2-adjacency"
                self.yang_parent_name = "adjacency-sid"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interfaces", ("interfaces", Srms.AdjacencySid.L2Adjacency.Interfaces))])
                self._leafs = OrderedDict()

                self.interfaces = Srms.AdjacencySid.L2Adjacency.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "l2-adjacency"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/adjacency-sid/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srms.AdjacencySid.L2Adjacency, [], name, value)


            class Interfaces(_Entity_):
                """
                Interface directory
                
                .. attribute:: interface
                
                	Segment Routing Adjacency SID Interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces.Interface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srms.AdjacencySid.L2Adjacency.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "l2-adjacency"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Srms.AdjacencySid.L2Adjacency.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/adjacency-sid/l2-adjacency/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces, [], name, value)


                class Interface(_Entity_):
                    """
                    Segment Routing Adjacency SID Interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: address_family
                    
                    	address family container
                    	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("address-family", ("address_family", Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.address_family = Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily()
                        self.address_family.parent = self
                        self._children_name_map["address_family"] = "address-family"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/adjacency-sid/l2-adjacency/interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface, ['interface_name'], name, value)


                    class AddressFamily(_Entity_):
                        """
                        address family container
                        
                        .. attribute:: ipv4
                        
                        	IP version 4
                        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IP version 6
                        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily, self).__init__()

                            self.yang_name = "address-family"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv4", ("ipv4", Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4)), ("ipv6", ("ipv6", Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6))])
                            self._leafs = OrderedDict()

                            self.ipv4 = Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4()
                            self.ipv4.parent = self
                            self._children_name_map["ipv4"] = "ipv4"

                            self.ipv6 = Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6()
                            self.ipv6.parent = self
                            self._children_name_map["ipv6"] = "ipv6"
                            self._segment_path = lambda: "address-family"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily, [], name, value)


                        class Ipv4(_Entity_):
                            """
                            IP version 4
                            
                            .. attribute:: sid_record
                            
                            	SID record
                            	**type**\: list of  		 :py:class:`SidRecord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-ms-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4, self).__init__()

                                self.yang_name = "ipv4"
                                self.yang_parent_name = "address-family"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("sid-record", ("sid_record", Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord))])
                                self._leafs = OrderedDict()

                                self.sid_record = YList(self)
                                self._segment_path = lambda: "ipv4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4, [], name, value)


                            class SidRecord(_Entity_):
                                """
                                SID record
                                
                                .. attribute:: sid_type
                                
                                	SID type
                                	**type**\:  :py:class:`SidTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SidTypeEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: sid_value
                                
                                	SID value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: nexthop_address
                                
                                	Nexthop address
                                	**type**\:  :py:class:`NexthopAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord.NexthopAddress>`
                                
                                	**config**\: False
                                
                                .. attribute:: interface_name
                                
                                	Interface name
                                	**type**\: str
                                
                                	**length:** 0..64
                                
                                	**config**\: False
                                
                                .. attribute:: sid_value_xr
                                
                                	SID Value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sid_type_xr
                                
                                	SID type
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: address_family
                                
                                	Interface address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: has_nexthop
                                
                                	Has nexthop
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: interface_count
                                
                                	Interface count
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                .. attribute:: interface_delete_count
                                
                                	Interface delete count
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'segment-routing-ms-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord, self).__init__()

                                    self.yang_name = "sid-record"
                                    self.yang_parent_name = "ipv4"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("nexthop-address", ("nexthop_address", Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord.NexthopAddress))])
                                    self._leafs = OrderedDict([
                                        ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SidTypeEnum', '')])),
                                        ('sid_value', (YLeaf(YType.uint32, 'sid-value'), ['int'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('sid_value_xr', (YLeaf(YType.uint32, 'sid-value-xr'), ['int'])),
                                        ('sid_type_xr', (YLeaf(YType.uint32, 'sid-type-xr'), ['int'])),
                                        ('address_family', (YLeaf(YType.uint32, 'address-family'), ['int'])),
                                        ('has_nexthop', (YLeaf(YType.boolean, 'has-nexthop'), ['bool'])),
                                        ('interface_count', (YLeaf(YType.int32, 'interface-count'), ['int'])),
                                        ('interface_delete_count', (YLeaf(YType.int32, 'interface-delete-count'), ['int'])),
                                    ])
                                    self.sid_type = None
                                    self.sid_value = None
                                    self.interface_name = None
                                    self.sid_value_xr = None
                                    self.sid_type_xr = None
                                    self.address_family = None
                                    self.has_nexthop = None
                                    self.interface_count = None
                                    self.interface_delete_count = None

                                    self.nexthop_address = Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord.NexthopAddress()
                                    self.nexthop_address.parent = self
                                    self._children_name_map["nexthop_address"] = "nexthop-address"
                                    self._segment_path = lambda: "sid-record"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord, ['sid_type', 'sid_value', 'interface_name', 'sid_value_xr', 'sid_type_xr', 'address_family', 'has_nexthop', 'interface_count', 'interface_delete_count'], name, value)


                                class NexthopAddress(_Entity_):
                                    """
                                    Nexthop address
                                    
                                    .. attribute:: af
                                    
                                    	AF
                                    	**type**\:  :py:class:`SrmsAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsAf>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4
                                    
                                    	IPv4
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6
                                    
                                    	IPv6
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-ms-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord.NexthopAddress, self).__init__()

                                        self.yang_name = "nexthop-address"
                                        self.yang_parent_name = "sid-record"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsAf', '')])),
                                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                        ])
                                        self.af = None
                                        self.ipv4 = None
                                        self.ipv6 = None
                                        self._segment_path = lambda: "nexthop-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord.NexthopAddress, ['af', 'ipv4', 'ipv6'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                                        return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord.NexthopAddress']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                                    return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4.SidRecord']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                                return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv4']['meta_info']


                        class Ipv6(_Entity_):
                            """
                            IP version 6
                            
                            .. attribute:: sid_record
                            
                            	SID record
                            	**type**\: list of  		 :py:class:`SidRecord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-ms-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6, self).__init__()

                                self.yang_name = "ipv6"
                                self.yang_parent_name = "address-family"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("sid-record", ("sid_record", Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord))])
                                self._leafs = OrderedDict()

                                self.sid_record = YList(self)
                                self._segment_path = lambda: "ipv6"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6, [], name, value)


                            class SidRecord(_Entity_):
                                """
                                SID record
                                
                                .. attribute:: sid_type
                                
                                	SID type
                                	**type**\:  :py:class:`SidTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SidTypeEnum>`
                                
                                	**config**\: False
                                
                                .. attribute:: sid_value
                                
                                	SID value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: nexthop_address
                                
                                	Nexthop address
                                	**type**\:  :py:class:`NexthopAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord.NexthopAddress>`
                                
                                	**config**\: False
                                
                                .. attribute:: interface_name
                                
                                	Interface name
                                	**type**\: str
                                
                                	**length:** 0..64
                                
                                	**config**\: False
                                
                                .. attribute:: sid_value_xr
                                
                                	SID Value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sid_type_xr
                                
                                	SID type
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: address_family
                                
                                	Interface address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: has_nexthop
                                
                                	Has nexthop
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: interface_count
                                
                                	Interface count
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                .. attribute:: interface_delete_count
                                
                                	Interface delete count
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'segment-routing-ms-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord, self).__init__()

                                    self.yang_name = "sid-record"
                                    self.yang_parent_name = "ipv6"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("nexthop-address", ("nexthop_address", Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord.NexthopAddress))])
                                    self._leafs = OrderedDict([
                                        ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SidTypeEnum', '')])),
                                        ('sid_value', (YLeaf(YType.uint32, 'sid-value'), ['int'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('sid_value_xr', (YLeaf(YType.uint32, 'sid-value-xr'), ['int'])),
                                        ('sid_type_xr', (YLeaf(YType.uint32, 'sid-type-xr'), ['int'])),
                                        ('address_family', (YLeaf(YType.uint32, 'address-family'), ['int'])),
                                        ('has_nexthop', (YLeaf(YType.boolean, 'has-nexthop'), ['bool'])),
                                        ('interface_count', (YLeaf(YType.int32, 'interface-count'), ['int'])),
                                        ('interface_delete_count', (YLeaf(YType.int32, 'interface-delete-count'), ['int'])),
                                    ])
                                    self.sid_type = None
                                    self.sid_value = None
                                    self.interface_name = None
                                    self.sid_value_xr = None
                                    self.sid_type_xr = None
                                    self.address_family = None
                                    self.has_nexthop = None
                                    self.interface_count = None
                                    self.interface_delete_count = None

                                    self.nexthop_address = Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord.NexthopAddress()
                                    self.nexthop_address.parent = self
                                    self._children_name_map["nexthop_address"] = "nexthop-address"
                                    self._segment_path = lambda: "sid-record"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord, ['sid_type', 'sid_value', 'interface_name', 'sid_value_xr', 'sid_type_xr', 'address_family', 'has_nexthop', 'interface_count', 'interface_delete_count'], name, value)


                                class NexthopAddress(_Entity_):
                                    """
                                    Nexthop address
                                    
                                    .. attribute:: af
                                    
                                    	AF
                                    	**type**\:  :py:class:`SrmsAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsAf>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4
                                    
                                    	IPv4
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6
                                    
                                    	IPv6
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-ms-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord.NexthopAddress, self).__init__()

                                        self.yang_name = "nexthop-address"
                                        self.yang_parent_name = "sid-record"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsAf', '')])),
                                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                        ])
                                        self.af = None
                                        self.ipv4 = None
                                        self.ipv6 = None
                                        self._segment_path = lambda: "nexthop-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord.NexthopAddress, ['af', 'ipv4', 'ipv6'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                                        return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord.NexthopAddress']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                                    return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6.SidRecord']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                                return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily.Ipv6']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces.Interface.AddressFamily']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces.Interface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.AdjacencySid.L2Adjacency.Interfaces']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.AdjacencySid.L2Adjacency']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
            return meta._meta_table['Srms.AdjacencySid']['meta_info']


    class Mapping(_Entity_):
        """
        IP prefix to SID mappings
        
        .. attribute:: mapping_ipv4
        
        	IPv4 prefix to SID mappings
        	**type**\:  :py:class:`MappingIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4>`
        
        	**config**\: False
        
        .. attribute:: mapping_ipv6
        
        	IPv6 prefix to SID mappings
        	**type**\:  :py:class:`MappingIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6>`
        
        	**config**\: False
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srms.Mapping, self).__init__()

            self.yang_name = "mapping"
            self.yang_parent_name = "srms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mapping-ipv4", ("mapping_ipv4", Srms.Mapping.MappingIpv4)), ("mapping-ipv6", ("mapping_ipv6", Srms.Mapping.MappingIpv6))])
            self._leafs = OrderedDict()

            self.mapping_ipv4 = Srms.Mapping.MappingIpv4()
            self.mapping_ipv4.parent = self
            self._children_name_map["mapping_ipv4"] = "mapping-ipv4"

            self.mapping_ipv6 = Srms.Mapping.MappingIpv6()
            self.mapping_ipv6.parent = self
            self._children_name_map["mapping_ipv6"] = "mapping-ipv6"
            self._segment_path = lambda: "mapping"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srms.Mapping, [], name, value)


        class MappingIpv4(_Entity_):
            """
            IPv4 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of  		 :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4.MappingMi>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srms.Mapping.MappingIpv4, self).__init__()

                self.yang_name = "mapping-ipv4"
                self.yang_parent_name = "mapping"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mapping-mi", ("mapping_mi", Srms.Mapping.MappingIpv4.MappingMi))])
                self._leafs = OrderedDict()

                self.mapping_mi = YList(self)
                self._segment_path = lambda: "mapping-ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srms.Mapping.MappingIpv4, [], name, value)


            class MappingMi(_Entity_):
                """
                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                
                .. attribute:: ip
                
                	IP
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: addr
                
                	addr
                	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4.MappingMi.Addr>`
                
                	**config**\: False
                
                .. attribute:: src
                
                	src
                	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                
                	**config**\: False
                
                .. attribute:: router
                
                	Router ID
                	**type**\: str
                
                	**length:** 0..30
                
                	**config**\: False
                
                .. attribute:: area
                
                	Area (OSPF) or Level (ISIS)
                	**type**\: str
                
                	**length:** 0..30
                
                	**config**\: False
                
                .. attribute:: prefix_xr
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: sid_start
                
                	Starting SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_count
                
                	SID range
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: last_prefix
                
                	Last IP Prefix
                	**type**\: str
                
                	**length:** 0..50
                
                	**config**\: False
                
                .. attribute:: last_sid_index
                
                	Last SID Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flag_attached
                
                	Attached flag
                	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srms.Mapping.MappingIpv4.MappingMi, self).__init__()

                    self.yang_name = "mapping-mi"
                    self.yang_parent_name = "mapping-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("addr", ("addr", Srms.Mapping.MappingIpv4.MappingMi.Addr))])
                    self._leafs = OrderedDict([
                        ('ip', (YLeaf(YType.str, 'ip'), ['str'])),
                        ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                        ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                        ('router', (YLeaf(YType.str, 'router'), ['str'])),
                        ('area', (YLeaf(YType.str, 'area'), ['str'])),
                        ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                        ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                        ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                        ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                        ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                        ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                    ])
                    self.ip = None
                    self.prefix = None
                    self.src = None
                    self.router = None
                    self.area = None
                    self.prefix_xr = None
                    self.sid_start = None
                    self.sid_count = None
                    self.last_prefix = None
                    self.last_sid_index = None
                    self.flag_attached = None

                    self.addr = Srms.Mapping.MappingIpv4.MappingMi.Addr()
                    self.addr.parent = self
                    self._children_name_map["addr"] = "addr"
                    self._segment_path = lambda: "mapping-mi"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Mapping.MappingIpv4.MappingMi, ['ip', 'prefix', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                class Addr(_Entity_):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4
                    
                    	IPv4
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srms.Mapping.MappingIpv4.MappingMi.Addr, self).__init__()

                        self.yang_name = "addr"
                        self.yang_parent_name = "mapping-mi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "addr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv4/mapping-mi/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Mapping.MappingIpv4.MappingMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Mapping.MappingIpv4.MappingMi.Addr']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Mapping.MappingIpv4.MappingMi']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.Mapping.MappingIpv4']['meta_info']


        class MappingIpv6(_Entity_):
            """
            IPv6 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of  		 :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6.MappingMi>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srms.Mapping.MappingIpv6, self).__init__()

                self.yang_name = "mapping-ipv6"
                self.yang_parent_name = "mapping"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mapping-mi", ("mapping_mi", Srms.Mapping.MappingIpv6.MappingMi))])
                self._leafs = OrderedDict()

                self.mapping_mi = YList(self)
                self._segment_path = lambda: "mapping-ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srms.Mapping.MappingIpv6, [], name, value)


            class MappingMi(_Entity_):
                """
                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                
                .. attribute:: ip
                
                	IP
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: addr
                
                	addr
                	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6.MappingMi.Addr>`
                
                	**config**\: False
                
                .. attribute:: src
                
                	src
                	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                
                	**config**\: False
                
                .. attribute:: router
                
                	Router ID
                	**type**\: str
                
                	**length:** 0..30
                
                	**config**\: False
                
                .. attribute:: area
                
                	Area (OSPF) or Level (ISIS)
                	**type**\: str
                
                	**length:** 0..30
                
                	**config**\: False
                
                .. attribute:: prefix_xr
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: sid_start
                
                	Starting SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_count
                
                	SID range
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: last_prefix
                
                	Last IP Prefix
                	**type**\: str
                
                	**length:** 0..50
                
                	**config**\: False
                
                .. attribute:: last_sid_index
                
                	Last SID Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flag_attached
                
                	Attached flag
                	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srms.Mapping.MappingIpv6.MappingMi, self).__init__()

                    self.yang_name = "mapping-mi"
                    self.yang_parent_name = "mapping-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("addr", ("addr", Srms.Mapping.MappingIpv6.MappingMi.Addr))])
                    self._leafs = OrderedDict([
                        ('ip', (YLeaf(YType.str, 'ip'), ['str'])),
                        ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                        ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                        ('router', (YLeaf(YType.str, 'router'), ['str'])),
                        ('area', (YLeaf(YType.str, 'area'), ['str'])),
                        ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                        ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                        ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                        ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                        ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                        ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                    ])
                    self.ip = None
                    self.prefix = None
                    self.src = None
                    self.router = None
                    self.area = None
                    self.prefix_xr = None
                    self.sid_start = None
                    self.sid_count = None
                    self.last_prefix = None
                    self.last_sid_index = None
                    self.flag_attached = None

                    self.addr = Srms.Mapping.MappingIpv6.MappingMi.Addr()
                    self.addr.parent = self
                    self._children_name_map["addr"] = "addr"
                    self._segment_path = lambda: "mapping-mi"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Mapping.MappingIpv6.MappingMi, ['ip', 'prefix', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                class Addr(_Entity_):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4
                    
                    	IPv4
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srms.Mapping.MappingIpv6.MappingMi.Addr, self).__init__()

                        self.yang_name = "addr"
                        self.yang_parent_name = "mapping-mi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "addr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv6/mapping-mi/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Mapping.MappingIpv6.MappingMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Mapping.MappingIpv6.MappingMi.Addr']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Mapping.MappingIpv6.MappingMi']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.Mapping.MappingIpv6']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
            return meta._meta_table['Srms.Mapping']['meta_info']


    class Policy(_Entity_):
        """
        Policy operational data
        
        .. attribute:: policy_ipv4
        
        	IPv4 policy operational data
        	**type**\:  :py:class:`PolicyIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4>`
        
        	**config**\: False
        
        .. attribute:: policy_ipv6
        
        	IPv6 policy operational data
        	**type**\:  :py:class:`PolicyIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6>`
        
        	**config**\: False
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srms.Policy, self).__init__()

            self.yang_name = "policy"
            self.yang_parent_name = "srms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-ipv4", ("policy_ipv4", Srms.Policy.PolicyIpv4)), ("policy-ipv6", ("policy_ipv6", Srms.Policy.PolicyIpv6))])
            self._leafs = OrderedDict()

            self.policy_ipv4 = Srms.Policy.PolicyIpv4()
            self.policy_ipv4.parent = self
            self._children_name_map["policy_ipv4"] = "policy-ipv4"

            self.policy_ipv6 = Srms.Policy.PolicyIpv6()
            self.policy_ipv6.parent = self
            self._children_name_map["policy_ipv6"] = "policy-ipv6"
            self._segment_path = lambda: "policy"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srms.Policy, [], name, value)


        class PolicyIpv4(_Entity_):
            """
            IPv4 policy operational data
            
            .. attribute:: policy_ipv4_backup
            
            	IPv4 backup policy operational data
            	**type**\:  :py:class:`PolicyIpv4Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup>`
            
            	**config**\: False
            
            .. attribute:: policy_ipv4_active
            
            	IPv4 active policy operational data
            	**type**\:  :py:class:`PolicyIpv4Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srms.Policy.PolicyIpv4, self).__init__()

                self.yang_name = "policy-ipv4"
                self.yang_parent_name = "policy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policy-ipv4-backup", ("policy_ipv4_backup", Srms.Policy.PolicyIpv4.PolicyIpv4Backup)), ("policy-ipv4-active", ("policy_ipv4_active", Srms.Policy.PolicyIpv4.PolicyIpv4Active))])
                self._leafs = OrderedDict()

                self.policy_ipv4_backup = Srms.Policy.PolicyIpv4.PolicyIpv4Backup()
                self.policy_ipv4_backup.parent = self
                self._children_name_map["policy_ipv4_backup"] = "policy-ipv4-backup"

                self.policy_ipv4_active = Srms.Policy.PolicyIpv4.PolicyIpv4Active()
                self.policy_ipv4_active.parent = self
                self._children_name_map["policy_ipv4_active"] = "policy-ipv4-active"
                self._segment_path = lambda: "policy-ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srms.Policy.PolicyIpv4, [], name, value)


            class PolicyIpv4Backup(_Entity_):
                """
                IPv4 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of  		 :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup, self).__init__()

                    self.yang_name = "policy-ipv4-backup"
                    self.yang_parent_name = "policy-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy-mi", ("policy_mi", Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi))])
                    self._leafs = OrderedDict()

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv4-backup"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Backup, [], name, value)


                class PolicyMi(_Entity_):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  (key)
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr>`
                    
                    	**config**\: False
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv4-backup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mi_id']
                        self._child_classes = OrderedDict([("addr", ("addr", Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr))])
                        self._leafs = OrderedDict([
                            ('mi_id', (YLeaf(YType.str, 'mi-id'), ['str'])),
                            ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                            ('router', (YLeaf(YType.str, 'router'), ['str'])),
                            ('area', (YLeaf(YType.str, 'area'), ['str'])),
                            ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                            ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                            ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                            ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                            ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                            ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                        ])
                        self.mi_id = None
                        self.src = None
                        self.router = None
                        self.area = None
                        self.prefix_xr = None
                        self.sid_start = None
                        self.sid_count = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.flag_attached = None

                        self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + str(self.mi_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/policy-ipv4-backup/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, ['mi_id', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                    class Addr(_Entity_):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "addr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup']['meta_info']


            class PolicyIpv4Active(_Entity_):
                """
                IPv4 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of  		 :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srms.Policy.PolicyIpv4.PolicyIpv4Active, self).__init__()

                    self.yang_name = "policy-ipv4-active"
                    self.yang_parent_name = "policy-ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy-mi", ("policy_mi", Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi))])
                    self._leafs = OrderedDict()

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv4-active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Active, [], name, value)


                class PolicyMi(_Entity_):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  (key)
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr>`
                    
                    	**config**\: False
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv4-active"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mi_id']
                        self._child_classes = OrderedDict([("addr", ("addr", Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr))])
                        self._leafs = OrderedDict([
                            ('mi_id', (YLeaf(YType.str, 'mi-id'), ['str'])),
                            ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                            ('router', (YLeaf(YType.str, 'router'), ['str'])),
                            ('area', (YLeaf(YType.str, 'area'), ['str'])),
                            ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                            ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                            ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                            ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                            ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                            ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                        ])
                        self.mi_id = None
                        self.src = None
                        self.router = None
                        self.area = None
                        self.prefix_xr = None
                        self.sid_start = None
                        self.sid_count = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.flag_attached = None

                        self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + str(self.mi_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/policy-ipv4-active/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, ['mi_id', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                    class Addr(_Entity_):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "addr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.Policy.PolicyIpv4']['meta_info']


        class PolicyIpv6(_Entity_):
            """
            IPv6 policy operational data
            
            .. attribute:: policy_ipv6_backup
            
            	IPv6 backup policy operational data
            	**type**\:  :py:class:`PolicyIpv6Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup>`
            
            	**config**\: False
            
            .. attribute:: policy_ipv6_active
            
            	IPv6 active policy operational data
            	**type**\:  :py:class:`PolicyIpv6Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srms.Policy.PolicyIpv6, self).__init__()

                self.yang_name = "policy-ipv6"
                self.yang_parent_name = "policy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policy-ipv6-backup", ("policy_ipv6_backup", Srms.Policy.PolicyIpv6.PolicyIpv6Backup)), ("policy-ipv6-active", ("policy_ipv6_active", Srms.Policy.PolicyIpv6.PolicyIpv6Active))])
                self._leafs = OrderedDict()

                self.policy_ipv6_backup = Srms.Policy.PolicyIpv6.PolicyIpv6Backup()
                self.policy_ipv6_backup.parent = self
                self._children_name_map["policy_ipv6_backup"] = "policy-ipv6-backup"

                self.policy_ipv6_active = Srms.Policy.PolicyIpv6.PolicyIpv6Active()
                self.policy_ipv6_active.parent = self
                self._children_name_map["policy_ipv6_active"] = "policy-ipv6-active"
                self._segment_path = lambda: "policy-ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srms.Policy.PolicyIpv6, [], name, value)


            class PolicyIpv6Backup(_Entity_):
                """
                IPv6 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of  		 :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup, self).__init__()

                    self.yang_name = "policy-ipv6-backup"
                    self.yang_parent_name = "policy-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy-mi", ("policy_mi", Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi))])
                    self._leafs = OrderedDict()

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv6-backup"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Backup, [], name, value)


                class PolicyMi(_Entity_):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  (key)
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr>`
                    
                    	**config**\: False
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv6-backup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mi_id']
                        self._child_classes = OrderedDict([("addr", ("addr", Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr))])
                        self._leafs = OrderedDict([
                            ('mi_id', (YLeaf(YType.str, 'mi-id'), ['str'])),
                            ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                            ('router', (YLeaf(YType.str, 'router'), ['str'])),
                            ('area', (YLeaf(YType.str, 'area'), ['str'])),
                            ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                            ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                            ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                            ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                            ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                            ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                        ])
                        self.mi_id = None
                        self.src = None
                        self.router = None
                        self.area = None
                        self.prefix_xr = None
                        self.sid_start = None
                        self.sid_count = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.flag_attached = None

                        self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + str(self.mi_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/policy-ipv6-backup/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, ['mi_id', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                    class Addr(_Entity_):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "addr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup']['meta_info']


            class PolicyIpv6Active(_Entity_):
                """
                IPv6 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of  		 :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srms.Policy.PolicyIpv6.PolicyIpv6Active, self).__init__()

                    self.yang_name = "policy-ipv6-active"
                    self.yang_parent_name = "policy-ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy-mi", ("policy_mi", Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi))])
                    self._leafs = OrderedDict()

                    self.policy_mi = YList(self)
                    self._segment_path = lambda: "policy-ipv6-active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Active, [], name, value)


                class PolicyMi(_Entity_):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  (key)
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:  :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr>`
                    
                    	**config**\: False
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:  :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    	**config**\: False
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\: str
                    
                    	**length:** 0..30
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:  :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv6-active"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mi_id']
                        self._child_classes = OrderedDict([("addr", ("addr", Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr))])
                        self._leafs = OrderedDict([
                            ('mi_id', (YLeaf(YType.str, 'mi-id'), ['str'])),
                            ('src', (YLeaf(YType.enumeration, 'src'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEB', '')])),
                            ('router', (YLeaf(YType.str, 'router'), ['str'])),
                            ('area', (YLeaf(YType.str, 'area'), ['str'])),
                            ('prefix_xr', (YLeaf(YType.uint8, 'prefix-xr'), ['int'])),
                            ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                            ('sid_count', (YLeaf(YType.uint32, 'sid-count'), ['int'])),
                            ('last_prefix', (YLeaf(YType.str, 'last-prefix'), ['str'])),
                            ('last_sid_index', (YLeaf(YType.uint32, 'last-sid-index'), ['int'])),
                            ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEB', '')])),
                        ])
                        self.mi_id = None
                        self.src = None
                        self.router = None
                        self.area = None
                        self.prefix_xr = None
                        self.sid_start = None
                        self.sid_count = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.flag_attached = None

                        self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._segment_path = lambda: "policy-mi" + "[mi-id='" + str(self.mi_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/policy-ipv6-active/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, ['mi_id', 'src', 'router', 'area', 'prefix_xr', 'sid_start', 'sid_count', 'last_prefix', 'last_sid_index', 'flag_attached'], name, value)


                    class Addr(_Entity_):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEB', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "addr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, ['af', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.Policy.PolicyIpv6']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
            return meta._meta_table['Srms.Policy']['meta_info']

    def clone_ptr(self):
        self._top_entity = Srms()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['Srms']['meta_info']


class Srlb(_Entity_):
    """
    srlb
    
    .. attribute:: srlb_inconsistency
    
    	SRLB Inconsistencies
    	**type**\:  :py:class:`SrlbInconsistency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srlb.SrlbInconsistency>`
    
    	**config**\: False
    
    

    """

    _prefix = 'segment-routing-ms-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Srlb, self).__init__()
        self._top_entity = None

        self.yang_name = "srlb"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("srlb-inconsistency", ("srlb_inconsistency", Srlb.SrlbInconsistency))])
        self._leafs = OrderedDict()

        self.srlb_inconsistency = Srlb.SrlbInconsistency()
        self.srlb_inconsistency.parent = self
        self._children_name_map["srlb_inconsistency"] = "srlb-inconsistency"
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srlb"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Srlb, [], name, value)


    class SrlbInconsistency(_Entity_):
        """
        SRLB Inconsistencies
        
        .. attribute:: start_srlb_range
        
        	Start label of Segment Routing Local Block range
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: end_srlb_range
        
        	End label of Segment Routing Local Block range
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlb.SrlbInconsistency, self).__init__()

            self.yang_name = "srlb-inconsistency"
            self.yang_parent_name = "srlb"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('start_srlb_range', (YLeaf(YType.uint32, 'start-srlb-range'), ['int'])),
                ('end_srlb_range', (YLeaf(YType.uint32, 'end-srlb-range'), ['int'])),
            ])
            self.start_srlb_range = None
            self.end_srlb_range = None
            self._segment_path = lambda: "srlb-inconsistency"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-oper:srlb/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlb.SrlbInconsistency, ['start_srlb_range', 'end_srlb_range'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
            return meta._meta_table['Srlb.SrlbInconsistency']['meta_info']

    def clone_ptr(self):
        self._top_entity = Srlb()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['Srlb']['meta_info']


