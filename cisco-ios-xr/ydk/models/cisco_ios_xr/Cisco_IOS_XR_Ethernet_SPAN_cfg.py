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

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SpanDestinationEnum(Enum):
    """
    SpanDestinationEnum

    Span destination

    .. data:: interface = 0

    	Destination Interface

    .. data:: pseudowire = 1

    	Destination Pseudowire

    .. data:: ipv4_address = 2

    	Destination next-hop IPv4 address

    .. data:: ipv6_address = 3

    	Destination next-hop IPv6 address

    """

    interface = 0

    pseudowire = 1

    ipv4_address = 2

    ipv6_address = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
        return meta._meta_table['SpanDestinationEnum']


class SpanMirrorIntervalEnum(Enum):
    """
    SpanMirrorIntervalEnum

    Span mirror interval

    .. data:: Y_512 = 1

    	Mirror 1 in every 512 packets

    .. data:: Y_1k = 2

    	Mirror 1 in every 1024 packets

    .. data:: Y_2k = 3

    	Mirror 1 in every 2048 packets

    .. data:: Y_4k = 4

    	Mirror 1 in every 4096 packets

    .. data:: Y_8k = 5

    	Mirror 1 in every 8192 packets

    .. data:: Y_16k = 6

    	Mirror 1 in every 16384 packets

    """

    Y_512 = 1

    Y_1k = 2

    Y_2k = 3

    Y_4k = 4

    Y_8k = 5

    Y_16k = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
        return meta._meta_table['SpanMirrorIntervalEnum']


class SpanTrafficDirectionEnum(Enum):
    """
    SpanTrafficDirectionEnum

    Span traffic direction

    .. data:: rx_only = 1

    	Replicate only received (ingress) traffic

    .. data:: tx_only = 2

    	Replicate only transmitted (egress) traffic

    """

    rx_only = 1

    tx_only = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
        return meta._meta_table['SpanTrafficDirectionEnum']



class SpanMonitorSession(object):
    """
    none
    
    .. attribute:: sessions
    
    	Monitor\-session configuration commands
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions>`
    
    

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
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions.Session>`
        
        

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
            
            .. attribute:: session  <key>
            
            	Session Name
            	**type**\:  str
            
            	**length:** 1..79
            
            .. attribute:: class_
            
            	Enable a Monitor Session.  Setting this item causes the Monitor Session to be created
            	**type**\:   :py:class:`SpanSessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClassEnum>`
            
            	**default value**\: ethernet
            
            .. attribute:: destination
            
            	Specify a destination
            	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions.Session.Destination>`
            
            

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
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: destination_ipv4_address
                
                	Specify the destination next\-hop IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_ipv6_address
                
                	Specify the destination next\-hop IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_type
                
                	Specify the type of destination
                	**type**\:   :py:class:`SpanDestinationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanDestinationEnum>`
                
                

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
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-cfg:destination'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.destination_interface_name is not None:
                        return True

                    if self.destination_ipv4_address is not None:
                        return True

                    if self.destination_ipv6_address is not None:
                        return True

                    if self.destination_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
                    return meta._meta_table['SpanMonitorSession.Sessions.Session.Destination']['meta_info']

            @property
            def _common_path(self):
                if self.session is None:
                    raise YPYModelError('Key property session is None')

                return '/Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-cfg:sessions/Cisco-IOS-XR-Ethernet-SPAN-cfg:session[Cisco-IOS-XR-Ethernet-SPAN-cfg:session = ' + str(self.session) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.session is not None:
                    return True

                if self.class_ is not None:
                    return True

                if self.destination is not None and self.destination._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
                return meta._meta_table['SpanMonitorSession.Sessions.Session']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-cfg:sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.session is not None:
                for child_ref in self.session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
            return meta._meta_table['SpanMonitorSession.Sessions']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.sessions is not None and self.sessions._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_cfg as meta
        return meta._meta_table['SpanMonitorSession']['meta_info']


