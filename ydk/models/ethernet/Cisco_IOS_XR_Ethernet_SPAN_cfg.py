""" Cisco_IOS_XR_Ethernet_SPAN_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN package configuration.

This module contains definitions
for the following management objects\:
  span\-monitor\-session\: none

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg
modules with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes import SpanSessionClass_Enum

class SpanDestination_Enum(Enum):
    """
    SpanDestination_Enum

    Span destination

    """

    """

    Destination Interface

    """
    INTERFACE = 0

    """

    Destination Pseudowire

    """
    PSEUDOWIRE = 1

    """

    Destination next\-hop IPv4 address

    """
    IPV4_ADDRESS = 2

    """

    Destination next\-hop IPv6 address

    """
    IPV6_ADDRESS = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
        return meta._meta_table['SpanDestination_Enum']


class SpanMirrorInterval_Enum(Enum):
    """
    SpanMirrorInterval_Enum

    Span mirror interval

    """

    """

    Mirror 1 in every 512 packets

    """
    Y_512 = 1

    """

    Mirror 1 in every 1024 packets

    """
    Y_1K = 2

    """

    Mirror 1 in every 2048 packets

    """
    Y_2K = 3

    """

    Mirror 1 in every 4096 packets

    """
    Y_4K = 4

    """

    Mirror 1 in every 8192 packets

    """
    Y_8K = 5

    """

    Mirror 1 in every 16384 packets

    """
    Y_16K = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
        return meta._meta_table['SpanMirrorInterval_Enum']


class SpanTrafficDirection_Enum(Enum):
    """
    SpanTrafficDirection_Enum

    Span traffic direction

    """

    """

    Replicate only received (ingress) traffic

    """
    RX_ONLY = 1

    """

    Replicate only transmitted (egress) traffic

    """
    TX_ONLY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
        return meta._meta_table['SpanTrafficDirection_Enum']



class SpanMonitorSession(object):
    """
    none
    
    .. attribute:: sessions
    
    	Monitor\-session configuration commands
    	**type**\: :py:class:`Sessions <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions>`
    
    

    """

    _prefix = 'ethernet-span-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.sessions = SpanMonitorSession.Sessions()
        self.sessions.parent = self


    class Sessions(object):
        """
        Monitor\-session configuration commands
        
        .. attribute:: session
        
        	Configuration for a particular Monitor Session
        	**type**\: list of :py:class:`Session <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions.Session>`
        
        

        """

        _prefix = 'ethernet-span-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.session = YList()
            self.session.parent = self
            self.session.name = 'session'


        class Session(object):
            """
            Configuration for a particular Monitor Session
            
            .. attribute:: session
            
            	Session Name
            	**type**\: str
            
            	**range:** 0..79
            
            .. attribute:: class_
            
            	Enable a Monitor Session.  Setting this item causes the Monitor Session to be created
            	**type**\: :py:class:`SpanSessionClass_Enum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass_Enum>`
            
            .. attribute:: destination
            
            	Specify a destination
            	**type**\: :py:class:`Destination <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions.Session.Destination>`
            
            

            """

            _prefix = 'ethernet-span-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.session = None
                self.class_ = None
                self.destination = SpanMonitorSession.Sessions.Session.Destination()
                self.destination.parent = self


            class Destination(object):
                """
                Specify a destination
                
                .. attribute:: destination_interface_name
                
                	Specify the destination interface name
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: destination_ipv4_address
                
                	Specify the destination next\-hop IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_ipv6_address
                
                	Specify the destination next\-hop IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_type
                
                	Specify the type of destination
                	**type**\: :py:class:`SpanDestination_Enum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanDestination_Enum>`
                
                

                """

                _prefix = 'ethernet-span-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.destination_interface_name = None
                    self.destination_ipv4_address = None
                    self.destination_ipv6_address = None
                    self.destination_type = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-cfg:destination'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.destination_interface_name is not None:
                        return True

                    if self.destination_ipv4_address is not None:
                        return True

                    if self.destination_ipv6_address is not None:
                        return True

                    if self.destination_type is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
                    return meta._meta_table['SpanMonitorSession.Sessions.Session.Destination']['meta_info']

            @property
            def _common_path(self):
                if self.session is None:
                    raise YPYDataValidationError('Key property session is None')

                return '/Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-cfg:sessions/Cisco-IOS-XR-Ethernet-SPAN-cfg:session[Cisco-IOS-XR-Ethernet-SPAN-cfg:session = ' + str(self.session) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.session is not None:
                    return True

                if self.class_ is not None:
                    return True

                if self.destination is not None and self.destination._has_data():
                    return True

                if self.destination is not None and self.destination.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
                return meta._meta_table['SpanMonitorSession.Sessions.Session']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-cfg:sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.session is not None:
                for child_ref in self.session:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
            return meta._meta_table['SpanMonitorSession.Sessions']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.sessions is not None and self.sessions._has_data():
            return True

        if self.sessions is not None and self.sessions.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
        return meta._meta_table['SpanMonitorSession']['meta_info']


