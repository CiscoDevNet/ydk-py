""" Cisco_IOS_XR_segment_routing_ms_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package operational data.

This module contains definitions
for the following management objects\:
  srms\: Segment Routing Mapping Server operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SrmsMiAfEBEnum(Enum):
    """
    SrmsMiAfEBEnum

    Srms mi af e b

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    none = 0

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['SrmsMiAfEBEnum']


class SrmsMiFlagEBEnum(Enum):
    """
    SrmsMiFlagEBEnum

    Srms mi flag e b

    .. data:: false = 0

    	False

    .. data:: true = 1

    	True

    """

    false = 0

    true = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['SrmsMiFlagEBEnum']


class SrmsMiSrcEBEnum(Enum):
    """
    SrmsMiSrcEBEnum

    Srms mi src e b

    .. data:: none = 0

    	None

    .. data:: local = 1

    	Local

    .. data:: remote = 2

    	Remote

    """

    none = 0

    local = 1

    remote = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['SrmsMiSrcEBEnum']



class Srms(object):
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
        self.mapping = Srms.Mapping()
        self.mapping.parent = self
        self.policy = Srms.Policy()
        self.policy.parent = self


    class Mapping(object):
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
            self.parent = None
            self.mapping_ipv4 = Srms.Mapping.MappingIpv4()
            self.mapping_ipv4.parent = self
            self.mapping_ipv6 = Srms.Mapping.MappingIpv6()
            self.mapping_ipv6.parent = self


        class MappingIpv4(object):
            """
            IPv4 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of    :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4.MappingMi>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mapping_mi = YList()
                self.mapping_mi.parent = self
                self.mapping_mi.name = 'mapping_mi'


            class MappingMi(object):
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
                	**type**\:   :py:class:`SrmsMiFlagEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEBEnum>`
                
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
                	**type**\:   :py:class:`SrmsMiSrcEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEBEnum>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.addr = Srms.Mapping.MappingIpv4.MappingMi.Addr()
                    self.addr.parent = self
                    self.area = None
                    self.flag_attached = None
                    self.ip = None
                    self.last_prefix = None
                    self.last_sid_index = None
                    self.prefix = None
                    self.prefix_xr = None
                    self.router = None
                    self.sid_count = None
                    self.sid_start = None
                    self.src = None


                class Addr(object):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:   :py:class:`SrmsMiAfEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEBEnum>`
                    
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
                        self.parent = None
                        self.af = None
                        self.ipv4 = None
                        self.ipv6 = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:mapping/Cisco-IOS-XR-segment-routing-ms-oper:mapping-ipv4/Cisco-IOS-XR-segment-routing-ms-oper:mapping-mi/Cisco-IOS-XR-segment-routing-ms-oper:addr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af is not None:
                            return True

                        if self.ipv4 is not None:
                            return True

                        if self.ipv6 is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Mapping.MappingIpv4.MappingMi.Addr']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:mapping/Cisco-IOS-XR-segment-routing-ms-oper:mapping-ipv4/Cisco-IOS-XR-segment-routing-ms-oper:mapping-mi'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.addr is not None and self.addr._has_data():
                        return True

                    if self.area is not None:
                        return True

                    if self.flag_attached is not None:
                        return True

                    if self.ip is not None:
                        return True

                    if self.last_prefix is not None:
                        return True

                    if self.last_sid_index is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.prefix_xr is not None:
                        return True

                    if self.router is not None:
                        return True

                    if self.sid_count is not None:
                        return True

                    if self.sid_start is not None:
                        return True

                    if self.src is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Mapping.MappingIpv4.MappingMi']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:mapping/Cisco-IOS-XR-segment-routing-ms-oper:mapping-ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mapping_mi is not None:
                    for child_ref in self.mapping_mi:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.Mapping.MappingIpv4']['meta_info']


        class MappingIpv6(object):
            """
            IPv6 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of    :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6.MappingMi>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mapping_mi = YList()
                self.mapping_mi.parent = self
                self.mapping_mi.name = 'mapping_mi'


            class MappingMi(object):
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
                	**type**\:   :py:class:`SrmsMiFlagEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEBEnum>`
                
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
                	**type**\:   :py:class:`SrmsMiSrcEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEBEnum>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.addr = Srms.Mapping.MappingIpv6.MappingMi.Addr()
                    self.addr.parent = self
                    self.area = None
                    self.flag_attached = None
                    self.ip = None
                    self.last_prefix = None
                    self.last_sid_index = None
                    self.prefix = None
                    self.prefix_xr = None
                    self.router = None
                    self.sid_count = None
                    self.sid_start = None
                    self.src = None


                class Addr(object):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:   :py:class:`SrmsMiAfEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEBEnum>`
                    
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
                        self.parent = None
                        self.af = None
                        self.ipv4 = None
                        self.ipv6 = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:mapping/Cisco-IOS-XR-segment-routing-ms-oper:mapping-ipv6/Cisco-IOS-XR-segment-routing-ms-oper:mapping-mi/Cisco-IOS-XR-segment-routing-ms-oper:addr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af is not None:
                            return True

                        if self.ipv4 is not None:
                            return True

                        if self.ipv6 is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Mapping.MappingIpv6.MappingMi.Addr']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:mapping/Cisco-IOS-XR-segment-routing-ms-oper:mapping-ipv6/Cisco-IOS-XR-segment-routing-ms-oper:mapping-mi'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.addr is not None and self.addr._has_data():
                        return True

                    if self.area is not None:
                        return True

                    if self.flag_attached is not None:
                        return True

                    if self.ip is not None:
                        return True

                    if self.last_prefix is not None:
                        return True

                    if self.last_sid_index is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.prefix_xr is not None:
                        return True

                    if self.router is not None:
                        return True

                    if self.sid_count is not None:
                        return True

                    if self.sid_start is not None:
                        return True

                    if self.src is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Mapping.MappingIpv6.MappingMi']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:mapping/Cisco-IOS-XR-segment-routing-ms-oper:mapping-ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mapping_mi is not None:
                    for child_ref in self.mapping_mi:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.Mapping.MappingIpv6']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:mapping'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mapping_ipv4 is not None and self.mapping_ipv4._has_data():
                return True

            if self.mapping_ipv6 is not None and self.mapping_ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
            return meta._meta_table['Srms.Mapping']['meta_info']


    class Policy(object):
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
            self.parent = None
            self.policy_ipv4 = Srms.Policy.PolicyIpv4()
            self.policy_ipv4.parent = self
            self.policy_ipv6 = Srms.Policy.PolicyIpv6()
            self.policy_ipv6.parent = self


        class PolicyIpv4(object):
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
                self.parent = None
                self.policy_ipv4_active = Srms.Policy.PolicyIpv4.PolicyIpv4Active()
                self.policy_ipv4_active.parent = self
                self.policy_ipv4_backup = Srms.Policy.PolicyIpv4.PolicyIpv4Backup()
                self.policy_ipv4_backup.parent = self


            class PolicyIpv4Backup(object):
                """
                IPv4 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.policy_mi = YList()
                    self.policy_mi.parent = self
                    self.policy_mi.name = 'policy_mi'


                class PolicyMi(object):
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
                    	**type**\:   :py:class:`SrmsMiFlagEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEBEnum>`
                    
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
                    	**type**\:   :py:class:`SrmsMiSrcEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEBEnum>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mi_id = None
                        self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self.area = None
                        self.flag_attached = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.prefix_xr = None
                        self.router = None
                        self.sid_count = None
                        self.sid_start = None
                        self.src = None


                    class Addr(object):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEBEnum>`
                        
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
                            self.parent = None
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-segment-routing-ms-oper:addr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.mi_id is None:
                            raise YPYModelError('Key property mi_id is None')

                        return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4-backup/Cisco-IOS-XR-segment-routing-ms-oper:policy-mi[Cisco-IOS-XR-segment-routing-ms-oper:mi-id = ' + str(self.mi_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.mi_id is not None:
                            return True

                        if self.addr is not None and self.addr._has_data():
                            return True

                        if self.area is not None:
                            return True

                        if self.flag_attached is not None:
                            return True

                        if self.last_prefix is not None:
                            return True

                        if self.last_sid_index is not None:
                            return True

                        if self.prefix_xr is not None:
                            return True

                        if self.router is not None:
                            return True

                        if self.sid_count is not None:
                            return True

                        if self.sid_start is not None:
                            return True

                        if self.src is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4-backup'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.policy_mi is not None:
                        for child_ref in self.policy_mi:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup']['meta_info']


            class PolicyIpv4Active(object):
                """
                IPv4 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.policy_mi = YList()
                    self.policy_mi.parent = self
                    self.policy_mi.name = 'policy_mi'


                class PolicyMi(object):
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
                    	**type**\:   :py:class:`SrmsMiFlagEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEBEnum>`
                    
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
                    	**type**\:   :py:class:`SrmsMiSrcEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEBEnum>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mi_id = None
                        self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self.area = None
                        self.flag_attached = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.prefix_xr = None
                        self.router = None
                        self.sid_count = None
                        self.sid_start = None
                        self.src = None


                    class Addr(object):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEBEnum>`
                        
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
                            self.parent = None
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-segment-routing-ms-oper:addr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.mi_id is None:
                            raise YPYModelError('Key property mi_id is None')

                        return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4-active/Cisco-IOS-XR-segment-routing-ms-oper:policy-mi[Cisco-IOS-XR-segment-routing-ms-oper:mi-id = ' + str(self.mi_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.mi_id is not None:
                            return True

                        if self.addr is not None and self.addr._has_data():
                            return True

                        if self.area is not None:
                            return True

                        if self.flag_attached is not None:
                            return True

                        if self.last_prefix is not None:
                            return True

                        if self.last_sid_index is not None:
                            return True

                        if self.prefix_xr is not None:
                            return True

                        if self.router is not None:
                            return True

                        if self.sid_count is not None:
                            return True

                        if self.sid_start is not None:
                            return True

                        if self.src is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4-active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.policy_mi is not None:
                        for child_ref in self.policy_mi:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.policy_ipv4_active is not None and self.policy_ipv4_active._has_data():
                    return True

                if self.policy_ipv4_backup is not None and self.policy_ipv4_backup._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.Policy.PolicyIpv4']['meta_info']


        class PolicyIpv6(object):
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
                self.parent = None
                self.policy_ipv6_active = Srms.Policy.PolicyIpv6.PolicyIpv6Active()
                self.policy_ipv6_active.parent = self
                self.policy_ipv6_backup = Srms.Policy.PolicyIpv6.PolicyIpv6Backup()
                self.policy_ipv6_backup.parent = self


            class PolicyIpv6Backup(object):
                """
                IPv6 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.policy_mi = YList()
                    self.policy_mi.parent = self
                    self.policy_mi.name = 'policy_mi'


                class PolicyMi(object):
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
                    	**type**\:   :py:class:`SrmsMiFlagEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEBEnum>`
                    
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
                    	**type**\:   :py:class:`SrmsMiSrcEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEBEnum>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mi_id = None
                        self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self.area = None
                        self.flag_attached = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.prefix_xr = None
                        self.router = None
                        self.sid_count = None
                        self.sid_start = None
                        self.src = None


                    class Addr(object):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEBEnum>`
                        
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
                            self.parent = None
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-segment-routing-ms-oper:addr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.mi_id is None:
                            raise YPYModelError('Key property mi_id is None')

                        return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6-backup/Cisco-IOS-XR-segment-routing-ms-oper:policy-mi[Cisco-IOS-XR-segment-routing-ms-oper:mi-id = ' + str(self.mi_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.mi_id is not None:
                            return True

                        if self.addr is not None and self.addr._has_data():
                            return True

                        if self.area is not None:
                            return True

                        if self.flag_attached is not None:
                            return True

                        if self.last_prefix is not None:
                            return True

                        if self.last_sid_index is not None:
                            return True

                        if self.prefix_xr is not None:
                            return True

                        if self.router is not None:
                            return True

                        if self.sid_count is not None:
                            return True

                        if self.sid_start is not None:
                            return True

                        if self.src is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6-backup'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.policy_mi is not None:
                        for child_ref in self.policy_mi:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup']['meta_info']


            class PolicyIpv6Active(object):
                """
                IPv6 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.policy_mi = YList()
                    self.policy_mi.parent = self
                    self.policy_mi.name = 'policy_mi'


                class PolicyMi(object):
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
                    	**type**\:   :py:class:`SrmsMiFlagEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEBEnum>`
                    
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
                    	**type**\:   :py:class:`SrmsMiSrcEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEBEnum>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mi_id = None
                        self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self.area = None
                        self.flag_attached = None
                        self.last_prefix = None
                        self.last_sid_index = None
                        self.prefix_xr = None
                        self.router = None
                        self.sid_count = None
                        self.sid_start = None
                        self.src = None


                    class Addr(object):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEBEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEBEnum>`
                        
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
                            self.parent = None
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-segment-routing-ms-oper:addr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                            return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.mi_id is None:
                            raise YPYModelError('Key property mi_id is None')

                        return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6-active/Cisco-IOS-XR-segment-routing-ms-oper:policy-mi[Cisco-IOS-XR-segment-routing-ms-oper:mi-id = ' + str(self.mi_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.mi_id is not None:
                            return True

                        if self.addr is not None and self.addr._has_data():
                            return True

                        if self.area is not None:
                            return True

                        if self.flag_attached is not None:
                            return True

                        if self.last_prefix is not None:
                            return True

                        if self.last_sid_index is not None:
                            return True

                        if self.prefix_xr is not None:
                            return True

                        if self.router is not None:
                            return True

                        if self.sid_count is not None:
                            return True

                        if self.sid_start is not None:
                            return True

                        if self.src is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                        return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6-active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.policy_mi is not None:
                        for child_ref in self.policy_mi:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                    return meta._meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy/Cisco-IOS-XR-segment-routing-ms-oper:policy-ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.policy_ipv6_active is not None and self.policy_ipv6_active._has_data():
                    return True

                if self.policy_ipv6_backup is not None and self.policy_ipv6_backup._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
                return meta._meta_table['Srms.Policy.PolicyIpv6']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-segment-routing-ms-oper:srms/Cisco-IOS-XR-segment-routing-ms-oper:policy'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.policy_ipv4 is not None and self.policy_ipv4._has_data():
                return True

            if self.policy_ipv6 is not None and self.policy_ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
            return meta._meta_table['Srms.Policy']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-segment-routing-ms-oper:srms'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.mapping is not None and self.mapping._has_data():
            return True

        if self.policy is not None and self.policy._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_oper as meta
        return meta._meta_table['Srms']['meta_info']


