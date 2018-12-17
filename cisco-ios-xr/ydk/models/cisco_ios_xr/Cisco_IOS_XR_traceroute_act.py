""" Cisco_IOS_XR_traceroute_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ping action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Traceroute(Entity):
    """
    Trace route to destination
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output>`
    
    

    """

    _prefix = 'traceroute-act'
    _revision = '2016-09-28'

    def __init__(self):
        super(Traceroute, self).__init__()
        self._top_entity = None

        self.yang_name = "traceroute"
        self.yang_parent_name = "Cisco-IOS-XR-traceroute-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Traceroute.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = Traceroute.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:  :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Destination>`
        
        .. attribute:: ipv4
        
        	
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Ipv4>`
        
        .. attribute:: ipv6
        
        	
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Ipv6>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Traceroute.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "traceroute"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("destination", ("destination", Traceroute.Input.Destination)), ("ipv4", ("ipv4", Traceroute.Input.Ipv4)), ("ipv6", ("ipv6", Traceroute.Input.Ipv6))])
            self._leafs = OrderedDict()

            self.destination = Traceroute.Input.Destination()
            self.destination.parent = self
            self._children_name_map["destination"] = "destination"

            self.ipv4 = Traceroute.Input.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"

            self.ipv6 = Traceroute.Input.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Traceroute.Input, [], name, value)


        class Destination(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\: str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\: int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: probe
            
            	Probe count
            	**type**\: int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\: bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\: int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\: int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: port
            
            	Port numbe
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\: bool
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\: str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                    ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ('probe', (YLeaf(YType.uint16, 'probe'), ['int'])),
                    ('numeric', (YLeaf(YType.boolean, 'numeric'), ['bool'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('min_ttl', (YLeaf(YType.uint16, 'min-ttl'), ['int'])),
                    ('max_ttl', (YLeaf(YType.uint16, 'max-ttl'), ['int'])),
                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                    ('verbose', (YLeaf(YType.boolean, 'verbose'), ['bool'])),
                    ('priority', (YLeaf(YType.uint16, 'priority'), ['int'])),
                    ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                ])
                self.destination = None
                self.source = None
                self.timeout = None
                self.probe = None
                self.numeric = None
                self.vrf_name = None
                self.min_ttl = None
                self.max_ttl = None
                self.port = None
                self.verbose = None
                self.priority = None
                self.outgoing_interface = None
                self._segment_path = lambda: "destination"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Destination, [u'destination', u'source', u'timeout', u'probe', u'numeric', u'vrf_name', u'min_ttl', u'max_ttl', u'port', u'verbose', 'priority', 'outgoing_interface'], name, value)


        class Ipv4(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\: str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\: int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: probe
            
            	Probe count
            	**type**\: int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\: bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\: int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\: int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: port
            
            	Port numbe
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\: bool
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                    ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ('probe', (YLeaf(YType.uint16, 'probe'), ['int'])),
                    ('numeric', (YLeaf(YType.boolean, 'numeric'), ['bool'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('min_ttl', (YLeaf(YType.uint16, 'min-ttl'), ['int'])),
                    ('max_ttl', (YLeaf(YType.uint16, 'max-ttl'), ['int'])),
                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                    ('verbose', (YLeaf(YType.boolean, 'verbose'), ['bool'])),
                ])
                self.destination = None
                self.source = None
                self.timeout = None
                self.probe = None
                self.numeric = None
                self.vrf_name = None
                self.min_ttl = None
                self.max_ttl = None
                self.port = None
                self.verbose = None
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Ipv4, [u'destination', u'source', u'timeout', u'probe', u'numeric', u'vrf_name', u'min_ttl', u'max_ttl', u'port', u'verbose'], name, value)


        class Ipv6(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\: str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\: int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: probe
            
            	Probe count
            	**type**\: int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\: bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\: int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\: int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: port
            
            	Port numbe
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\: bool
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\: str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                    ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ('probe', (YLeaf(YType.uint16, 'probe'), ['int'])),
                    ('numeric', (YLeaf(YType.boolean, 'numeric'), ['bool'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('min_ttl', (YLeaf(YType.uint16, 'min-ttl'), ['int'])),
                    ('max_ttl', (YLeaf(YType.uint16, 'max-ttl'), ['int'])),
                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                    ('verbose', (YLeaf(YType.boolean, 'verbose'), ['bool'])),
                    ('priority', (YLeaf(YType.uint16, 'priority'), ['int'])),
                    ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                ])
                self.destination = None
                self.source = None
                self.timeout = None
                self.probe = None
                self.numeric = None
                self.vrf_name = None
                self.min_ttl = None
                self.max_ttl = None
                self.port = None
                self.verbose = None
                self.priority = None
                self.outgoing_interface = None
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Ipv6, [u'destination', u'source', u'timeout', u'probe', u'numeric', u'vrf_name', u'min_ttl', u'max_ttl', u'port', u'verbose', 'priority', 'outgoing_interface'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: traceroute_response
        
        	
        	**type**\:  :py:class:`TracerouteResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Traceroute.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "traceroute"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("traceroute-response", ("traceroute_response", Traceroute.Output.TracerouteResponse))])
            self._leafs = OrderedDict()

            self.traceroute_response = Traceroute.Output.TracerouteResponse()
            self.traceroute_response.parent = self
            self._children_name_map["traceroute_response"] = "traceroute-response"
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Traceroute.Output, [], name, value)


        class TracerouteResponse(Entity):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4>`
            
            .. attribute:: ipv6
            
            	
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6>`
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Output.TracerouteResponse, self).__init__()

                self.yang_name = "traceroute-response"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4", ("ipv4", Traceroute.Output.TracerouteResponse.Ipv4)), ("ipv6", ("ipv6", Traceroute.Output.TracerouteResponse.Ipv6))])
                self._leafs = OrderedDict()

                self.ipv4 = Traceroute.Output.TracerouteResponse.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"

                self.ipv6 = Traceroute.Output.TracerouteResponse.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._segment_path = lambda: "traceroute-response"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Output.TracerouteResponse, [], name, value)


            class Ipv4(Entity):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\: str
                
                .. attribute:: hops
                
                	
                	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\: str
                
                

                """

                _prefix = 'traceroute-act'
                _revision = '2016-09-28'

                def __init__(self):
                    super(Traceroute.Output.TracerouteResponse.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "traceroute-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("hops", ("hops", Traceroute.Output.TracerouteResponse.Ipv4.Hops))])
                    self._leafs = OrderedDict([
                        ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                        ('verbose_output', (YLeaf(YType.str, 'verbose-output'), ['str'])),
                    ])
                    self.destination = None
                    self.verbose_output = None

                    self.hops = Traceroute.Output.TracerouteResponse.Ipv4.Hops()
                    self.hops.parent = self
                    self._children_name_map["hops"] = "hops"
                    self._segment_path = lambda: "ipv4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4, [u'destination', u'verbose_output'], name, value)


                class Hops(Entity):
                    """
                    
                    
                    .. attribute:: hop
                    
                    	
                    	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Traceroute.Output.TracerouteResponse.Ipv4.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hop", ("hop", Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop))])
                        self._leafs = OrderedDict()

                        self.hop = YList(self)
                        self._segment_path = lambda: "hops"
                        self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/ipv4/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops, [], name, value)


                    class Hop(Entity):
                        """
                        
                        
                        .. attribute:: hop_index  (key)
                        
                        	Index of the hop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_address
                        
                        	Address of the hop
                        	**type**\: str
                        
                        .. attribute:: hop_hostname
                        
                        	Hostname of the hop
                        	**type**\: str
                        
                        .. attribute:: probes
                        
                        	
                        	**type**\:  :py:class:`Probes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes>`
                        
                        

                        """

                        _prefix = 'traceroute-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop, self).__init__()

                            self.yang_name = "hop"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['hop_index']
                            self._child_classes = OrderedDict([("probes", ("probes", Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes))])
                            self._leafs = OrderedDict([
                                ('hop_index', (YLeaf(YType.uint32, 'hop-index'), ['int'])),
                                ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                ('hop_hostname', (YLeaf(YType.str, 'hop-hostname'), ['str'])),
                            ])
                            self.hop_index = None
                            self.hop_address = None
                            self.hop_hostname = None

                            self.probes = Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes()
                            self.probes.parent = self
                            self._children_name_map["probes"] = "probes"
                            self._segment_path = lambda: "hop" + "[hop-index='" + str(self.hop_index) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/ipv4/hops/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop, [u'hop_index', u'hop_address', u'hop_hostname'], name, value)


                        class Probes(Entity):
                            """
                            
                            
                            .. attribute:: probe
                            
                            	
                            	**type**\: list of  		 :py:class:`Probe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe>`
                            
                            

                            """

                            _prefix = 'traceroute-act'
                            _revision = '2016-09-28'

                            def __init__(self):
                                super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes, self).__init__()

                                self.yang_name = "probes"
                                self.yang_parent_name = "hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("probe", ("probe", Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe))])
                                self._leafs = OrderedDict()

                                self.probe = YList(self)
                                self._segment_path = lambda: "probes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes, [], name, value)


                            class Probe(Entity):
                                """
                                
                                
                                .. attribute:: probe_index  (key)
                                
                                	Index of the probe
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: result
                                
                                	Response for each probe
                                	**type**\: str
                                
                                .. attribute:: delta_time
                                
                                	Delta time in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hop_address
                                
                                	Address of the hop
                                	**type**\: str
                                
                                .. attribute:: hop_hostname
                                
                                	Hostname of the hop
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'traceroute-act'
                                _revision = '2016-09-28'

                                def __init__(self):
                                    super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe, self).__init__()

                                    self.yang_name = "probe"
                                    self.yang_parent_name = "probes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['probe_index']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('probe_index', (YLeaf(YType.uint32, 'probe-index'), ['int'])),
                                        ('result', (YLeaf(YType.str, 'result'), ['str'])),
                                        ('delta_time', (YLeaf(YType.uint32, 'delta-time'), ['int'])),
                                        ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                        ('hop_hostname', (YLeaf(YType.str, 'hop-hostname'), ['str'])),
                                    ])
                                    self.probe_index = None
                                    self.result = None
                                    self.delta_time = None
                                    self.hop_address = None
                                    self.hop_hostname = None
                                    self._segment_path = lambda: "probe" + "[probe-index='" + str(self.probe_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe, [u'probe_index', u'result', u'delta_time', u'hop_address', u'hop_hostname'], name, value)


            class Ipv6(Entity):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\: str
                
                .. attribute:: hops
                
                	
                	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\: str
                
                

                """

                _prefix = 'traceroute-act'
                _revision = '2016-09-28'

                def __init__(self):
                    super(Traceroute.Output.TracerouteResponse.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "traceroute-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("hops", ("hops", Traceroute.Output.TracerouteResponse.Ipv6.Hops))])
                    self._leafs = OrderedDict([
                        ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
                        ('verbose_output', (YLeaf(YType.str, 'verbose-output'), ['str'])),
                    ])
                    self.destination = None
                    self.verbose_output = None

                    self.hops = Traceroute.Output.TracerouteResponse.Ipv6.Hops()
                    self.hops.parent = self
                    self._children_name_map["hops"] = "hops"
                    self._segment_path = lambda: "ipv6"
                    self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6, [u'destination', u'verbose_output'], name, value)


                class Hops(Entity):
                    """
                    
                    
                    .. attribute:: hop
                    
                    	
                    	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Traceroute.Output.TracerouteResponse.Ipv6.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hop", ("hop", Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop))])
                        self._leafs = OrderedDict()

                        self.hop = YList(self)
                        self._segment_path = lambda: "hops"
                        self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/ipv6/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops, [], name, value)


                    class Hop(Entity):
                        """
                        
                        
                        .. attribute:: hop_index  (key)
                        
                        	Index of the hop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_address
                        
                        	Address of the hop
                        	**type**\: str
                        
                        .. attribute:: hop_hostname
                        
                        	Hostname of the hop
                        	**type**\: str
                        
                        .. attribute:: probes
                        
                        	
                        	**type**\:  :py:class:`Probes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes>`
                        
                        

                        """

                        _prefix = 'traceroute-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop, self).__init__()

                            self.yang_name = "hop"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['hop_index']
                            self._child_classes = OrderedDict([("probes", ("probes", Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes))])
                            self._leafs = OrderedDict([
                                ('hop_index', (YLeaf(YType.uint32, 'hop-index'), ['int'])),
                                ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                ('hop_hostname', (YLeaf(YType.str, 'hop-hostname'), ['str'])),
                            ])
                            self.hop_index = None
                            self.hop_address = None
                            self.hop_hostname = None

                            self.probes = Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes()
                            self.probes.parent = self
                            self._children_name_map["probes"] = "probes"
                            self._segment_path = lambda: "hop" + "[hop-index='" + str(self.hop_index) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/ipv6/hops/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop, [u'hop_index', u'hop_address', u'hop_hostname'], name, value)


                        class Probes(Entity):
                            """
                            
                            
                            .. attribute:: probe
                            
                            	
                            	**type**\: list of  		 :py:class:`Probe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe>`
                            
                            

                            """

                            _prefix = 'traceroute-act'
                            _revision = '2016-09-28'

                            def __init__(self):
                                super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes, self).__init__()

                                self.yang_name = "probes"
                                self.yang_parent_name = "hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("probe", ("probe", Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe))])
                                self._leafs = OrderedDict()

                                self.probe = YList(self)
                                self._segment_path = lambda: "probes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes, [], name, value)


                            class Probe(Entity):
                                """
                                
                                
                                .. attribute:: probe_index  (key)
                                
                                	Index of the probe
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: result
                                
                                	Response for each probe
                                	**type**\: str
                                
                                .. attribute:: delta_time
                                
                                	Delta time in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hop_address
                                
                                	Address of the hop
                                	**type**\: str
                                
                                .. attribute:: hop_hostname
                                
                                	Hostname of the hop
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'traceroute-act'
                                _revision = '2016-09-28'

                                def __init__(self):
                                    super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe, self).__init__()

                                    self.yang_name = "probe"
                                    self.yang_parent_name = "probes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['probe_index']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('probe_index', (YLeaf(YType.uint32, 'probe-index'), ['int'])),
                                        ('result', (YLeaf(YType.str, 'result'), ['str'])),
                                        ('delta_time', (YLeaf(YType.uint32, 'delta-time'), ['int'])),
                                        ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                        ('hop_hostname', (YLeaf(YType.str, 'hop-hostname'), ['str'])),
                                    ])
                                    self.probe_index = None
                                    self.result = None
                                    self.delta_time = None
                                    self.hop_address = None
                                    self.hop_hostname = None
                                    self._segment_path = lambda: "probe" + "[probe-index='" + str(self.probe_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe, [u'probe_index', u'result', u'delta_time', u'hop_address', u'hop_hostname'], name, value)

    def clone_ptr(self):
        self._top_entity = Traceroute()
        return self._top_entity

