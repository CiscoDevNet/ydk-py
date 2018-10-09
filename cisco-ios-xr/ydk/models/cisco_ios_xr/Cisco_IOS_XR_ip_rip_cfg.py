""" Cisco_IOS_XR_ip_rip_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rip package configuration.

This module contains definitions
for the following management objects\:
  rip\: RIP configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BgpRedistRoute(Enum):
    """
    BgpRedistRoute (Enum Class)

    Bgp redist route

    .. data:: all = 0

    	All routes

    .. data:: internal = 512

    	Internal routes only

    .. data:: external = 1024

    	External routes only

    .. data:: local = 2048

    	Local routes only

    """

    all = Enum.YLeaf(0, "all")

    internal = Enum.YLeaf(512, "internal")

    external = Enum.YLeaf(1024, "external")

    local = Enum.YLeaf(2048, "local")


class DefaultInformationOption(Enum):
    """
    DefaultInformationOption (Enum Class)

    Default information option

    .. data:: always = 0

    	Always

    .. data:: policy = 1

    	Use route-policy

    """

    always = Enum.YLeaf(0, "always")

    policy = Enum.YLeaf(1, "policy")


class DefaultRedistRoute(Enum):
    """
    DefaultRedistRoute (Enum Class)

    Default redist route

    .. data:: all = 0

    	All routes

    """

    all = Enum.YLeaf(0, "all")


class IsisRedistRoute(Enum):
    """
    IsisRedistRoute (Enum Class)

    Isis redist route

    .. data:: level1 = 1

    	Level-1 routes only

    .. data:: level2 = 2

    	Level-1 routes only

    .. data:: level1_and2 = 3

    	Level-1 and level-2 routes

    """

    level1 = Enum.YLeaf(1, "level1")

    level2 = Enum.YLeaf(2, "level2")

    level1_and2 = Enum.YLeaf(3, "level1-and2")


class RipAuthMode(Enum):
    """
    RipAuthMode (Enum Class)

    Rip auth mode

    .. data:: text = 2

    	Text mode

    .. data:: md5 = 3

    	MD5 mode

    """

    text = Enum.YLeaf(2, "text")

    md5 = Enum.YLeaf(3, "md5")


class RipExtCommunity(Enum):
    """
    RipExtCommunity (Enum Class)

    Rip ext community

    .. data:: as_ = 0

    	AS:nn format

    .. data:: ipv4_address = 1

    	IPV4Address:nn format

    .. data:: four_byte_as = 2

    	4-byte ASN format

    """

    as_ = Enum.YLeaf(0, "as")

    ipv4_address = Enum.YLeaf(1, "ipv4-address")

    four_byte_as = Enum.YLeaf(2, "four-byte-as")



class Rip(Entity):
    """
    RIP configuration
    
    .. attribute:: default_vrf
    
    	RIP configuration for Default VRF
    	**type**\:  :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf>`
    
    .. attribute:: vrfs
    
    	VRF related RIP configuration
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs>`
    
    

    """

    _prefix = 'ip-rip-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Rip, self).__init__()
        self._top_entity = None

        self.yang_name = "rip"
        self.yang_parent_name = "Cisco-IOS-XR-ip-rip-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("default-vrf", ("default_vrf", Rip.DefaultVrf)), ("vrfs", ("vrfs", Rip.Vrfs))])
        self._leafs = OrderedDict()

        self.default_vrf = Rip.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"

        self.vrfs = Rip.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Rip, [], name, value)


    class DefaultVrf(Entity):
        """
        RIP configuration for Default VRF
        
        .. attribute:: enable
        
        	Starts RIP configuration for Default VRF
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: broadcast_for_v2
        
        	Send RIP v2 output packets to broadcast address
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: distance
        
        	Administrative distance
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 120
        
        .. attribute:: default_information
        
        	Controls default information origination
        	**type**\:  :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.DefaultInformation>`
        
        	**presence node**\: True
        
        .. attribute:: default_metric
        
        	Default metric of redistributed routes
        	**type**\: int
        
        	**range:** 0..16
        
        .. attribute:: output_delay
        
        	Inter\-packet delay for RIP updates
        	**type**\: int
        
        	**range:** 8..50
        
        	**units**\: millisecond
        
        .. attribute:: auto_summary
        
        	Enable automatic network number summarization
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: redistribution
        
        	Redistribute information from another routing protocol
        	**type**\:  :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution>`
        
        .. attribute:: ip_distances
        
        	Table of IP specific administrative distances
        	**type**\:  :py:class:`IpDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.IpDistances>`
        
        .. attribute:: policy_out
        
        	Route Policy for outbound routing updates
        	**type**\: str
        
        .. attribute:: interfaces
        
        	Table of RIP interfaces
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces>`
        
        .. attribute:: neighbors
        
        	Configure RIP Neighbors
        	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Neighbors>`
        
        .. attribute:: validate_source_disable
        
        	Disable validation of source address of routing updates
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: maximum_paths
        
        	Maximum number of paths allowed per route
        	**type**\: int
        
        	**range:** 1..128
        
        	**default value**\: 4
        
        .. attribute:: nsf
        
        	Enable Cisco Non Stop Forwarding
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: policy_in
        
        	Route Policy for inbbound routing updates
        	**type**\: str
        
        .. attribute:: timers
        
        	Various routing timers
        	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Timers>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'ip-rip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "rip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("default-information", ("default_information", Rip.DefaultVrf.DefaultInformation)), ("redistribution", ("redistribution", Rip.DefaultVrf.Redistribution)), ("ip-distances", ("ip_distances", Rip.DefaultVrf.IpDistances)), ("interfaces", ("interfaces", Rip.DefaultVrf.Interfaces)), ("neighbors", ("neighbors", Rip.DefaultVrf.Neighbors)), ("timers", ("timers", Rip.DefaultVrf.Timers))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ('broadcast_for_v2', (YLeaf(YType.empty, 'broadcast-for-v2'), ['Empty'])),
                ('distance', (YLeaf(YType.uint32, 'distance'), ['int'])),
                ('default_metric', (YLeaf(YType.uint32, 'default-metric'), ['int'])),
                ('output_delay', (YLeaf(YType.uint32, 'output-delay'), ['int'])),
                ('auto_summary', (YLeaf(YType.empty, 'auto-summary'), ['Empty'])),
                ('policy_out', (YLeaf(YType.str, 'policy-out'), ['str'])),
                ('validate_source_disable', (YLeaf(YType.empty, 'validate-source-disable'), ['Empty'])),
                ('maximum_paths', (YLeaf(YType.uint32, 'maximum-paths'), ['int'])),
                ('nsf', (YLeaf(YType.empty, 'nsf'), ['Empty'])),
                ('policy_in', (YLeaf(YType.str, 'policy-in'), ['str'])),
            ])
            self.enable = None
            self.broadcast_for_v2 = None
            self.distance = None
            self.default_metric = None
            self.output_delay = None
            self.auto_summary = None
            self.policy_out = None
            self.validate_source_disable = None
            self.maximum_paths = None
            self.nsf = None
            self.policy_in = None

            self.default_information = None
            self._children_name_map["default_information"] = "default-information"

            self.redistribution = Rip.DefaultVrf.Redistribution()
            self.redistribution.parent = self
            self._children_name_map["redistribution"] = "redistribution"

            self.ip_distances = Rip.DefaultVrf.IpDistances()
            self.ip_distances.parent = self
            self._children_name_map["ip_distances"] = "ip-distances"

            self.interfaces = Rip.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"

            self.neighbors = Rip.DefaultVrf.Neighbors()
            self.neighbors.parent = self
            self._children_name_map["neighbors"] = "neighbors"

            self.timers = None
            self._children_name_map["timers"] = "timers"
            self._segment_path = lambda: "default-vrf"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Rip.DefaultVrf, ['enable', 'broadcast_for_v2', 'distance', 'default_metric', 'output_delay', 'auto_summary', 'policy_out', 'validate_source_disable', 'maximum_paths', 'nsf', 'policy_in'], name, value)


        class DefaultInformation(Entity):
            """
            Controls default information origination
            
            .. attribute:: route_policy_name
            
            	Route policy name
            	**type**\: str
            
            .. attribute:: option
            
            	Origination option
            	**type**\:  :py:class:`DefaultInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultInformationOption>`
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.DefaultInformation, self).__init__()

                self.yang_name = "default-information"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                    ('option', (YLeaf(YType.enumeration, 'option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultInformationOption', '')])),
                ])
                self.route_policy_name = None
                self.option = None
                self._segment_path = lambda: "default-information"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.DefaultInformation, ['route_policy_name', 'option'], name, value)


        class Redistribution(Entity):
            """
            Redistribute information from another routing
            protocol
            
            .. attribute:: connected
            
            	Redistribute connected routes
            	**type**\:  :py:class:`Connected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Connected>`
            
            	**presence node**\: True
            
            .. attribute:: bgps
            
            	Redistribute BGP routes
            	**type**\:  :py:class:`Bgps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Bgps>`
            
            .. attribute:: isises
            
            	Redistribute IS\-IS routes
            	**type**\:  :py:class:`Isises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Isises>`
            
            .. attribute:: eigrp_s
            
            	Redistribute EIGRP routes
            	**type**\:  :py:class:`EigrpS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.EigrpS>`
            
            .. attribute:: static
            
            	Redistribute static routes
            	**type**\:  :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Static>`
            
            	**presence node**\: True
            
            .. attribute:: ospfs
            
            	Redistribute OSPF routes
            	**type**\:  :py:class:`Ospfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Ospfs>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Redistribution, self).__init__()

                self.yang_name = "redistribution"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("connected", ("connected", Rip.DefaultVrf.Redistribution.Connected)), ("bgps", ("bgps", Rip.DefaultVrf.Redistribution.Bgps)), ("isises", ("isises", Rip.DefaultVrf.Redistribution.Isises)), ("eigrp-s", ("eigrp_s", Rip.DefaultVrf.Redistribution.EigrpS)), ("static", ("static", Rip.DefaultVrf.Redistribution.Static)), ("ospfs", ("ospfs", Rip.DefaultVrf.Redistribution.Ospfs))])
                self._leafs = OrderedDict()

                self.connected = None
                self._children_name_map["connected"] = "connected"

                self.bgps = Rip.DefaultVrf.Redistribution.Bgps()
                self.bgps.parent = self
                self._children_name_map["bgps"] = "bgps"

                self.isises = Rip.DefaultVrf.Redistribution.Isises()
                self.isises.parent = self
                self._children_name_map["isises"] = "isises"

                self.eigrp_s = Rip.DefaultVrf.Redistribution.EigrpS()
                self.eigrp_s.parent = self
                self._children_name_map["eigrp_s"] = "eigrp-s"

                self.static = None
                self._children_name_map["static"] = "static"

                self.ospfs = Rip.DefaultVrf.Redistribution.Ospfs()
                self.ospfs.parent = self
                self._children_name_map["ospfs"] = "ospfs"
                self._segment_path = lambda: "redistribution"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Redistribution, [], name, value)


            class Connected(Entity):
                """
                Redistribute connected routes
                
                .. attribute:: route_policy_name
                
                	Route Policy name
                	**type**\: str
                
                .. attribute:: route_type
                
                	Route type
                	**type**\:  :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Connected, self).__init__()

                    self.yang_name = "connected"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                        ('route_type', (YLeaf(YType.enumeration, 'route-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRoute', '')])),
                    ])
                    self.route_policy_name = None
                    self.route_type = None
                    self._segment_path = lambda: "connected"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Connected, ['route_policy_name', 'route_type'], name, value)


            class Bgps(Entity):
                """
                Redistribute BGP routes
                
                .. attribute:: bgp
                
                	Autonomous system number
                	**type**\: list of  		 :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Bgps.Bgp>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Bgps, self).__init__()

                    self.yang_name = "bgps"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bgp", ("bgp", Rip.DefaultVrf.Redistribution.Bgps.Bgp))])
                    self._leafs = OrderedDict()

                    self.bgp = YList(self)
                    self._segment_path = lambda: "bgps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Bgps, [], name, value)


                class Bgp(Entity):
                    """
                    Autonomous system number
                    
                    .. attribute:: asnxx  (key)
                    
                    	Higher 16 bits of 4\-byte BGP AS number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: asnyy  (key)
                    
                    	2\-byte or 4\-byte BGP AS number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: policy
                    
                    	Route Policy name
                    	**type**\: str
                    
                    .. attribute:: type
                    
                    	Route type
                    	**type**\:  :py:class:`BgpRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.BgpRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Bgps.Bgp, self).__init__()

                        self.yang_name = "bgp"
                        self.yang_parent_name = "bgps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['asnxx','asnyy']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('asnxx', (YLeaf(YType.uint32, 'asnxx'), ['int'])),
                            ('asnyy', (YLeaf(YType.uint32, 'asnyy'), ['int'])),
                            ('policy', (YLeaf(YType.str, 'policy'), ['str'])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'BgpRedistRoute', '')])),
                        ])
                        self.asnxx = None
                        self.asnyy = None
                        self.policy = None
                        self.type = None
                        self._segment_path = lambda: "bgp" + "[asnxx='" + str(self.asnxx) + "']" + "[asnyy='" + str(self.asnyy) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/bgps/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Redistribution.Bgps.Bgp, ['asnxx', 'asnyy', 'policy', 'type'], name, value)


            class Isises(Entity):
                """
                Redistribute IS\-IS routes
                
                .. attribute:: isis
                
                	Redistribute IS\-IS routes
                	**type**\: list of  		 :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Isises.Isis>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Isises, self).__init__()

                    self.yang_name = "isises"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("isis", ("isis", Rip.DefaultVrf.Redistribution.Isises.Isis))])
                    self._leafs = OrderedDict()

                    self.isis = YList(self)
                    self._segment_path = lambda: "isises"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Isises, [], name, value)


                class Isis(Entity):
                    """
                    Redistribute IS\-IS routes
                    
                    .. attribute:: isis_name  (key)
                    
                    	IS\-IS instance name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\: str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:  :py:class:`IsisRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.IsisRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Isises.Isis, self).__init__()

                        self.yang_name = "isis"
                        self.yang_parent_name = "isises"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['isis_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('isis_name', (YLeaf(YType.str, 'isis-name'), ['str'])),
                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                            ('route_type', (YLeaf(YType.enumeration, 'route-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'IsisRedistRoute', '')])),
                        ])
                        self.isis_name = None
                        self.route_policy_name = None
                        self.route_type = None
                        self._segment_path = lambda: "isis" + "[isis-name='" + str(self.isis_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/isises/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Redistribution.Isises.Isis, ['isis_name', 'route_policy_name', 'route_type'], name, value)


            class EigrpS(Entity):
                """
                Redistribute EIGRP routes
                
                .. attribute:: eigrp
                
                	Redistribute EIGRP routes
                	**type**\: list of  		 :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.EigrpS.Eigrp>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.EigrpS, self).__init__()

                    self.yang_name = "eigrp-s"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("eigrp", ("eigrp", Rip.DefaultVrf.Redistribution.EigrpS.Eigrp))])
                    self._leafs = OrderedDict()

                    self.eigrp = YList(self)
                    self._segment_path = lambda: "eigrp-s"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.EigrpS, [], name, value)


                class Eigrp(Entity):
                    """
                    Redistribute EIGRP routes
                    
                    .. attribute:: as_  (key)
                    
                    	Autonomous system number
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\: str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:  :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.EigrpS.Eigrp, self).__init__()

                        self.yang_name = "eigrp"
                        self.yang_parent_name = "eigrp-s"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['as_']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                            ('route_type', (YLeaf(YType.enumeration, 'route-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRoute', '')])),
                        ])
                        self.as_ = None
                        self.route_policy_name = None
                        self.route_type = None
                        self._segment_path = lambda: "eigrp" + "[as='" + str(self.as_) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/eigrp-s/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Redistribution.EigrpS.Eigrp, ['as_', 'route_policy_name', 'route_type'], name, value)


            class Static(Entity):
                """
                Redistribute static routes
                
                .. attribute:: route_policy_name
                
                	Route Policy name
                	**type**\: str
                
                .. attribute:: route_type
                
                	Route type
                	**type**\:  :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Static, self).__init__()

                    self.yang_name = "static"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                        ('route_type', (YLeaf(YType.enumeration, 'route-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRoute', '')])),
                    ])
                    self.route_policy_name = None
                    self.route_type = None
                    self._segment_path = lambda: "static"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Static, ['route_policy_name', 'route_type'], name, value)


            class Ospfs(Entity):
                """
                Redistribute OSPF routes
                
                .. attribute:: ospf
                
                	Redistribute OSPF routes
                	**type**\: list of  		 :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Ospfs.Ospf>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Ospfs, self).__init__()

                    self.yang_name = "ospfs"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospf", ("ospf", Rip.DefaultVrf.Redistribution.Ospfs.Ospf))])
                    self._leafs = OrderedDict()

                    self.ospf = YList(self)
                    self._segment_path = lambda: "ospfs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Ospfs, [], name, value)


                class Ospf(Entity):
                    """
                    Redistribute OSPF routes
                    
                    .. attribute:: ospf_name  (key)
                    
                    	Process ID for the OSPF instance
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\: str
                    
                    .. attribute:: internal
                    
                    	Internal routes
                    	**type**\: bool
                    
                    .. attribute:: external
                    
                    	External routes
                    	**type**\: bool
                    
                    .. attribute:: external_type
                    
                    	External route type
                    	**type**\: int
                    
                    	**range:** 0..2
                    
                    .. attribute:: nssa_external
                    
                    	NSSA External routes
                    	**type**\: bool
                    
                    .. attribute:: nssa_external_type
                    
                    	NSSA External route type
                    	**type**\: int
                    
                    	**range:** 0..2
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Ospfs.Ospf, self).__init__()

                        self.yang_name = "ospf"
                        self.yang_parent_name = "ospfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['ospf_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ospf_name', (YLeaf(YType.str, 'ospf-name'), ['str'])),
                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                            ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                            ('external', (YLeaf(YType.boolean, 'external'), ['bool'])),
                            ('external_type', (YLeaf(YType.uint32, 'external-type'), ['int'])),
                            ('nssa_external', (YLeaf(YType.boolean, 'nssa-external'), ['bool'])),
                            ('nssa_external_type', (YLeaf(YType.uint32, 'nssa-external-type'), ['int'])),
                        ])
                        self.ospf_name = None
                        self.route_policy_name = None
                        self.internal = None
                        self.external = None
                        self.external_type = None
                        self.nssa_external = None
                        self.nssa_external_type = None
                        self._segment_path = lambda: "ospf" + "[ospf-name='" + str(self.ospf_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/ospfs/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Redistribution.Ospfs.Ospf, ['ospf_name', 'route_policy_name', 'internal', 'external', 'external_type', 'nssa_external', 'nssa_external_type'], name, value)


        class IpDistances(Entity):
            """
            Table of IP specific administrative distances
            
            .. attribute:: ip_distance
            
            	IP specific administrative distance
            	**type**\: list of  		 :py:class:`IpDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.IpDistances.IpDistance>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.IpDistances, self).__init__()

                self.yang_name = "ip-distances"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ip-distance", ("ip_distance", Rip.DefaultVrf.IpDistances.IpDistance))])
                self._leafs = OrderedDict()

                self.ip_distance = YList(self)
                self._segment_path = lambda: "ip-distances"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.IpDistances, [], name, value)


            class IpDistance(Entity):
                """
                IP specific administrative distance
                
                .. attribute:: address  (key)
                
                	IP Source address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: netmask  (key)
                
                	IP address mask
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: distance
                
                	Administrative distance
                	**type**\: int
                
                	**range:** 0..255
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.IpDistances.IpDistance, self).__init__()

                    self.yang_name = "ip-distance"
                    self.yang_parent_name = "ip-distances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['address','netmask']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ('netmask', (YLeaf(YType.str, 'netmask'), ['str'])),
                        ('distance', (YLeaf(YType.uint32, 'distance'), ['int'])),
                    ])
                    self.address = None
                    self.netmask = None
                    self.distance = None
                    self._segment_path = lambda: "ip-distance" + "[address='" + str(self.address) + "']" + "[netmask='" + str(self.netmask) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/ip-distances/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.IpDistances.IpDistance, ['address', 'netmask', 'distance'], name, value)


        class Interfaces(Entity):
            """
            Table of RIP interfaces
            
            .. attribute:: interface
            
            	RIP interface name
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Rip.DefaultVrf.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Interfaces, [], name, value)


            class Interface(Entity):
                """
                RIP interface name
                
                .. attribute:: interface_name  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: authentication
                
                	Authentication keychain and mode
                	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.Authentication>`
                
                	**presence node**\: True
                
                .. attribute:: site_of_origin
                
                	SOO community for prefixes learned over this interface
                	**type**\:  :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin>`
                
                .. attribute:: receive_version
                
                	RIP versions supported for receiving advertisements
                	**type**\:  :py:class:`ReceiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion>`
                
                .. attribute:: send_version
                
                	RIP versions supported for sending advertisements
                	**type**\:  :py:class:`SendVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.SendVersion>`
                
                .. attribute:: broadcast_for_v2
                
                	Send RIP v2 output packets to broadcast address
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: poison_reverse
                
                	Enable poison reverse
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: passive
                
                	Suppress routing updates on this interface
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	Starts RIP interface configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: policy_out
                
                	Route Policy for outbound routing updates
                	**type**\: str
                
                .. attribute:: accept_metric_zero
                
                	Accept RIP updates with metric 0
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: policy_in
                
                	Route Policy for inbound routing updates
                	**type**\: str
                
                .. attribute:: split_horizon_disable
                
                	Disable split horizon
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([("authentication", ("authentication", Rip.DefaultVrf.Interfaces.Interface.Authentication)), ("site-of-origin", ("site_of_origin", Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin)), ("receive-version", ("receive_version", Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion)), ("send-version", ("send_version", Rip.DefaultVrf.Interfaces.Interface.SendVersion))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('broadcast_for_v2', (YLeaf(YType.empty, 'broadcast-for-v2'), ['Empty'])),
                        ('poison_reverse', (YLeaf(YType.empty, 'poison-reverse'), ['Empty'])),
                        ('passive', (YLeaf(YType.empty, 'passive'), ['Empty'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('policy_out', (YLeaf(YType.str, 'policy-out'), ['str'])),
                        ('accept_metric_zero', (YLeaf(YType.empty, 'accept-metric-zero'), ['Empty'])),
                        ('policy_in', (YLeaf(YType.str, 'policy-in'), ['str'])),
                        ('split_horizon_disable', (YLeaf(YType.empty, 'split-horizon-disable'), ['Empty'])),
                    ])
                    self.interface_name = None
                    self.broadcast_for_v2 = None
                    self.poison_reverse = None
                    self.passive = None
                    self.enable = None
                    self.policy_out = None
                    self.accept_metric_zero = None
                    self.policy_in = None
                    self.split_horizon_disable = None

                    self.authentication = None
                    self._children_name_map["authentication"] = "authentication"

                    self.site_of_origin = Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin()
                    self.site_of_origin.parent = self
                    self._children_name_map["site_of_origin"] = "site-of-origin"

                    self.receive_version = Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion()
                    self.receive_version.parent = self
                    self._children_name_map["receive_version"] = "receive-version"

                    self.send_version = Rip.DefaultVrf.Interfaces.Interface.SendVersion()
                    self.send_version.parent = self
                    self._children_name_map["send_version"] = "send-version"
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface, ['interface_name', 'broadcast_for_v2', 'poison_reverse', 'passive', 'enable', 'policy_out', 'accept_metric_zero', 'policy_in', 'split_horizon_disable'], name, value)


                class Authentication(Entity):
                    """
                    Authentication keychain and mode
                    
                    .. attribute:: keychain
                    
                    	Name of keychain
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mode
                    
                    	Authentication mode
                    	**type**\:  :py:class:`RipAuthMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipAuthMode>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('keychain', (YLeaf(YType.str, 'keychain'), ['str'])),
                            ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'RipAuthMode', '')])),
                        ])
                        self.keychain = None
                        self.mode = None
                        self._segment_path = lambda: "authentication"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.Authentication, ['keychain', 'mode'], name, value)


                class SiteOfOrigin(Entity):
                    """
                    SOO community for prefixes learned over this
                    interface
                    
                    .. attribute:: type
                    
                    	Extended community type
                    	**type**\:  :py:class:`RipExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipExtCommunity>`
                    
                    .. attribute:: as_xx
                    
                    	AS Number for AS\:nn format
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: as_yy
                    
                    	32 bit value for AS\:nn format
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: as_index
                    
                    	AS Number Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address
                    
                    	IPV4 address for IPV4Address\:nn format
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: address_index
                    
                    	16bit value for IPV4Address\:nn format
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin, self).__init__()

                        self.yang_name = "site-of-origin"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'RipExtCommunity', '')])),
                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                            ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                            ('as_index', (YLeaf(YType.uint32, 'as-index'), ['int'])),
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                        ])
                        self.type = None
                        self.as_xx = None
                        self.as_yy = None
                        self.as_index = None
                        self.address = None
                        self.address_index = None
                        self._segment_path = lambda: "site-of-origin"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin, ['type', 'as_xx', 'as_yy', 'as_index', 'address', 'address_index'], name, value)


                class ReceiveVersion(Entity):
                    """
                    RIP versions supported for receiving
                    advertisements
                    
                    .. attribute:: version1
                    
                    	Support RIP version 1
                    	**type**\: bool
                    
                    .. attribute:: version2
                    
                    	Support RIP version 2
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion, self).__init__()

                        self.yang_name = "receive-version"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('version1', (YLeaf(YType.boolean, 'version1'), ['bool'])),
                            ('version2', (YLeaf(YType.boolean, 'version2'), ['bool'])),
                        ])
                        self.version1 = None
                        self.version2 = None
                        self._segment_path = lambda: "receive-version"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion, ['version1', 'version2'], name, value)


                class SendVersion(Entity):
                    """
                    RIP versions supported for sending
                    advertisements
                    
                    .. attribute:: version1
                    
                    	Support RIP version 1
                    	**type**\: bool
                    
                    .. attribute:: version2
                    
                    	Support RIP version 2
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.SendVersion, self).__init__()

                        self.yang_name = "send-version"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('version1', (YLeaf(YType.boolean, 'version1'), ['bool'])),
                            ('version2', (YLeaf(YType.boolean, 'version2'), ['bool'])),
                        ])
                        self.version1 = None
                        self.version2 = None
                        self._segment_path = lambda: "send-version"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.SendVersion, ['version1', 'version2'], name, value)


        class Neighbors(Entity):
            """
            Configure RIP Neighbors
            
            .. attribute:: neighbor
            
            	Neighbor address
            	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Neighbors.Neighbor>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Neighbors, self).__init__()

                self.yang_name = "neighbors"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("neighbor", ("neighbor", Rip.DefaultVrf.Neighbors.Neighbor))])
                self._leafs = OrderedDict()

                self.neighbor = YList(self)
                self._segment_path = lambda: "neighbors"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Neighbors, [], name, value)


            class Neighbor(Entity):
                """
                Neighbor address
                
                .. attribute:: neighbor_address  (key)
                
                	IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Neighbors.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "neighbors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['neighbor_address']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                    ])
                    self.neighbor_address = None
                    self._segment_path = lambda: "neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/neighbors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Neighbors.Neighbor, ['neighbor_address'], name, value)


        class Timers(Entity):
            """
            Various routing timers
            
            .. attribute:: update_timer
            
            	Interval between updates
            	**type**\: int
            
            	**range:** 5..50000
            
            	**mandatory**\: True
            
            .. attribute:: invalid_timer
            
            	Invalid
            	**type**\: int
            
            	**range:** 15..200000
            
            	**mandatory**\: True
            
            .. attribute:: holddown_timer
            
            	Holddown
            	**type**\: int
            
            	**range:** 15..200000
            
            	**mandatory**\: True
            
            .. attribute:: flush_timer
            
            	Flush
            	**type**\: int
            
            	**range:** 16..250000
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Timers, self).__init__()

                self.yang_name = "timers"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                    ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                    ('holddown_timer', (YLeaf(YType.uint32, 'holddown-timer'), ['int'])),
                    ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                ])
                self.update_timer = None
                self.invalid_timer = None
                self.holddown_timer = None
                self.flush_timer = None
                self._segment_path = lambda: "timers"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Timers, ['update_timer', 'invalid_timer', 'holddown_timer', 'flush_timer'], name, value)


    class Vrfs(Entity):
        """
        VRF related RIP configuration
        
        .. attribute:: vrf
        
        	RIP configuration for a particular VRF
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-rip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "rip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Rip.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Rip.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            RIP configuration for a particular VRF
            
            .. attribute:: vrf_name  (key)
            
            	VRF Name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: enable
            
            	Starts RIP configuration for a particular VRF
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: broadcast_for_v2
            
            	Send RIP v2 output packets to broadcast address
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: distance
            
            	Administrative distance
            	**type**\: int
            
            	**range:** 0..255
            
            	**default value**\: 120
            
            .. attribute:: default_information
            
            	Controls default information origination
            	**type**\:  :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.DefaultInformation>`
            
            	**presence node**\: True
            
            .. attribute:: default_metric
            
            	Default metric of redistributed routes
            	**type**\: int
            
            	**range:** 0..16
            
            .. attribute:: output_delay
            
            	Inter\-packet delay for RIP updates
            	**type**\: int
            
            	**range:** 8..50
            
            	**units**\: millisecond
            
            .. attribute:: auto_summary
            
            	Enable automatic network number summarization
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redistribution
            
            	Redistribute information from another routing protocol
            	**type**\:  :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution>`
            
            .. attribute:: ip_distances
            
            	Table of IP specific administrative distances
            	**type**\:  :py:class:`IpDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.IpDistances>`
            
            .. attribute:: policy_out
            
            	Route Policy for outbound routing updates
            	**type**\: str
            
            .. attribute:: interfaces
            
            	Table of RIP interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: neighbors
            
            	Configure RIP Neighbors
            	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Neighbors>`
            
            .. attribute:: validate_source_disable
            
            	Disable validation of source address of routing updates
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum_paths
            
            	Maximum number of paths allowed per route
            	**type**\: int
            
            	**range:** 1..128
            
            	**default value**\: 4
            
            .. attribute:: nsf
            
            	Enable Cisco Non Stop Forwarding
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: policy_in
            
            	Route Policy for inbbound routing updates
            	**type**\: str
            
            .. attribute:: timers
            
            	Various routing timers
            	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Timers>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("default-information", ("default_information", Rip.Vrfs.Vrf.DefaultInformation)), ("redistribution", ("redistribution", Rip.Vrfs.Vrf.Redistribution)), ("ip-distances", ("ip_distances", Rip.Vrfs.Vrf.IpDistances)), ("interfaces", ("interfaces", Rip.Vrfs.Vrf.Interfaces)), ("neighbors", ("neighbors", Rip.Vrfs.Vrf.Neighbors)), ("timers", ("timers", Rip.Vrfs.Vrf.Timers))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('broadcast_for_v2', (YLeaf(YType.empty, 'broadcast-for-v2'), ['Empty'])),
                    ('distance', (YLeaf(YType.uint32, 'distance'), ['int'])),
                    ('default_metric', (YLeaf(YType.uint32, 'default-metric'), ['int'])),
                    ('output_delay', (YLeaf(YType.uint32, 'output-delay'), ['int'])),
                    ('auto_summary', (YLeaf(YType.empty, 'auto-summary'), ['Empty'])),
                    ('policy_out', (YLeaf(YType.str, 'policy-out'), ['str'])),
                    ('validate_source_disable', (YLeaf(YType.empty, 'validate-source-disable'), ['Empty'])),
                    ('maximum_paths', (YLeaf(YType.uint32, 'maximum-paths'), ['int'])),
                    ('nsf', (YLeaf(YType.empty, 'nsf'), ['Empty'])),
                    ('policy_in', (YLeaf(YType.str, 'policy-in'), ['str'])),
                ])
                self.vrf_name = None
                self.enable = None
                self.broadcast_for_v2 = None
                self.distance = None
                self.default_metric = None
                self.output_delay = None
                self.auto_summary = None
                self.policy_out = None
                self.validate_source_disable = None
                self.maximum_paths = None
                self.nsf = None
                self.policy_in = None

                self.default_information = None
                self._children_name_map["default_information"] = "default-information"

                self.redistribution = Rip.Vrfs.Vrf.Redistribution()
                self.redistribution.parent = self
                self._children_name_map["redistribution"] = "redistribution"

                self.ip_distances = Rip.Vrfs.Vrf.IpDistances()
                self.ip_distances.parent = self
                self._children_name_map["ip_distances"] = "ip-distances"

                self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.neighbors = Rip.Vrfs.Vrf.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"

                self.timers = None
                self._children_name_map["timers"] = "timers"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.Vrfs.Vrf, ['vrf_name', 'enable', 'broadcast_for_v2', 'distance', 'default_metric', 'output_delay', 'auto_summary', 'policy_out', 'validate_source_disable', 'maximum_paths', 'nsf', 'policy_in'], name, value)


            class DefaultInformation(Entity):
                """
                Controls default information origination
                
                .. attribute:: route_policy_name
                
                	Route policy name
                	**type**\: str
                
                .. attribute:: option
                
                	Origination option
                	**type**\:  :py:class:`DefaultInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultInformationOption>`
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.DefaultInformation, self).__init__()

                    self.yang_name = "default-information"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                        ('option', (YLeaf(YType.enumeration, 'option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultInformationOption', '')])),
                    ])
                    self.route_policy_name = None
                    self.option = None
                    self._segment_path = lambda: "default-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.DefaultInformation, ['route_policy_name', 'option'], name, value)


            class Redistribution(Entity):
                """
                Redistribute information from another routing
                protocol
                
                .. attribute:: connected
                
                	Redistribute connected routes
                	**type**\:  :py:class:`Connected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Connected>`
                
                	**presence node**\: True
                
                .. attribute:: bgps
                
                	Redistribute BGP routes
                	**type**\:  :py:class:`Bgps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Bgps>`
                
                .. attribute:: isises
                
                	Redistribute IS\-IS routes
                	**type**\:  :py:class:`Isises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Isises>`
                
                .. attribute:: eigrp_s
                
                	Redistribute EIGRP routes
                	**type**\:  :py:class:`EigrpS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.EigrpS>`
                
                .. attribute:: static
                
                	Redistribute static routes
                	**type**\:  :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Static>`
                
                	**presence node**\: True
                
                .. attribute:: ospfs
                
                	Redistribute OSPF routes
                	**type**\:  :py:class:`Ospfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Ospfs>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Redistribution, self).__init__()

                    self.yang_name = "redistribution"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("connected", ("connected", Rip.Vrfs.Vrf.Redistribution.Connected)), ("bgps", ("bgps", Rip.Vrfs.Vrf.Redistribution.Bgps)), ("isises", ("isises", Rip.Vrfs.Vrf.Redistribution.Isises)), ("eigrp-s", ("eigrp_s", Rip.Vrfs.Vrf.Redistribution.EigrpS)), ("static", ("static", Rip.Vrfs.Vrf.Redistribution.Static)), ("ospfs", ("ospfs", Rip.Vrfs.Vrf.Redistribution.Ospfs))])
                    self._leafs = OrderedDict()

                    self.connected = None
                    self._children_name_map["connected"] = "connected"

                    self.bgps = Rip.Vrfs.Vrf.Redistribution.Bgps()
                    self.bgps.parent = self
                    self._children_name_map["bgps"] = "bgps"

                    self.isises = Rip.Vrfs.Vrf.Redistribution.Isises()
                    self.isises.parent = self
                    self._children_name_map["isises"] = "isises"

                    self.eigrp_s = Rip.Vrfs.Vrf.Redistribution.EigrpS()
                    self.eigrp_s.parent = self
                    self._children_name_map["eigrp_s"] = "eigrp-s"

                    self.static = None
                    self._children_name_map["static"] = "static"

                    self.ospfs = Rip.Vrfs.Vrf.Redistribution.Ospfs()
                    self.ospfs.parent = self
                    self._children_name_map["ospfs"] = "ospfs"
                    self._segment_path = lambda: "redistribution"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Redistribution, [], name, value)


                class Connected(Entity):
                    """
                    Redistribute connected routes
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\: str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:  :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Connected, self).__init__()

                        self.yang_name = "connected"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                            ('route_type', (YLeaf(YType.enumeration, 'route-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRoute', '')])),
                        ])
                        self.route_policy_name = None
                        self.route_type = None
                        self._segment_path = lambda: "connected"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Connected, ['route_policy_name', 'route_type'], name, value)


                class Bgps(Entity):
                    """
                    Redistribute BGP routes
                    
                    .. attribute:: bgp
                    
                    	Autonomous system number
                    	**type**\: list of  		 :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Bgps, self).__init__()

                        self.yang_name = "bgps"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("bgp", ("bgp", Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp))])
                        self._leafs = OrderedDict()

                        self.bgp = YList(self)
                        self._segment_path = lambda: "bgps"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Bgps, [], name, value)


                    class Bgp(Entity):
                        """
                        Autonomous system number
                        
                        .. attribute:: asnxx  (key)
                        
                        	Higher 16 bits of 4\-byte BGP AS number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: asnyy  (key)
                        
                        	2\-byte or 4\-byte BGP AS number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policy
                        
                        	Route Policy name
                        	**type**\: str
                        
                        .. attribute:: type
                        
                        	Route type
                        	**type**\:  :py:class:`BgpRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.BgpRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp, self).__init__()

                            self.yang_name = "bgp"
                            self.yang_parent_name = "bgps"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['asnxx','asnyy']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('asnxx', (YLeaf(YType.uint32, 'asnxx'), ['int'])),
                                ('asnyy', (YLeaf(YType.uint32, 'asnyy'), ['int'])),
                                ('policy', (YLeaf(YType.str, 'policy'), ['str'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'BgpRedistRoute', '')])),
                            ])
                            self.asnxx = None
                            self.asnyy = None
                            self.policy = None
                            self.type = None
                            self._segment_path = lambda: "bgp" + "[asnxx='" + str(self.asnxx) + "']" + "[asnyy='" + str(self.asnyy) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp, ['asnxx', 'asnyy', 'policy', 'type'], name, value)


                class Isises(Entity):
                    """
                    Redistribute IS\-IS routes
                    
                    .. attribute:: isis
                    
                    	Redistribute IS\-IS routes
                    	**type**\: list of  		 :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Isises.Isis>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Isises, self).__init__()

                        self.yang_name = "isises"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("isis", ("isis", Rip.Vrfs.Vrf.Redistribution.Isises.Isis))])
                        self._leafs = OrderedDict()

                        self.isis = YList(self)
                        self._segment_path = lambda: "isises"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Isises, [], name, value)


                    class Isis(Entity):
                        """
                        Redistribute IS\-IS routes
                        
                        .. attribute:: isis_name  (key)
                        
                        	IS\-IS instance name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\: str
                        
                        .. attribute:: route_type
                        
                        	Route type
                        	**type**\:  :py:class:`IsisRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.IsisRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Isises.Isis, self).__init__()

                            self.yang_name = "isis"
                            self.yang_parent_name = "isises"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['isis_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('isis_name', (YLeaf(YType.str, 'isis-name'), ['str'])),
                                ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                ('route_type', (YLeaf(YType.enumeration, 'route-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'IsisRedistRoute', '')])),
                            ])
                            self.isis_name = None
                            self.route_policy_name = None
                            self.route_type = None
                            self._segment_path = lambda: "isis" + "[isis-name='" + str(self.isis_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Isises.Isis, ['isis_name', 'route_policy_name', 'route_type'], name, value)


                class EigrpS(Entity):
                    """
                    Redistribute EIGRP routes
                    
                    .. attribute:: eigrp
                    
                    	Redistribute EIGRP routes
                    	**type**\: list of  		 :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.EigrpS, self).__init__()

                        self.yang_name = "eigrp-s"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("eigrp", ("eigrp", Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp))])
                        self._leafs = OrderedDict()

                        self.eigrp = YList(self)
                        self._segment_path = lambda: "eigrp-s"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.EigrpS, [], name, value)


                    class Eigrp(Entity):
                        """
                        Redistribute EIGRP routes
                        
                        .. attribute:: as_  (key)
                        
                        	Autonomous system number
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\: str
                        
                        .. attribute:: route_type
                        
                        	Route type
                        	**type**\:  :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp, self).__init__()

                            self.yang_name = "eigrp"
                            self.yang_parent_name = "eigrp-s"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['as_']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                ('route_type', (YLeaf(YType.enumeration, 'route-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRoute', '')])),
                            ])
                            self.as_ = None
                            self.route_policy_name = None
                            self.route_type = None
                            self._segment_path = lambda: "eigrp" + "[as='" + str(self.as_) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp, ['as_', 'route_policy_name', 'route_type'], name, value)


                class Static(Entity):
                    """
                    Redistribute static routes
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\: str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:  :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Static, self).__init__()

                        self.yang_name = "static"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                            ('route_type', (YLeaf(YType.enumeration, 'route-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRoute', '')])),
                        ])
                        self.route_policy_name = None
                        self.route_type = None
                        self._segment_path = lambda: "static"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Static, ['route_policy_name', 'route_type'], name, value)


                class Ospfs(Entity):
                    """
                    Redistribute OSPF routes
                    
                    .. attribute:: ospf
                    
                    	Redistribute OSPF routes
                    	**type**\: list of  		 :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Ospfs, self).__init__()

                        self.yang_name = "ospfs"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ospf", ("ospf", Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf))])
                        self._leafs = OrderedDict()

                        self.ospf = YList(self)
                        self._segment_path = lambda: "ospfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Ospfs, [], name, value)


                    class Ospf(Entity):
                        """
                        Redistribute OSPF routes
                        
                        .. attribute:: ospf_name  (key)
                        
                        	Process ID for the OSPF instance
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\: str
                        
                        .. attribute:: internal
                        
                        	Internal routes
                        	**type**\: bool
                        
                        .. attribute:: external
                        
                        	External routes
                        	**type**\: bool
                        
                        .. attribute:: external_type
                        
                        	External route type
                        	**type**\: int
                        
                        	**range:** 0..2
                        
                        .. attribute:: nssa_external
                        
                        	NSSA External routes
                        	**type**\: bool
                        
                        .. attribute:: nssa_external_type
                        
                        	NSSA External route type
                        	**type**\: int
                        
                        	**range:** 0..2
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf, self).__init__()

                            self.yang_name = "ospf"
                            self.yang_parent_name = "ospfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ospf_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ospf_name', (YLeaf(YType.str, 'ospf-name'), ['str'])),
                                ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                ('external', (YLeaf(YType.boolean, 'external'), ['bool'])),
                                ('external_type', (YLeaf(YType.uint32, 'external-type'), ['int'])),
                                ('nssa_external', (YLeaf(YType.boolean, 'nssa-external'), ['bool'])),
                                ('nssa_external_type', (YLeaf(YType.uint32, 'nssa-external-type'), ['int'])),
                            ])
                            self.ospf_name = None
                            self.route_policy_name = None
                            self.internal = None
                            self.external = None
                            self.external_type = None
                            self.nssa_external = None
                            self.nssa_external_type = None
                            self._segment_path = lambda: "ospf" + "[ospf-name='" + str(self.ospf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf, ['ospf_name', 'route_policy_name', 'internal', 'external', 'external_type', 'nssa_external', 'nssa_external_type'], name, value)


            class IpDistances(Entity):
                """
                Table of IP specific administrative distances
                
                .. attribute:: ip_distance
                
                	IP specific administrative distance
                	**type**\: list of  		 :py:class:`IpDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.IpDistances.IpDistance>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.IpDistances, self).__init__()

                    self.yang_name = "ip-distances"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ip-distance", ("ip_distance", Rip.Vrfs.Vrf.IpDistances.IpDistance))])
                    self._leafs = OrderedDict()

                    self.ip_distance = YList(self)
                    self._segment_path = lambda: "ip-distances"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.IpDistances, [], name, value)


                class IpDistance(Entity):
                    """
                    IP specific administrative distance
                    
                    .. attribute:: address  (key)
                    
                    	IP Source address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  (key)
                    
                    	IP address mask
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: distance
                    
                    	Administrative distance
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.IpDistances.IpDistance, self).__init__()

                        self.yang_name = "ip-distance"
                        self.yang_parent_name = "ip-distances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','netmask']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('netmask', (YLeaf(YType.str, 'netmask'), ['str'])),
                            ('distance', (YLeaf(YType.uint32, 'distance'), ['int'])),
                        ])
                        self.address = None
                        self.netmask = None
                        self.distance = None
                        self._segment_path = lambda: "ip-distance" + "[address='" + str(self.address) + "']" + "[netmask='" + str(self.netmask) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.IpDistances.IpDistance, ['address', 'netmask', 'distance'], name, value)


            class Interfaces(Entity):
                """
                Table of RIP interfaces
                
                .. attribute:: interface
                
                	RIP interface name
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Rip.Vrfs.Vrf.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    RIP interface name
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: authentication
                    
                    	Authentication keychain and mode
                    	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.Authentication>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: site_of_origin
                    
                    	SOO community for prefixes learned over this interface
                    	**type**\:  :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin>`
                    
                    .. attribute:: receive_version
                    
                    	RIP versions supported for receiving advertisements
                    	**type**\:  :py:class:`ReceiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion>`
                    
                    .. attribute:: send_version
                    
                    	RIP versions supported for sending advertisements
                    	**type**\:  :py:class:`SendVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion>`
                    
                    .. attribute:: broadcast_for_v2
                    
                    	Send RIP v2 output packets to broadcast address
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: poison_reverse
                    
                    	Enable poison reverse
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: passive
                    
                    	Suppress routing updates on this interface
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Starts RIP interface configuration
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: policy_out
                    
                    	Route Policy for outbound routing updates
                    	**type**\: str
                    
                    .. attribute:: accept_metric_zero
                    
                    	Accept RIP updates with metric 0
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: policy_in
                    
                    	Route Policy for inbound routing updates
                    	**type**\: str
                    
                    .. attribute:: split_horizon_disable
                    
                    	Disable split horizon
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("authentication", ("authentication", Rip.Vrfs.Vrf.Interfaces.Interface.Authentication)), ("site-of-origin", ("site_of_origin", Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin)), ("receive-version", ("receive_version", Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion)), ("send-version", ("send_version", Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('broadcast_for_v2', (YLeaf(YType.empty, 'broadcast-for-v2'), ['Empty'])),
                            ('poison_reverse', (YLeaf(YType.empty, 'poison-reverse'), ['Empty'])),
                            ('passive', (YLeaf(YType.empty, 'passive'), ['Empty'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ('policy_out', (YLeaf(YType.str, 'policy-out'), ['str'])),
                            ('accept_metric_zero', (YLeaf(YType.empty, 'accept-metric-zero'), ['Empty'])),
                            ('policy_in', (YLeaf(YType.str, 'policy-in'), ['str'])),
                            ('split_horizon_disable', (YLeaf(YType.empty, 'split-horizon-disable'), ['Empty'])),
                        ])
                        self.interface_name = None
                        self.broadcast_for_v2 = None
                        self.poison_reverse = None
                        self.passive = None
                        self.enable = None
                        self.policy_out = None
                        self.accept_metric_zero = None
                        self.policy_in = None
                        self.split_horizon_disable = None

                        self.authentication = None
                        self._children_name_map["authentication"] = "authentication"

                        self.site_of_origin = Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin()
                        self.site_of_origin.parent = self
                        self._children_name_map["site_of_origin"] = "site-of-origin"

                        self.receive_version = Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion()
                        self.receive_version.parent = self
                        self._children_name_map["receive_version"] = "receive-version"

                        self.send_version = Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion()
                        self.send_version.parent = self
                        self._children_name_map["send_version"] = "send-version"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface, ['interface_name', 'broadcast_for_v2', 'poison_reverse', 'passive', 'enable', 'policy_out', 'accept_metric_zero', 'policy_in', 'split_horizon_disable'], name, value)


                    class Authentication(Entity):
                        """
                        Authentication keychain and mode
                        
                        .. attribute:: keychain
                        
                        	Name of keychain
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mode
                        
                        	Authentication mode
                        	**type**\:  :py:class:`RipAuthMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipAuthMode>`
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('keychain', (YLeaf(YType.str, 'keychain'), ['str'])),
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'RipAuthMode', '')])),
                            ])
                            self.keychain = None
                            self.mode = None
                            self._segment_path = lambda: "authentication"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.Authentication, ['keychain', 'mode'], name, value)


                    class SiteOfOrigin(Entity):
                        """
                        SOO community for prefixes learned over this
                        interface
                        
                        .. attribute:: type
                        
                        	Extended community type
                        	**type**\:  :py:class:`RipExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipExtCommunity>`
                        
                        .. attribute:: as_xx
                        
                        	AS Number for AS\:nn format
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: as_yy
                        
                        	32 bit value for AS\:nn format
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: as_index
                        
                        	AS Number Index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: address
                        
                        	IPV4 address for IPV4Address\:nn format
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_index
                        
                        	16bit value for IPV4Address\:nn format
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin, self).__init__()

                            self.yang_name = "site-of-origin"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'RipExtCommunity', '')])),
                                ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                ('as_index', (YLeaf(YType.uint32, 'as-index'), ['int'])),
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                            ])
                            self.type = None
                            self.as_xx = None
                            self.as_yy = None
                            self.as_index = None
                            self.address = None
                            self.address_index = None
                            self._segment_path = lambda: "site-of-origin"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin, ['type', 'as_xx', 'as_yy', 'as_index', 'address', 'address_index'], name, value)


                    class ReceiveVersion(Entity):
                        """
                        RIP versions supported for receiving
                        advertisements
                        
                        .. attribute:: version1
                        
                        	Support RIP version 1
                        	**type**\: bool
                        
                        .. attribute:: version2
                        
                        	Support RIP version 2
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion, self).__init__()

                            self.yang_name = "receive-version"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('version1', (YLeaf(YType.boolean, 'version1'), ['bool'])),
                                ('version2', (YLeaf(YType.boolean, 'version2'), ['bool'])),
                            ])
                            self.version1 = None
                            self.version2 = None
                            self._segment_path = lambda: "receive-version"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion, ['version1', 'version2'], name, value)


                    class SendVersion(Entity):
                        """
                        RIP versions supported for sending
                        advertisements
                        
                        .. attribute:: version1
                        
                        	Support RIP version 1
                        	**type**\: bool
                        
                        .. attribute:: version2
                        
                        	Support RIP version 2
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion, self).__init__()

                            self.yang_name = "send-version"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('version1', (YLeaf(YType.boolean, 'version1'), ['bool'])),
                                ('version2', (YLeaf(YType.boolean, 'version2'), ['bool'])),
                            ])
                            self.version1 = None
                            self.version2 = None
                            self._segment_path = lambda: "send-version"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion, ['version1', 'version2'], name, value)


            class Neighbors(Entity):
                """
                Configure RIP Neighbors
                
                .. attribute:: neighbor
                
                	Neighbor address
                	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Neighbors.Neighbor>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("neighbor", ("neighbor", Rip.Vrfs.Vrf.Neighbors.Neighbor))])
                    self._leafs = OrderedDict()

                    self.neighbor = YList(self)
                    self._segment_path = lambda: "neighbors"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Neighbors, [], name, value)


                class Neighbor(Entity):
                    """
                    Neighbor address
                    
                    .. attribute:: neighbor_address  (key)
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Neighbors.Neighbor, self).__init__()

                        self.yang_name = "neighbor"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['neighbor_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                        ])
                        self.neighbor_address = None
                        self._segment_path = lambda: "neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Neighbors.Neighbor, ['neighbor_address'], name, value)


            class Timers(Entity):
                """
                Various routing timers
                
                .. attribute:: update_timer
                
                	Interval between updates
                	**type**\: int
                
                	**range:** 5..50000
                
                	**mandatory**\: True
                
                .. attribute:: invalid_timer
                
                	Invalid
                	**type**\: int
                
                	**range:** 15..200000
                
                	**mandatory**\: True
                
                .. attribute:: holddown_timer
                
                	Holddown
                	**type**\: int
                
                	**range:** 15..200000
                
                	**mandatory**\: True
                
                .. attribute:: flush_timer
                
                	Flush
                	**type**\: int
                
                	**range:** 16..250000
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Timers, self).__init__()

                    self.yang_name = "timers"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                        ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                        ('holddown_timer', (YLeaf(YType.uint32, 'holddown-timer'), ['int'])),
                        ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                    ])
                    self.update_timer = None
                    self.invalid_timer = None
                    self.holddown_timer = None
                    self.flush_timer = None
                    self._segment_path = lambda: "timers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Timers, ['update_timer', 'invalid_timer', 'holddown_timer', 'flush_timer'], name, value)

    def clone_ptr(self):
        self._top_entity = Rip()
        return self._top_entity

