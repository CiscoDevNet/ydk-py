""" Cisco_IOS_XR_Ethernet_SPAN_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN package operational data.

This module contains definitions
for the following management objects\:
  span\-monitor\-session\: Monitor Session operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DestinationClassEnum(Enum):
    """
    DestinationClassEnum

    Destination class

    .. data:: interface_class = 0

    	Destination is an interface

    .. data:: pseudowire_class = 1

    	Destination is a pseudowire

    .. data:: next_hop_ipv4_class = 2

    	Destination is a next-hop IPv4 address

    .. data:: next_hop_ipv6_class = 3

    	Destination is a next-hop IPv6 address

    .. data:: invalid_class = 255

    	Destination is not specified

    """

    interface_class = 0

    pseudowire_class = 1

    next_hop_ipv4_class = 2

    next_hop_ipv6_class = 3

    invalid_class = 255


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['DestinationClassEnum']


class ImStateEnumEnum(Enum):
    """
    ImStateEnumEnum

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = 0

    im_state_admin_down = 1

    im_state_down = 2

    im_state_up = 3

    im_state_shutdown = 4

    im_state_err_disable = 5

    im_state_down_immediate = 6

    im_state_down_immediate_admin = 7

    im_state_down_graceful = 8

    im_state_begin_shutdown = 9

    im_state_end_shutdown = 10

    im_state_begin_error_disable = 11

    im_state_end_error_disable = 12

    im_state_begin_down_graceful = 13

    im_state_reset = 14

    im_state_operational = 15

    im_state_not_operational = 16

    im_state_unknown = 17

    im_state_last = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['ImStateEnumEnum']


class MirrorIntervalEnum(Enum):
    """
    MirrorIntervalEnum

    Monitor\-session mirror intervals

    .. data:: mirror_interval_all = 0

    	Mirror all packets

    .. data:: mirror_interval512 = 1

    	Mirror Interval 512

    .. data:: mirror_interval1k = 2

    	Mirror Interval 1K

    .. data:: mirror_interval2k = 3

    	Mirror Interval 2K

    .. data:: mirror_interval4k = 4

    	Mirror Interval 4K

    .. data:: mirror_interval8k = 5

    	Mirror Interval 8K

    .. data:: mirror_interval16k = 6

    	Mirror Interval 16K

    """

    mirror_interval_all = 0

    mirror_interval512 = 1

    mirror_interval1k = 2

    mirror_interval2k = 3

    mirror_interval4k = 4

    mirror_interval8k = 5

    mirror_interval16k = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['MirrorIntervalEnum']


class SessionClassEnum(Enum):
    """
    SessionClassEnum

    Session class

    .. data:: ethernet_class = 0

    	Ethernet mirroring session

    .. data:: ipv4_class = 1

    	IPv4 mirroring session

    .. data:: ipv6_class = 2

    	IPv6 mirroring session

    .. data:: invalid_class = 65535

    	Invalid session class

    """

    ethernet_class = 0

    ipv4_class = 1

    ipv6_class = 2

    invalid_class = 65535


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['SessionClassEnum']


class TrafficDirectionEnum(Enum):
    """
    TrafficDirectionEnum

    Monitor\-session traffic directions

    .. data:: invalid = 0

    	Invalid

    .. data:: rx_only = 1

    	Received

    .. data:: tx_only = 2

    	Transmitted

    .. data:: both = 3

    	Both

    """

    invalid = 0

    rx_only = 1

    tx_only = 2

    both = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['TrafficDirectionEnum']



class SpanMonitorSession(object):
    """
    Monitor Session operational data
    
    .. attribute:: global_
    
    	Global operational data
    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_>`
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes>`
    
    

    """

    _prefix = 'ethernet-span-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.global_ = SpanMonitorSession.Global_()
        self.global_.parent = self
        self.nodes = SpanMonitorSession.Nodes()
        self.nodes.parent = self


    class Global_(object):
        """
        Global operational data
        
        .. attribute:: global_sessions
        
        	Global Monitor Sessions table
        	**type**\:   :py:class:`GlobalSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions>`
        
        .. attribute:: statistics
        
        	Table of statistics for source interfaces
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.Statistics>`
        
        

        """

        _prefix = 'ethernet-span-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.global_sessions = SpanMonitorSession.Global_.GlobalSessions()
            self.global_sessions.parent = self
            self.statistics = SpanMonitorSession.Global_.Statistics()
            self.statistics.parent = self


        class Statistics(object):
            """
            Table of statistics for source interfaces
            
            .. attribute:: statistic
            
            	Statistics for a particular source interface
            	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.Statistics.Statistic>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.statistic = YList()
                self.statistic.parent = self
                self.statistic.name = 'statistic'


            class Statistic(object):
                """
                Statistics for a particular source interface
                
                .. attribute:: session  <key>
                
                	Session Name
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: interface  <key>
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: octets_not_mirrored
                
                	Octets Not Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: packets_not_mirrored
                
                	Packets Not Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_octets_mirrored
                
                	RX Octets Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_packets_mirrored
                
                	RX Packets Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_octets_mirrored
                
                	TX Octets Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets_mirrored
                
                	TX Packets Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.session = None
                    self.interface = None
                    self.octets_not_mirrored = None
                    self.packets_not_mirrored = None
                    self.rx_octets_mirrored = None
                    self.rx_packets_mirrored = None
                    self.tx_octets_mirrored = None
                    self.tx_packets_mirrored = None

                @property
                def _common_path(self):
                    if self.session is None:
                        raise YPYModelError('Key property session is None')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')

                    return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:global/Cisco-IOS-XR-Ethernet-SPAN-oper:statistics/Cisco-IOS-XR-Ethernet-SPAN-oper:statistic[Cisco-IOS-XR-Ethernet-SPAN-oper:session = ' + str(self.session) + '][Cisco-IOS-XR-Ethernet-SPAN-oper:interface = ' + str(self.interface) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.octets_not_mirrored is not None:
                        return True

                    if self.packets_not_mirrored is not None:
                        return True

                    if self.rx_octets_mirrored is not None:
                        return True

                    if self.rx_packets_mirrored is not None:
                        return True

                    if self.tx_octets_mirrored is not None:
                        return True

                    if self.tx_packets_mirrored is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                    return meta._meta_table['SpanMonitorSession.Global_.Statistics.Statistic']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:global/Cisco-IOS-XR-Ethernet-SPAN-oper:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.statistic is not None:
                    for child_ref in self.statistic:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                return meta._meta_table['SpanMonitorSession.Global_.Statistics']['meta_info']


        class GlobalSessions(object):
            """
            Global Monitor Sessions table
            
            .. attribute:: global_session
            
            	Information about a globally\-configured monitor session
            	**type**\: list of    :py:class:`GlobalSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.global_session = YList()
                self.global_session.parent = self
                self.global_session.name = 'global_session'


            class GlobalSession(object):
                """
                Information about a globally\-configured
                monitor session
                
                .. attribute:: session  <key>
                
                	Session Name
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: destination_data
                
                	Destination data
                	**type**\:   :py:class:`DestinationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData>`
                
                .. attribute:: destination_error
                
                	Last error observed for the destination 
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_id
                
                	Destination ID
                	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId>`
                
                .. attribute:: destination_interface_handle
                
                	Destination interface handle (deprecated by DestinationID, invalid for pseudowires)
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: destination_interface_name
                
                	Destination interface name (deprecated by DestinationData, invalid for pseudowires)
                	**type**\:  str
                
                .. attribute:: id
                
                	Numerical ID assigned to session
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_error
                
                	Last error observed for the destination interface (deprecated by DestinationError)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: name
                
                	Session Name
                	**type**\:  str
                
                .. attribute:: session_class
                
                	Session class
                	**type**\:   :py:class:`SessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.session = None
                    self.destination_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData()
                    self.destination_data.parent = self
                    self.destination_error = None
                    self.destination_id = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId()
                    self.destination_id.parent = self
                    self.destination_interface_handle = None
                    self.destination_interface_name = None
                    self.id = None
                    self.interface_error = None
                    self.name = None
                    self.session_class = None


                class DestinationData(object):
                    """
                    Destination data
                    
                    .. attribute:: destination_class
                    
                    	DestinationClass
                    	**type**\:   :py:class:`DestinationClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                    
                    .. attribute:: interface_data
                    
                    	Interface data
                    	**type**\:   :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData>`
                    
                    .. attribute:: invalid_value
                    
                    	Invalid Parameter
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_hop_ipv4_data
                    
                    	Next\-hop IPv4 data
                    	**type**\:   :py:class:`NextHopIpv4Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data>`
                    
                    .. attribute:: next_hop_ipv6_data
                    
                    	Next\-hop IPv6 data
                    	**type**\:   :py:class:`NextHopIpv6Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data>`
                    
                    .. attribute:: pseudowire_data
                    
                    	Pseudowire data
                    	**type**\:   :py:class:`PseudowireData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_class = None
                        self.interface_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData()
                        self.interface_data.parent = self
                        self.invalid_value = None
                        self.next_hop_ipv4_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data()
                        self.next_hop_ipv4_data.parent = self
                        self.next_hop_ipv6_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data()
                        self.next_hop_ipv6_data.parent = self
                        self.pseudowire_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData()
                        self.pseudowire_data.parent = self


                    class InterfaceData(object):
                        """
                        Interface data
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: interface_state
                        
                        	Interface State
                        	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.ImStateEnumEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.interface_state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:interface-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.interface_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData']['meta_info']


                    class PseudowireData(object):
                        """
                        Pseudowire data
                        
                        .. attribute:: pseudowire_is_up
                        
                        	Pseudowire State
                        	**type**\:  bool
                        
                        .. attribute:: pseudowire_name
                        
                        	Pseudowire Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.pseudowire_is_up = None
                            self.pseudowire_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:pseudowire-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.pseudowire_is_up is not None:
                                return True

                            if self.pseudowire_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData']['meta_info']


                    class NextHopIpv4Data(object):
                        """
                        Next\-hop IPv4 data
                        
                        .. attribute:: address_is_reachable
                        
                        	Address is reachable
                        	**type**\:  bool
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_is_reachable = None
                            self.ipv4_address = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:next-hop-ipv4-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address_is_reachable is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data']['meta_info']


                    class NextHopIpv6Data(object):
                        """
                        Next\-hop IPv6 data
                        
                        .. attribute:: address_is_reachable
                        
                        	Address is reachable
                        	**type**\:  bool
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_is_reachable = None
                            self.ipv6_address = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:next-hop-ipv6-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address_is_reachable is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:destination-data'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.destination_class is not None:
                            return True

                        if self.interface_data is not None and self.interface_data._has_data():
                            return True

                        if self.invalid_value is not None:
                            return True

                        if self.next_hop_ipv4_data is not None and self.next_hop_ipv4_data._has_data():
                            return True

                        if self.next_hop_ipv6_data is not None and self.next_hop_ipv6_data._has_data():
                            return True

                        if self.pseudowire_data is not None and self.pseudowire_data._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                        return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData']['meta_info']


                class DestinationId(object):
                    """
                    Destination ID
                    
                    .. attribute:: destination_class
                    
                    	DestinationClass
                    	**type**\:   :py:class:`DestinationClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                    
                    .. attribute:: interface
                    
                    	Interface Handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: invalid_value
                    
                    	Invalid Parameter
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_address_and_vrf
                    
                    	IPv4 address
                    	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf>`
                    
                    .. attribute:: ipv6_address_and_vrf
                    
                    	IPv6 address
                    	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf>`
                    
                    .. attribute:: pseudowire_id
                    
                    	Pseudowire XCID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_class = None
                        self.interface = None
                        self.invalid_value = None
                        self.ipv4_address_and_vrf = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf()
                        self.ipv4_address_and_vrf.parent = self
                        self.ipv6_address_and_vrf = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf()
                        self.ipv6_address_and_vrf.parent = self
                        self.pseudowire_id = None


                    class Ipv4AddressAndVrf(object):
                        """
                        IPv4 address
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ipv4_address = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv4-address-and-vrf'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ipv4_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf']['meta_info']


                    class Ipv6AddressAndVrf(object):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ipv6_address = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv6-address-and-vrf'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ipv6_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:destination-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.destination_class is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.invalid_value is not None:
                            return True

                        if self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf._has_data():
                            return True

                        if self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf._has_data():
                            return True

                        if self.pseudowire_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                        return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId']['meta_info']

                @property
                def _common_path(self):
                    if self.session is None:
                        raise YPYModelError('Key property session is None')

                    return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:global/Cisco-IOS-XR-Ethernet-SPAN-oper:global-sessions/Cisco-IOS-XR-Ethernet-SPAN-oper:global-session[Cisco-IOS-XR-Ethernet-SPAN-oper:session = ' + str(self.session) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session is not None:
                        return True

                    if self.destination_data is not None and self.destination_data._has_data():
                        return True

                    if self.destination_error is not None:
                        return True

                    if self.destination_id is not None and self.destination_id._has_data():
                        return True

                    if self.destination_interface_handle is not None:
                        return True

                    if self.destination_interface_name is not None:
                        return True

                    if self.id is not None:
                        return True

                    if self.interface_error is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.session_class is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                    return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:global/Cisco-IOS-XR-Ethernet-SPAN-oper:global-sessions'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.global_session is not None:
                    for child_ref in self.global_session:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                return meta._meta_table['SpanMonitorSession.Global_.GlobalSessions']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.global_sessions is not None and self.global_sessions._has_data():
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
            return meta._meta_table['SpanMonitorSession.Global_']['meta_info']


    class Nodes(object):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-span-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: attachments
            
            	Table of source interfaces configured as attached to a session
            	**type**\:   :py:class:`Attachments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments>`
            
            .. attribute:: hardware_sessions
            
            	Table of sessions set up in the hardware.  When all sessions are operating correctly the entries in this table should match those entries in GlobalSessionTable that have a destination configured
            	**type**\:   :py:class:`HardwareSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions>`
            
            .. attribute:: interfaces
            
            	Table of source interfaces set up in the hardware.  The entries in this table should match the entries in AttachmentTable when all sessions are operating correctly
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = None
                self.attachments = SpanMonitorSession.Nodes.Node.Attachments()
                self.attachments.parent = self
                self.hardware_sessions = SpanMonitorSession.Nodes.Node.HardwareSessions()
                self.hardware_sessions.parent = self
                self.interfaces = SpanMonitorSession.Nodes.Node.Interfaces()
                self.interfaces.parent = self


            class Attachments(object):
                """
                Table of source interfaces configured as
                attached to a session
                
                .. attribute:: attachment
                
                	Information about a particular source interface configured as attached to monitor session
                	**type**\: list of    :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.attachment = YList()
                    self.attachment.parent = self
                    self.attachment.name = 'attachment'


                class Attachment(object):
                    """
                    Information about a particular source
                    interface configured as attached to monitor
                    session
                    
                    .. attribute:: session  <key>
                    
                    	Session Name
                    	**type**\:  str
                    
                    	**length:** 1..79
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: dest_pw_type_not_supported
                    
                    	The destination PW type is not supported
                    	**type**\:  bool
                    
                    .. attribute:: destination_id
                    
                    	Destination ID
                    	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: global_class
                    
                    	Global session class
                    	**type**\:   :py:class:`SessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                    
                    .. attribute:: id
                    
                    	Numerical ID assigned to session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_class
                    
                    	Local attachment class
                    	**type**\:   :py:class:`SessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                    
                    .. attribute:: name
                    
                    	Session Name
                    	**type**\:  str
                    
                    .. attribute:: pfi_error
                    
                    	Last error returned from PFI for this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_is_configured
                    
                    	The Session is configured globally
                    	**type**\:  bool
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: source_interface_is_a_destination
                    
                    	This source interface is a destination for another monitor\-session
                    	**type**\:  bool
                    
                    .. attribute:: source_interface_state
                    
                    	Source interface state
                    	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.ImStateEnumEnum>`
                    
                    .. attribute:: traffic_direction
                    
                    	Traffic mirroring direction (deprecated by TrafficParameters)
                    	**type**\:   :py:class:`TrafficDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                    
                    .. attribute:: traffic_parameters
                    
                    	Traffic mirroring parameters
                    	**type**\:   :py:class:`TrafficParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.session = None
                        self.interface = None
                        self.dest_pw_type_not_supported = None
                        self.destination_id = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId()
                        self.destination_id.parent = self
                        self.destination_interface = None
                        self.global_class = None
                        self.id = None
                        self.local_class = None
                        self.name = None
                        self.pfi_error = None
                        self.session_is_configured = None
                        self.source_interface = None
                        self.source_interface_is_a_destination = None
                        self.source_interface_state = None
                        self.traffic_direction = None
                        self.traffic_parameters = SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters()
                        self.traffic_parameters.parent = self


                    class TrafficParameters(object):
                        """
                        Traffic mirroring parameters
                        
                        .. attribute:: is_acl_enabled
                        
                        	ACL enabled
                        	**type**\:  bool
                        
                        .. attribute:: mirror_bytes
                        
                        	Number of bytes to mirror
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: mirror_interval
                        
                        	Interval between mirrored packets
                        	**type**\:   :py:class:`MirrorIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorIntervalEnum>`
                        
                        .. attribute:: port_level
                        
                        	Port level mirroring
                        	**type**\:  bool
                        
                        .. attribute:: traffic_direction
                        
                        	Direction
                        	**type**\:   :py:class:`TrafficDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_acl_enabled = None
                            self.mirror_bytes = None
                            self.mirror_interval = None
                            self.port_level = None
                            self.traffic_direction = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:traffic-parameters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.is_acl_enabled is not None:
                                return True

                            if self.mirror_bytes is not None:
                                return True

                            if self.mirror_interval is not None:
                                return True

                            if self.port_level is not None:
                                return True

                            if self.traffic_direction is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters']['meta_info']


                    class DestinationId(object):
                        """
                        Destination ID
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.destination_class = None
                            self.interface = None
                            self.invalid_value = None
                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self.pseudowire_id = None


                        class Ipv4AddressAndVrf(object):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv4-address-and-vrf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf']['meta_info']


                        class Ipv6AddressAndVrf(object):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv6_address = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv6-address-and-vrf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv6_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:destination-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.destination_class is not None:
                                return True

                            if self.interface is not None:
                                return True

                            if self.invalid_value is not None:
                                return True

                            if self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf._has_data():
                                return True

                            if self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf._has_data():
                                return True

                            if self.pseudowire_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.session is None:
                            raise YPYModelError('Key property session is None')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:attachment[Cisco-IOS-XR-Ethernet-SPAN-oper:session = ' + str(self.session) + '][Cisco-IOS-XR-Ethernet-SPAN-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.dest_pw_type_not_supported is not None:
                            return True

                        if self.destination_id is not None and self.destination_id._has_data():
                            return True

                        if self.destination_interface is not None:
                            return True

                        if self.global_class is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.local_class is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.pfi_error is not None:
                            return True

                        if self.session_is_configured is not None:
                            return True

                        if self.source_interface is not None:
                            return True

                        if self.source_interface_is_a_destination is not None:
                            return True

                        if self.source_interface_state is not None:
                            return True

                        if self.traffic_direction is not None:
                            return True

                        if self.traffic_parameters is not None and self.traffic_parameters._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                        return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:attachments'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.attachment is not None:
                        for child_ref in self.attachment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                    return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments']['meta_info']


            class HardwareSessions(object):
                """
                Table of sessions set up in the hardware. 
                When all sessions are operating correctly the
                entries in this table should match those
                entries in GlobalSessionTable that have a
                destination configured
                
                .. attribute:: hardware_session
                
                	Information about a particular session that is set up in the hardware
                	**type**\: list of    :py:class:`HardwareSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.hardware_session = YList()
                    self.hardware_session.parent = self
                    self.hardware_session.name = 'hardware_session'


                class HardwareSession(object):
                    """
                    Information about a particular session that
                    is set up in the hardware
                    
                    .. attribute:: destination_id
                    
                    	Destination ID
                    	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: id
                    
                    	Assigned numerical ID for this session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	Configured Session Name
                    	**type**\:  str
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this session while programming the hardware
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_class
                    
                    	Sesssion class
                    	**type**\:   :py:class:`SpanSessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClassEnum>`
                    
                    .. attribute:: session_class_xr
                    
                    	Session class
                    	**type**\:   :py:class:`SessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_id = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId()
                        self.destination_id.parent = self
                        self.destination_interface = None
                        self.id = None
                        self.name = None
                        self.platform_error = None
                        self.session_class = None
                        self.session_class_xr = None
                        self.session_id = None


                    class DestinationId(object):
                        """
                        Destination ID
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.destination_class = None
                            self.interface = None
                            self.invalid_value = None
                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self.pseudowire_id = None


                        class Ipv4AddressAndVrf(object):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv4-address-and-vrf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf']['meta_info']


                        class Ipv6AddressAndVrf(object):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv6_address = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv6-address-and-vrf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv6_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:destination-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.destination_class is not None:
                                return True

                            if self.interface is not None:
                                return True

                            if self.invalid_value is not None:
                                return True

                            if self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf._has_data():
                                return True

                            if self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf._has_data():
                                return True

                            if self.pseudowire_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:hardware-session'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.destination_id is not None and self.destination_id._has_data():
                            return True

                        if self.destination_interface is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.platform_error is not None:
                            return True

                        if self.session_class is not None:
                            return True

                        if self.session_class_xr is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                        return meta._meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:hardware-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.hardware_session is not None:
                        for child_ref in self.hardware_session:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                    return meta._meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions']['meta_info']


            class Interfaces(object):
                """
                Table of source interfaces set up in the
                hardware.  The entries in this table should
                match the entries in AttachmentTable when all
                sessions are operating correctly
                
                .. attribute:: interface
                
                	Information about a particular interface that is set up in the hardware
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Information about a particular interface that
                    is set up in the hardware
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: attachment
                    
                    	Attachment information
                    	**type**\: list of    :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment>`
                    
                    .. attribute:: destination_id
                    
                    	Destination ID (deprecated by Attachment)
                    	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by Attachment)
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this interface while programming the hardware
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: traffic_direction
                    
                    	Traffic mirroring direction (deprecated by Attachment)
                    	**type**\:   :py:class:`TrafficDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                    
                    .. attribute:: traffic_mirroring_parameters
                    
                    	Traffic mirroring parameters (deprecated by Attachment)
                    	**type**\:   :py:class:`TrafficMirroringParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.attachment = YList()
                        self.attachment.parent = self
                        self.attachment.name = 'attachment'
                        self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId()
                        self.destination_id.parent = self
                        self.destination_interface = None
                        self.platform_error = None
                        self.source_interface = None
                        self.traffic_direction = None
                        self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters()
                        self.traffic_mirroring_parameters.parent = self


                    class DestinationId(object):
                        """
                        Destination ID (deprecated by Attachment)
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.destination_class = None
                            self.interface = None
                            self.invalid_value = None
                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self.pseudowire_id = None


                        class Ipv4AddressAndVrf(object):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv4-address-and-vrf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf']['meta_info']


                        class Ipv6AddressAndVrf(object):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv6_address = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv6-address-and-vrf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv6_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:destination-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.destination_class is not None:
                                return True

                            if self.interface is not None:
                                return True

                            if self.invalid_value is not None:
                                return True

                            if self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf._has_data():
                                return True

                            if self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf._has_data():
                                return True

                            if self.pseudowire_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId']['meta_info']


                    class TrafficMirroringParameters(object):
                        """
                        Traffic mirroring parameters (deprecated by
                        Attachment)
                        
                        .. attribute:: is_acl_enabled
                        
                        	ACL enabled
                        	**type**\:  bool
                        
                        .. attribute:: mirror_bytes
                        
                        	Number of bytes to mirror
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: mirror_interval
                        
                        	Interval between mirrored packets
                        	**type**\:   :py:class:`MirrorIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorIntervalEnum>`
                        
                        .. attribute:: port_level
                        
                        	Port level mirroring
                        	**type**\:  bool
                        
                        .. attribute:: traffic_direction
                        
                        	Direction
                        	**type**\:   :py:class:`TrafficDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_acl_enabled = None
                            self.mirror_bytes = None
                            self.mirror_interval = None
                            self.port_level = None
                            self.traffic_direction = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:traffic-mirroring-parameters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.is_acl_enabled is not None:
                                return True

                            if self.mirror_bytes is not None:
                                return True

                            if self.mirror_interval is not None:
                                return True

                            if self.port_level is not None:
                                return True

                            if self.traffic_direction is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters']['meta_info']


                    class Attachment(object):
                        """
                        Attachment information
                        
                        .. attribute:: class_
                        
                        	Attachment class
                        	**type**\:   :py:class:`SessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                        
                        .. attribute:: destination_id
                        
                        	Destination ID
                        	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId>`
                        
                        .. attribute:: traffic_mirroring_parameters
                        
                        	Traffic mirroring parameters
                        	**type**\:   :py:class:`TrafficMirroringParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.class_ = None
                            self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId()
                            self.destination_id.parent = self
                            self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters()
                            self.traffic_mirroring_parameters.parent = self


                        class DestinationId(object):
                            """
                            Destination ID
                            
                            .. attribute:: destination_class
                            
                            	DestinationClass
                            	**type**\:   :py:class:`DestinationClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                            
                            .. attribute:: interface
                            
                            	Interface Handle
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: invalid_value
                            
                            	Invalid Parameter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_address_and_vrf
                            
                            	IPv4 address
                            	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf>`
                            
                            .. attribute:: ipv6_address_and_vrf
                            
                            	IPv6 address
                            	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf>`
                            
                            .. attribute:: pseudowire_id
                            
                            	Pseudowire XCID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.destination_class = None
                                self.interface = None
                                self.invalid_value = None
                                self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf()
                                self.ipv4_address_and_vrf.parent = self
                                self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf()
                                self.ipv6_address_and_vrf.parent = self
                                self.pseudowire_id = None


                            class Ipv4AddressAndVrf(object):
                                """
                                IPv4 address
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-span-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv4_address = None
                                    self.vrf_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv4-address-and-vrf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv4_address is not None:
                                        return True

                                    if self.vrf_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                    return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf']['meta_info']


                            class Ipv6AddressAndVrf(object):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-span-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_address = None
                                    self.vrf_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:ipv6-address-and-vrf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv6_address is not None:
                                        return True

                                    if self.vrf_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                    return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:destination-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.destination_class is not None:
                                    return True

                                if self.interface is not None:
                                    return True

                                if self.invalid_value is not None:
                                    return True

                                if self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf._has_data():
                                    return True

                                if self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf._has_data():
                                    return True

                                if self.pseudowire_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId']['meta_info']


                        class TrafficMirroringParameters(object):
                            """
                            Traffic mirroring parameters
                            
                            .. attribute:: is_acl_enabled
                            
                            	ACL enabled
                            	**type**\:  bool
                            
                            .. attribute:: mirror_bytes
                            
                            	Number of bytes to mirror
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: mirror_interval
                            
                            	Interval between mirrored packets
                            	**type**\:   :py:class:`MirrorIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorIntervalEnum>`
                            
                            .. attribute:: port_level
                            
                            	Port level mirroring
                            	**type**\:  bool
                            
                            .. attribute:: traffic_direction
                            
                            	Direction
                            	**type**\:   :py:class:`TrafficDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.is_acl_enabled = None
                                self.mirror_bytes = None
                                self.mirror_interval = None
                                self.port_level = None
                                self.traffic_direction = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:traffic-mirroring-parameters'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.is_acl_enabled is not None:
                                    return True

                                if self.mirror_bytes is not None:
                                    return True

                                if self.mirror_interval is not None:
                                    return True

                                if self.port_level is not None:
                                    return True

                                if self.traffic_direction is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:attachment'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.class_ is not None:
                                return True

                            if self.destination_id is not None and self.destination_id._has_data():
                                return True

                            if self.traffic_mirroring_parameters is not None and self.traffic_mirroring_parameters._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:interface[Cisco-IOS-XR-Ethernet-SPAN-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.attachment is not None:
                            for child_ref in self.attachment:
                                if child_ref._has_data():
                                    return True

                        if self.destination_id is not None and self.destination_id._has_data():
                            return True

                        if self.destination_interface is not None:
                            return True

                        if self.platform_error is not None:
                            return True

                        if self.source_interface is not None:
                            return True

                        if self.traffic_direction is not None:
                            return True

                        if self.traffic_mirroring_parameters is not None and self.traffic_mirroring_parameters._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                        return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                    return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYModelError('Key property node is None')

                return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:nodes/Cisco-IOS-XR-Ethernet-SPAN-oper:node[Cisco-IOS-XR-Ethernet-SPAN-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    return True

                if self.attachments is not None and self.attachments._has_data():
                    return True

                if self.hardware_sessions is not None and self.hardware_sessions._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                return meta._meta_table['SpanMonitorSession.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
            return meta._meta_table['SpanMonitorSession.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['SpanMonitorSession']['meta_info']


