""" Cisco_IOS_XR_Ethernet_SPAN_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN package operational data.

This module contains definitions
for the following management objects\:
  span\-monitor\-session\: Monitor Session operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes import SpanSessionClassEnum

class DestinationClassEnum(Enum):
    """
    DestinationClassEnum

    Destination class

    .. data:: INTERFACE_CLASS = 0

    	Destination is an interface

    .. data:: PSEUDOWIRE_CLASS = 1

    	Destination is a pseudowire

    .. data:: NEXT_HOP_IPV4_CLASS = 2

    	Destination is a next-hop IPv4 address

    .. data:: NEXT_HOP_IPV6_CLASS = 3

    	Destination is a next-hop IPv6 address

    .. data:: INVALID_CLASS = 255

    	Destination is not specified

    """

    INTERFACE_CLASS = 0

    PSEUDOWIRE_CLASS = 1

    NEXT_HOP_IPV4_CLASS = 2

    NEXT_HOP_IPV6_CLASS = 3

    INVALID_CLASS = 255


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['DestinationClassEnum']


class ImStateEnumEnum(Enum):
    """
    ImStateEnumEnum

    Im state enum

    .. data:: IM_STATE_NOT_READY = 0

    	im state not ready

    .. data:: IM_STATE_ADMIN_DOWN = 1

    	im state admin down

    .. data:: IM_STATE_DOWN = 2

    	im state down

    .. data:: IM_STATE_UP = 3

    	im state up

    .. data:: IM_STATE_SHUTDOWN = 4

    	im state shutdown

    .. data:: IM_STATE_ERR_DISABLE = 5

    	im state err disable

    .. data:: IM_STATE_DOWN_IMMEDIATE = 6

    	im state down immediate

    .. data:: IM_STATE_DOWN_IMMEDIATE_ADMIN = 7

    	im state down immediate admin

    .. data:: IM_STATE_DOWN_GRACEFUL = 8

    	im state down graceful

    .. data:: IM_STATE_BEGIN_SHUTDOWN = 9

    	im state begin shutdown

    .. data:: IM_STATE_END_SHUTDOWN = 10

    	im state end shutdown

    .. data:: IM_STATE_BEGIN_ERROR_DISABLE = 11

    	im state begin error disable

    .. data:: IM_STATE_END_ERROR_DISABLE = 12

    	im state end error disable

    .. data:: IM_STATE_BEGIN_DOWN_GRACEFUL = 13

    	im state begin down graceful

    .. data:: IM_STATE_RESET = 14

    	im state reset

    .. data:: IM_STATE_OPERATIONAL = 15

    	im state operational

    .. data:: IM_STATE_NOT_OPERATIONAL = 16

    	im state not operational

    .. data:: IM_STATE_UNKNOWN = 17

    	im state unknown

    .. data:: IM_STATE_LAST = 18

    	im state last

    """

    IM_STATE_NOT_READY = 0

    IM_STATE_ADMIN_DOWN = 1

    IM_STATE_DOWN = 2

    IM_STATE_UP = 3

    IM_STATE_SHUTDOWN = 4

    IM_STATE_ERR_DISABLE = 5

    IM_STATE_DOWN_IMMEDIATE = 6

    IM_STATE_DOWN_IMMEDIATE_ADMIN = 7

    IM_STATE_DOWN_GRACEFUL = 8

    IM_STATE_BEGIN_SHUTDOWN = 9

    IM_STATE_END_SHUTDOWN = 10

    IM_STATE_BEGIN_ERROR_DISABLE = 11

    IM_STATE_END_ERROR_DISABLE = 12

    IM_STATE_BEGIN_DOWN_GRACEFUL = 13

    IM_STATE_RESET = 14

    IM_STATE_OPERATIONAL = 15

    IM_STATE_NOT_OPERATIONAL = 16

    IM_STATE_UNKNOWN = 17

    IM_STATE_LAST = 18


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['ImStateEnumEnum']


class MirrorIntervalEnum(Enum):
    """
    MirrorIntervalEnum

    Monitor\-session mirror intervals

    .. data:: MIRROR_INTERVAL_ALL = 0

    	Mirror all packets

    .. data:: MIRROR_INTERVAL512 = 1

    	Mirror Interval 512

    .. data:: MIRROR_INTERVAL1K = 2

    	Mirror Interval 1K

    .. data:: MIRROR_INTERVAL2K = 3

    	Mirror Interval 2K

    .. data:: MIRROR_INTERVAL4K = 4

    	Mirror Interval 4K

    .. data:: MIRROR_INTERVAL8K = 5

    	Mirror Interval 8K

    .. data:: MIRROR_INTERVAL16K = 6

    	Mirror Interval 16K

    """

    MIRROR_INTERVAL_ALL = 0

    MIRROR_INTERVAL512 = 1

    MIRROR_INTERVAL1K = 2

    MIRROR_INTERVAL2K = 3

    MIRROR_INTERVAL4K = 4

    MIRROR_INTERVAL8K = 5

    MIRROR_INTERVAL16K = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['MirrorIntervalEnum']


class SessionClassEnum(Enum):
    """
    SessionClassEnum

    Session class

    .. data:: ETHERNET_CLASS = 0

    	Ethernet mirroring session

    .. data:: IPV4_CLASS = 1

    	IPv4 mirroring session

    .. data:: IPV6_CLASS = 2

    	IPv6 mirroring session

    .. data:: INVALID_CLASS = 65535

    	Invalid session class

    """

    ETHERNET_CLASS = 0

    IPV4_CLASS = 1

    IPV6_CLASS = 2

    INVALID_CLASS = 65535


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['SessionClassEnum']


class TrafficDirectionEnum(Enum):
    """
    TrafficDirectionEnum

    Monitor\-session traffic directions

    .. data:: INVALID = 0

    	Invalid

    .. data:: RX_ONLY = 1

    	Received

    .. data:: TX_ONLY = 2

    	Transmitted

    .. data:: BOTH = 3

    	Both

    """

    INVALID = 0

    RX_ONLY = 1

    TX_ONLY = 2

    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['TrafficDirectionEnum']



class SpanMonitorSession(object):
    """
    Monitor Session operational data
    
    .. attribute:: global_
    
    	Global operational data
    	**type**\: :py:class:`Global <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global>`
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\: :py:class:`Nodes <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes>`
    
    

    """

    _prefix = 'ethernet-span-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.global_ = SpanMonitorSession.Global()
        self.global_.parent = self
        self.nodes = SpanMonitorSession.Nodes()
        self.nodes.parent = self


    class Global(object):
        """
        Global operational data
        
        .. attribute:: global_sessions
        
        	Global Monitor Sessions table
        	**type**\: :py:class:`GlobalSessions <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions>`
        
        

        """

        _prefix = 'ethernet-span-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.global_sessions = SpanMonitorSession.Global.GlobalSessions()
            self.global_sessions.parent = self


        class GlobalSessions(object):
            """
            Global Monitor Sessions table
            
            .. attribute:: global_session
            
            	Information about a globally\-configured monitor session
            	**type**\: list of :py:class:`GlobalSession <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession>`
            
            

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
                	**type**\: str
                
                	**range:** 0..79
                
                .. attribute:: destination_data
                
                	Destination data
                	**type**\: :py:class:`DestinationData <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData>`
                
                .. attribute:: destination_error
                
                	Last error observed for the destination 
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_id
                
                	Destination ID
                	**type**\: :py:class:`DestinationId <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId>`
                
                .. attribute:: destination_interface_handle
                
                	Destination interface handle (deprecated by DestinationID, invalid for pseudowires)
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: destination_interface_name
                
                	Destination interface name (deprecated by DestinationData, invalid for pseudowires)
                	**type**\: str
                
                .. attribute:: id
                
                	Numerical ID assigned to session
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_error
                
                	Last error observed for the destination interface (deprecated by DestinationError)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: name
                
                	Session Name
                	**type**\: str
                
                .. attribute:: session_class
                
                	Session class
                	**type**\: :py:class:`SessionClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.session = None
                    self.destination_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData()
                    self.destination_data.parent = self
                    self.destination_error = None
                    self.destination_id = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId()
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
                    	**type**\: :py:class:`DestinationClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                    
                    .. attribute:: interface_data
                    
                    	Interface data
                    	**type**\: :py:class:`InterfaceData <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData>`
                    
                    .. attribute:: invalid_value
                    
                    	Invalid Parameter
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_hop_ipv4_data
                    
                    	Next\-hop IPv4 data
                    	**type**\: :py:class:`NextHopIpv4Data <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data>`
                    
                    .. attribute:: next_hop_ipv6_data
                    
                    	Next\-hop IPv6 data
                    	**type**\: :py:class:`NextHopIpv6Data <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data>`
                    
                    .. attribute:: pseudowire_data
                    
                    	Pseudowire data
                    	**type**\: :py:class:`PseudowireData <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_class = None
                        self.interface_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData()
                        self.interface_data.parent = self
                        self.invalid_value = None
                        self.next_hop_ipv4_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data()
                        self.next_hop_ipv4_data.parent = self
                        self.next_hop_ipv6_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data()
                        self.next_hop_ipv6_data.parent = self
                        self.pseudowire_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData()
                        self.pseudowire_data.parent = self


                    class InterfaceData(object):
                        """
                        Interface data
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        .. attribute:: interface_state
                        
                        	Interface State
                        	**type**\: :py:class:`ImStateEnumEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.ImStateEnumEnum>`
                        
                        

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
                            if not self.is_config():
                                return False
                            if self.interface_name is not None:
                                return True

                            if self.interface_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData']['meta_info']


                    class PseudowireData(object):
                        """
                        Pseudowire data
                        
                        .. attribute:: pseudowire_is_up
                        
                        	Pseudowire State
                        	**type**\: bool
                        
                        .. attribute:: pseudowire_name
                        
                        	Pseudowire Name
                        	**type**\: str
                        
                        

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
                            if not self.is_config():
                                return False
                            if self.pseudowire_is_up is not None:
                                return True

                            if self.pseudowire_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData']['meta_info']


                    class NextHopIpv4Data(object):
                        """
                        Next\-hop IPv4 data
                        
                        .. attribute:: address_is_reachable
                        
                        	Address is reachable
                        	**type**\: bool
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        

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
                            if not self.is_config():
                                return False
                            if self.address_is_reachable is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data']['meta_info']


                    class NextHopIpv6Data(object):
                        """
                        Next\-hop IPv6 data
                        
                        .. attribute:: address_is_reachable
                        
                        	Address is reachable
                        	**type**\: bool
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        

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
                            if not self.is_config():
                                return False
                            if self.address_is_reachable is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:destination-data'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                        return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData']['meta_info']


                class DestinationId(object):
                    """
                    Destination ID
                    
                    .. attribute:: destination_class
                    
                    	DestinationClass
                    	**type**\: :py:class:`DestinationClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                    
                    .. attribute:: interface
                    
                    	Interface Handle
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: invalid_value
                    
                    	Invalid Parameter
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_address_and_vrf
                    
                    	IPv4 address
                    	**type**\: :py:class:`Ipv4AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf>`
                    
                    .. attribute:: ipv6_address_and_vrf
                    
                    	IPv6 address
                    	**type**\: :py:class:`Ipv6AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf>`
                    
                    .. attribute:: pseudowire_id
                    
                    	Pseudowire XCID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_class = None
                        self.interface = None
                        self.invalid_value = None
                        self.ipv4_address_and_vrf = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf()
                        self.ipv4_address_and_vrf.parent = self
                        self.ipv6_address_and_vrf = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf()
                        self.ipv6_address_and_vrf.parent = self
                        self.pseudowire_id = None


                    class Ipv4AddressAndVrf(object):
                        """
                        IPv4 address
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF
                        	**type**\: str
                        
                        

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
                            if not self.is_config():
                                return False
                            if self.ipv4_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf']['meta_info']


                    class Ipv6AddressAndVrf(object):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF
                        	**type**\: str
                        
                        

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
                            if not self.is_config():
                                return False
                            if self.ipv6_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:destination-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                        return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId']['meta_info']

                @property
                def _common_path(self):
                    if self.session is None:
                        raise YPYModelError('Key property session is None')

                    return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:global/Cisco-IOS-XR-Ethernet-SPAN-oper:global-sessions/Cisco-IOS-XR-Ethernet-SPAN-oper:global-session[Cisco-IOS-XR-Ethernet-SPAN-oper:session = ' + str(self.session) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                    return meta._meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:global/Cisco-IOS-XR-Ethernet-SPAN-oper:global-sessions'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.global_session is not None:
                    for child_ref in self.global_session:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                return meta._meta_table['SpanMonitorSession.Global.GlobalSessions']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.global_sessions is not None and self.global_sessions._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
            return meta._meta_table['SpanMonitorSession.Global']['meta_info']


    class Nodes(object):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of :py:class:`Node <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node>`
        
        

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
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: attachments
            
            	Table of source interfaces configured as attached to a session
            	**type**\: :py:class:`Attachments <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments>`
            
            .. attribute:: hardware_sessions
            
            	Table of sessions set up in the hardware.  When all sessions are operating correctly the entries in this table should match those entries in GlobalSessionTable that have a destination configured
            	**type**\: :py:class:`HardwareSessions <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions>`
            
            .. attribute:: interfaces
            
            	Table of source interfaces set up in the hardware.  The entries in this table should match the entries in AttachmentTable when all sessions are operating correctly
            	**type**\: :py:class:`Interfaces <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces>`
            
            

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
                	**type**\: list of :py:class:`Attachment <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment>`
                
                

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
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: session  <key>
                    
                    	Session Name
                    	**type**\: str
                    
                    	**range:** 0..79
                    
                    .. attribute:: dest_pw_type_not_supported
                    
                    	The destination PW type is not supported
                    	**type**\: bool
                    
                    .. attribute:: destination_id
                    
                    	Destination ID
                    	**type**\: :py:class:`DestinationId <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: global_class
                    
                    	Global session class
                    	**type**\: :py:class:`SessionClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                    
                    .. attribute:: id
                    
                    	Numerical ID assigned to session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_class
                    
                    	Local attachment class
                    	**type**\: :py:class:`SessionClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                    
                    .. attribute:: name
                    
                    	Session Name
                    	**type**\: str
                    
                    .. attribute:: pfi_error
                    
                    	Last error returned from PFI for this interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_is_configured
                    
                    	The Session is configured globally
                    	**type**\: bool
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: source_interface_state
                    
                    	Source interface state
                    	**type**\: :py:class:`ImStateEnumEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.ImStateEnumEnum>`
                    
                    .. attribute:: traffic_direction
                    
                    	Traffic mirroring direction (deprecated by TrafficParameters)
                    	**type**\: :py:class:`TrafficDirectionEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                    
                    .. attribute:: traffic_parameters
                    
                    	Traffic mirroring parameters
                    	**type**\: :py:class:`TrafficParameters <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.session = None
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
                        self.source_interface_state = None
                        self.traffic_direction = None
                        self.traffic_parameters = SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters()
                        self.traffic_parameters.parent = self


                    class TrafficParameters(object):
                        """
                        Traffic mirroring parameters
                        
                        .. attribute:: is_acl_enabled
                        
                        	ACL enabled
                        	**type**\: bool
                        
                        .. attribute:: mirror_bytes
                        
                        	Number of bytes to mirror
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mirror_interval
                        
                        	Interval between mirrored packets
                        	**type**\: :py:class:`MirrorIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorIntervalEnum>`
                        
                        .. attribute:: port_level
                        
                        	Port level mirroring
                        	**type**\: bool
                        
                        .. attribute:: traffic_direction
                        
                        	Direction
                        	**type**\: :py:class:`TrafficDirectionEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                        
                        

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
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters']['meta_info']


                    class DestinationId(object):
                        """
                        Destination ID
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\: :py:class:`DestinationClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\: :py:class:`Ipv4AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\: :py:class:`Ipv6AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\: int
                        
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
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

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
                                if not self.is_config():
                                    return False
                                if self.ipv4_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf']['meta_info']


                        class Ipv6AddressAndVrf(object):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

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
                                if not self.is_config():
                                    return False
                                if self.ipv6_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')
                        if self.session is None:
                            raise YPYModelError('Key property session is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-oper:attachment[Cisco-IOS-XR-Ethernet-SPAN-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-Ethernet-SPAN-oper:session = ' + str(self.session) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface is not None:
                            return True

                        if self.session is not None:
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

                        if self.source_interface_state is not None:
                            return True

                        if self.traffic_direction is not None:
                            return True

                        if self.traffic_parameters is not None and self.traffic_parameters._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                    if not self.is_config():
                        return False
                    if self.attachment is not None:
                        for child_ref in self.attachment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                	**type**\: list of :py:class:`HardwareSession <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession>`
                
                

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
                    	**type**\: :py:class:`DestinationId <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: id
                    
                    	Assigned numerical ID for this session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	Configured Session Name
                    	**type**\: str
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this session while programming the hardware
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_class
                    
                    	Sesssion class
                    	**type**\: :py:class:`SpanSessionClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClassEnum>`
                    
                    .. attribute:: session_class_xr
                    
                    	Session class
                    	**type**\: :py:class:`SessionClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
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
                        	**type**\: :py:class:`DestinationClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\: :py:class:`Ipv4AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\: :py:class:`Ipv6AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\: int
                        
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
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

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
                                if not self.is_config():
                                    return False
                                if self.ipv4_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf']['meta_info']


                        class Ipv6AddressAndVrf(object):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

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
                                if not self.is_config():
                                    return False
                                if self.ipv6_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                    if not self.is_config():
                        return False
                    if self.hardware_session is not None:
                        for child_ref in self.hardware_session:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                    return meta._meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions']['meta_info']


            class Interfaces(object):
                """
                Table of source interfaces set up in the
                hardware.  The entries in this table should
                match the entries in AttachmentTable when all
                sessions are operating correctly
                
                .. attribute:: interface
                
                	Information about a particular interface that is set up in the hardware
                	**type**\: list of :py:class:`Interface <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface>`
                
                

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
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: attachment
                    
                    	Attachment information
                    	**type**\: list of :py:class:`Attachment <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment>`
                    
                    .. attribute:: destination_id
                    
                    	Destination ID (deprecated by Attachment)
                    	**type**\: :py:class:`DestinationId <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by Attachment)
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this interface while programming the hardware
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: traffic_direction
                    
                    	Traffic mirroring direction (deprecated by Attachment)
                    	**type**\: :py:class:`TrafficDirectionEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                    
                    .. attribute:: traffic_mirroring_parameters
                    
                    	Traffic mirroring parameters (deprecated by Attachment)
                    	**type**\: :py:class:`TrafficMirroringParameters <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters>`
                    
                    

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
                        	**type**\: :py:class:`DestinationClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\: :py:class:`Ipv4AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\: :py:class:`Ipv6AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\: int
                        
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
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

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
                                if not self.is_config():
                                    return False
                                if self.ipv4_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf']['meta_info']


                        class Ipv6AddressAndVrf(object):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

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
                                if not self.is_config():
                                    return False
                                if self.ipv6_address is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId']['meta_info']


                    class TrafficMirroringParameters(object):
                        """
                        Traffic mirroring parameters (deprecated by
                        Attachment)
                        
                        .. attribute:: is_acl_enabled
                        
                        	ACL enabled
                        	**type**\: bool
                        
                        .. attribute:: mirror_bytes
                        
                        	Number of bytes to mirror
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mirror_interval
                        
                        	Interval between mirrored packets
                        	**type**\: :py:class:`MirrorIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorIntervalEnum>`
                        
                        .. attribute:: port_level
                        
                        	Port level mirroring
                        	**type**\: bool
                        
                        .. attribute:: traffic_direction
                        
                        	Direction
                        	**type**\: :py:class:`TrafficDirectionEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                        
                        

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
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                            return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters']['meta_info']


                    class Attachment(object):
                        """
                        Attachment information
                        
                        .. attribute:: class_
                        
                        	Attachment class
                        	**type**\: :py:class:`SessionClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClassEnum>`
                        
                        .. attribute:: destination_id
                        
                        	Destination ID
                        	**type**\: :py:class:`DestinationId <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId>`
                        
                        .. attribute:: traffic_mirroring_parameters
                        
                        	Traffic mirroring parameters
                        	**type**\: :py:class:`TrafficMirroringParameters <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters>`
                        
                        

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
                            	**type**\: :py:class:`DestinationClassEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClassEnum>`
                            
                            .. attribute:: interface
                            
                            	Interface Handle
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: invalid_value
                            
                            	Invalid Parameter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_address_and_vrf
                            
                            	IPv4 address
                            	**type**\: :py:class:`Ipv4AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf>`
                            
                            .. attribute:: ipv6_address_and_vrf
                            
                            	IPv6 address
                            	**type**\: :py:class:`Ipv6AddressAndVrf <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf>`
                            
                            .. attribute:: pseudowire_id
                            
                            	Pseudowire XCID
                            	**type**\: int
                            
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
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF
                                	**type**\: str
                                
                                

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
                                    if not self.is_config():
                                        return False
                                    if self.ipv4_address is not None:
                                        return True

                                    if self.vrf_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                    return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf']['meta_info']


                            class Ipv6AddressAndVrf(object):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF
                                	**type**\: str
                                
                                

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
                                    if not self.is_config():
                                        return False
                                    if self.ipv6_address is not None:
                                        return True

                                    if self.vrf_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                                return meta._meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId']['meta_info']


                        class TrafficMirroringParameters(object):
                            """
                            Traffic mirroring parameters
                            
                            .. attribute:: is_acl_enabled
                            
                            	ACL enabled
                            	**type**\: bool
                            
                            .. attribute:: mirror_bytes
                            
                            	Number of bytes to mirror
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mirror_interval
                            
                            	Interval between mirrored packets
                            	**type**\: :py:class:`MirrorIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorIntervalEnum>`
                            
                            .. attribute:: port_level
                            
                            	Port level mirroring
                            	**type**\: bool
                            
                            .. attribute:: traffic_direction
                            
                            	Direction
                            	**type**\: :py:class:`TrafficDirectionEnum <ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirectionEnum>`
                            
                            

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
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                            if not self.is_config():
                                return False
                            if self.class_ is not None:
                                return True

                            if self.destination_id is not None and self.destination_id._has_data():
                                return True

                            if self.traffic_mirroring_parameters is not None and self.traffic_mirroring_parameters._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                    if not self.is_config():
                        return False
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
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
                if not self.is_config():
                    return False
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
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
                return meta._meta_table['SpanMonitorSession.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/Cisco-IOS-XR-Ethernet-SPAN-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
            return meta._meta_table['SpanMonitorSession.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_oper as meta
        return meta._meta_table['SpanMonitorSession']['meta_info']


