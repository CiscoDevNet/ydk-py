""" Cisco_IOS_XR_man_xml_ttyagent_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-xml\-ttyagent package configuration.

This module contains definitions
for the following management objects\:
  xr\-xml\: XML
  netconf\: netconf

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class XrXml(Entity):
    """
    XML
    
    .. attribute:: agent
    
    	XML agent
    	**type**\:  :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(XrXml, self).__init__()
        self._top_entity = None

        self.yang_name = "xr-xml"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("agent", ("agent", XrXml.Agent))])
        self._leafs = OrderedDict()

        self.agent = XrXml.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._segment_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(XrXml, [], name, value)


    class Agent(Entity):
        """
        XML agent
        
        .. attribute:: default
        
        	XML default dedicated agent
        	**type**\:  :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default>`
        
        .. attribute:: tty
        
        	XML TTY agent
        	**type**\:  :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty>`
        
        .. attribute:: ssl
        
        	XML SSL agent
        	**type**\:  :py:class:`Ssl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl>`
        
        

        """

        _prefix = 'man-xml-ttyagent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(XrXml.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "xr-xml"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("default", ("default", XrXml.Agent.Default)), ("tty", ("tty", XrXml.Agent.Tty)), ("ssl", ("ssl", XrXml.Agent.Ssl))])
            self._leafs = OrderedDict()

            self.default = XrXml.Agent.Default()
            self.default.parent = self
            self._children_name_map["default"] = "default"

            self.tty = XrXml.Agent.Tty()
            self.tty.parent = self
            self._children_name_map["tty"] = "tty"

            self.ssl = XrXml.Agent.Ssl()
            self.ssl.parent = self
            self._children_name_map["ssl"] = "ssl"
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(XrXml.Agent, [], name, value)


        class Default(Entity):
            """
            XML default dedicated agent
            
            .. attribute:: ipv6_enable
            
            	IPv6 Transport State
            	**type**\: bool
            
            .. attribute:: ipv4_disable
            
            	TRUE to disable IPV4
            	**type**\: bool
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Session>`
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\: int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Throttle>`
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\: int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            .. attribute:: vrfs
            
            	List of VRFs
            	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Vrfs>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(XrXml.Agent.Default, self).__init__()

                self.yang_name = "default"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("session", ("session", XrXml.Agent.Default.Session)), ("throttle", ("throttle", XrXml.Agent.Default.Throttle)), ("vrfs", ("vrfs", XrXml.Agent.Default.Vrfs))])
                self._leafs = OrderedDict([
                    ('ipv6_enable', (YLeaf(YType.boolean, 'ipv6-enable'), ['bool'])),
                    ('ipv4_disable', (YLeaf(YType.boolean, 'ipv4-disable'), ['bool'])),
                    ('iteration_size', (YLeaf(YType.uint32, 'iteration-size'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('streaming_size', (YLeaf(YType.uint32, 'streaming-size'), ['int'])),
                ])
                self.ipv6_enable = None
                self.ipv4_disable = None
                self.iteration_size = None
                self.enable = None
                self.streaming_size = None

                self.session = XrXml.Agent.Default.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"

                self.throttle = XrXml.Agent.Default.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"

                self.vrfs = XrXml.Agent.Default.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._segment_path = lambda: "default"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(XrXml.Agent.Default, ['ipv6_enable', 'ipv4_disable', 'iteration_size', 'enable', 'streaming_size'], name, value)


            class Session(Entity):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\: int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(XrXml.Agent.Default.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "default"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ])
                    self.timeout = None
                    self._segment_path = lambda: "session"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/default/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Default.Session, ['timeout'], name, value)


            class Throttle(Entity):
                """
                XML agent throttling
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\: int
                
                	**range:** 1000..30000
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\: int
                
                	**range:** 100..1024
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(XrXml.Agent.Default.Throttle, self).__init__()

                    self.yang_name = "throttle"
                    self.yang_parent_name = "default"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('process_rate', (YLeaf(YType.uint32, 'process-rate'), ['int'])),
                        ('memory', (YLeaf(YType.uint32, 'memory'), ['int'])),
                    ])
                    self.process_rate = None
                    self.memory = None
                    self._segment_path = lambda: "throttle"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/default/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Default.Throttle, ['process_rate', 'memory'], name, value)


            class Vrfs(Entity):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	A specific VRF
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Vrfs.Vrf>`
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(XrXml.Agent.Default.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "default"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf", ("vrf", XrXml.Agent.Default.Vrfs.Vrf))])
                    self._leafs = OrderedDict()

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/default/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Default.Vrfs, [], name, value)


                class Vrf(Entity):
                    """
                    A specific VRF
                    
                    .. attribute:: vrf_name  (key)
                    
                    	VRF name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	IPv6 Transport Access list for VRF
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv4_access_list
                    
                    	IPv4 Transport Access list for VRF
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: access_list
                    
                    	Access list for XML agent
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: shutdown
                    
                    	Shutdown default VRF. This is applicable only for VRF default
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(XrXml.Agent.Default.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('ipv6_access_list', (YLeaf(YType.str, 'ipv6-access-list'), ['str'])),
                            ('ipv4_access_list', (YLeaf(YType.str, 'ipv4-access-list'), ['str'])),
                            ('access_list', (YLeaf(YType.str, 'access-list'), ['str'])),
                            ('shutdown', (YLeaf(YType.empty, 'shutdown'), ['Empty'])),
                        ])
                        self.vrf_name = None
                        self.ipv6_access_list = None
                        self.ipv4_access_list = None
                        self.access_list = None
                        self.shutdown = None
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/default/vrfs/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(XrXml.Agent.Default.Vrfs.Vrf, ['vrf_name', 'ipv6_access_list', 'ipv4_access_list', 'access_list', 'shutdown'], name, value)


        class Tty(Entity):
            """
            XML TTY agent
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty.Session>`
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\: int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty.Throttle>`
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\: int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(XrXml.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("session", ("session", XrXml.Agent.Tty.Session)), ("throttle", ("throttle", XrXml.Agent.Tty.Throttle))])
                self._leafs = OrderedDict([
                    ('iteration_size', (YLeaf(YType.uint32, 'iteration-size'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('streaming_size', (YLeaf(YType.uint32, 'streaming-size'), ['int'])),
                ])
                self.iteration_size = None
                self.enable = None
                self.streaming_size = None

                self.session = XrXml.Agent.Tty.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"

                self.throttle = XrXml.Agent.Tty.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"
                self._segment_path = lambda: "tty"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(XrXml.Agent.Tty, ['iteration_size', 'enable', 'streaming_size'], name, value)


            class Session(Entity):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\: int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(XrXml.Agent.Tty.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "tty"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ])
                    self.timeout = None
                    self._segment_path = lambda: "session"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/tty/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Tty.Session, ['timeout'], name, value)


            class Throttle(Entity):
                """
                XML agent throttling
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\: int
                
                	**range:** 1000..30000
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\: int
                
                	**range:** 100..1024
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(XrXml.Agent.Tty.Throttle, self).__init__()

                    self.yang_name = "throttle"
                    self.yang_parent_name = "tty"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('process_rate', (YLeaf(YType.uint32, 'process-rate'), ['int'])),
                        ('memory', (YLeaf(YType.uint32, 'memory'), ['int'])),
                    ])
                    self.process_rate = None
                    self.memory = None
                    self._segment_path = lambda: "throttle"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/tty/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Tty.Throttle, ['process_rate', 'memory'], name, value)


        class Ssl(Entity):
            """
            XML SSL agent
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Session>`
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\: int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Throttle>`
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\: int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            .. attribute:: vrfs
            
            	List of VRFs
            	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Vrfs>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(XrXml.Agent.Ssl, self).__init__()

                self.yang_name = "ssl"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("session", ("session", XrXml.Agent.Ssl.Session)), ("throttle", ("throttle", XrXml.Agent.Ssl.Throttle)), ("vrfs", ("vrfs", XrXml.Agent.Ssl.Vrfs))])
                self._leafs = OrderedDict([
                    ('iteration_size', (YLeaf(YType.uint32, 'iteration-size'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('streaming_size', (YLeaf(YType.uint32, 'streaming-size'), ['int'])),
                ])
                self.iteration_size = None
                self.enable = None
                self.streaming_size = None

                self.session = XrXml.Agent.Ssl.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"

                self.throttle = XrXml.Agent.Ssl.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"

                self.vrfs = XrXml.Agent.Ssl.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._segment_path = lambda: "ssl"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(XrXml.Agent.Ssl, ['iteration_size', 'enable', 'streaming_size'], name, value)


            class Session(Entity):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\: int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(XrXml.Agent.Ssl.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "ssl"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ])
                    self.timeout = None
                    self._segment_path = lambda: "session"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/ssl/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Ssl.Session, ['timeout'], name, value)


            class Throttle(Entity):
                """
                XML agent throttling
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\: int
                
                	**range:** 1000..30000
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\: int
                
                	**range:** 100..1024
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(XrXml.Agent.Ssl.Throttle, self).__init__()

                    self.yang_name = "throttle"
                    self.yang_parent_name = "ssl"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('process_rate', (YLeaf(YType.uint32, 'process-rate'), ['int'])),
                        ('memory', (YLeaf(YType.uint32, 'memory'), ['int'])),
                    ])
                    self.process_rate = None
                    self.memory = None
                    self._segment_path = lambda: "throttle"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/ssl/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Ssl.Throttle, ['process_rate', 'memory'], name, value)


            class Vrfs(Entity):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	A specific VRF
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Vrfs.Vrf>`
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(XrXml.Agent.Ssl.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "ssl"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf", ("vrf", XrXml.Agent.Ssl.Vrfs.Vrf))])
                    self._leafs = OrderedDict()

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/ssl/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Ssl.Vrfs, [], name, value)


                class Vrf(Entity):
                    """
                    A specific VRF
                    
                    .. attribute:: vrf_name  (key)
                    
                    	VRF name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	IPv6 Transport Access list for VRF
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv4_access_list
                    
                    	IPv4 Transport Access list for VRF
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: access_list
                    
                    	Access list for XML agent
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: shutdown
                    
                    	Shutdown default VRF. This is applicable only for VRF default
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(XrXml.Agent.Ssl.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('ipv6_access_list', (YLeaf(YType.str, 'ipv6-access-list'), ['str'])),
                            ('ipv4_access_list', (YLeaf(YType.str, 'ipv4-access-list'), ['str'])),
                            ('access_list', (YLeaf(YType.str, 'access-list'), ['str'])),
                            ('shutdown', (YLeaf(YType.empty, 'shutdown'), ['Empty'])),
                        ])
                        self.vrf_name = None
                        self.ipv6_access_list = None
                        self.ipv4_access_list = None
                        self.access_list = None
                        self.shutdown = None
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/ssl/vrfs/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(XrXml.Agent.Ssl.Vrfs.Vrf, ['vrf_name', 'ipv6_access_list', 'ipv4_access_list', 'access_list', 'shutdown'], name, value)

    def clone_ptr(self):
        self._top_entity = XrXml()
        return self._top_entity

class Netconf(Entity):
    """
    netconf
    
    .. attribute:: agent
    
    	XML agent
    	**type**\:  :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Netconf, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("agent", ("agent", Netconf.Agent))])
        self._leafs = OrderedDict()

        self.agent = Netconf.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._segment_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Netconf, [], name, value)


    class Agent(Entity):
        """
        XML agent
        
        .. attribute:: tty
        
        	NETCONF agent over TTY
        	**type**\:  :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Netconf.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "netconf"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tty", ("tty", Netconf.Agent.Tty))])
            self._leafs = OrderedDict()

            self.tty = Netconf.Agent.Tty()
            self.tty.parent = self
            self._children_name_map["tty"] = "tty"
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Netconf.Agent, [], name, value)


        class Tty(Entity):
            """
            NETCONF agent over TTY
            
            .. attribute:: throttle
            
            	NETCONF agent throttling
            	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty.Throttle>`
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty.Session>`
            
            .. attribute:: enable
            
            	Enable specified NETCONF agent
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Netconf.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("throttle", ("throttle", Netconf.Agent.Tty.Throttle)), ("session", ("session", Netconf.Agent.Tty.Session))])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None

                self.throttle = Netconf.Agent.Tty.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"

                self.session = Netconf.Agent.Tty.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._segment_path = lambda: "tty"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Netconf.Agent.Tty, ['enable'], name, value)


            class Throttle(Entity):
                """
                NETCONF agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\: int
                
                	**range:** 100..1024
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: offload_memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\: int
                
                	**range:** 0..12000
                
                	**units**\: megabyte
                
                	**default value**\: 0
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\: int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Netconf.Agent.Tty.Throttle, self).__init__()

                    self.yang_name = "throttle"
                    self.yang_parent_name = "tty"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('memory', (YLeaf(YType.uint32, 'memory'), ['int'])),
                        ('offload_memory', (YLeaf(YType.uint32, 'offload-memory'), ['int'])),
                        ('process_rate', (YLeaf(YType.uint32, 'process-rate'), ['int'])),
                    ])
                    self.memory = None
                    self.offload_memory = None
                    self.process_rate = None
                    self._segment_path = lambda: "throttle"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/agent/tty/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Netconf.Agent.Tty.Throttle, ['memory', 'offload_memory', 'process_rate'], name, value)


            class Session(Entity):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\: int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Netconf.Agent.Tty.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "tty"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ])
                    self.timeout = None
                    self._segment_path = lambda: "session"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/agent/tty/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Netconf.Agent.Tty.Session, ['timeout'], name, value)

    def clone_ptr(self):
        self._top_entity = Netconf()
        return self._top_entity

