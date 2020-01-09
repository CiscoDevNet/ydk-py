""" Cisco_IOS_XR_traceroute_act 

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




class Traceroute(_Entity_):
    """
    Trace route to destination
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output>`
    
    

    """

    _prefix = 'traceroute-act'
    _revision = '2018-10-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class Input(_Entity_):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:  :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Destination>`
        
        	**presence node**\: True
        
        .. attribute:: ipv4
        
        	
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Ipv4>`
        
        	**presence node**\: True
        
        .. attribute:: ipv6
        
        	
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Ipv6>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2018-10-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Traceroute.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "traceroute"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("destination", ("destination", Traceroute.Input.Destination)), ("ipv4", ("ipv4", Traceroute.Input.Ipv4)), ("ipv6", ("ipv6", Traceroute.Input.Ipv6))])
            self._leafs = OrderedDict()

            self.destination = None
            self._children_name_map["destination"] = "destination"

            self.ipv4 = None
            self._children_name_map["ipv4"] = "ipv4"

            self.ipv6 = None
            self._children_name_map["ipv6"] = "ipv6"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Traceroute.Input, [], name, value)


        class Destination(_Entity_):
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
            
            .. attribute:: srv6_header
            
            	srv6 header
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\: str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'traceroute-act'
            _revision = '2018-10-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Traceroute.Input.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
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
                    ('srv6_header', (YLeaf(YType.empty, 'srv6-header'), ['Empty'])),
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
                self.srv6_header = None
                self.priority = None
                self.outgoing_interface = None
                self._segment_path = lambda: "destination"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Destination, ['destination', 'source', 'timeout', 'probe', 'numeric', 'vrf_name', 'min_ttl', 'max_ttl', 'port', 'verbose', 'srv6_header', 'priority', 'outgoing_interface'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                return meta._meta_table['Traceroute.Input.Destination']['meta_info']


        class Ipv4(_Entity_):
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
            
            .. attribute:: srv6_header
            
            	srv6 header
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'traceroute-act'
            _revision = '2018-10-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Traceroute.Input.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
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
                    ('srv6_header', (YLeaf(YType.empty, 'srv6-header'), ['Empty'])),
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
                self.srv6_header = None
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Ipv4, ['destination', 'source', 'timeout', 'probe', 'numeric', 'vrf_name', 'min_ttl', 'max_ttl', 'port', 'verbose', 'srv6_header'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                return meta._meta_table['Traceroute.Input.Ipv4']['meta_info']


        class Ipv6(_Entity_):
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
            
            .. attribute:: srv6_header
            
            	srv6 header
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\: str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'traceroute-act'
            _revision = '2018-10-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Traceroute.Input.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
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
                    ('srv6_header', (YLeaf(YType.empty, 'srv6-header'), ['Empty'])),
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
                self.srv6_header = None
                self.priority = None
                self.outgoing_interface = None
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Input.Ipv6, ['destination', 'source', 'timeout', 'probe', 'numeric', 'vrf_name', 'min_ttl', 'max_ttl', 'port', 'verbose', 'srv6_header', 'priority', 'outgoing_interface'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                return meta._meta_table['Traceroute.Input.Ipv6']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
            return meta._meta_table['Traceroute.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: traceroute_response
        
        	
        	**type**\:  :py:class:`TracerouteResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2018-10-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class TracerouteResponse(_Entity_):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4>`
            
            	**presence node**\: True
            
            .. attribute:: ipv6
            
            	
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2018-10-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Traceroute.Output.TracerouteResponse, self).__init__()

                self.yang_name = "traceroute-response"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4", ("ipv4", Traceroute.Output.TracerouteResponse.Ipv4)), ("ipv6", ("ipv6", Traceroute.Output.TracerouteResponse.Ipv6))])
                self._leafs = OrderedDict()

                self.ipv4 = None
                self._children_name_map["ipv4"] = "ipv4"

                self.ipv6 = None
                self._children_name_map["ipv6"] = "ipv6"
                self._segment_path = lambda: "traceroute-response"
                self._absolute_path = lambda: "Cisco-IOS-XR-traceroute-act:traceroute/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Traceroute.Output.TracerouteResponse, [], name, value)


            class Ipv4(_Entity_):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\: str
                
                .. attribute:: hops
                
                	
                	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\: str
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'traceroute-act'
                _revision = '2018-10-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Traceroute.Output.TracerouteResponse.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "traceroute-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("hops", ("hops", Traceroute.Output.TracerouteResponse.Ipv4.Hops))])
                    self.is_presence_container = True
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
                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4, ['destination', 'verbose_output'], name, value)


                class Hops(_Entity_):
                    """
                    
                    
                    .. attribute:: hop
                    
                    	
                    	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2018-10-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Hop(_Entity_):
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
                        _revision = '2018-10-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop, ['hop_index', 'hop_address', 'hop_hostname'], name, value)


                        class Probes(_Entity_):
                            """
                            
                            
                            .. attribute:: probe
                            
                            	
                            	**type**\: list of  		 :py:class:`Probe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe>`
                            
                            

                            """

                            _prefix = 'traceroute-act'
                            _revision = '2018-10-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class Probe(_Entity_):
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
                                
                                .. attribute:: srv6_header
                                
                                	
                                	**type**\:  :py:class:`Srv6Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header>`
                                
                                

                                """

                                _prefix = 'traceroute-act'
                                _revision = '2018-10-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe, self).__init__()

                                    self.yang_name = "probe"
                                    self.yang_parent_name = "probes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['probe_index']
                                    self._child_classes = OrderedDict([("srv6-header", ("srv6_header", Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header))])
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

                                    self.srv6_header = Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header()
                                    self.srv6_header.parent = self
                                    self._children_name_map["srv6_header"] = "srv6-header"
                                    self._segment_path = lambda: "probe" + "[probe-index='" + str(self.probe_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe, ['probe_index', 'result', 'delta_time', 'hop_address', 'hop_hostname'], name, value)


                                class Srv6Header(_Entity_):
                                    """
                                    
                                    
                                    .. attribute:: destination_address
                                    
                                    	Destination address for srv6 header
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: segments_left
                                    
                                    	Number of segments left
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: segments
                                    
                                    	
                                    	**type**\:  :py:class:`Segments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header.Segments>`
                                    
                                    

                                    """

                                    _prefix = 'traceroute-act'
                                    _revision = '2018-10-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header, self).__init__()

                                        self.yang_name = "srv6-header"
                                        self.yang_parent_name = "probe"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("segments", ("segments", Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header.Segments))])
                                        self._leafs = OrderedDict([
                                            ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                                            ('segments_left', (YLeaf(YType.uint32, 'segments-left'), ['int'])),
                                        ])
                                        self.destination_address = None
                                        self.segments_left = None

                                        self.segments = Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header.Segments()
                                        self.segments.parent = self
                                        self._children_name_map["segments"] = "segments"
                                        self._segment_path = lambda: "srv6-header"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header, ['destination_address', 'segments_left'], name, value)


                                    class Segments(_Entity_):
                                        """
                                        
                                        
                                        .. attribute:: segment
                                        
                                        	sid in sidlist
                                        	**type**\: list of str
                                        
                                        

                                        """

                                        _prefix = 'traceroute-act'
                                        _revision = '2018-10-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header.Segments, self).__init__()

                                            self.yang_name = "segments"
                                            self.yang_parent_name = "srv6-header"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('segment', (YLeafList(YType.str, 'segment'), ['str'])),
                                            ])
                                            self.segment = []
                                            self._segment_path = lambda: "segments"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header.Segments, ['segment'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                                            return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header.Segments']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                                        return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe.Srv6Header']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                                    return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes.Probe']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                                return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop.Probes']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                            return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv4.Hops.Hop']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                        return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv4.Hops']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                    return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv4']['meta_info']


            class Ipv6(_Entity_):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\: str
                
                .. attribute:: hops
                
                	
                	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\: str
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'traceroute-act'
                _revision = '2018-10-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Traceroute.Output.TracerouteResponse.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "traceroute-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("hops", ("hops", Traceroute.Output.TracerouteResponse.Ipv6.Hops))])
                    self.is_presence_container = True
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
                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6, ['destination', 'verbose_output'], name, value)


                class Hops(_Entity_):
                    """
                    
                    
                    .. attribute:: hop
                    
                    	
                    	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2018-10-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Hop(_Entity_):
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
                        _revision = '2018-10-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop, ['hop_index', 'hop_address', 'hop_hostname'], name, value)


                        class Probes(_Entity_):
                            """
                            
                            
                            .. attribute:: probe
                            
                            	
                            	**type**\: list of  		 :py:class:`Probe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe>`
                            
                            

                            """

                            _prefix = 'traceroute-act'
                            _revision = '2018-10-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class Probe(_Entity_):
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
                                
                                .. attribute:: srv6_header
                                
                                	
                                	**type**\:  :py:class:`Srv6Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header>`
                                
                                

                                """

                                _prefix = 'traceroute-act'
                                _revision = '2018-10-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe, self).__init__()

                                    self.yang_name = "probe"
                                    self.yang_parent_name = "probes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['probe_index']
                                    self._child_classes = OrderedDict([("srv6-header", ("srv6_header", Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header))])
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

                                    self.srv6_header = Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header()
                                    self.srv6_header.parent = self
                                    self._children_name_map["srv6_header"] = "srv6-header"
                                    self._segment_path = lambda: "probe" + "[probe-index='" + str(self.probe_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe, ['probe_index', 'result', 'delta_time', 'hop_address', 'hop_hostname'], name, value)


                                class Srv6Header(_Entity_):
                                    """
                                    
                                    
                                    .. attribute:: destination_address
                                    
                                    	Destination address for srv6 header
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: segments_left
                                    
                                    	Number of segments left
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: segments
                                    
                                    	
                                    	**type**\:  :py:class:`Segments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header.Segments>`
                                    
                                    

                                    """

                                    _prefix = 'traceroute-act'
                                    _revision = '2018-10-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header, self).__init__()

                                        self.yang_name = "srv6-header"
                                        self.yang_parent_name = "probe"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("segments", ("segments", Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header.Segments))])
                                        self._leafs = OrderedDict([
                                            ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                                            ('segments_left', (YLeaf(YType.uint32, 'segments-left'), ['int'])),
                                        ])
                                        self.destination_address = None
                                        self.segments_left = None

                                        self.segments = Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header.Segments()
                                        self.segments.parent = self
                                        self._children_name_map["segments"] = "segments"
                                        self._segment_path = lambda: "srv6-header"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header, ['destination_address', 'segments_left'], name, value)


                                    class Segments(_Entity_):
                                        """
                                        
                                        
                                        .. attribute:: segment
                                        
                                        	sid in sidlist
                                        	**type**\: list of str
                                        
                                        

                                        """

                                        _prefix = 'traceroute-act'
                                        _revision = '2018-10-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header.Segments, self).__init__()

                                            self.yang_name = "segments"
                                            self.yang_parent_name = "srv6-header"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('segment', (YLeafList(YType.str, 'segment'), ['str'])),
                                            ])
                                            self.segment = []
                                            self._segment_path = lambda: "segments"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header.Segments, ['segment'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                                            return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header.Segments']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                                        return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe.Srv6Header']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                                    return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes.Probe']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                                return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop.Probes']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                            return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv6.Hops.Hop']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                        return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv6.Hops']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                    return meta._meta_table['Traceroute.Output.TracerouteResponse.Ipv6']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                return meta._meta_table['Traceroute.Output.TracerouteResponse']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
            return meta._meta_table['Traceroute.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = Traceroute()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
        return meta._meta_table['Traceroute']['meta_info']


