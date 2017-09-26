""" Cisco_IOS_XR_ip_rip_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rip package configuration.

This module contains definitions
for the following management objects\:
  rip\: RIP configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BgpRedistRoute(Enum):
    """
    BgpRedistRoute

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
    DefaultInformationOption

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
    DefaultRedistRoute

    Default redist route

    .. data:: all = 0

    	All routes

    """

    all = Enum.YLeaf(0, "all")


class IsisRedistRoute(Enum):
    """
    IsisRedistRoute

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
    RipAuthMode

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
    RipExtCommunity

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
    	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf>`
    
    .. attribute:: vrfs
    
    	VRF related RIP configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs>`
    
    

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
        self._child_container_classes = {"default-vrf" : ("default_vrf", Rip.DefaultVrf), "vrfs" : ("vrfs", Rip.Vrfs)}
        self._child_list_classes = {}

        self.default_vrf = Rip.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"
        self._children_yang_names.add("default-vrf")

        self.vrfs = Rip.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip"


    class DefaultVrf(Entity):
        """
        RIP configuration for Default VRF
        
        .. attribute:: auto_summary
        
        	Enable automatic network number summarization
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: broadcast_for_v2
        
        	Send RIP v2 output packets to broadcast address
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: default_information
        
        	Controls default information origination
        	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.DefaultInformation>`
        
        	**presence node**\: True
        
        .. attribute:: default_metric
        
        	Default metric of redistributed routes
        	**type**\:  int
        
        	**range:** 0..16
        
        .. attribute:: distance
        
        	Administrative distance
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 120
        
        .. attribute:: enable
        
        	Starts RIP configuration for Default VRF
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interfaces
        
        	Table of RIP interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces>`
        
        .. attribute:: ip_distances
        
        	Table of IP specific administrative distances
        	**type**\:   :py:class:`IpDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.IpDistances>`
        
        .. attribute:: maximum_paths
        
        	Maximum number of paths allowed per route
        	**type**\:  int
        
        	**range:** 1..128
        
        	**default value**\: 4
        
        .. attribute:: neighbors
        
        	Configure RIP Neighbors
        	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Neighbors>`
        
        .. attribute:: nsf
        
        	Enable Cisco Non Stop Forwarding
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: output_delay
        
        	Inter\-packet delay for RIP updates
        	**type**\:  int
        
        	**range:** 8..50
        
        	**units**\: millisecond
        
        .. attribute:: policy_in
        
        	Route Policy for inbbound routing updates
        	**type**\:  str
        
        .. attribute:: policy_out
        
        	Route Policy for outbound routing updates
        	**type**\:  str
        
        .. attribute:: redistribution
        
        	Redistribute information from another routing protocol
        	**type**\:   :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution>`
        
        .. attribute:: timers
        
        	Various routing timers
        	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Timers>`
        
        	**presence node**\: True
        
        .. attribute:: validate_source_disable
        
        	Disable validation of source address of routing updates
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-rip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "rip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"default-information" : ("default_information", Rip.DefaultVrf.DefaultInformation), "interfaces" : ("interfaces", Rip.DefaultVrf.Interfaces), "ip-distances" : ("ip_distances", Rip.DefaultVrf.IpDistances), "neighbors" : ("neighbors", Rip.DefaultVrf.Neighbors), "redistribution" : ("redistribution", Rip.DefaultVrf.Redistribution), "timers" : ("timers", Rip.DefaultVrf.Timers)}
            self._child_list_classes = {}

            self.auto_summary = YLeaf(YType.empty, "auto-summary")

            self.broadcast_for_v2 = YLeaf(YType.empty, "broadcast-for-v2")

            self.default_metric = YLeaf(YType.uint32, "default-metric")

            self.distance = YLeaf(YType.uint32, "distance")

            self.enable = YLeaf(YType.empty, "enable")

            self.maximum_paths = YLeaf(YType.uint32, "maximum-paths")

            self.nsf = YLeaf(YType.empty, "nsf")

            self.output_delay = YLeaf(YType.uint32, "output-delay")

            self.policy_in = YLeaf(YType.str, "policy-in")

            self.policy_out = YLeaf(YType.str, "policy-out")

            self.validate_source_disable = YLeaf(YType.empty, "validate-source-disable")

            self.default_information = None
            self._children_name_map["default_information"] = "default-information"
            self._children_yang_names.add("default-information")

            self.interfaces = Rip.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.ip_distances = Rip.DefaultVrf.IpDistances()
            self.ip_distances.parent = self
            self._children_name_map["ip_distances"] = "ip-distances"
            self._children_yang_names.add("ip-distances")

            self.neighbors = Rip.DefaultVrf.Neighbors()
            self.neighbors.parent = self
            self._children_name_map["neighbors"] = "neighbors"
            self._children_yang_names.add("neighbors")

            self.redistribution = Rip.DefaultVrf.Redistribution()
            self.redistribution.parent = self
            self._children_name_map["redistribution"] = "redistribution"
            self._children_yang_names.add("redistribution")

            self.timers = None
            self._children_name_map["timers"] = "timers"
            self._children_yang_names.add("timers")
            self._segment_path = lambda: "default-vrf"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rip.DefaultVrf, ['auto_summary', 'broadcast_for_v2', 'default_metric', 'distance', 'enable', 'maximum_paths', 'nsf', 'output_delay', 'policy_in', 'policy_out', 'validate_source_disable'], name, value)


        class DefaultInformation(Entity):
            """
            Controls default information origination
            
            .. attribute:: option
            
            	Origination option
            	**type**\:   :py:class:`DefaultInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultInformationOption>`
            
            	**mandatory**\: True
            
            .. attribute:: route_policy_name
            
            	Route policy name
            	**type**\:  str
            
            

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
                self._child_container_classes = {}
                self._child_list_classes = {}
                self.is_presence_container = True

                self.option = YLeaf(YType.enumeration, "option")

                self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                self._segment_path = lambda: "default-information"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.DefaultInformation, ['option', 'route_policy_name'], name, value)


        class Interfaces(Entity):
            """
            Table of RIP interfaces
            
            .. attribute:: interface
            
            	RIP interface name
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Rip.DefaultVrf.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Interfaces, [], name, value)


            class Interface(Entity):
                """
                RIP interface name
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: accept_metric_zero
                
                	Accept RIP updates with metric 0
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: authentication
                
                	Authentication keychain and mode
                	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.Authentication>`
                
                	**presence node**\: True
                
                .. attribute:: broadcast_for_v2
                
                	Send RIP v2 output packets to broadcast address
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	Starts RIP interface configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: passive
                
                	Suppress routing updates on this interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: poison_reverse
                
                	Enable poison reverse
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: policy_in
                
                	Route Policy for inbound routing updates
                	**type**\:  str
                
                .. attribute:: policy_out
                
                	Route Policy for outbound routing updates
                	**type**\:  str
                
                .. attribute:: receive_version
                
                	RIP versions supported for receiving advertisements
                	**type**\:   :py:class:`ReceiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion>`
                
                .. attribute:: send_version
                
                	RIP versions supported for sending advertisements
                	**type**\:   :py:class:`SendVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.SendVersion>`
                
                .. attribute:: site_of_origin
                
                	SOO community for prefixes learned over this interface
                	**type**\:   :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin>`
                
                .. attribute:: split_horizon_disable
                
                	Disable split horizon
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"authentication" : ("authentication", Rip.DefaultVrf.Interfaces.Interface.Authentication), "receive-version" : ("receive_version", Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion), "send-version" : ("send_version", Rip.DefaultVrf.Interfaces.Interface.SendVersion), "site-of-origin" : ("site_of_origin", Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin)}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.accept_metric_zero = YLeaf(YType.empty, "accept-metric-zero")

                    self.broadcast_for_v2 = YLeaf(YType.empty, "broadcast-for-v2")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.passive = YLeaf(YType.empty, "passive")

                    self.poison_reverse = YLeaf(YType.empty, "poison-reverse")

                    self.policy_in = YLeaf(YType.str, "policy-in")

                    self.policy_out = YLeaf(YType.str, "policy-out")

                    self.split_horizon_disable = YLeaf(YType.empty, "split-horizon-disable")

                    self.authentication = None
                    self._children_name_map["authentication"] = "authentication"
                    self._children_yang_names.add("authentication")

                    self.receive_version = Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion()
                    self.receive_version.parent = self
                    self._children_name_map["receive_version"] = "receive-version"
                    self._children_yang_names.add("receive-version")

                    self.send_version = Rip.DefaultVrf.Interfaces.Interface.SendVersion()
                    self.send_version.parent = self
                    self._children_name_map["send_version"] = "send-version"
                    self._children_yang_names.add("send-version")

                    self.site_of_origin = Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin()
                    self.site_of_origin.parent = self
                    self._children_name_map["site_of_origin"] = "site-of-origin"
                    self._children_yang_names.add("site-of-origin")
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface, ['interface_name', 'accept_metric_zero', 'broadcast_for_v2', 'enable', 'passive', 'poison_reverse', 'policy_in', 'policy_out', 'split_horizon_disable'], name, value)


                class Authentication(Entity):
                    """
                    Authentication keychain and mode
                    
                    .. attribute:: keychain
                    
                    	Name of keychain
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mode
                    
                    	Authentication mode
                    	**type**\:   :py:class:`RipAuthMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipAuthMode>`
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.keychain = YLeaf(YType.str, "keychain")

                        self.mode = YLeaf(YType.enumeration, "mode")
                        self._segment_path = lambda: "authentication"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.Authentication, ['keychain', 'mode'], name, value)


                class ReceiveVersion(Entity):
                    """
                    RIP versions supported for receiving
                    advertisements
                    
                    .. attribute:: version1
                    
                    	Support RIP version 1
                    	**type**\:  bool
                    
                    .. attribute:: version2
                    
                    	Support RIP version 2
                    	**type**\:  bool
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.version1 = YLeaf(YType.boolean, "version1")

                        self.version2 = YLeaf(YType.boolean, "version2")
                        self._segment_path = lambda: "receive-version"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion, ['version1', 'version2'], name, value)


                class SendVersion(Entity):
                    """
                    RIP versions supported for sending
                    advertisements
                    
                    .. attribute:: version1
                    
                    	Support RIP version 1
                    	**type**\:  bool
                    
                    .. attribute:: version2
                    
                    	Support RIP version 2
                    	**type**\:  bool
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.version1 = YLeaf(YType.boolean, "version1")

                        self.version2 = YLeaf(YType.boolean, "version2")
                        self._segment_path = lambda: "send-version"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.SendVersion, ['version1', 'version2'], name, value)


                class SiteOfOrigin(Entity):
                    """
                    SOO community for prefixes learned over this
                    interface
                    
                    .. attribute:: address
                    
                    	IPV4 address for IPV4Address\:nn format
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: address_index
                    
                    	16bit value for IPV4Address\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: as_index
                    
                    	AS Number Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: as_xx
                    
                    	AS Number for AS\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: as_yy
                    
                    	32 bit value for AS\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	Extended community type
                    	**type**\:   :py:class:`RipExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipExtCommunity>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin, self).__init__()

                        self.yang_name = "site-of-origin"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.address_index = YLeaf(YType.uint32, "address-index")

                        self.as_index = YLeaf(YType.uint32, "as-index")

                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                        self.as_yy = YLeaf(YType.uint32, "as-yy")

                        self.type = YLeaf(YType.enumeration, "type")
                        self._segment_path = lambda: "site-of-origin"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin, ['address', 'address_index', 'as_index', 'as_xx', 'as_yy', 'type'], name, value)


        class IpDistances(Entity):
            """
            Table of IP specific administrative distances
            
            .. attribute:: ip_distance
            
            	IP specific administrative distance
            	**type**\: list of    :py:class:`IpDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.IpDistances.IpDistance>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.IpDistances, self).__init__()

                self.yang_name = "ip-distances"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"ip-distance" : ("ip_distance", Rip.DefaultVrf.IpDistances.IpDistance)}

                self.ip_distance = YList(self)
                self._segment_path = lambda: "ip-distances"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.IpDistances, [], name, value)


            class IpDistance(Entity):
                """
                IP specific administrative distance
                
                .. attribute:: address  <key>
                
                	IP Source address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: netmask  <key>
                
                	IP address mask
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: distance
                
                	Administrative distance
                	**type**\:  int
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.address = YLeaf(YType.str, "address")

                    self.netmask = YLeaf(YType.str, "netmask")

                    self.distance = YLeaf(YType.uint32, "distance")
                    self._segment_path = lambda: "ip-distance" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/ip-distances/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.IpDistances.IpDistance, ['address', 'netmask', 'distance'], name, value)


        class Neighbors(Entity):
            """
            Configure RIP Neighbors
            
            .. attribute:: neighbor
            
            	Neighbor address
            	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Neighbors.Neighbor>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Neighbors, self).__init__()

                self.yang_name = "neighbors"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"neighbor" : ("neighbor", Rip.DefaultVrf.Neighbors.Neighbor)}

                self.neighbor = YList(self)
                self._segment_path = lambda: "neighbors"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Neighbors, [], name, value)


            class Neighbor(Entity):
                """
                Neighbor address
                
                .. attribute:: neighbor_address  <key>
                
                	IPv4 address
                	**type**\:  str
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.neighbor_address = YLeaf(YType.str, "neighbor-address")
                    self._segment_path = lambda: "neighbor" + "[neighbor-address='" + self.neighbor_address.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/neighbors/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Neighbors.Neighbor, ['neighbor_address'], name, value)


        class Redistribution(Entity):
            """
            Redistribute information from another routing
            protocol
            
            .. attribute:: bgps
            
            	Redistribute BGP routes
            	**type**\:   :py:class:`Bgps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Bgps>`
            
            .. attribute:: connected
            
            	Redistribute connected routes
            	**type**\:   :py:class:`Connected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Connected>`
            
            	**presence node**\: True
            
            .. attribute:: eigrp_s
            
            	Redistribute EIGRP routes
            	**type**\:   :py:class:`EigrpS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.EigrpS>`
            
            .. attribute:: isises
            
            	Redistribute IS\-IS routes
            	**type**\:   :py:class:`Isises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Isises>`
            
            .. attribute:: ospfs
            
            	Redistribute OSPF routes
            	**type**\:   :py:class:`Ospfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Ospfs>`
            
            .. attribute:: static
            
            	Redistribute static routes
            	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Static>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Redistribution, self).__init__()

                self.yang_name = "redistribution"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bgps" : ("bgps", Rip.DefaultVrf.Redistribution.Bgps), "connected" : ("connected", Rip.DefaultVrf.Redistribution.Connected), "eigrp-s" : ("eigrp_s", Rip.DefaultVrf.Redistribution.EigrpS), "isises" : ("isises", Rip.DefaultVrf.Redistribution.Isises), "ospfs" : ("ospfs", Rip.DefaultVrf.Redistribution.Ospfs), "static" : ("static", Rip.DefaultVrf.Redistribution.Static)}
                self._child_list_classes = {}

                self.bgps = Rip.DefaultVrf.Redistribution.Bgps()
                self.bgps.parent = self
                self._children_name_map["bgps"] = "bgps"
                self._children_yang_names.add("bgps")

                self.connected = None
                self._children_name_map["connected"] = "connected"
                self._children_yang_names.add("connected")

                self.eigrp_s = Rip.DefaultVrf.Redistribution.EigrpS()
                self.eigrp_s.parent = self
                self._children_name_map["eigrp_s"] = "eigrp-s"
                self._children_yang_names.add("eigrp-s")

                self.isises = Rip.DefaultVrf.Redistribution.Isises()
                self.isises.parent = self
                self._children_name_map["isises"] = "isises"
                self._children_yang_names.add("isises")

                self.ospfs = Rip.DefaultVrf.Redistribution.Ospfs()
                self.ospfs.parent = self
                self._children_name_map["ospfs"] = "ospfs"
                self._children_yang_names.add("ospfs")

                self.static = None
                self._children_name_map["static"] = "static"
                self._children_yang_names.add("static")
                self._segment_path = lambda: "redistribution"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()


            class Bgps(Entity):
                """
                Redistribute BGP routes
                
                .. attribute:: bgp
                
                	Autonomous system number
                	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Bgps.Bgp>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Bgps, self).__init__()

                    self.yang_name = "bgps"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"bgp" : ("bgp", Rip.DefaultVrf.Redistribution.Bgps.Bgp)}

                    self.bgp = YList(self)
                    self._segment_path = lambda: "bgps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Bgps, [], name, value)


                class Bgp(Entity):
                    """
                    Autonomous system number
                    
                    .. attribute:: asnxx  <key>
                    
                    	Higher 16 bits of 4\-byte BGP AS number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: asnyy  <key>
                    
                    	2\-byte or 4\-byte BGP AS number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: policy
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: type
                    
                    	Route type
                    	**type**\:   :py:class:`BgpRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.BgpRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Bgps.Bgp, self).__init__()

                        self.yang_name = "bgp"
                        self.yang_parent_name = "bgps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.asnxx = YLeaf(YType.uint32, "asnxx")

                        self.asnyy = YLeaf(YType.uint32, "asnyy")

                        self.policy = YLeaf(YType.str, "policy")

                        self.type = YLeaf(YType.enumeration, "type")
                        self._segment_path = lambda: "bgp" + "[asnxx='" + self.asnxx.get() + "']" + "[asnyy='" + self.asnyy.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/bgps/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Redistribution.Bgps.Bgp, ['asnxx', 'asnyy', 'policy', 'type'], name, value)


            class Connected(Entity):
                """
                Redistribute connected routes
                
                .. attribute:: route_policy_name
                
                	Route Policy name
                	**type**\:  str
                
                .. attribute:: route_type
                
                	Route type
                	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                
                

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                    self.route_type = YLeaf(YType.enumeration, "route-type")
                    self._segment_path = lambda: "connected"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Connected, ['route_policy_name', 'route_type'], name, value)


            class EigrpS(Entity):
                """
                Redistribute EIGRP routes
                
                .. attribute:: eigrp
                
                	Redistribute EIGRP routes
                	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.EigrpS.Eigrp>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.EigrpS, self).__init__()

                    self.yang_name = "eigrp-s"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"eigrp" : ("eigrp", Rip.DefaultVrf.Redistribution.EigrpS.Eigrp)}

                    self.eigrp = YList(self)
                    self._segment_path = lambda: "eigrp-s"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.EigrpS, [], name, value)


                class Eigrp(Entity):
                    """
                    Redistribute EIGRP routes
                    
                    .. attribute:: as_  <key>
                    
                    	Autonomous system number
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.EigrpS.Eigrp, self).__init__()

                        self.yang_name = "eigrp"
                        self.yang_parent_name = "eigrp-s"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.as_ = YLeaf(YType.uint32, "as")

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        self.route_type = YLeaf(YType.enumeration, "route-type")
                        self._segment_path = lambda: "eigrp" + "[as='" + self.as_.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/eigrp-s/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Redistribution.EigrpS.Eigrp, ['as_', 'route_policy_name', 'route_type'], name, value)


            class Isises(Entity):
                """
                Redistribute IS\-IS routes
                
                .. attribute:: isis
                
                	Redistribute IS\-IS routes
                	**type**\: list of    :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Isises.Isis>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Isises, self).__init__()

                    self.yang_name = "isises"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"isis" : ("isis", Rip.DefaultVrf.Redistribution.Isises.Isis)}

                    self.isis = YList(self)
                    self._segment_path = lambda: "isises"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Isises, [], name, value)


                class Isis(Entity):
                    """
                    Redistribute IS\-IS routes
                    
                    .. attribute:: isis_name  <key>
                    
                    	IS\-IS instance name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`IsisRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.IsisRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Isises.Isis, self).__init__()

                        self.yang_name = "isis"
                        self.yang_parent_name = "isises"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.isis_name = YLeaf(YType.str, "isis-name")

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        self.route_type = YLeaf(YType.enumeration, "route-type")
                        self._segment_path = lambda: "isis" + "[isis-name='" + self.isis_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/isises/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Redistribution.Isises.Isis, ['isis_name', 'route_policy_name', 'route_type'], name, value)


            class Ospfs(Entity):
                """
                Redistribute OSPF routes
                
                .. attribute:: ospf
                
                	Redistribute OSPF routes
                	**type**\: list of    :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Ospfs.Ospf>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Ospfs, self).__init__()

                    self.yang_name = "ospfs"
                    self.yang_parent_name = "redistribution"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ospf" : ("ospf", Rip.DefaultVrf.Redistribution.Ospfs.Ospf)}

                    self.ospf = YList(self)
                    self._segment_path = lambda: "ospfs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Ospfs, [], name, value)


                class Ospf(Entity):
                    """
                    Redistribute OSPF routes
                    
                    .. attribute:: ospf_name  <key>
                    
                    	Process ID for the OSPF instance
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: external
                    
                    	External routes
                    	**type**\:  bool
                    
                    .. attribute:: external_type
                    
                    	External route type
                    	**type**\:  int
                    
                    	**range:** 0..2
                    
                    .. attribute:: internal
                    
                    	Internal routes
                    	**type**\:  bool
                    
                    .. attribute:: nssa_external
                    
                    	NSSA External routes
                    	**type**\:  bool
                    
                    .. attribute:: nssa_external_type
                    
                    	NSSA External route type
                    	**type**\:  int
                    
                    	**range:** 0..2
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Ospfs.Ospf, self).__init__()

                        self.yang_name = "ospf"
                        self.yang_parent_name = "ospfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ospf_name = YLeaf(YType.str, "ospf-name")

                        self.external = YLeaf(YType.boolean, "external")

                        self.external_type = YLeaf(YType.uint32, "external-type")

                        self.internal = YLeaf(YType.boolean, "internal")

                        self.nssa_external = YLeaf(YType.boolean, "nssa-external")

                        self.nssa_external_type = YLeaf(YType.uint32, "nssa-external-type")

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                        self._segment_path = lambda: "ospf" + "[ospf-name='" + self.ospf_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/ospfs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Redistribution.Ospfs.Ospf, ['ospf_name', 'external', 'external_type', 'internal', 'nssa_external', 'nssa_external_type', 'route_policy_name'], name, value)


            class Static(Entity):
                """
                Redistribute static routes
                
                .. attribute:: route_policy_name
                
                	Route Policy name
                	**type**\:  str
                
                .. attribute:: route_type
                
                	Route type
                	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                
                

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                    self.route_type = YLeaf(YType.enumeration, "route-type")
                    self._segment_path = lambda: "static"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Redistribution.Static, ['route_policy_name', 'route_type'], name, value)


        class Timers(Entity):
            """
            Various routing timers
            
            .. attribute:: flush_timer
            
            	Flush
            	**type**\:  int
            
            	**range:** 16..250000
            
            	**mandatory**\: True
            
            .. attribute:: holddown_timer
            
            	Holddown
            	**type**\:  int
            
            	**range:** 15..200000
            
            	**mandatory**\: True
            
            .. attribute:: invalid_timer
            
            	Invalid
            	**type**\:  int
            
            	**range:** 15..200000
            
            	**mandatory**\: True
            
            .. attribute:: update_timer
            
            	Interval between updates
            	**type**\:  int
            
            	**range:** 5..50000
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}
                self.is_presence_container = True

                self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                self.holddown_timer = YLeaf(YType.uint32, "holddown-timer")

                self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                self.update_timer = YLeaf(YType.uint32, "update-timer")
                self._segment_path = lambda: "timers"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Timers, ['flush_timer', 'holddown_timer', 'invalid_timer', 'update_timer'], name, value)


    class Vrfs(Entity):
        """
        VRF related RIP configuration
        
        .. attribute:: vrf
        
        	RIP configuration for a particular VRF
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-rip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "rip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", Rip.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rip.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            RIP configuration for a particular VRF
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: auto_summary
            
            	Enable automatic network number summarization
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: broadcast_for_v2
            
            	Send RIP v2 output packets to broadcast address
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: default_information
            
            	Controls default information origination
            	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.DefaultInformation>`
            
            	**presence node**\: True
            
            .. attribute:: default_metric
            
            	Default metric of redistributed routes
            	**type**\:  int
            
            	**range:** 0..16
            
            .. attribute:: distance
            
            	Administrative distance
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 120
            
            .. attribute:: enable
            
            	Starts RIP configuration for a particular VRF
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interfaces
            
            	Table of RIP interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: ip_distances
            
            	Table of IP specific administrative distances
            	**type**\:   :py:class:`IpDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.IpDistances>`
            
            .. attribute:: maximum_paths
            
            	Maximum number of paths allowed per route
            	**type**\:  int
            
            	**range:** 1..128
            
            	**default value**\: 4
            
            .. attribute:: neighbors
            
            	Configure RIP Neighbors
            	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Neighbors>`
            
            .. attribute:: nsf
            
            	Enable Cisco Non Stop Forwarding
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: output_delay
            
            	Inter\-packet delay for RIP updates
            	**type**\:  int
            
            	**range:** 8..50
            
            	**units**\: millisecond
            
            .. attribute:: policy_in
            
            	Route Policy for inbbound routing updates
            	**type**\:  str
            
            .. attribute:: policy_out
            
            	Route Policy for outbound routing updates
            	**type**\:  str
            
            .. attribute:: redistribution
            
            	Redistribute information from another routing protocol
            	**type**\:   :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution>`
            
            .. attribute:: timers
            
            	Various routing timers
            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Timers>`
            
            	**presence node**\: True
            
            .. attribute:: validate_source_disable
            
            	Disable validation of source address of routing updates
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"default-information" : ("default_information", Rip.Vrfs.Vrf.DefaultInformation), "interfaces" : ("interfaces", Rip.Vrfs.Vrf.Interfaces), "ip-distances" : ("ip_distances", Rip.Vrfs.Vrf.IpDistances), "neighbors" : ("neighbors", Rip.Vrfs.Vrf.Neighbors), "redistribution" : ("redistribution", Rip.Vrfs.Vrf.Redistribution), "timers" : ("timers", Rip.Vrfs.Vrf.Timers)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.auto_summary = YLeaf(YType.empty, "auto-summary")

                self.broadcast_for_v2 = YLeaf(YType.empty, "broadcast-for-v2")

                self.default_metric = YLeaf(YType.uint32, "default-metric")

                self.distance = YLeaf(YType.uint32, "distance")

                self.enable = YLeaf(YType.empty, "enable")

                self.maximum_paths = YLeaf(YType.uint32, "maximum-paths")

                self.nsf = YLeaf(YType.empty, "nsf")

                self.output_delay = YLeaf(YType.uint32, "output-delay")

                self.policy_in = YLeaf(YType.str, "policy-in")

                self.policy_out = YLeaf(YType.str, "policy-out")

                self.validate_source_disable = YLeaf(YType.empty, "validate-source-disable")

                self.default_information = None
                self._children_name_map["default_information"] = "default-information"
                self._children_yang_names.add("default-information")

                self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.ip_distances = Rip.Vrfs.Vrf.IpDistances()
                self.ip_distances.parent = self
                self._children_name_map["ip_distances"] = "ip-distances"
                self._children_yang_names.add("ip-distances")

                self.neighbors = Rip.Vrfs.Vrf.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
                self._children_yang_names.add("neighbors")

                self.redistribution = Rip.Vrfs.Vrf.Redistribution()
                self.redistribution.parent = self
                self._children_name_map["redistribution"] = "redistribution"
                self._children_yang_names.add("redistribution")

                self.timers = None
                self._children_name_map["timers"] = "timers"
                self._children_yang_names.add("timers")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-cfg:rip/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.Vrfs.Vrf, ['vrf_name', 'auto_summary', 'broadcast_for_v2', 'default_metric', 'distance', 'enable', 'maximum_paths', 'nsf', 'output_delay', 'policy_in', 'policy_out', 'validate_source_disable'], name, value)


            class DefaultInformation(Entity):
                """
                Controls default information origination
                
                .. attribute:: option
                
                	Origination option
                	**type**\:   :py:class:`DefaultInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultInformationOption>`
                
                	**mandatory**\: True
                
                .. attribute:: route_policy_name
                
                	Route policy name
                	**type**\:  str
                
                

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.option = YLeaf(YType.enumeration, "option")

                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                    self._segment_path = lambda: "default-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.DefaultInformation, ['option', 'route_policy_name'], name, value)


            class Interfaces(Entity):
                """
                Table of RIP interfaces
                
                .. attribute:: interface
                
                	RIP interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Rip.Vrfs.Vrf.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    RIP interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: accept_metric_zero
                    
                    	Accept RIP updates with metric 0
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: authentication
                    
                    	Authentication keychain and mode
                    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.Authentication>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: broadcast_for_v2
                    
                    	Send RIP v2 output packets to broadcast address
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Starts RIP interface configuration
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: passive
                    
                    	Suppress routing updates on this interface
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: poison_reverse
                    
                    	Enable poison reverse
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: policy_in
                    
                    	Route Policy for inbound routing updates
                    	**type**\:  str
                    
                    .. attribute:: policy_out
                    
                    	Route Policy for outbound routing updates
                    	**type**\:  str
                    
                    .. attribute:: receive_version
                    
                    	RIP versions supported for receiving advertisements
                    	**type**\:   :py:class:`ReceiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion>`
                    
                    .. attribute:: send_version
                    
                    	RIP versions supported for sending advertisements
                    	**type**\:   :py:class:`SendVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion>`
                    
                    .. attribute:: site_of_origin
                    
                    	SOO community for prefixes learned over this interface
                    	**type**\:   :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin>`
                    
                    .. attribute:: split_horizon_disable
                    
                    	Disable split horizon
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"authentication" : ("authentication", Rip.Vrfs.Vrf.Interfaces.Interface.Authentication), "receive-version" : ("receive_version", Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion), "send-version" : ("send_version", Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion), "site-of-origin" : ("site_of_origin", Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.accept_metric_zero = YLeaf(YType.empty, "accept-metric-zero")

                        self.broadcast_for_v2 = YLeaf(YType.empty, "broadcast-for-v2")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.passive = YLeaf(YType.empty, "passive")

                        self.poison_reverse = YLeaf(YType.empty, "poison-reverse")

                        self.policy_in = YLeaf(YType.str, "policy-in")

                        self.policy_out = YLeaf(YType.str, "policy-out")

                        self.split_horizon_disable = YLeaf(YType.empty, "split-horizon-disable")

                        self.authentication = None
                        self._children_name_map["authentication"] = "authentication"
                        self._children_yang_names.add("authentication")

                        self.receive_version = Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion()
                        self.receive_version.parent = self
                        self._children_name_map["receive_version"] = "receive-version"
                        self._children_yang_names.add("receive-version")

                        self.send_version = Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion()
                        self.send_version.parent = self
                        self._children_name_map["send_version"] = "send-version"
                        self._children_yang_names.add("send-version")

                        self.site_of_origin = Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin()
                        self.site_of_origin.parent = self
                        self._children_name_map["site_of_origin"] = "site-of-origin"
                        self._children_yang_names.add("site-of-origin")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface, ['interface_name', 'accept_metric_zero', 'broadcast_for_v2', 'enable', 'passive', 'poison_reverse', 'policy_in', 'policy_out', 'split_horizon_disable'], name, value)


                    class Authentication(Entity):
                        """
                        Authentication keychain and mode
                        
                        .. attribute:: keychain
                        
                        	Name of keychain
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mode
                        
                        	Authentication mode
                        	**type**\:   :py:class:`RipAuthMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipAuthMode>`
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.keychain = YLeaf(YType.str, "keychain")

                            self.mode = YLeaf(YType.enumeration, "mode")
                            self._segment_path = lambda: "authentication"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.Authentication, ['keychain', 'mode'], name, value)


                    class ReceiveVersion(Entity):
                        """
                        RIP versions supported for receiving
                        advertisements
                        
                        .. attribute:: version1
                        
                        	Support RIP version 1
                        	**type**\:  bool
                        
                        .. attribute:: version2
                        
                        	Support RIP version 2
                        	**type**\:  bool
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.version1 = YLeaf(YType.boolean, "version1")

                            self.version2 = YLeaf(YType.boolean, "version2")
                            self._segment_path = lambda: "receive-version"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion, ['version1', 'version2'], name, value)


                    class SendVersion(Entity):
                        """
                        RIP versions supported for sending
                        advertisements
                        
                        .. attribute:: version1
                        
                        	Support RIP version 1
                        	**type**\:  bool
                        
                        .. attribute:: version2
                        
                        	Support RIP version 2
                        	**type**\:  bool
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.version1 = YLeaf(YType.boolean, "version1")

                            self.version2 = YLeaf(YType.boolean, "version2")
                            self._segment_path = lambda: "send-version"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion, ['version1', 'version2'], name, value)


                    class SiteOfOrigin(Entity):
                        """
                        SOO community for prefixes learned over this
                        interface
                        
                        .. attribute:: address
                        
                        	IPV4 address for IPV4Address\:nn format
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_index
                        
                        	16bit value for IPV4Address\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: as_index
                        
                        	AS Number Index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: as_xx
                        
                        	AS Number for AS\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: as_yy
                        
                        	32 bit value for AS\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Extended community type
                        	**type**\:   :py:class:`RipExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipExtCommunity>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin, self).__init__()

                            self.yang_name = "site-of-origin"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.address_index = YLeaf(YType.uint32, "address-index")

                            self.as_index = YLeaf(YType.uint32, "as-index")

                            self.as_xx = YLeaf(YType.uint32, "as-xx")

                            self.as_yy = YLeaf(YType.uint32, "as-yy")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "site-of-origin"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin, ['address', 'address_index', 'as_index', 'as_xx', 'as_yy', 'type'], name, value)


            class IpDistances(Entity):
                """
                Table of IP specific administrative distances
                
                .. attribute:: ip_distance
                
                	IP specific administrative distance
                	**type**\: list of    :py:class:`IpDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.IpDistances.IpDistance>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.IpDistances, self).__init__()

                    self.yang_name = "ip-distances"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"ip-distance" : ("ip_distance", Rip.Vrfs.Vrf.IpDistances.IpDistance)}

                    self.ip_distance = YList(self)
                    self._segment_path = lambda: "ip-distances"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.IpDistances, [], name, value)


                class IpDistance(Entity):
                    """
                    IP specific administrative distance
                    
                    .. attribute:: address  <key>
                    
                    	IP Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  <key>
                    
                    	IP address mask
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: distance
                    
                    	Administrative distance
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")

                        self.distance = YLeaf(YType.uint32, "distance")
                        self._segment_path = lambda: "ip-distance" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.IpDistances.IpDistance, ['address', 'netmask', 'distance'], name, value)


            class Neighbors(Entity):
                """
                Configure RIP Neighbors
                
                .. attribute:: neighbor
                
                	Neighbor address
                	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Neighbors.Neighbor>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"neighbor" : ("neighbor", Rip.Vrfs.Vrf.Neighbors.Neighbor)}

                    self.neighbor = YList(self)
                    self._segment_path = lambda: "neighbors"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Neighbors, [], name, value)


                class Neighbor(Entity):
                    """
                    Neighbor address
                    
                    .. attribute:: neighbor_address  <key>
                    
                    	IPv4 address
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")
                        self._segment_path = lambda: "neighbor" + "[neighbor-address='" + self.neighbor_address.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Neighbors.Neighbor, ['neighbor_address'], name, value)


            class Redistribution(Entity):
                """
                Redistribute information from another routing
                protocol
                
                .. attribute:: bgps
                
                	Redistribute BGP routes
                	**type**\:   :py:class:`Bgps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Bgps>`
                
                .. attribute:: connected
                
                	Redistribute connected routes
                	**type**\:   :py:class:`Connected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Connected>`
                
                	**presence node**\: True
                
                .. attribute:: eigrp_s
                
                	Redistribute EIGRP routes
                	**type**\:   :py:class:`EigrpS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.EigrpS>`
                
                .. attribute:: isises
                
                	Redistribute IS\-IS routes
                	**type**\:   :py:class:`Isises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Isises>`
                
                .. attribute:: ospfs
                
                	Redistribute OSPF routes
                	**type**\:   :py:class:`Ospfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Ospfs>`
                
                .. attribute:: static
                
                	Redistribute static routes
                	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Static>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Redistribution, self).__init__()

                    self.yang_name = "redistribution"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"bgps" : ("bgps", Rip.Vrfs.Vrf.Redistribution.Bgps), "connected" : ("connected", Rip.Vrfs.Vrf.Redistribution.Connected), "eigrp-s" : ("eigrp_s", Rip.Vrfs.Vrf.Redistribution.EigrpS), "isises" : ("isises", Rip.Vrfs.Vrf.Redistribution.Isises), "ospfs" : ("ospfs", Rip.Vrfs.Vrf.Redistribution.Ospfs), "static" : ("static", Rip.Vrfs.Vrf.Redistribution.Static)}
                    self._child_list_classes = {}

                    self.bgps = Rip.Vrfs.Vrf.Redistribution.Bgps()
                    self.bgps.parent = self
                    self._children_name_map["bgps"] = "bgps"
                    self._children_yang_names.add("bgps")

                    self.connected = None
                    self._children_name_map["connected"] = "connected"
                    self._children_yang_names.add("connected")

                    self.eigrp_s = Rip.Vrfs.Vrf.Redistribution.EigrpS()
                    self.eigrp_s.parent = self
                    self._children_name_map["eigrp_s"] = "eigrp-s"
                    self._children_yang_names.add("eigrp-s")

                    self.isises = Rip.Vrfs.Vrf.Redistribution.Isises()
                    self.isises.parent = self
                    self._children_name_map["isises"] = "isises"
                    self._children_yang_names.add("isises")

                    self.ospfs = Rip.Vrfs.Vrf.Redistribution.Ospfs()
                    self.ospfs.parent = self
                    self._children_name_map["ospfs"] = "ospfs"
                    self._children_yang_names.add("ospfs")

                    self.static = None
                    self._children_name_map["static"] = "static"
                    self._children_yang_names.add("static")
                    self._segment_path = lambda: "redistribution"


                class Bgps(Entity):
                    """
                    Redistribute BGP routes
                    
                    .. attribute:: bgp
                    
                    	Autonomous system number
                    	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Bgps, self).__init__()

                        self.yang_name = "bgps"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"bgp" : ("bgp", Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp)}

                        self.bgp = YList(self)
                        self._segment_path = lambda: "bgps"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Bgps, [], name, value)


                    class Bgp(Entity):
                        """
                        Autonomous system number
                        
                        .. attribute:: asnxx  <key>
                        
                        	Higher 16 bits of 4\-byte BGP AS number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: asnyy  <key>
                        
                        	2\-byte or 4\-byte BGP AS number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policy
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: type
                        
                        	Route type
                        	**type**\:   :py:class:`BgpRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.BgpRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp, self).__init__()

                            self.yang_name = "bgp"
                            self.yang_parent_name = "bgps"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.asnxx = YLeaf(YType.uint32, "asnxx")

                            self.asnyy = YLeaf(YType.uint32, "asnyy")

                            self.policy = YLeaf(YType.str, "policy")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "bgp" + "[asnxx='" + self.asnxx.get() + "']" + "[asnyy='" + self.asnyy.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp, ['asnxx', 'asnyy', 'policy', 'type'], name, value)


                class Connected(Entity):
                    """
                    Redistribute connected routes
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

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
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        self.route_type = YLeaf(YType.enumeration, "route-type")
                        self._segment_path = lambda: "connected"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Connected, ['route_policy_name', 'route_type'], name, value)


                class EigrpS(Entity):
                    """
                    Redistribute EIGRP routes
                    
                    .. attribute:: eigrp
                    
                    	Redistribute EIGRP routes
                    	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.EigrpS, self).__init__()

                        self.yang_name = "eigrp-s"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"eigrp" : ("eigrp", Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp)}

                        self.eigrp = YList(self)
                        self._segment_path = lambda: "eigrp-s"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.EigrpS, [], name, value)


                    class Eigrp(Entity):
                        """
                        Redistribute EIGRP routes
                        
                        .. attribute:: as_  <key>
                        
                        	Autonomous system number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: route_type
                        
                        	Route type
                        	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp, self).__init__()

                            self.yang_name = "eigrp"
                            self.yang_parent_name = "eigrp-s"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.as_ = YLeaf(YType.uint32, "as")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                            self.route_type = YLeaf(YType.enumeration, "route-type")
                            self._segment_path = lambda: "eigrp" + "[as='" + self.as_.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp, ['as_', 'route_policy_name', 'route_type'], name, value)


                class Isises(Entity):
                    """
                    Redistribute IS\-IS routes
                    
                    .. attribute:: isis
                    
                    	Redistribute IS\-IS routes
                    	**type**\: list of    :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Isises.Isis>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Isises, self).__init__()

                        self.yang_name = "isises"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"isis" : ("isis", Rip.Vrfs.Vrf.Redistribution.Isises.Isis)}

                        self.isis = YList(self)
                        self._segment_path = lambda: "isises"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Isises, [], name, value)


                    class Isis(Entity):
                        """
                        Redistribute IS\-IS routes
                        
                        .. attribute:: isis_name  <key>
                        
                        	IS\-IS instance name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: route_type
                        
                        	Route type
                        	**type**\:   :py:class:`IsisRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.IsisRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Isises.Isis, self).__init__()

                            self.yang_name = "isis"
                            self.yang_parent_name = "isises"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.isis_name = YLeaf(YType.str, "isis-name")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                            self.route_type = YLeaf(YType.enumeration, "route-type")
                            self._segment_path = lambda: "isis" + "[isis-name='" + self.isis_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Isises.Isis, ['isis_name', 'route_policy_name', 'route_type'], name, value)


                class Ospfs(Entity):
                    """
                    Redistribute OSPF routes
                    
                    .. attribute:: ospf
                    
                    	Redistribute OSPF routes
                    	**type**\: list of    :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Ospfs, self).__init__()

                        self.yang_name = "ospfs"
                        self.yang_parent_name = "redistribution"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"ospf" : ("ospf", Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf)}

                        self.ospf = YList(self)
                        self._segment_path = lambda: "ospfs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Ospfs, [], name, value)


                    class Ospf(Entity):
                        """
                        Redistribute OSPF routes
                        
                        .. attribute:: ospf_name  <key>
                        
                        	Process ID for the OSPF instance
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: external
                        
                        	External routes
                        	**type**\:  bool
                        
                        .. attribute:: external_type
                        
                        	External route type
                        	**type**\:  int
                        
                        	**range:** 0..2
                        
                        .. attribute:: internal
                        
                        	Internal routes
                        	**type**\:  bool
                        
                        .. attribute:: nssa_external
                        
                        	NSSA External routes
                        	**type**\:  bool
                        
                        .. attribute:: nssa_external_type
                        
                        	NSSA External route type
                        	**type**\:  int
                        
                        	**range:** 0..2
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf, self).__init__()

                            self.yang_name = "ospf"
                            self.yang_parent_name = "ospfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ospf_name = YLeaf(YType.str, "ospf-name")

                            self.external = YLeaf(YType.boolean, "external")

                            self.external_type = YLeaf(YType.uint32, "external-type")

                            self.internal = YLeaf(YType.boolean, "internal")

                            self.nssa_external = YLeaf(YType.boolean, "nssa-external")

                            self.nssa_external_type = YLeaf(YType.uint32, "nssa-external-type")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                            self._segment_path = lambda: "ospf" + "[ospf-name='" + self.ospf_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf, ['ospf_name', 'external', 'external_type', 'internal', 'nssa_external', 'nssa_external_type', 'route_policy_name'], name, value)


                class Static(Entity):
                    """
                    Redistribute static routes
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

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
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        self.route_type = YLeaf(YType.enumeration, "route-type")
                        self._segment_path = lambda: "static"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Redistribution.Static, ['route_policy_name', 'route_type'], name, value)


            class Timers(Entity):
                """
                Various routing timers
                
                .. attribute:: flush_timer
                
                	Flush
                	**type**\:  int
                
                	**range:** 16..250000
                
                	**mandatory**\: True
                
                .. attribute:: holddown_timer
                
                	Holddown
                	**type**\:  int
                
                	**range:** 15..200000
                
                	**mandatory**\: True
                
                .. attribute:: invalid_timer
                
                	Invalid
                	**type**\:  int
                
                	**range:** 15..200000
                
                	**mandatory**\: True
                
                .. attribute:: update_timer
                
                	Interval between updates
                	**type**\:  int
                
                	**range:** 5..50000
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.holddown_timer = YLeaf(YType.uint32, "holddown-timer")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")
                    self._segment_path = lambda: "timers"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Timers, ['flush_timer', 'holddown_timer', 'invalid_timer', 'update_timer'], name, value)

    def clone_ptr(self):
        self._top_entity = Rip()
        return self._top_entity

