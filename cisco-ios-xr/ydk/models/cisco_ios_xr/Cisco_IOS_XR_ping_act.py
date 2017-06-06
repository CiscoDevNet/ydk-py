""" Cisco_IOS_XR_ping_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ping action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PingRpc(object):
    """
    Send echo messages
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output>`
    
    

    """

    _prefix = 'ping-act'
    _revision = '2016-09-28'

    def __init__(self):
        self.input = PingRpc.Input()
        self.input.parent = self
        self.output = PingRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Input.Destination>`
        
        .. attribute:: ipv4
        
        	
        	**type**\: list of    :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Input.Ipv4>`
        
        .. attribute:: ipv6
        
        	
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Input.Ipv6>`
        
        

        """

        _prefix = 'ping-act'
        _revision = '2016-09-28'

        def __init__(self):
            self.parent = None
            self.destination = PingRpc.Input.Destination()
            self.destination.parent = self
            self.ipv4 = YList()
            self.ipv4.parent = self
            self.ipv4.name = 'ipv4'
            self.ipv6 = PingRpc.Input.Ipv6()
            self.ipv6.parent = self


        class Destination(object):
            """
            
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\:  int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: destination
            
            	Ping destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: do_not_frag
            
            	Do Not Fragment
            	**type**\:  bool
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of ping to link local address
            	**type**\:  str
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: priority
            
            	Priority of the packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\:  bool
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: type_of_service
            
            	Type of Service
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: validate
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                self.parent = None
                self.data_size = None
                self.destination = None
                self.do_not_frag = None
                self.interval = None
                self.outgoing_interface = None
                self.pattern = None
                self.priority = None
                self.repeat_count = None
                self.source = None
                self.sweep = None
                self.timeout = None
                self.type_of_service = None
                self.validate = None
                self.verbose = None
                self.vrf_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:input/Cisco-IOS-XR-ping-act:destination'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.data_size is not None:
                    return True

                if self.destination is not None:
                    return True

                if self.do_not_frag is not None:
                    return True

                if self.interval is not None:
                    return True

                if self.outgoing_interface is not None:
                    return True

                if self.pattern is not None:
                    return True

                if self.priority is not None:
                    return True

                if self.repeat_count is not None:
                    return True

                if self.source is not None:
                    return True

                if self.sweep is not None:
                    return True

                if self.timeout is not None:
                    return True

                if self.type_of_service is not None:
                    return True

                if self.validate is not None:
                    return True

                if self.verbose is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                return meta._meta_table['PingRpc.Input.Destination']['meta_info']


        class Ipv4(object):
            """
            
            
            .. attribute:: destination  <key>
            
            	Ping destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\:  int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: do_not_frag
            
            	Do Not Fragment
            	**type**\:  bool
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\:  bool
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: type_of_service
            
            	Type of Service
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: validate
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                self.parent = None
                self.destination = None
                self.data_size = None
                self.do_not_frag = None
                self.interval = None
                self.pattern = None
                self.repeat_count = None
                self.source = None
                self.sweep = None
                self.timeout = None
                self.type_of_service = None
                self.validate = None
                self.verbose = None
                self.vrf_name = None

            @property
            def _common_path(self):
                if self.destination is None:
                    raise YPYModelError('Key property destination is None')

                return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:input/Cisco-IOS-XR-ping-act:ipv4[Cisco-IOS-XR-ping-act:destination = ' + str(self.destination) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.destination is not None:
                    return True

                if self.data_size is not None:
                    return True

                if self.do_not_frag is not None:
                    return True

                if self.interval is not None:
                    return True

                if self.pattern is not None:
                    return True

                if self.repeat_count is not None:
                    return True

                if self.source is not None:
                    return True

                if self.sweep is not None:
                    return True

                if self.timeout is not None:
                    return True

                if self.type_of_service is not None:
                    return True

                if self.validate is not None:
                    return True

                if self.verbose is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                return meta._meta_table['PingRpc.Input.Ipv4']['meta_info']


        class Ipv6(object):
            """
            
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\:  int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: destination
            
            	Ping destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of ping to link local address
            	**type**\:  str
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: priority
            
            	Priority of the packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\:  bool
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                self.parent = None
                self.data_size = None
                self.destination = None
                self.interval = None
                self.outgoing_interface = None
                self.pattern = None
                self.priority = None
                self.repeat_count = None
                self.source = None
                self.sweep = None
                self.timeout = None
                self.verbose = None
                self.vrf_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:input/Cisco-IOS-XR-ping-act:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.data_size is not None:
                    return True

                if self.destination is not None:
                    return True

                if self.interval is not None:
                    return True

                if self.outgoing_interface is not None:
                    return True

                if self.pattern is not None:
                    return True

                if self.priority is not None:
                    return True

                if self.repeat_count is not None:
                    return True

                if self.source is not None:
                    return True

                if self.sweep is not None:
                    return True

                if self.timeout is not None:
                    return True

                if self.verbose is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                return meta._meta_table['PingRpc.Input.Ipv6']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.destination is not None and self.destination._has_data():
                return True

            if self.ipv4 is not None:
                for child_ref in self.ipv4:
                    if child_ref._has_data():
                        return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
            return meta._meta_table['PingRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: ping_response
        
        	
        	**type**\:   :py:class:`PingResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse>`
        
        

        """

        _prefix = 'ping-act'
        _revision = '2016-09-28'

        def __init__(self):
            self.parent = None
            self.ping_response = PingRpc.Output.PingResponse()
            self.ping_response.parent = self


        class PingResponse(object):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\: list of    :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse.Ipv4>`
            
            .. attribute:: ipv6
            
            	
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse.Ipv6>`
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                self.parent = None
                self.ipv4 = YList()
                self.ipv4.parent = self
                self.ipv4.name = 'ipv4'
                self.ipv6 = PingRpc.Output.PingResponse.Ipv6()
                self.ipv6.parent = self


            class Ipv4(object):
                """
                
                
                .. attribute:: destination  <key>
                
                	Ping destination address or hostname
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: data_size
                
                	Size of ping packet
                	**type**\:  int
                
                	**range:** 36..18024
                
                	**default value**\: 100
                
                .. attribute:: hits
                
                	Number of packets reach to destination and get reply back
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: interval
                
                	Ping interval in milli seconds
                	**type**\:  int
                
                	**range:** 0..3600
                
                	**default value**\: 10
                
                .. attribute:: pattern
                
                	Pattern of payload data
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: ping_error_response
                
                	Error response for each ping, in case of bulk ping
                	**type**\:  str
                
                .. attribute:: repeat_count
                
                	Number of ping packets to be sent out
                	**type**\:  int
                
                	**range:** 1..64
                
                	**default value**\: 5
                
                .. attribute:: replies
                
                	
                	**type**\:   :py:class:`Replies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse.Ipv4.Replies>`
                
                .. attribute:: rotate_pattern
                
                	Rotate Pattern is enabled
                	**type**\:  bool
                
                .. attribute:: rtt_avg
                
                	Average value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_max
                
                	Maximum value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_min
                
                	Minimum value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: success_rate
                
                	Successful rate of ping
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep
                
                	Sweep is enabled
                	**type**\:  bool
                
                .. attribute:: sweep_max
                
                	Maximum value of sweep size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep_min
                
                	Minimum value of sweep size
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout
                
                	Timeout in seconds
                	**type**\:  int
                
                	**range:** 0..36
                
                	**default value**\: 2
                
                .. attribute:: total
                
                	Total number of packets sent out
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ping-act'
                _revision = '2016-09-28'

                def __init__(self):
                    self.parent = None
                    self.destination = None
                    self.data_size = None
                    self.hits = None
                    self.interval = None
                    self.pattern = None
                    self.ping_error_response = None
                    self.repeat_count = None
                    self.replies = PingRpc.Output.PingResponse.Ipv4.Replies()
                    self.replies.parent = self
                    self.rotate_pattern = None
                    self.rtt_avg = None
                    self.rtt_max = None
                    self.rtt_min = None
                    self.success_rate = None
                    self.sweep = None
                    self.sweep_max = None
                    self.sweep_min = None
                    self.timeout = None
                    self.total = None


                class Replies(object):
                    """
                    
                    
                    .. attribute:: reply
                    
                    	
                    	**type**\: list of    :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse.Ipv4.Replies.Reply>`
                    
                    

                    """

                    _prefix = 'ping-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        self.parent = None
                        self.reply = YList()
                        self.reply.parent = self
                        self.reply.name = 'reply'


                    class Reply(object):
                        """
                        
                        
                        .. attribute:: reply_index  <key>
                        
                        	Index of the reply list
                        	**type**\:  int
                        
                        	**range:** 1..2147483647
                        
                        .. attribute:: broadcast_reply_addresses
                        
                        	
                        	**type**\:   :py:class:`BroadcastReplyAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses>`
                        
                        .. attribute:: result
                        
                        	Response for each packet
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ping-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            self.parent = None
                            self.reply_index = None
                            self.broadcast_reply_addresses = PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses()
                            self.broadcast_reply_addresses.parent = self
                            self.result = None


                        class BroadcastReplyAddresses(object):
                            """
                            
                            
                            .. attribute:: broadcast_reply_address
                            
                            	
                            	**type**\: list of    :py:class:`BroadcastReplyAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress>`
                            
                            

                            """

                            _prefix = 'ping-act'
                            _revision = '2016-09-28'

                            def __init__(self):
                                self.parent = None
                                self.broadcast_reply_address = YList()
                                self.broadcast_reply_address.parent = self
                                self.broadcast_reply_address.name = 'broadcast_reply_address'


                            class BroadcastReplyAddress(object):
                                """
                                
                                
                                .. attribute:: reply_address  <key>
                                
                                	Broadcast reply address
                                	**type**\:  str
                                
                                .. attribute:: result
                                
                                	Sign for each reply packet
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ping-act'
                                _revision = '2016-09-28'

                                def __init__(self):
                                    self.parent = None
                                    self.reply_address = None
                                    self.result = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.reply_address is None:
                                        raise YPYModelError('Key property reply_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ping-act:broadcast-reply-address[Cisco-IOS-XR-ping-act:reply-address = ' + str(self.reply_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    if self.parent is None:
                                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                                    return self.parent.is_config()

                                def _has_data(self):
                                    if self.reply_address is not None:
                                        return True

                                    if self.result is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                                    return meta._meta_table['PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ping-act:broadcast-reply-addresses'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                if self.parent is None:
                                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                                return self.parent.is_config()

                            def _has_data(self):
                                if self.broadcast_reply_address is not None:
                                    for child_ref in self.broadcast_reply_address:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                                return meta._meta_table['PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.reply_index is None:
                                raise YPYModelError('Key property reply_index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ping-act:reply[Cisco-IOS-XR-ping-act:reply-index = ' + str(self.reply_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            if self.parent is None:
                                raise YPYError('Parent reference is needed to determine if entity has configuration data')
                            return self.parent.is_config()

                        def _has_data(self):
                            if self.reply_index is not None:
                                return True

                            if self.broadcast_reply_addresses is not None and self.broadcast_reply_addresses._has_data():
                                return True

                            if self.result is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                            return meta._meta_table['PingRpc.Output.PingResponse.Ipv4.Replies.Reply']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ping-act:replies'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.reply is not None:
                            for child_ref in self.reply:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                        return meta._meta_table['PingRpc.Output.PingResponse.Ipv4.Replies']['meta_info']

                @property
                def _common_path(self):
                    if self.destination is None:
                        raise YPYModelError('Key property destination is None')

                    return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:output/Cisco-IOS-XR-ping-act:ping-response/Cisco-IOS-XR-ping-act:ipv4[Cisco-IOS-XR-ping-act:destination = ' + str(self.destination) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.destination is not None:
                        return True

                    if self.data_size is not None:
                        return True

                    if self.hits is not None:
                        return True

                    if self.interval is not None:
                        return True

                    if self.pattern is not None:
                        return True

                    if self.ping_error_response is not None:
                        return True

                    if self.repeat_count is not None:
                        return True

                    if self.replies is not None and self.replies._has_data():
                        return True

                    if self.rotate_pattern is not None:
                        return True

                    if self.rtt_avg is not None:
                        return True

                    if self.rtt_max is not None:
                        return True

                    if self.rtt_min is not None:
                        return True

                    if self.success_rate is not None:
                        return True

                    if self.sweep is not None:
                        return True

                    if self.sweep_max is not None:
                        return True

                    if self.sweep_min is not None:
                        return True

                    if self.timeout is not None:
                        return True

                    if self.total is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                    return meta._meta_table['PingRpc.Output.PingResponse.Ipv4']['meta_info']


            class Ipv6(object):
                """
                
                
                .. attribute:: data_size
                
                	Size of ping packet
                	**type**\:  int
                
                	**range:** 36..18024
                
                	**default value**\: 100
                
                .. attribute:: destination
                
                	Ping destination address or hostname
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: hits
                
                	Number of packets reach to destination and get reply back
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: interval
                
                	Ping interval in milli seconds
                	**type**\:  int
                
                	**range:** 0..3600
                
                	**default value**\: 10
                
                .. attribute:: pattern
                
                	Pattern of payload data
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: repeat_count
                
                	Number of ping packets to be sent out
                	**type**\:  int
                
                	**range:** 1..64
                
                	**default value**\: 5
                
                .. attribute:: replies
                
                	
                	**type**\:   :py:class:`Replies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse.Ipv6.Replies>`
                
                .. attribute:: rotate_pattern
                
                	Rotate Pattern is enabled
                	**type**\:  bool
                
                .. attribute:: rtt_avg
                
                	Average value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_max
                
                	Maximum value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_min
                
                	Minimum value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: success_rate
                
                	Successful rate of ping
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep
                
                	Sweep is enabled
                	**type**\:  bool
                
                .. attribute:: sweep_max
                
                	Maximum value of sweep size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep_min
                
                	Minimum value of sweep size
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout
                
                	Timeout in seconds
                	**type**\:  int
                
                	**range:** 0..36
                
                	**default value**\: 2
                
                .. attribute:: total
                
                	Total number of packets sent out
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ping-act'
                _revision = '2016-09-28'

                def __init__(self):
                    self.parent = None
                    self.data_size = None
                    self.destination = None
                    self.hits = None
                    self.interval = None
                    self.pattern = None
                    self.repeat_count = None
                    self.replies = PingRpc.Output.PingResponse.Ipv6.Replies()
                    self.replies.parent = self
                    self.rotate_pattern = None
                    self.rtt_avg = None
                    self.rtt_max = None
                    self.rtt_min = None
                    self.success_rate = None
                    self.sweep = None
                    self.sweep_max = None
                    self.sweep_min = None
                    self.timeout = None
                    self.total = None


                class Replies(object):
                    """
                    
                    
                    .. attribute:: reply
                    
                    	
                    	**type**\: list of    :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.PingRpc.Output.PingResponse.Ipv6.Replies.Reply>`
                    
                    

                    """

                    _prefix = 'ping-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        self.parent = None
                        self.reply = YList()
                        self.reply.parent = self
                        self.reply.name = 'reply'


                    class Reply(object):
                        """
                        
                        
                        .. attribute:: reply_index  <key>
                        
                        	Index of the reply list
                        	**type**\:  int
                        
                        	**range:** 1..2147483647
                        
                        .. attribute:: result
                        
                        	Response for each packet
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ping-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            self.parent = None
                            self.reply_index = None
                            self.result = None

                        @property
                        def _common_path(self):
                            if self.reply_index is None:
                                raise YPYModelError('Key property reply_index is None')

                            return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:output/Cisco-IOS-XR-ping-act:ping-response/Cisco-IOS-XR-ping-act:ipv6/Cisco-IOS-XR-ping-act:replies/Cisco-IOS-XR-ping-act:reply[Cisco-IOS-XR-ping-act:reply-index = ' + str(self.reply_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            if self.parent is None:
                                raise YPYError('Parent reference is needed to determine if entity has configuration data')
                            return self.parent.is_config()

                        def _has_data(self):
                            if self.reply_index is not None:
                                return True

                            if self.result is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                            return meta._meta_table['PingRpc.Output.PingResponse.Ipv6.Replies.Reply']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:output/Cisco-IOS-XR-ping-act:ping-response/Cisco-IOS-XR-ping-act:ipv6/Cisco-IOS-XR-ping-act:replies'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.reply is not None:
                            for child_ref in self.reply:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                        return meta._meta_table['PingRpc.Output.PingResponse.Ipv6.Replies']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:output/Cisco-IOS-XR-ping-act:ping-response/Cisco-IOS-XR-ping-act:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.data_size is not None:
                        return True

                    if self.destination is not None:
                        return True

                    if self.hits is not None:
                        return True

                    if self.interval is not None:
                        return True

                    if self.pattern is not None:
                        return True

                    if self.repeat_count is not None:
                        return True

                    if self.replies is not None and self.replies._has_data():
                        return True

                    if self.rotate_pattern is not None:
                        return True

                    if self.rtt_avg is not None:
                        return True

                    if self.rtt_max is not None:
                        return True

                    if self.rtt_min is not None:
                        return True

                    if self.success_rate is not None:
                        return True

                    if self.sweep is not None:
                        return True

                    if self.sweep_max is not None:
                        return True

                    if self.sweep_min is not None:
                        return True

                    if self.timeout is not None:
                        return True

                    if self.total is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                    return meta._meta_table['PingRpc.Output.PingResponse.Ipv6']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:output/Cisco-IOS-XR-ping-act:ping-response'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.ipv4 is not None:
                    for child_ref in self.ipv4:
                        if child_ref._has_data():
                            return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                return meta._meta_table['PingRpc.Output.PingResponse']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ping-act:ping/Cisco-IOS-XR-ping-act:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.ping_response is not None and self.ping_response._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
            return meta._meta_table['PingRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ping-act:ping'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
        return meta._meta_table['PingRpc']['meta_info']


