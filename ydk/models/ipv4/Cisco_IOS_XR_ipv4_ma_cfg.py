""" Cisco_IOS_XR_ipv4_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-ma package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-network\-global\: IPv4 network global configuration data
  subscriber\-pta\: subscriber pta

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv4QppbEnum(Enum):
    """
    Ipv4QppbEnum

    Ipv4 qppb

    .. data:: NONE = 0

    	No QPPB configuration

    .. data:: IP_PREC = 1

    	Enable ip-precedence based QPPB

    .. data:: QOS_GRP = 2

    	Enable qos-group based QPPB

    .. data:: BOTH = 3

    	Enable both ip-precedence and qos-group based

    	QPPB

    """

    NONE = 0

    IP_PREC = 1

    QOS_GRP = 2

    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
        return meta._meta_table['Ipv4QppbEnum']



class Ipv4NetworkGlobal(object):
    """
    IPv4 network global configuration data
    
    .. attribute:: icmp
    
    	ICMP options
    	**type**\: :py:class:`Icmp <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Icmp>`
    
    .. attribute:: qppb
    
    	QPPB
    	**type**\: :py:class:`Qppb <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Qppb>`
    
    .. attribute:: reassemble_max_packets
    
    	Percentage of total packets available in the system
    	**type**\: int
    
    	**range:** 1..50
    
    .. attribute:: reassemble_time_out
    
    	Number of seconds a reassembly queue will hold before timeout
    	**type**\: int
    
    	**range:** 1..120
    
    .. attribute:: source_route
    
    	The flag for enabling whether to process packets with source routing header options
    	**type**\: bool
    
    .. attribute:: unnumbered
    
    	Enable IPv4 processing without an explicit address
    	**type**\: :py:class:`Unnumbered <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered>`
    
    

    """

    _prefix = 'ipv4-ma-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.icmp = Ipv4NetworkGlobal.Icmp()
        self.icmp.parent = self
        self.qppb = Ipv4NetworkGlobal.Qppb()
        self.qppb.parent = self
        self.reassemble_max_packets = None
        self.reassemble_time_out = None
        self.source_route = None
        self.unnumbered = Ipv4NetworkGlobal.Unnumbered()
        self.unnumbered.parent = self


    class Icmp(object):
        """
        ICMP options
        
        .. attribute:: rate_limit
        
        	Rate limit generation of ICMP messages
        	**type**\: :py:class:`RateLimit <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Icmp.RateLimit>`
        
        

        """

        _prefix = 'ipv4-ma-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.rate_limit = Ipv4NetworkGlobal.Icmp.RateLimit()
            self.rate_limit.parent = self


        class RateLimit(object):
            """
            Rate limit generation of ICMP messages
            
            .. attribute:: unreachable
            
            	Destination Unreachable rate limiting
            	**type**\: :py:class:`Unreachable <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Icmp.RateLimit.Unreachable>`
            
            

            """

            _prefix = 'ipv4-ma-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.unreachable = Ipv4NetworkGlobal.Icmp.RateLimit.Unreachable()
                self.unreachable.parent = self


            class Unreachable(object):
                """
                Destination Unreachable rate limiting
                
                .. attribute:: df
                
                	Destination Unreachable DF packets requiring fragmentation response rate limit value in milliseconds
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: rate
                
                	Destination Unreachable packet response rate limit value in milliseconds
                	**type**\: int
                
                	**range:** 1..4294967295
                
                

                """

                _prefix = 'ipv4-ma-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.df = None
                    self.rate = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/Cisco-IOS-XR-ipv4-ma-cfg:icmp/Cisco-IOS-XR-ipv4-ma-cfg:rate-limit/Cisco-IOS-XR-ipv4-ma-cfg:unreachable'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.df is not None:
                        return True

                    if self.rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
                    return meta._meta_table['Ipv4NetworkGlobal.Icmp.RateLimit.Unreachable']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/Cisco-IOS-XR-ipv4-ma-cfg:icmp/Cisco-IOS-XR-ipv4-ma-cfg:rate-limit'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.unreachable is not None and self.unreachable._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
                return meta._meta_table['Ipv4NetworkGlobal.Icmp.RateLimit']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/Cisco-IOS-XR-ipv4-ma-cfg:icmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.rate_limit is not None and self.rate_limit._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
            return meta._meta_table['Ipv4NetworkGlobal.Icmp']['meta_info']


    class Qppb(object):
        """
        QPPB
        
        .. attribute:: destination
        
        	QPPB configuration on destination
        	**type**\: :py:class:`Ipv4QppbEnum <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4QppbEnum>`
        
        .. attribute:: source
        
        	QPPB configuration on source
        	**type**\: :py:class:`Ipv4QppbEnum <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4QppbEnum>`
        
        

        """

        _prefix = 'ipv4-ma-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.destination = None
            self.source = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/Cisco-IOS-XR-ipv4-ma-cfg:qppb'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.destination is not None:
                return True

            if self.source is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
            return meta._meta_table['Ipv4NetworkGlobal.Qppb']['meta_info']


    class Unnumbered(object):
        """
        Enable IPv4 processing without an explicit
        address
        
        .. attribute:: mpls
        
        	Configure MPLS routing protocol parameters
        	**type**\: :py:class:`Mpls <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered.Mpls>`
        
        

        """

        _prefix = 'ipv4-ma-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.mpls = Ipv4NetworkGlobal.Unnumbered.Mpls()
            self.mpls.parent = self


        class Mpls(object):
            """
            Configure MPLS routing protocol parameters
            
            .. attribute:: te
            
            	IPv4 commands for MPLS Traffic Engineering
            	**type**\: :py:class:`Te <ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered.Mpls.Te>`
            
            

            """

            _prefix = 'ipv4-ma-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.te = Ipv4NetworkGlobal.Unnumbered.Mpls.Te()
                self.te.parent = self


            class Te(object):
                """
                IPv4 commands for MPLS Traffic Engineering
                
                .. attribute:: interface
                
                	Enable IP processing without an explicit address on MPLS Traffic\-Eng
                	**type**\: str
                
                

                """

                _prefix = 'ipv4-ma-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.interface = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/Cisco-IOS-XR-ipv4-ma-cfg:unnumbered/Cisco-IOS-XR-ipv4-ma-cfg:mpls/Cisco-IOS-XR-ipv4-ma-cfg:te'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
                    return meta._meta_table['Ipv4NetworkGlobal.Unnumbered.Mpls.Te']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/Cisco-IOS-XR-ipv4-ma-cfg:unnumbered/Cisco-IOS-XR-ipv4-ma-cfg:mpls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.te is not None and self.te._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
                return meta._meta_table['Ipv4NetworkGlobal.Unnumbered.Mpls']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/Cisco-IOS-XR-ipv4-ma-cfg:unnumbered'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.mpls is not None and self.mpls._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
            return meta._meta_table['Ipv4NetworkGlobal.Unnumbered']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.icmp is not None and self.icmp._has_data():
            return True

        if self.qppb is not None and self.qppb._has_data():
            return True

        if self.reassemble_max_packets is not None:
            return True

        if self.reassemble_time_out is not None:
            return True

        if self.source_route is not None:
            return True

        if self.unnumbered is not None and self.unnumbered._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
        return meta._meta_table['Ipv4NetworkGlobal']['meta_info']


class SubscriberPta(object):
    """
    subscriber pta
    
    .. attribute:: tcp_mss_adjust
    
    	TCP MSS Adjust (bytes)
    	**type**\: int
    
    	**range:** 1280..1536
    
    

    """

    _prefix = 'ipv4-ma-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.tcp_mss_adjust = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ma-cfg:subscriber-pta'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.tcp_mss_adjust is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_cfg as meta
        return meta._meta_table['SubscriberPta']['meta_info']


