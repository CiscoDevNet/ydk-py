""" Cisco_IOS_XR_ip_icmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-icmp package configuration.

This module contains definitions
for the following management objects\:
  icmp\: IP ICMP configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SourcePolicyEnum(Enum):
    """
    SourcePolicyEnum

    Source policy

    .. data:: vrf = 1

    	Set Source Selection Policy to vrf

    .. data:: rfc = 2

    	Set Source Selection Policy to rfc

    """

    vrf = 1

    rfc = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_icmp_cfg as meta
        return meta._meta_table['SourcePolicyEnum']



class Icmp(object):
    """
    IP ICMP configuration data
    
    .. attribute:: ip_protocol
    
    	IP Protocol Type
    	**type**\: list of    :py:class:`IpProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.IpProtocol>`
    
    

    """

    _prefix = 'ip-icmp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.ip_protocol = YList()
        self.ip_protocol.parent = self
        self.ip_protocol.name = 'ip_protocol'


    class IpProtocol(object):
        """
        IP Protocol Type
        
        .. attribute:: protocol_type  <key>
        
        	IP Protocol Type; ipv4 or ipv6
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: rate_limit
        
        	Set ratelimit of ICMP packets
        	**type**\:   :py:class:`RateLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.IpProtocol.RateLimit>`
        
        .. attribute:: source
        
        	IP ICMP Source Address Selection Policy
        	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.IpProtocol.Source>`
        
        

        """

        _prefix = 'ip-icmp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.protocol_type = None
            self.rate_limit = Icmp.IpProtocol.RateLimit()
            self.rate_limit.parent = self
            self.source = Icmp.IpProtocol.Source()
            self.source.parent = self


        class RateLimit(object):
            """
            Set ratelimit of ICMP packets
            
            .. attribute:: unreachable
            
            	Set unreachable ICMP packets ratelimit
            	**type**\:   :py:class:`Unreachable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.IpProtocol.RateLimit.Unreachable>`
            
            

            """

            _prefix = 'ip-icmp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.unreachable = Icmp.IpProtocol.RateLimit.Unreachable()
                self.unreachable.parent = self


            class Unreachable(object):
                """
                Set unreachable ICMP packets ratelimit
                
                .. attribute:: fragmentation
                
                	Rate Limit of Unreachable DF paclets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rate
                
                	Rate Limit of Unreachable ICMP paclets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-icmp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.fragmentation = None
                    self.rate = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-icmp-cfg:unreachable'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.fragmentation is not None:
                        return True

                    if self.rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_icmp_cfg as meta
                    return meta._meta_table['Icmp.IpProtocol.RateLimit.Unreachable']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-ip-icmp-cfg:rate-limit'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.unreachable is not None and self.unreachable._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_icmp_cfg as meta
                return meta._meta_table['Icmp.IpProtocol.RateLimit']['meta_info']


        class Source(object):
            """
            IP ICMP Source Address Selection Policy
            
            .. attribute:: source_address_policy
            
            	Configure Source Address Policy
            	**type**\:   :py:class:`SourcePolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.SourcePolicyEnum>`
            
            

            """

            _prefix = 'ip-icmp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.source_address_policy = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-ip-icmp-cfg:source'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.source_address_policy is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_icmp_cfg as meta
                return meta._meta_table['Icmp.IpProtocol.Source']['meta_info']

        @property
        def _common_path(self):
            if self.protocol_type is None:
                raise YPYModelError('Key property protocol_type is None')

            return '/Cisco-IOS-XR-ip-icmp-cfg:icmp/Cisco-IOS-XR-ip-icmp-cfg:ip-protocol[Cisco-IOS-XR-ip-icmp-cfg:protocol-type = ' + str(self.protocol_type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.protocol_type is not None:
                return True

            if self.rate_limit is not None and self.rate_limit._has_data():
                return True

            if self.source is not None and self.source._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_icmp_cfg as meta
            return meta._meta_table['Icmp.IpProtocol']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-icmp-cfg:icmp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.ip_protocol is not None:
            for child_ref in self.ip_protocol:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_icmp_cfg as meta
        return meta._meta_table['Icmp']['meta_info']


