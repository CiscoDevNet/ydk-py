""" Cisco_IOS_XR_traceroute_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ping action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Traceroute(Entity):
    """
    Trace route to destination
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output>`
    
    

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
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = Traceroute.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Traceroute.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute"


    class Input(Entity):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Destination>`
        
        .. attribute:: ipv4
        
        	
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Ipv4>`
        
        .. attribute:: ipv6
        
        	
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Ipv6>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Traceroute.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "traceroute"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"destination" : ("destination", Traceroute.Input.Destination), "ipv4" : ("ipv4", Traceroute.Input.Ipv4), "ipv6" : ("ipv6", Traceroute.Input.Ipv6)}
            self._child_list_classes = {}

            self.destination = Traceroute.Input.Destination()
            self.destination.parent = self
            self._children_name_map["destination"] = "destination"
            self._children_yang_names.add("destination")

            self.ipv4 = Traceroute.Input.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = Traceroute.Input.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/%s" % self._segment_path()


        class Destination(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\:  str
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.destination = YLeaf(YType.str, "destination")

                self.max_ttl = YLeaf(YType.uint16, "max-ttl")

                self.min_ttl = YLeaf(YType.uint16, "min-ttl")

                self.numeric = YLeaf(YType.boolean, "numeric")

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.port = YLeaf(YType.uint32, "port")

                self.priority = YLeaf(YType.uint16, "priority")

                self.probe = YLeaf(YType.uint16, "probe")

                self.source = YLeaf(YType.str, "source")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "destination"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Destination, ['destination', 'max_ttl', 'min_ttl', 'numeric', 'outgoing_interface', 'port', 'priority', 'probe', 'source', 'timeout', 'verbose', 'vrf_name'], name, value)


        class Ipv4(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.destination = YLeaf(YType.str, "destination")

                self.max_ttl = YLeaf(YType.uint16, "max-ttl")

                self.min_ttl = YLeaf(YType.uint16, "min-ttl")

                self.numeric = YLeaf(YType.boolean, "numeric")

                self.port = YLeaf(YType.uint32, "port")

                self.probe = YLeaf(YType.uint16, "probe")

                self.source = YLeaf(YType.str, "source")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Ipv4, ['destination', 'max_ttl', 'min_ttl', 'numeric', 'port', 'probe', 'source', 'timeout', 'verbose', 'vrf_name'], name, value)


        class Ipv6(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\:  str
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.destination = YLeaf(YType.str, "destination")

                self.max_ttl = YLeaf(YType.uint16, "max-ttl")

                self.min_ttl = YLeaf(YType.uint16, "min-ttl")

                self.numeric = YLeaf(YType.boolean, "numeric")

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.port = YLeaf(YType.uint32, "port")

                self.priority = YLeaf(YType.uint16, "priority")

                self.probe = YLeaf(YType.uint16, "probe")

                self.source = YLeaf(YType.str, "source")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Ipv6, ['destination', 'max_ttl', 'min_ttl', 'numeric', 'outgoing_interface', 'port', 'priority', 'probe', 'source', 'timeout', 'verbose', 'vrf_name'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: traceroute_response
        
        	
        	**type**\:   :py:class:`TracerouteResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Traceroute.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "traceroute"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"traceroute-response" : ("traceroute_response", Traceroute.Output.TracerouteResponse)}
            self._child_list_classes = {}

            self.traceroute_response = Traceroute.Output.TracerouteResponse()
            self.traceroute_response.parent = self
            self._children_name_map["traceroute_response"] = "traceroute-response"
            self._children_yang_names.add("traceroute-response")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/%s" % self._segment_path()


        class TracerouteResponse(Entity):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4>`
            
            .. attribute:: ipv6
            
            	
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6>`
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Output.TracerouteResponse, self).__init__()

                self.yang_name = "traceroute-response"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ipv4" : ("ipv4", Traceroute.Output.TracerouteResponse.Ipv4), "ipv6" : ("ipv6", Traceroute.Output.TracerouteResponse.Ipv6)}
                self._child_list_classes = {}

                self.ipv4 = Traceroute.Output.TracerouteResponse.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Traceroute.Output.TracerouteResponse.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")
                self._segment_path = lambda: "traceroute-response"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/%s" % self._segment_path()


            class Ipv4(Entity):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\:  str
                
                .. attribute:: hops
                
                	
                	**type**\: list of    :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\:  str
                
                

                """

                _prefix = 'traceroute-act'
                _revision = '2016-09-28'

                def __init__(self):
                    super(Traceroute.Output.TracerouteResponse.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "traceroute-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"hops" : ("hops", Traceroute.Output.TracerouteResponse.Ipv4.Hops)}

                    self.destination = YLeaf(YType.str, "destination")

                    self.verbose_output = YLeaf(YType.str, "verbose-output")

                    self.hops = YList(self)
                    self._segment_path = lambda: "ipv4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4, ['destination', 'verbose_output'], name, value)


                class Hops(Entity):
                    """
                    
                    
                    .. attribute:: hop_index  <key>
                    
                    	Index of the hop
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hop_address
                    
                    	Address of the hop
                    	**type**\:  str
                    
                    .. attribute:: hop_hostname
                    
                    	Hostname of the hop
                    	**type**\:  str
                    
                    .. attribute:: probes
                    
                    	
                    	**type**\: list of    :py:class:`Probes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Traceroute.Output.TracerouteResponse.Ipv4.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"probes" : ("probes", Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes)}

                        self.hop_index = YLeaf(YType.uint32, "hop-index")

                        self.hop_address = YLeaf(YType.str, "hop-address")

                        self.hop_hostname = YLeaf(YType.str, "hop-hostname")

                        self.probes = YList(self)
                        self._segment_path = lambda: "hops" + "[hop-index='" + self.hop_index.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/ipv4/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops, ['hop_index', 'hop_address', 'hop_hostname'], name, value)


                    class Probes(Entity):
                        """
                        
                        
                        .. attribute:: probe_index  <key>
                        
                        	Index of the probe
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delta_time
                        
                        	Delta time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_address
                        
                        	Address of the hop
                        	**type**\:  str
                        
                        .. attribute:: hop_hostname
                        
                        	Hostname of the hop
                        	**type**\:  str
                        
                        .. attribute:: result
                        
                        	Response for each probe
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'traceroute-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes, self).__init__()

                            self.yang_name = "probes"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.probe_index = YLeaf(YType.uint32, "probe-index")

                            self.delta_time = YLeaf(YType.uint32, "delta-time")

                            self.hop_address = YLeaf(YType.str, "hop-address")

                            self.hop_hostname = YLeaf(YType.str, "hop-hostname")

                            self.result = YLeaf(YType.str, "result")
                            self._segment_path = lambda: "probes" + "[probe-index='" + self.probe_index.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes, ['probe_index', 'delta_time', 'hop_address', 'hop_hostname', 'result'], name, value)


            class Ipv6(Entity):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\:  str
                
                .. attribute:: hops
                
                	
                	**type**\: list of    :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\:  str
                
                

                """

                _prefix = 'traceroute-act'
                _revision = '2016-09-28'

                def __init__(self):
                    super(Traceroute.Output.TracerouteResponse.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "traceroute-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"hops" : ("hops", Traceroute.Output.TracerouteResponse.Ipv6.Hops)}

                    self.destination = YLeaf(YType.str, "destination")

                    self.verbose_output = YLeaf(YType.str, "verbose-output")

                    self.hops = YList(self)
                    self._segment_path = lambda: "ipv6"
                    self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6, ['destination', 'verbose_output'], name, value)


                class Hops(Entity):
                    """
                    
                    
                    .. attribute:: hop_index  <key>
                    
                    	Index of the hop
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hop_address
                    
                    	Address of the hop
                    	**type**\:  str
                    
                    .. attribute:: hop_hostname
                    
                    	Hostname of the hop
                    	**type**\:  str
                    
                    .. attribute:: probes
                    
                    	
                    	**type**\: list of    :py:class:`Probes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Traceroute.Output.TracerouteResponse.Ipv6.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"probes" : ("probes", Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes)}

                        self.hop_index = YLeaf(YType.uint32, "hop-index")

                        self.hop_address = YLeaf(YType.str, "hop-address")

                        self.hop_hostname = YLeaf(YType.str, "hop-hostname")

                        self.probes = YList(self)
                        self._segment_path = lambda: "hops" + "[hop-index='" + self.hop_index.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/ipv6/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops, ['hop_index', 'hop_address', 'hop_hostname'], name, value)


                    class Probes(Entity):
                        """
                        
                        
                        .. attribute:: probe_index  <key>
                        
                        	Index of the probe
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delta_time
                        
                        	Delta time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_address
                        
                        	Address of the hop
                        	**type**\:  str
                        
                        .. attribute:: hop_hostname
                        
                        	Hostname of the hop
                        	**type**\:  str
                        
                        .. attribute:: result
                        
                        	Response for each probe
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'traceroute-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes, self).__init__()

                            self.yang_name = "probes"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.probe_index = YLeaf(YType.uint32, "probe-index")

                            self.delta_time = YLeaf(YType.uint32, "delta-time")

                            self.hop_address = YLeaf(YType.str, "hop-address")

                            self.hop_hostname = YLeaf(YType.str, "hop-hostname")

                            self.result = YLeaf(YType.str, "result")
                            self._segment_path = lambda: "probes" + "[probe-index='" + self.probe_index.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes, ['probe_index', 'delta_time', 'hop_address', 'hop_hostname', 'result'], name, value)

    def clone_ptr(self):
        self._top_entity = Traceroute()
        return self._top_entity

