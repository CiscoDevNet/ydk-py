""" Cisco_IOS_XR_ping_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ping action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ping(Entity):
    """
    Send echo messages
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output>`
    
    

    """

    _prefix = 'ping-act'
    _revision = '2016-09-28'

    def __init__(self):
        super(Ping, self).__init__()
        self._top_entity = None

        self.yang_name = "ping"
        self.yang_parent_name = "Cisco-IOS-XR-ping-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = Ping.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Ping.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XR-ping-act:ping"


    class Input(Entity):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Destination>`
        
        .. attribute:: ipv4
        
        	
        	**type**\: list of    :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Ipv4>`
        
        .. attribute:: ipv6
        
        	
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Ipv6>`
        
        

        """

        _prefix = 'ping-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Ping.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ping"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"destination" : ("destination", Ping.Input.Destination), "ipv6" : ("ipv6", Ping.Input.Ipv6)}
            self._child_list_classes = {"ipv4" : ("ipv4", Ping.Input.Ipv4)}

            self.destination = Ping.Input.Destination()
            self.destination.parent = self
            self._children_name_map["destination"] = "destination"
            self._children_yang_names.add("destination")

            self.ipv6 = Ping.Input.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")

            self.ipv4 = YList(self)
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ping.Input, [], name, value)


        class Destination(Entity):
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
                super(Ping.Input.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.data_size = YLeaf(YType.uint64, "data-size")

                self.destination = YLeaf(YType.str, "destination")

                self.do_not_frag = YLeaf(YType.boolean, "do-not-frag")

                self.interval = YLeaf(YType.uint32, "interval")

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.pattern = YLeaf(YType.str, "pattern")

                self.priority = YLeaf(YType.uint8, "priority")

                self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                self.source = YLeaf(YType.str, "source")

                self.sweep = YLeaf(YType.boolean, "sweep")

                self.timeout = YLeaf(YType.uint64, "timeout")

                self.type_of_service = YLeaf(YType.uint8, "type-of-service")

                self.validate = YLeaf(YType.boolean, "validate")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "destination"
                self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ping.Input.Destination, ['data_size', 'destination', 'do_not_frag', 'interval', 'outgoing_interface', 'pattern', 'priority', 'repeat_count', 'source', 'sweep', 'timeout', 'type_of_service', 'validate', 'verbose', 'vrf_name'], name, value)


        class Ipv4(Entity):
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
                super(Ping.Input.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.destination = YLeaf(YType.str, "destination")

                self.data_size = YLeaf(YType.uint64, "data-size")

                self.do_not_frag = YLeaf(YType.boolean, "do-not-frag")

                self.interval = YLeaf(YType.uint32, "interval")

                self.pattern = YLeaf(YType.str, "pattern")

                self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                self.source = YLeaf(YType.str, "source")

                self.sweep = YLeaf(YType.boolean, "sweep")

                self.timeout = YLeaf(YType.uint64, "timeout")

                self.type_of_service = YLeaf(YType.uint8, "type-of-service")

                self.validate = YLeaf(YType.boolean, "validate")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "ipv4" + "[destination='" + self.destination.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ping.Input.Ipv4, ['destination', 'data_size', 'do_not_frag', 'interval', 'pattern', 'repeat_count', 'source', 'sweep', 'timeout', 'type_of_service', 'validate', 'verbose', 'vrf_name'], name, value)


        class Ipv6(Entity):
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
                super(Ping.Input.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.data_size = YLeaf(YType.uint64, "data-size")

                self.destination = YLeaf(YType.str, "destination")

                self.interval = YLeaf(YType.uint32, "interval")

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.pattern = YLeaf(YType.str, "pattern")

                self.priority = YLeaf(YType.uint8, "priority")

                self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                self.source = YLeaf(YType.str, "source")

                self.sweep = YLeaf(YType.boolean, "sweep")

                self.timeout = YLeaf(YType.uint64, "timeout")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ping.Input.Ipv6, ['data_size', 'destination', 'interval', 'outgoing_interface', 'pattern', 'priority', 'repeat_count', 'source', 'sweep', 'timeout', 'verbose', 'vrf_name'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: ping_response
        
        	
        	**type**\:   :py:class:`PingResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse>`
        
        

        """

        _prefix = 'ping-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Ping.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "ping"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"ping-response" : ("ping_response", Ping.Output.PingResponse)}
            self._child_list_classes = {}

            self.ping_response = Ping.Output.PingResponse()
            self.ping_response.parent = self
            self._children_name_map["ping_response"] = "ping-response"
            self._children_yang_names.add("ping-response")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/%s" % self._segment_path()


        class PingResponse(Entity):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\: list of    :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4>`
            
            .. attribute:: ipv6
            
            	
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6>`
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Ping.Output.PingResponse, self).__init__()

                self.yang_name = "ping-response"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ipv6" : ("ipv6", Ping.Output.PingResponse.Ipv6)}
                self._child_list_classes = {"ipv4" : ("ipv4", Ping.Output.PingResponse.Ipv4)}

                self.ipv6 = Ping.Output.PingResponse.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")

                self.ipv4 = YList(self)
                self._segment_path = lambda: "ping-response"
                self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ping.Output.PingResponse, [], name, value)


            class Ipv4(Entity):
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
                
                	
                	**type**\:   :py:class:`Replies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies>`
                
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
                    super(Ping.Output.PingResponse.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "ping-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"replies" : ("replies", Ping.Output.PingResponse.Ipv4.Replies)}
                    self._child_list_classes = {}

                    self.destination = YLeaf(YType.str, "destination")

                    self.data_size = YLeaf(YType.uint64, "data-size")

                    self.hits = YLeaf(YType.uint64, "hits")

                    self.interval = YLeaf(YType.uint32, "interval")

                    self.pattern = YLeaf(YType.str, "pattern")

                    self.ping_error_response = YLeaf(YType.str, "ping-error-response")

                    self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                    self.rotate_pattern = YLeaf(YType.boolean, "rotate-pattern")

                    self.rtt_avg = YLeaf(YType.uint64, "rtt-avg")

                    self.rtt_max = YLeaf(YType.uint64, "rtt-max")

                    self.rtt_min = YLeaf(YType.uint64, "rtt-min")

                    self.success_rate = YLeaf(YType.uint64, "success-rate")

                    self.sweep = YLeaf(YType.boolean, "sweep")

                    self.sweep_max = YLeaf(YType.uint64, "sweep-max")

                    self.sweep_min = YLeaf(YType.uint32, "sweep-min")

                    self.timeout = YLeaf(YType.uint64, "timeout")

                    self.total = YLeaf(YType.uint64, "total")

                    self.replies = Ping.Output.PingResponse.Ipv4.Replies()
                    self.replies.parent = self
                    self._children_name_map["replies"] = "replies"
                    self._children_yang_names.add("replies")
                    self._segment_path = lambda: "ipv4" + "[destination='" + self.destination.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/ping-response/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ping.Output.PingResponse.Ipv4, ['destination', 'data_size', 'hits', 'interval', 'pattern', 'ping_error_response', 'repeat_count', 'rotate_pattern', 'rtt_avg', 'rtt_max', 'rtt_min', 'success_rate', 'sweep', 'sweep_max', 'sweep_min', 'timeout', 'total'], name, value)


                class Replies(Entity):
                    """
                    
                    
                    .. attribute:: reply
                    
                    	
                    	**type**\: list of    :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply>`
                    
                    

                    """

                    _prefix = 'ping-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Ping.Output.PingResponse.Ipv4.Replies, self).__init__()

                        self.yang_name = "replies"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"reply" : ("reply", Ping.Output.PingResponse.Ipv4.Replies.Reply)}

                        self.reply = YList(self)
                        self._segment_path = lambda: "replies"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ping.Output.PingResponse.Ipv4.Replies, [], name, value)


                    class Reply(Entity):
                        """
                        
                        
                        .. attribute:: reply_index  <key>
                        
                        	Index of the reply list
                        	**type**\:  int
                        
                        	**range:** 1..2147483647
                        
                        .. attribute:: broadcast_reply_addresses
                        
                        	
                        	**type**\:   :py:class:`BroadcastReplyAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses>`
                        
                        .. attribute:: result
                        
                        	Response for each packet
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ping-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Ping.Output.PingResponse.Ipv4.Replies.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "replies"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"broadcast-reply-addresses" : ("broadcast_reply_addresses", Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses)}
                            self._child_list_classes = {}

                            self.reply_index = YLeaf(YType.uint64, "reply-index")

                            self.result = YLeaf(YType.str, "result")

                            self.broadcast_reply_addresses = Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses()
                            self.broadcast_reply_addresses.parent = self
                            self._children_name_map["broadcast_reply_addresses"] = "broadcast-reply-addresses"
                            self._children_yang_names.add("broadcast-reply-addresses")
                            self._segment_path = lambda: "reply" + "[reply-index='" + self.reply_index.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ping.Output.PingResponse.Ipv4.Replies.Reply, ['reply_index', 'result'], name, value)


                        class BroadcastReplyAddresses(Entity):
                            """
                            
                            
                            .. attribute:: broadcast_reply_address
                            
                            	
                            	**type**\: list of    :py:class:`BroadcastReplyAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress>`
                            
                            

                            """

                            _prefix = 'ping-act'
                            _revision = '2016-09-28'

                            def __init__(self):
                                super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses, self).__init__()

                                self.yang_name = "broadcast-reply-addresses"
                                self.yang_parent_name = "reply"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"broadcast-reply-address" : ("broadcast_reply_address", Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress)}

                                self.broadcast_reply_address = YList(self)
                                self._segment_path = lambda: "broadcast-reply-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses, [], name, value)


                            class BroadcastReplyAddress(Entity):
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
                                    super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress, self).__init__()

                                    self.yang_name = "broadcast-reply-address"
                                    self.yang_parent_name = "broadcast-reply-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.reply_address = YLeaf(YType.str, "reply-address")

                                    self.result = YLeaf(YType.str, "result")
                                    self._segment_path = lambda: "broadcast-reply-address" + "[reply-address='" + self.reply_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress, ['reply_address', 'result'], name, value)


            class Ipv6(Entity):
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
                
                	
                	**type**\:   :py:class:`Replies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6.Replies>`
                
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
                    super(Ping.Output.PingResponse.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "ping-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"replies" : ("replies", Ping.Output.PingResponse.Ipv6.Replies)}
                    self._child_list_classes = {}

                    self.data_size = YLeaf(YType.uint64, "data-size")

                    self.destination = YLeaf(YType.str, "destination")

                    self.hits = YLeaf(YType.uint64, "hits")

                    self.interval = YLeaf(YType.uint32, "interval")

                    self.pattern = YLeaf(YType.str, "pattern")

                    self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                    self.rotate_pattern = YLeaf(YType.boolean, "rotate-pattern")

                    self.rtt_avg = YLeaf(YType.uint64, "rtt-avg")

                    self.rtt_max = YLeaf(YType.uint64, "rtt-max")

                    self.rtt_min = YLeaf(YType.uint64, "rtt-min")

                    self.success_rate = YLeaf(YType.uint64, "success-rate")

                    self.sweep = YLeaf(YType.boolean, "sweep")

                    self.sweep_max = YLeaf(YType.uint64, "sweep-max")

                    self.sweep_min = YLeaf(YType.uint32, "sweep-min")

                    self.timeout = YLeaf(YType.uint64, "timeout")

                    self.total = YLeaf(YType.uint64, "total")

                    self.replies = Ping.Output.PingResponse.Ipv6.Replies()
                    self.replies.parent = self
                    self._children_name_map["replies"] = "replies"
                    self._children_yang_names.add("replies")
                    self._segment_path = lambda: "ipv6"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/ping-response/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ping.Output.PingResponse.Ipv6, ['data_size', 'destination', 'hits', 'interval', 'pattern', 'repeat_count', 'rotate_pattern', 'rtt_avg', 'rtt_max', 'rtt_min', 'success_rate', 'sweep', 'sweep_max', 'sweep_min', 'timeout', 'total'], name, value)


                class Replies(Entity):
                    """
                    
                    
                    .. attribute:: reply
                    
                    	
                    	**type**\: list of    :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6.Replies.Reply>`
                    
                    

                    """

                    _prefix = 'ping-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Ping.Output.PingResponse.Ipv6.Replies, self).__init__()

                        self.yang_name = "replies"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"reply" : ("reply", Ping.Output.PingResponse.Ipv6.Replies.Reply)}

                        self.reply = YList(self)
                        self._segment_path = lambda: "replies"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/ping-response/ipv6/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ping.Output.PingResponse.Ipv6.Replies, [], name, value)


                    class Reply(Entity):
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
                            super(Ping.Output.PingResponse.Ipv6.Replies.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "replies"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.reply_index = YLeaf(YType.uint64, "reply-index")

                            self.result = YLeaf(YType.str, "result")
                            self._segment_path = lambda: "reply" + "[reply-index='" + self.reply_index.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/ping-response/ipv6/replies/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ping.Output.PingResponse.Ipv6.Replies.Reply, ['reply_index', 'result'], name, value)

    def clone_ptr(self):
        self._top_entity = Ping()
        return self._top_entity

