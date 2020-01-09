""" Cisco_IOS_XR_ping_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ping action package configuration.

Copyright (c) 2016, 2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ping(_Entity_):
    """
    Send echo messages
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output>`
    
    

    """

    _prefix = 'ping-act'
    _revision = '2018-10-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ping, self).__init__()
        self._top_entity = None

        self.yang_name = "ping"
        self.yang_parent_name = "Cisco-IOS-XR-ping-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Ping.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = Ping.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-ping-act:ping"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:  :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Destination>`
        
        	**presence node**\: True
        
        .. attribute:: ipv4
        
        	
        	**type**\: list of  		 :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Ipv4>`
        
        .. attribute:: ipv6
        
        	
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Ipv6>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'ping-act'
        _revision = '2018-10-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ping.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ping"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("destination", ("destination", Ping.Input.Destination)), ("ipv4", ("ipv4", Ping.Input.Ipv4)), ("ipv6", ("ipv6", Ping.Input.Ipv6))])
            self._leafs = OrderedDict()

            self.destination = None
            self._children_name_map["destination"] = "destination"

            self.ipv6 = None
            self._children_name_map["ipv6"] = "ipv6"

            self.ipv4 = YList(self)
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ping.Input, [], name, value)


        class Destination(_Entity_):
            """
            
            
            .. attribute:: destination
            
            	Ping destination address or hostname
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\: int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\: int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\: int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\: bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\: str
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\: bool
            
            .. attribute:: type_of_service
            
            	Type of Service
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: do_not_frag
            
            	Do Not Fragment
            	**type**\: bool
            
            .. attribute:: validate
            
            	Validate return packet
            	**type**\: bool
            
            .. attribute:: priority
            
            	Priority of the packet
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of ping to link local address
            	**type**\: str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ping-act'
            _revision = '2018-10-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ping.Input.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                    ('repeat_count', (YLeaf(YType.uint64, 'repeat-count'), ['int'])),
                    ('data_size', (YLeaf(YType.uint64, 'data-size'), ['int'])),
                    ('timeout', (YLeaf(YType.uint64, 'timeout'), ['int'])),
                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                    ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                    ('sweep', (YLeaf(YType.boolean, 'sweep'), ['bool'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                    ('verbose', (YLeaf(YType.boolean, 'verbose'), ['bool'])),
                    ('type_of_service', (YLeaf(YType.uint8, 'type-of-service'), ['int'])),
                    ('do_not_frag', (YLeaf(YType.boolean, 'do-not-frag'), ['bool'])),
                    ('validate', (YLeaf(YType.boolean, 'validate'), ['bool'])),
                    ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                    ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                ])
                self.destination = None
                self.repeat_count = None
                self.data_size = None
                self.timeout = None
                self.interval = None
                self.pattern = None
                self.sweep = None
                self.vrf_name = None
                self.source = None
                self.verbose = None
                self.type_of_service = None
                self.do_not_frag = None
                self.validate = None
                self.priority = None
                self.outgoing_interface = None
                self._segment_path = lambda: "destination"
                self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ping.Input.Destination, ['destination', 'repeat_count', 'data_size', 'timeout', 'interval', 'pattern', 'sweep', 'vrf_name', 'source', 'verbose', 'type_of_service', 'do_not_frag', 'validate', 'priority', 'outgoing_interface'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                return meta._meta_table['Ping.Input.Destination']['meta_info']


        class Ipv4(_Entity_):
            """
            
            
            .. attribute:: destination  (key)
            
            	Ping destination address or hostname
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\: int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\: int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\: int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\: bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\: str
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\: bool
            
            .. attribute:: type_of_service
            
            	Type of Service
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: do_not_frag
            
            	Do Not Fragment
            	**type**\: bool
            
            .. attribute:: validate
            
            	Validate return packet
            	**type**\: bool
            
            

            """

            _prefix = 'ping-act'
            _revision = '2018-10-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ping.Input.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['destination']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                    ('repeat_count', (YLeaf(YType.uint64, 'repeat-count'), ['int'])),
                    ('data_size', (YLeaf(YType.uint64, 'data-size'), ['int'])),
                    ('timeout', (YLeaf(YType.uint64, 'timeout'), ['int'])),
                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                    ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                    ('sweep', (YLeaf(YType.boolean, 'sweep'), ['bool'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                    ('verbose', (YLeaf(YType.boolean, 'verbose'), ['bool'])),
                    ('type_of_service', (YLeaf(YType.uint8, 'type-of-service'), ['int'])),
                    ('do_not_frag', (YLeaf(YType.boolean, 'do-not-frag'), ['bool'])),
                    ('validate', (YLeaf(YType.boolean, 'validate'), ['bool'])),
                ])
                self.destination = None
                self.repeat_count = None
                self.data_size = None
                self.timeout = None
                self.interval = None
                self.pattern = None
                self.sweep = None
                self.vrf_name = None
                self.source = None
                self.verbose = None
                self.type_of_service = None
                self.do_not_frag = None
                self.validate = None
                self._segment_path = lambda: "ipv4" + "[destination='" + str(self.destination) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ping.Input.Ipv4, ['destination', 'repeat_count', 'data_size', 'timeout', 'interval', 'pattern', 'sweep', 'vrf_name', 'source', 'verbose', 'type_of_service', 'do_not_frag', 'validate'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                return meta._meta_table['Ping.Input.Ipv4']['meta_info']


        class Ipv6(_Entity_):
            """
            
            
            .. attribute:: destination
            
            	Ping destination address or hostname
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\: int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\: int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\: int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\: bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\: str
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\: bool
            
            .. attribute:: priority
            
            	Priority of the packet
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of ping to link local address
            	**type**\: str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ping-act'
            _revision = '2018-10-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ping.Input.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                    ('repeat_count', (YLeaf(YType.uint64, 'repeat-count'), ['int'])),
                    ('data_size', (YLeaf(YType.uint64, 'data-size'), ['int'])),
                    ('timeout', (YLeaf(YType.uint64, 'timeout'), ['int'])),
                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                    ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                    ('sweep', (YLeaf(YType.boolean, 'sweep'), ['bool'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                    ('verbose', (YLeaf(YType.boolean, 'verbose'), ['bool'])),
                    ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                    ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                ])
                self.destination = None
                self.repeat_count = None
                self.data_size = None
                self.timeout = None
                self.interval = None
                self.pattern = None
                self.sweep = None
                self.vrf_name = None
                self.source = None
                self.verbose = None
                self.priority = None
                self.outgoing_interface = None
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ping.Input.Ipv6, ['destination', 'repeat_count', 'data_size', 'timeout', 'interval', 'pattern', 'sweep', 'vrf_name', 'source', 'verbose', 'priority', 'outgoing_interface'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                return meta._meta_table['Ping.Input.Ipv6']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
            return meta._meta_table['Ping.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: ping_response
        
        	
        	**type**\:  :py:class:`PingResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse>`
        
        

        """

        _prefix = 'ping-act'
        _revision = '2018-10-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ping.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "ping"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ping-response", ("ping_response", Ping.Output.PingResponse))])
            self._leafs = OrderedDict()

            self.ping_response = Ping.Output.PingResponse()
            self.ping_response.parent = self
            self._children_name_map["ping_response"] = "ping-response"
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ping.Output, [], name, value)


        class PingResponse(_Entity_):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\: list of  		 :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4>`
            
            .. attribute:: ipv6
            
            	
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ping-act'
            _revision = '2018-10-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ping.Output.PingResponse, self).__init__()

                self.yang_name = "ping-response"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4", ("ipv4", Ping.Output.PingResponse.Ipv4)), ("ipv6", ("ipv6", Ping.Output.PingResponse.Ipv6))])
                self._leafs = OrderedDict()

                self.ipv6 = None
                self._children_name_map["ipv6"] = "ipv6"

                self.ipv4 = YList(self)
                self._segment_path = lambda: "ping-response"
                self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ping.Output.PingResponse, [], name, value)


            class Ipv4(_Entity_):
                """
                
                
                .. attribute:: destination  (key)
                
                	Ping destination address or hostname
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: repeat_count
                
                	Number of ping packets to be sent out
                	**type**\: int
                
                	**range:** 1..64
                
                	**default value**\: 5
                
                .. attribute:: data_size
                
                	Size of ping packet
                	**type**\: int
                
                	**range:** 36..18024
                
                	**default value**\: 100
                
                .. attribute:: timeout
                
                	Timeout in seconds
                	**type**\: int
                
                	**range:** 0..36
                
                	**default value**\: 2
                
                .. attribute:: interval
                
                	Ping interval in milli seconds
                	**type**\: int
                
                	**range:** 0..3600
                
                	**default value**\: 10
                
                .. attribute:: pattern
                
                	Pattern of payload data
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: sweep
                
                	Sweep is enabled
                	**type**\: bool
                
                .. attribute:: replies
                
                	
                	**type**\:  :py:class:`Replies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies>`
                
                .. attribute:: hits
                
                	Number of packets reach to destination and get reply back
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total
                
                	Total number of packets sent out
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: success_rate
                
                	Successful rate of ping
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_min
                
                	Minimum value of Round Trip Time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_avg
                
                	Average value of Round Trip Time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_max
                
                	Maximum value of Round Trip Time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep_min
                
                	Minimum value of sweep size
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sweep_max
                
                	Maximum value of sweep size
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rotate_pattern
                
                	Rotate Pattern is enabled
                	**type**\: bool
                
                .. attribute:: ping_error_response
                
                	Error response for each ping, in case of bulk ping
                	**type**\: str
                
                

                """

                _prefix = 'ping-act'
                _revision = '2018-10-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ping.Output.PingResponse.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "ping-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['destination']
                    self._child_classes = OrderedDict([("replies", ("replies", Ping.Output.PingResponse.Ipv4.Replies))])
                    self._leafs = OrderedDict([
                        ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                        ('repeat_count', (YLeaf(YType.uint64, 'repeat-count'), ['int'])),
                        ('data_size', (YLeaf(YType.uint64, 'data-size'), ['int'])),
                        ('timeout', (YLeaf(YType.uint64, 'timeout'), ['int'])),
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                        ('sweep', (YLeaf(YType.boolean, 'sweep'), ['bool'])),
                        ('hits', (YLeaf(YType.uint64, 'hits'), ['int'])),
                        ('total', (YLeaf(YType.uint64, 'total'), ['int'])),
                        ('success_rate', (YLeaf(YType.uint64, 'success-rate'), ['int'])),
                        ('rtt_min', (YLeaf(YType.uint64, 'rtt-min'), ['int'])),
                        ('rtt_avg', (YLeaf(YType.uint64, 'rtt-avg'), ['int'])),
                        ('rtt_max', (YLeaf(YType.uint64, 'rtt-max'), ['int'])),
                        ('sweep_min', (YLeaf(YType.uint32, 'sweep-min'), ['int'])),
                        ('sweep_max', (YLeaf(YType.uint64, 'sweep-max'), ['int'])),
                        ('rotate_pattern', (YLeaf(YType.boolean, 'rotate-pattern'), ['bool'])),
                        ('ping_error_response', (YLeaf(YType.str, 'ping-error-response'), ['str'])),
                    ])
                    self.destination = None
                    self.repeat_count = None
                    self.data_size = None
                    self.timeout = None
                    self.interval = None
                    self.pattern = None
                    self.sweep = None
                    self.hits = None
                    self.total = None
                    self.success_rate = None
                    self.rtt_min = None
                    self.rtt_avg = None
                    self.rtt_max = None
                    self.sweep_min = None
                    self.sweep_max = None
                    self.rotate_pattern = None
                    self.ping_error_response = None

                    self.replies = Ping.Output.PingResponse.Ipv4.Replies()
                    self.replies.parent = self
                    self._children_name_map["replies"] = "replies"
                    self._segment_path = lambda: "ipv4" + "[destination='" + str(self.destination) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/ping-response/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ping.Output.PingResponse.Ipv4, ['destination', 'repeat_count', 'data_size', 'timeout', 'interval', 'pattern', 'sweep', 'hits', 'total', 'success_rate', 'rtt_min', 'rtt_avg', 'rtt_max', 'sweep_min', 'sweep_max', 'rotate_pattern', 'ping_error_response'], name, value)


                class Replies(_Entity_):
                    """
                    
                    
                    .. attribute:: reply
                    
                    	
                    	**type**\: list of  		 :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply>`
                    
                    

                    """

                    _prefix = 'ping-act'
                    _revision = '2018-10-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ping.Output.PingResponse.Ipv4.Replies, self).__init__()

                        self.yang_name = "replies"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("reply", ("reply", Ping.Output.PingResponse.Ipv4.Replies.Reply))])
                        self._leafs = OrderedDict()

                        self.reply = YList(self)
                        self._segment_path = lambda: "replies"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ping.Output.PingResponse.Ipv4.Replies, [], name, value)


                    class Reply(_Entity_):
                        """
                        
                        
                        .. attribute:: reply_index  (key)
                        
                        	Index of the reply list
                        	**type**\: int
                        
                        	**range:** 1..2147483647
                        
                        .. attribute:: result
                        
                        	Response for each packet
                        	**type**\: str
                        
                        .. attribute:: broadcast_reply_addresses
                        
                        	
                        	**type**\:  :py:class:`BroadcastReplyAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses>`
                        
                        

                        """

                        _prefix = 'ping-act'
                        _revision = '2018-10-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ping.Output.PingResponse.Ipv4.Replies.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "replies"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['reply_index']
                            self._child_classes = OrderedDict([("broadcast-reply-addresses", ("broadcast_reply_addresses", Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses))])
                            self._leafs = OrderedDict([
                                ('reply_index', (YLeaf(YType.uint64, 'reply-index'), ['int'])),
                                ('result', (YLeaf(YType.str, 'result'), ['str'])),
                            ])
                            self.reply_index = None
                            self.result = None

                            self.broadcast_reply_addresses = Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses()
                            self.broadcast_reply_addresses.parent = self
                            self._children_name_map["broadcast_reply_addresses"] = "broadcast-reply-addresses"
                            self._segment_path = lambda: "reply" + "[reply-index='" + str(self.reply_index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ping.Output.PingResponse.Ipv4.Replies.Reply, ['reply_index', 'result'], name, value)


                        class BroadcastReplyAddresses(_Entity_):
                            """
                            
                            
                            .. attribute:: broadcast_reply_address
                            
                            	
                            	**type**\: list of  		 :py:class:`BroadcastReplyAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress>`
                            
                            

                            """

                            _prefix = 'ping-act'
                            _revision = '2018-10-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses, self).__init__()

                                self.yang_name = "broadcast-reply-addresses"
                                self.yang_parent_name = "reply"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("broadcast-reply-address", ("broadcast_reply_address", Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress))])
                                self._leafs = OrderedDict()

                                self.broadcast_reply_address = YList(self)
                                self._segment_path = lambda: "broadcast-reply-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses, [], name, value)


                            class BroadcastReplyAddress(_Entity_):
                                """
                                
                                
                                .. attribute:: reply_address  (key)
                                
                                	Broadcast reply address
                                	**type**\: str
                                
                                .. attribute:: result
                                
                                	Sign for each reply packet
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ping-act'
                                _revision = '2018-10-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress, self).__init__()

                                    self.yang_name = "broadcast-reply-address"
                                    self.yang_parent_name = "broadcast-reply-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['reply_address']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('reply_address', (YLeaf(YType.str, 'reply-address'), ['str'])),
                                        ('result', (YLeaf(YType.str, 'result'), ['str'])),
                                    ])
                                    self.reply_address = None
                                    self.result = None
                                    self._segment_path = lambda: "broadcast-reply-address" + "[reply-address='" + str(self.reply_address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress, ['reply_address', 'result'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                                    return meta._meta_table['Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                                return meta._meta_table['Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                            return meta._meta_table['Ping.Output.PingResponse.Ipv4.Replies.Reply']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                        return meta._meta_table['Ping.Output.PingResponse.Ipv4.Replies']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                    return meta._meta_table['Ping.Output.PingResponse.Ipv4']['meta_info']


            class Ipv6(_Entity_):
                """
                
                
                .. attribute:: destination
                
                	Ping destination address or hostname
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: repeat_count
                
                	Number of ping packets to be sent out
                	**type**\: int
                
                	**range:** 1..64
                
                	**default value**\: 5
                
                .. attribute:: data_size
                
                	Size of ping packet
                	**type**\: int
                
                	**range:** 36..18024
                
                	**default value**\: 100
                
                .. attribute:: timeout
                
                	Timeout in seconds
                	**type**\: int
                
                	**range:** 0..36
                
                	**default value**\: 2
                
                .. attribute:: interval
                
                	Ping interval in milli seconds
                	**type**\: int
                
                	**range:** 0..3600
                
                	**default value**\: 10
                
                .. attribute:: pattern
                
                	Pattern of payload data
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: sweep
                
                	Sweep is enabled
                	**type**\: bool
                
                .. attribute:: sweep_min
                
                	Minimum value of sweep size
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sweep_max
                
                	Maximum value of sweep size
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rotate_pattern
                
                	Rotate Pattern is enabled
                	**type**\: bool
                
                .. attribute:: replies
                
                	
                	**type**\:  :py:class:`Replies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6.Replies>`
                
                .. attribute:: hits
                
                	Number of packets reach to destination and get reply back
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total
                
                	Total number of packets sent out
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: success_rate
                
                	Successful rate of ping
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_min
                
                	Minimum value of Round Trip Time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_avg
                
                	Average value of Round Trip Time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_max
                
                	Maximum value of Round Trip Time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ping-act'
                _revision = '2018-10-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ping.Output.PingResponse.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "ping-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("replies", ("replies", Ping.Output.PingResponse.Ipv6.Replies))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                        ('repeat_count', (YLeaf(YType.uint64, 'repeat-count'), ['int'])),
                        ('data_size', (YLeaf(YType.uint64, 'data-size'), ['int'])),
                        ('timeout', (YLeaf(YType.uint64, 'timeout'), ['int'])),
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                        ('sweep', (YLeaf(YType.boolean, 'sweep'), ['bool'])),
                        ('sweep_min', (YLeaf(YType.uint32, 'sweep-min'), ['int'])),
                        ('sweep_max', (YLeaf(YType.uint64, 'sweep-max'), ['int'])),
                        ('rotate_pattern', (YLeaf(YType.boolean, 'rotate-pattern'), ['bool'])),
                        ('hits', (YLeaf(YType.uint64, 'hits'), ['int'])),
                        ('total', (YLeaf(YType.uint64, 'total'), ['int'])),
                        ('success_rate', (YLeaf(YType.uint64, 'success-rate'), ['int'])),
                        ('rtt_min', (YLeaf(YType.uint64, 'rtt-min'), ['int'])),
                        ('rtt_avg', (YLeaf(YType.uint64, 'rtt-avg'), ['int'])),
                        ('rtt_max', (YLeaf(YType.uint64, 'rtt-max'), ['int'])),
                    ])
                    self.destination = None
                    self.repeat_count = None
                    self.data_size = None
                    self.timeout = None
                    self.interval = None
                    self.pattern = None
                    self.sweep = None
                    self.sweep_min = None
                    self.sweep_max = None
                    self.rotate_pattern = None
                    self.hits = None
                    self.total = None
                    self.success_rate = None
                    self.rtt_min = None
                    self.rtt_avg = None
                    self.rtt_max = None

                    self.replies = Ping.Output.PingResponse.Ipv6.Replies()
                    self.replies.parent = self
                    self._children_name_map["replies"] = "replies"
                    self._segment_path = lambda: "ipv6"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/ping-response/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ping.Output.PingResponse.Ipv6, ['destination', 'repeat_count', 'data_size', 'timeout', 'interval', 'pattern', 'sweep', 'sweep_min', 'sweep_max', 'rotate_pattern', 'hits', 'total', 'success_rate', 'rtt_min', 'rtt_avg', 'rtt_max'], name, value)


                class Replies(_Entity_):
                    """
                    
                    
                    .. attribute:: reply
                    
                    	
                    	**type**\: list of  		 :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6.Replies.Reply>`
                    
                    

                    """

                    _prefix = 'ping-act'
                    _revision = '2018-10-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ping.Output.PingResponse.Ipv6.Replies, self).__init__()

                        self.yang_name = "replies"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("reply", ("reply", Ping.Output.PingResponse.Ipv6.Replies.Reply))])
                        self._leafs = OrderedDict()

                        self.reply = YList(self)
                        self._segment_path = lambda: "replies"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/ping-response/ipv6/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ping.Output.PingResponse.Ipv6.Replies, [], name, value)


                    class Reply(_Entity_):
                        """
                        
                        
                        .. attribute:: reply_index  (key)
                        
                        	Index of the reply list
                        	**type**\: int
                        
                        	**range:** 1..2147483647
                        
                        .. attribute:: result
                        
                        	Response for each packet
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ping-act'
                        _revision = '2018-10-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ping.Output.PingResponse.Ipv6.Replies.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "replies"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['reply_index']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reply_index', (YLeaf(YType.uint64, 'reply-index'), ['int'])),
                                ('result', (YLeaf(YType.str, 'result'), ['str'])),
                            ])
                            self.reply_index = None
                            self.result = None
                            self._segment_path = lambda: "reply" + "[reply-index='" + str(self.reply_index) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ping-act:ping/output/ping-response/ipv6/replies/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ping.Output.PingResponse.Ipv6.Replies.Reply, ['reply_index', 'result'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                            return meta._meta_table['Ping.Output.PingResponse.Ipv6.Replies.Reply']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                        return meta._meta_table['Ping.Output.PingResponse.Ipv6.Replies']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                    return meta._meta_table['Ping.Output.PingResponse.Ipv6']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
                return meta._meta_table['Ping.Output.PingResponse']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
            return meta._meta_table['Ping.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ping()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ping_act as meta
        return meta._meta_table['Ping']['meta_info']


