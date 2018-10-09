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

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SpanDestination(Enum):
    """
    SpanDestination (Enum Class)

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

    interface = Enum.YLeaf(0, "interface")

    pseudowire = Enum.YLeaf(1, "pseudowire")

    ipv4_address = Enum.YLeaf(2, "ipv4-address")

    ipv6_address = Enum.YLeaf(3, "ipv6-address")


class SpanMirrorInterval(Enum):
    """
    SpanMirrorInterval (Enum Class)

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

    Y_512 = Enum.YLeaf(1, "512")

    Y_1k = Enum.YLeaf(2, "1k")

    Y_2k = Enum.YLeaf(3, "2k")

    Y_4k = Enum.YLeaf(4, "4k")

    Y_8k = Enum.YLeaf(5, "8k")

    Y_16k = Enum.YLeaf(6, "16k")


class SpanTrafficDirection(Enum):
    """
    SpanTrafficDirection (Enum Class)

    Span traffic direction

    .. data:: rx_only = 1

    	Replicate only received (ingress) traffic

    .. data:: tx_only = 2

    	Replicate only transmitted (egress) traffic

    """

    rx_only = Enum.YLeaf(1, "rx-only")

    tx_only = Enum.YLeaf(2, "tx-only")



class SpanMonitorSession(Entity):
    """
    none
    
    .. attribute:: sessions
    
    	Monitor\-session configuration commands
    	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions>`
    
    

    """

    _prefix = 'ethernet-span-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SpanMonitorSession, self).__init__()
        self._top_entity = None

        self.yang_name = "span-monitor-session"
        self.yang_parent_name = "Cisco-IOS-XR-Ethernet-SPAN-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sessions", ("sessions", SpanMonitorSession.Sessions))])
        self._leafs = OrderedDict()

        self.sessions = SpanMonitorSession.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SpanMonitorSession, [], name, value)


    class Sessions(Entity):
        """
        Monitor\-session configuration commands
        
        .. attribute:: session
        
        	Configuration for a particular Monitor Session
        	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions.Session>`
        
        

        """

        _prefix = 'ethernet-span-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SpanMonitorSession.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "span-monitor-session"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("session", ("session", SpanMonitorSession.Sessions.Session))])
            self._leafs = OrderedDict()

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SpanMonitorSession.Sessions, [], name, value)


        class Session(Entity):
            """
            Configuration for a particular Monitor Session
            
            .. attribute:: session  (key)
            
            	Session Name
            	**type**\: str
            
            	**length:** 1..79
            
            .. attribute:: destination
            
            	Specify a destination
            	**type**\:  :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions.Session.Destination>`
            
            .. attribute:: class_
            
            	Enable a Monitor Session.  Setting this item causes the Monitor Session to be created
            	**type**\:  :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
            
            	**default value**\: ethernet
            
            .. attribute:: inject_interface
            
            	Specify the inject interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'ethernet-span-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SpanMonitorSession.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['session']
                self._child_classes = OrderedDict([("destination", ("destination", SpanMonitorSession.Sessions.Session.Destination))])
                self._leafs = OrderedDict([
                    ('session', (YLeaf(YType.str, 'session'), ['str'])),
                    ('class_', (YLeaf(YType.enumeration, 'class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass', '')])),
                    ('inject_interface', (YLeaf(YType.str, 'inject-interface'), ['str'])),
                ])
                self.session = None
                self.class_ = None
                self.inject_interface = None

                self.destination = SpanMonitorSession.Sessions.Session.Destination()
                self.destination.parent = self
                self._children_name_map["destination"] = "destination"
                self._segment_path = lambda: "session" + "[session='" + str(self.session) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session/sessions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SpanMonitorSession.Sessions.Session, ['session', 'class_', 'inject_interface'], name, value)


            class Destination(Entity):
                """
                Specify a destination
                
                .. attribute:: destination_type
                
                	Specify the type of destination
                	**type**\:  :py:class:`SpanDestination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanDestination>`
                
                .. attribute:: destination_interface_name
                
                	Specify the destination interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: destination_ipv4_address
                
                	Specify the destination next\-hop IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_ipv6_address
                
                	Specify the destination next\-hop IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ethernet-span-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Sessions.Session.Destination, self).__init__()

                    self.yang_name = "destination"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('destination_type', (YLeaf(YType.enumeration, 'destination-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanDestination', '')])),
                        ('destination_interface_name', (YLeaf(YType.str, 'destination-interface-name'), ['str'])),
                        ('destination_ipv4_address', (YLeaf(YType.str, 'destination-ipv4-address'), ['str'])),
                        ('destination_ipv6_address', (YLeaf(YType.str, 'destination-ipv6-address'), ['str'])),
                    ])
                    self.destination_type = None
                    self.destination_interface_name = None
                    self.destination_ipv4_address = None
                    self.destination_ipv6_address = None
                    self._segment_path = lambda: "destination"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Sessions.Session.Destination, ['destination_type', 'destination_interface_name', 'destination_ipv4_address', 'destination_ipv6_address'], name, value)

    def clone_ptr(self):
        self._top_entity = SpanMonitorSession()
        return self._top_entity

