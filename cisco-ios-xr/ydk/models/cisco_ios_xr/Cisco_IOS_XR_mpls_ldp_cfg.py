""" Cisco_IOS_XR_mpls_ldp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-ldp package configuration.

This module contains definitions
for the following management objects\:
  mpls\-ldp\: MPLS LDP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MldpPolicyMode(Enum):
    """
    MldpPolicyMode

    Mldp policy mode

    .. data:: inbound = 1

    	Inbound route policy

    .. data:: outbound = 2

    	Outbound route policy

    """

    inbound = Enum.YLeaf(1, "inbound")

    outbound = Enum.YLeaf(2, "outbound")


class MplsLdpAdvertiseBgpAcl(Enum):
    """
    MplsLdpAdvertiseBgpAcl

    Mpls ldp advertise bgp acl

    .. data:: peer_acl = 1

    	BGP prefixes advertised to peers permitted by

    	ACL

    """

    peer_acl = Enum.YLeaf(1, "peer-acl")


class MplsLdpDownstreamOnDemand(Enum):
    """
    MplsLdpDownstreamOnDemand

    Mpls ldp downstream on demand

    .. data:: peer_acl = 1

    	Downstream on Demand peers permitted by ACL

    """

    peer_acl = Enum.YLeaf(1, "peer-acl")


class MplsLdpExpNull(Enum):
    """
    MplsLdpExpNull

    Mpls ldp exp null

    .. data:: all = 1

    	Advertise explicit-null for all connected

    	prefixes to all peers

    .. data:: for_ = 2

    	Advertise explicit-null for prefix(es)

    	permitted by prefix ACL

    .. data:: to = 3

    	Advertise explicit-null for all connected

    	prefixes to peer(s) permitted by peer ACL

    .. data:: for_to = 4

    	Advertise explicit-null for prefix(es)

    	permitted by prefix ACL to peer(s) permitted by

    	peer ACL

    """

    all = Enum.YLeaf(1, "all")

    for_ = Enum.YLeaf(2, "for")

    to = Enum.YLeaf(3, "to")

    for_to = Enum.YLeaf(4, "for-to")


class MplsLdpLabelAdvertise(Enum):
    """
    MplsLdpLabelAdvertise

    Mpls ldp label advertise

    .. data:: for_ = 1

    	Advertise label for prefix(es) permitted by

    	prefix ACL

    .. data:: for_to = 2

    	Advertise label for prefix(es) permitted by

    	prefix ACL to peer(s) permitted by peer ACL

    """

    for_ = Enum.YLeaf(1, "for")

    for_to = Enum.YLeaf(2, "for-to")


class MplsLdpLabelAllocation(Enum):
    """
    MplsLdpLabelAllocation

    Mpls ldp label allocation

    .. data:: acl = 1

    	Allocate label for prefixes permitted by ACL

    .. data:: host = 2

    	Allocate label for host routes only

    """

    acl = Enum.YLeaf(1, "acl")

    host = Enum.YLeaf(2, "host")


class MplsLdpNbrPassword(Enum):
    """
    MplsLdpNbrPassword

    Mpls ldp nbr password

    .. data:: disable = 1

    	Disable the global default password for this

    	neighbor

    .. data:: specified = 2

    	Specify a password for this neighbor

    """

    disable = Enum.YLeaf(1, "disable")

    specified = Enum.YLeaf(2, "specified")


class MplsLdpSessionProtection(Enum):
    """
    MplsLdpSessionProtection

    Mpls ldp session protection

    .. data:: all = 1

    	Protect all peer sessions

    .. data:: for_ = 2

    	Protect peer session(s) permitted by peer ACL

    .. data:: all_with_duration = 3

    	Protect all peer sessions and holdup protection

    	for given duration

    .. data:: for_with_duration = 4

    	Protect peer session(s) permitted by peer ACL

    	and holdup protection for given duration

    .. data:: all_with_forever = 5

    	Protect all peer sessions and holdup protection

    	forever

    .. data:: for_with_forever = 6

    	Protect peer session(s) permitted by peer ACL

    	and holdup protection forever

    """

    all = Enum.YLeaf(1, "all")

    for_ = Enum.YLeaf(2, "for")

    all_with_duration = Enum.YLeaf(3, "all-with-duration")

    for_with_duration = Enum.YLeaf(4, "for-with-duration")

    all_with_forever = Enum.YLeaf(5, "all-with-forever")

    for_with_forever = Enum.YLeaf(6, "for-with-forever")


class MplsLdpTargetedAccept(Enum):
    """
    MplsLdpTargetedAccept

    Mpls ldp targeted accept

    .. data:: all = 1

    	Accept targeted hello from all

    .. data:: from_ = 2

    	Accept targeted hello from peer ACL

    """

    all = Enum.YLeaf(1, "all")

    from_ = Enum.YLeaf(2, "from")


class MplsLdpTransportAddress(Enum):
    """
    MplsLdpTransportAddress

    Mpls ldp transport address

    .. data:: interface = 1

    	Use interface IP address

    .. data:: address = 2

    	Use given IP address

    """

    interface = Enum.YLeaf(1, "interface")

    address = Enum.YLeaf(2, "address")


class MplsLdpafName(Enum):
    """
    MplsLdpafName

    Mpls ldpaf name

    .. data:: ipv4 = 4

    	IPv4

    .. data:: ipv6 = 6

    	IPv6

    """

    ipv4 = Enum.YLeaf(4, "ipv4")

    ipv6 = Enum.YLeaf(6, "ipv6")



class MplsLdp(Entity):
    """
    MPLS LDP configuration
    
    .. attribute:: default_vrf
    
    	Global VRF attribute configuration for MPLS LDP
    	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf>`
    
    .. attribute:: enable
    
    	Enable Label Distribution Protocol (LDP) globally.Without creating this object the LDP feature will not be enabled. Deleting this object will stop the LDP feature
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: global_
    
    	Global configuration for MPLS LDP
    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_>`
    
    .. attribute:: vrfs
    
    	VRF Table attribute configuration for MPLS LDP
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs>`
    
    

    """

    _prefix = 'mpls-ldp-cfg'
    _revision = '2017-06-26'

    def __init__(self):
        super(MplsLdp, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-ldp"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-ldp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"default-vrf" : ("default_vrf", MplsLdp.DefaultVrf), "global" : ("global_", MplsLdp.Global_), "vrfs" : ("vrfs", MplsLdp.Vrfs)}
        self._child_list_classes = {}

        self.enable = YLeaf(YType.empty, "enable")

        self.default_vrf = MplsLdp.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"
        self._children_yang_names.add("default-vrf")

        self.global_ = MplsLdp.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.vrfs = MplsLdp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp"

    def __setattr__(self, name, value):
        self._perform_setattr(MplsLdp, ['enable'], name, value)


    class DefaultVrf(Entity):
        """
        Global VRF attribute configuration for MPLS LDP
        
        .. attribute:: afs
        
        	Address Family specific configuration for MPLS LDP
        	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs>`
        
        .. attribute:: global_
        
        	Default VRF Global configuration for MPLS LDP
        	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_>`
        
        .. attribute:: interfaces
        
        	MPLS LDP configuration pertaining to interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces>`
        
        

        """

        _prefix = 'mpls-ldp-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(MplsLdp.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "mpls-ldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"afs" : ("afs", MplsLdp.DefaultVrf.Afs), "global" : ("global_", MplsLdp.DefaultVrf.Global_), "interfaces" : ("interfaces", MplsLdp.DefaultVrf.Interfaces)}
            self._child_list_classes = {}

            self.afs = MplsLdp.DefaultVrf.Afs()
            self.afs.parent = self
            self._children_name_map["afs"] = "afs"
            self._children_yang_names.add("afs")

            self.global_ = MplsLdp.DefaultVrf.Global_()
            self.global_.parent = self
            self._children_name_map["global_"] = "global"
            self._children_yang_names.add("global")

            self.interfaces = MplsLdp.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "default-vrf"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/%s" % self._segment_path()


        class Afs(Entity):
            """
            Address Family specific configuration for MPLS
            LDP
            
            .. attribute:: af
            
            	Configure data for given Address Family
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.DefaultVrf.Afs, self).__init__()

                self.yang_name = "afs"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"af" : ("af", MplsLdp.DefaultVrf.Afs.Af)}

                self.af = YList(self)
                self._segment_path = lambda: "afs"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.DefaultVrf.Afs, [], name, value)


            class Af(Entity):
                """
                Configure data for given Address Family
                
                .. attribute:: af_name  <key>
                
                	Address Family type
                	**type**\:   :py:class:`MplsLdpafName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafName>`
                
                .. attribute:: discovery
                
                	Configure Discovery parameters
                	**type**\:   :py:class:`Discovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Discovery>`
                
                .. attribute:: enable
                
                	Enable Address Family
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: label
                
                	Configure Label policies and control
                	**type**\:   :py:class:`Label <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label>`
                
                .. attribute:: neighbor
                
                	Configuration related to Neighbors
                	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Neighbor>`
                
                .. attribute:: redistribution_protocol
                
                	MPLS LDP configuration for protocol redistribution
                	**type**\:   :py:class:`RedistributionProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol>`
                
                .. attribute:: traffic_engineering
                
                	MPLS Traffic Engingeering parameters for LDP
                	**type**\:   :py:class:`TrafficEngineering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Afs.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "afs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"discovery" : ("discovery", MplsLdp.DefaultVrf.Afs.Af.Discovery), "label" : ("label", MplsLdp.DefaultVrf.Afs.Af.Label), "neighbor" : ("neighbor", MplsLdp.DefaultVrf.Afs.Af.Neighbor), "redistribution-protocol" : ("redistribution_protocol", MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol), "traffic-engineering" : ("traffic_engineering", MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering)}
                    self._child_list_classes = {}

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.discovery = MplsLdp.DefaultVrf.Afs.Af.Discovery()
                    self.discovery.parent = self
                    self._children_name_map["discovery"] = "discovery"
                    self._children_yang_names.add("discovery")

                    self.label = MplsLdp.DefaultVrf.Afs.Af.Label()
                    self.label.parent = self
                    self._children_name_map["label"] = "label"
                    self._children_yang_names.add("label")

                    self.neighbor = MplsLdp.DefaultVrf.Afs.Af.Neighbor()
                    self.neighbor.parent = self
                    self._children_name_map["neighbor"] = "neighbor"
                    self._children_yang_names.add("neighbor")

                    self.redistribution_protocol = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol()
                    self.redistribution_protocol.parent = self
                    self._children_name_map["redistribution_protocol"] = "redistribution-protocol"
                    self._children_yang_names.add("redistribution-protocol")

                    self.traffic_engineering = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering()
                    self.traffic_engineering.parent = self
                    self._children_name_map["traffic_engineering"] = "traffic-engineering"
                    self._children_yang_names.add("traffic-engineering")
                    self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/afs/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af, ['af_name', 'enable'], name, value)


                class Discovery(Entity):
                    """
                    Configure Discovery parameters
                    
                    .. attribute:: targeted_hello_accept
                    
                    	Configure acceptance from and responding to targeted hellos
                    	**type**\:   :py:class:`TargetedHelloAccept <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept>`
                    
                    .. attribute:: transport_address
                    
                    	Global discovery transport address for address family
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.Discovery, self).__init__()

                        self.yang_name = "discovery"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"targeted-hello-accept" : ("targeted_hello_accept", MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept)}
                        self._child_list_classes = {}

                        self.transport_address = YLeaf(YType.str, "transport-address")

                        self.targeted_hello_accept = MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept()
                        self.targeted_hello_accept.parent = self
                        self._children_name_map["targeted_hello_accept"] = "targeted-hello-accept"
                        self._children_yang_names.add("targeted-hello-accept")
                        self._segment_path = lambda: "discovery"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Discovery, ['transport_address'], name, value)


                    class TargetedHelloAccept(Entity):
                        """
                        Configure acceptance from and responding to
                        targeted hellos.
                        
                        .. attribute:: accept_type
                        
                        	Type of acceptance
                        	**type**\:   :py:class:`MplsLdpTargetedAccept <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpTargetedAccept>`
                        
                        .. attribute:: peer_acl_name
                        
                        	Name of peer ACL
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept, self).__init__()

                            self.yang_name = "targeted-hello-accept"
                            self.yang_parent_name = "discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.accept_type = YLeaf(YType.enumeration, "accept-type")

                            self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")
                            self._segment_path = lambda: "targeted-hello-accept"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept, ['accept_type', 'peer_acl_name'], name, value)


                class Label(Entity):
                    """
                    Configure Label policies and control
                    
                    .. attribute:: local
                    
                    	Configure local label policies and control
                    	**type**\:   :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local>`
                    
                    .. attribute:: remote
                    
                    	Configure remote/peer label policies and control
                    	**type**\:   :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Remote>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.Label, self).__init__()

                        self.yang_name = "label"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"local" : ("local", MplsLdp.DefaultVrf.Afs.Af.Label.Local), "remote" : ("remote", MplsLdp.DefaultVrf.Afs.Af.Label.Remote)}
                        self._child_list_classes = {}

                        self.local = MplsLdp.DefaultVrf.Afs.Af.Label.Local()
                        self.local.parent = self
                        self._children_name_map["local"] = "local"
                        self._children_yang_names.add("local")

                        self.remote = MplsLdp.DefaultVrf.Afs.Af.Label.Remote()
                        self.remote.parent = self
                        self._children_name_map["remote"] = "remote"
                        self._children_yang_names.add("remote")
                        self._segment_path = lambda: "label"


                    class Local(Entity):
                        """
                        Configure local label policies and control
                        
                        .. attribute:: advertise
                        
                        	Configure outbound label advertisement
                        	**type**\:   :py:class:`Advertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise>`
                        
                        .. attribute:: allocate
                        
                        	Control local label allocation for prefix(es)
                        	**type**\:   :py:class:`Allocate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate>`
                        
                        .. attribute:: default_route
                        
                        	Enable MPLS forwarding for default route
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: implicit_null_override
                        
                        	Control use of implicit\-null label for set of prefix(es)
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Local, self).__init__()

                            self.yang_name = "local"
                            self.yang_parent_name = "label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"advertise" : ("advertise", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise), "allocate" : ("allocate", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate)}
                            self._child_list_classes = {}

                            self.default_route = YLeaf(YType.empty, "default-route")

                            self.implicit_null_override = YLeaf(YType.str, "implicit-null-override")

                            self.advertise = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise()
                            self.advertise.parent = self
                            self._children_name_map["advertise"] = "advertise"
                            self._children_yang_names.add("advertise")

                            self.allocate = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate()
                            self.allocate.parent = self
                            self._children_name_map["allocate"] = "allocate"
                            self._children_yang_names.add("allocate")
                            self._segment_path = lambda: "local"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local, ['default_route', 'implicit_null_override'], name, value)


                        class Advertise(Entity):
                            """
                            Configure outbound label advertisement
                            
                            .. attribute:: disable
                            
                            	Disable label advertisement
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: explicit_null
                            
                            	Configure advertisment of explicit\-null for connected prefixes
                            	**type**\:   :py:class:`ExplicitNull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull>`
                            
                            .. attribute:: interfaces
                            
                            	Configure outbound label advertisement for an interface
                            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces>`
                            
                            .. attribute:: peer_advertise_policies
                            
                            	Configure peer centric outbound label advertisement using ACL
                            	**type**\:   :py:class:`PeerAdvertisePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies>`
                            
                            .. attribute:: prefix_advertise_policies
                            
                            	Configure prefix centric outbound label advertisement using ACL
                            	**type**\:   :py:class:`PrefixAdvertisePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise, self).__init__()

                                self.yang_name = "advertise"
                                self.yang_parent_name = "local"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"explicit-null" : ("explicit_null", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull), "interfaces" : ("interfaces", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces), "peer-advertise-policies" : ("peer_advertise_policies", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies), "prefix-advertise-policies" : ("prefix_advertise_policies", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies)}
                                self._child_list_classes = {}

                                self.disable = YLeaf(YType.empty, "disable")

                                self.explicit_null = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull()
                                self.explicit_null.parent = self
                                self._children_name_map["explicit_null"] = "explicit-null"
                                self._children_yang_names.add("explicit-null")

                                self.interfaces = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces()
                                self.interfaces.parent = self
                                self._children_name_map["interfaces"] = "interfaces"
                                self._children_yang_names.add("interfaces")

                                self.peer_advertise_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies()
                                self.peer_advertise_policies.parent = self
                                self._children_name_map["peer_advertise_policies"] = "peer-advertise-policies"
                                self._children_yang_names.add("peer-advertise-policies")

                                self.prefix_advertise_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies()
                                self.prefix_advertise_policies.parent = self
                                self._children_name_map["prefix_advertise_policies"] = "prefix-advertise-policies"
                                self._children_yang_names.add("prefix-advertise-policies")
                                self._segment_path = lambda: "advertise"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise, ['disable'], name, value)


                            class ExplicitNull(Entity):
                                """
                                Configure advertisment of explicit\-null
                                for connected prefixes.
                                
                                .. attribute:: explicit_null_type
                                
                                	Explicit Null command variant
                                	**type**\:   :py:class:`MplsLdpExpNull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpExpNull>`
                                
                                .. attribute:: peer_acl_name
                                
                                	Name of peer ACL
                                	**type**\:  str
                                
                                .. attribute:: prefix_acl_name
                                
                                	Name of prefix ACL
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull, self).__init__()

                                    self.yang_name = "explicit-null"
                                    self.yang_parent_name = "advertise"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.explicit_null_type = YLeaf(YType.enumeration, "explicit-null-type")

                                    self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                                    self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                    self._segment_path = lambda: "explicit-null"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull, ['explicit_null_type', 'peer_acl_name', 'prefix_acl_name'], name, value)


                            class Interfaces(Entity):
                                """
                                Configure outbound label advertisement for
                                an interface
                                
                                .. attribute:: interface
                                
                                	Control advertisement of interface's host IP address
                                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces, self).__init__()

                                    self.yang_name = "interfaces"
                                    self.yang_parent_name = "advertise"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"interface" : ("interface", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface)}

                                    self.interface = YList(self)
                                    self._segment_path = lambda: "interfaces"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces, [], name, value)


                                class Interface(Entity):
                                    """
                                    Control advertisement of interface's host
                                    IP address
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Name of interface
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, self).__init__()

                                        self.yang_name = "interface"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")
                                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, ['interface_name'], name, value)


                            class PeerAdvertisePolicies(Entity):
                                """
                                Configure peer centric outbound label
                                advertisement using ACL
                                
                                .. attribute:: peer_advertise_policy
                                
                                	Control advertisement of prefix(es) using ACL
                                	**type**\: list of    :py:class:`PeerAdvertisePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, self).__init__()

                                    self.yang_name = "peer-advertise-policies"
                                    self.yang_parent_name = "advertise"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"peer-advertise-policy" : ("peer_advertise_policy", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy)}

                                    self.peer_advertise_policy = YList(self)
                                    self._segment_path = lambda: "peer-advertise-policies"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, [], name, value)


                                class PeerAdvertisePolicy(Entity):
                                    """
                                    Control advertisement of prefix(es) using
                                    ACL
                                    
                                    .. attribute:: lsr_id  <key>
                                    
                                    	LSR ID of neighbor
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: label_space_id  <key>
                                    
                                    	Label space ID of neighbor
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: prefix_acl_name
                                    
                                    	Name of prefix ACL
                                    	**type**\:  str
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, self).__init__()

                                        self.yang_name = "peer-advertise-policy"
                                        self.yang_parent_name = "peer-advertise-policies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.lsr_id = YLeaf(YType.str, "lsr-id")

                                        self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                        self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                        self._segment_path = lambda: "peer-advertise-policy" + "[lsr-id='" + self.lsr_id.get() + "']" + "[label-space-id='" + self.label_space_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, ['lsr_id', 'label_space_id', 'prefix_acl_name'], name, value)


                            class PrefixAdvertisePolicies(Entity):
                                """
                                Configure prefix centric outbound label
                                advertisement using ACL
                                
                                .. attribute:: prefix_advertise_policy
                                
                                	Control advertisement of prefix(es) using ACL
                                	**type**\: list of    :py:class:`PrefixAdvertisePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies, self).__init__()

                                    self.yang_name = "prefix-advertise-policies"
                                    self.yang_parent_name = "advertise"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"prefix-advertise-policy" : ("prefix_advertise_policy", MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy)}

                                    self.prefix_advertise_policy = YList(self)
                                    self._segment_path = lambda: "prefix-advertise-policies"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies, [], name, value)


                                class PrefixAdvertisePolicy(Entity):
                                    """
                                    Control advertisement of prefix(es) using
                                    ACL
                                    
                                    .. attribute:: prefix_acl_name  <key>
                                    
                                    	Name of prefix ACL
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: advertise_type
                                    
                                    	Label advertise type
                                    	**type**\:   :py:class:`MplsLdpLabelAdvertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpLabelAdvertise>`
                                    
                                    .. attribute:: peer_acl_name
                                    
                                    	Name of peer ACL
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy, self).__init__()

                                        self.yang_name = "prefix-advertise-policy"
                                        self.yang_parent_name = "prefix-advertise-policies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                        self.advertise_type = YLeaf(YType.enumeration, "advertise-type")

                                        self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")
                                        self._segment_path = lambda: "prefix-advertise-policy" + "[prefix-acl-name='" + self.prefix_acl_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy, ['prefix_acl_name', 'advertise_type', 'peer_acl_name'], name, value)


                        class Allocate(Entity):
                            """
                            Control local label allocation for
                            prefix(es)
                            
                            .. attribute:: allocation_type
                            
                            	Label allocation type
                            	**type**\:   :py:class:`MplsLdpLabelAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpLabelAllocation>`
                            
                            .. attribute:: prefix_acl_name
                            
                            	Name of prefix ACL
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate, self).__init__()

                                self.yang_name = "allocate"
                                self.yang_parent_name = "local"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.allocation_type = YLeaf(YType.enumeration, "allocation-type")

                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                self._segment_path = lambda: "allocate"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate, ['allocation_type', 'prefix_acl_name'], name, value)


                    class Remote(Entity):
                        """
                        Configure remote/peer label policies and
                        control
                        
                        .. attribute:: accept
                        
                        	Configure inbound label acceptance
                        	**type**\:   :py:class:`Accept <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote, self).__init__()

                            self.yang_name = "remote"
                            self.yang_parent_name = "label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"accept" : ("accept", MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept)}
                            self._child_list_classes = {}

                            self.accept = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept()
                            self.accept.parent = self
                            self._children_name_map["accept"] = "accept"
                            self._children_yang_names.add("accept")
                            self._segment_path = lambda: "remote"


                        class Accept(Entity):
                            """
                            Configure inbound label acceptance
                            
                            .. attribute:: peer_accept_policies
                            
                            	Configuration related to neighbors for inbound label acceptance
                            	**type**\:   :py:class:`PeerAcceptPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept, self).__init__()

                                self.yang_name = "accept"
                                self.yang_parent_name = "remote"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"peer-accept-policies" : ("peer_accept_policies", MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies)}
                                self._child_list_classes = {}

                                self.peer_accept_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies()
                                self.peer_accept_policies.parent = self
                                self._children_name_map["peer_accept_policies"] = "peer-accept-policies"
                                self._children_yang_names.add("peer-accept-policies")
                                self._segment_path = lambda: "accept"


                            class PeerAcceptPolicies(Entity):
                                """
                                Configuration related to neighbors for
                                inbound label acceptance
                                
                                .. attribute:: peer_accept_policy
                                
                                	Control acceptance of labels from a neighbor for prefix(es) using ACL
                                	**type**\: list of    :py:class:`PeerAcceptPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, self).__init__()

                                    self.yang_name = "peer-accept-policies"
                                    self.yang_parent_name = "accept"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"peer-accept-policy" : ("peer_accept_policy", MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy)}

                                    self.peer_accept_policy = YList(self)
                                    self._segment_path = lambda: "peer-accept-policies"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, [], name, value)


                                class PeerAcceptPolicy(Entity):
                                    """
                                    Control acceptance of labels from a
                                    neighbor for prefix(es) using ACL
                                    
                                    .. attribute:: lsr_id  <key>
                                    
                                    	LSR ID of neighbor
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: label_space_id  <key>
                                    
                                    	Label space ID of neighbor
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: prefix_acl_name
                                    
                                    	Name of prefix ACL
                                    	**type**\:  str
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, self).__init__()

                                        self.yang_name = "peer-accept-policy"
                                        self.yang_parent_name = "peer-accept-policies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.lsr_id = YLeaf(YType.str, "lsr-id")

                                        self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                        self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                        self._segment_path = lambda: "peer-accept-policy" + "[lsr-id='" + self.lsr_id.get() + "']" + "[label-space-id='" + self.label_space_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, ['lsr_id', 'label_space_id', 'prefix_acl_name'], name, value)


                class Neighbor(Entity):
                    """
                    Configuration related to Neighbors
                    
                    .. attribute:: addresses
                    
                    	Configuration related to neighbors using neighbor address
                    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.Neighbor, self).__init__()

                        self.yang_name = "neighbor"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"addresses" : ("addresses", MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses)}
                        self._child_list_classes = {}

                        self.addresses = MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"
                        self._children_yang_names.add("addresses")
                        self._segment_path = lambda: "neighbor"


                    class Addresses(Entity):
                        """
                        Configuration related to neighbors using
                        neighbor address
                        
                        .. attribute:: address
                        
                        	IP address based configuration related to a neighbor
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"address" : ("address", MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address)}

                            self.address = YList(self)
                            self._segment_path = lambda: "addresses"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses, [], name, value)


                        class Address(Entity):
                            """
                            IP address based configuration related to a
                            neighbor
                            
                            .. attribute:: ip_address  <key>
                            
                            	The IP address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: targeted
                            
                            	Establish targeted session with given address
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip_address = YLeaf(YType.str, "ip-address")

                                self.targeted = YLeaf(YType.empty, "targeted")
                                self._segment_path = lambda: "address" + "[ip-address='" + self.ip_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address, ['ip_address', 'targeted'], name, value)


                class RedistributionProtocol(Entity):
                    """
                    MPLS LDP configuration for protocol
                    redistribution
                    
                    .. attribute:: bgp
                    
                    	MPLS LDP configuration for protocol redistribution
                    	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol, self).__init__()

                        self.yang_name = "redistribution-protocol"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"bgp" : ("bgp", MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp)}
                        self._child_list_classes = {}

                        self.bgp = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp()
                        self.bgp.parent = self
                        self._children_name_map["bgp"] = "bgp"
                        self._children_yang_names.add("bgp")
                        self._segment_path = lambda: "redistribution-protocol"


                    class Bgp(Entity):
                        """
                        MPLS LDP configuration for protocol
                        redistribution
                        
                        .. attribute:: advertise_to
                        
                        	ACL containing list of neighbors for BGP route redistribution
                        	**type**\:   :py:class:`AdvertiseTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo>`
                        
                        .. attribute:: as_
                        
                        	MPLS LDP configuration for protocol redistribution
                        	**type**\:   :py:class:`As_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp, self).__init__()

                            self.yang_name = "bgp"
                            self.yang_parent_name = "redistribution-protocol"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"advertise-to" : ("advertise_to", MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo), "as" : ("as_", MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_)}
                            self._child_list_classes = {}

                            self.advertise_to = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo()
                            self.advertise_to.parent = self
                            self._children_name_map["advertise_to"] = "advertise-to"
                            self._children_yang_names.add("advertise-to")

                            self.as_ = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_()
                            self.as_.parent = self
                            self._children_name_map["as_"] = "as"
                            self._children_yang_names.add("as")
                            self._segment_path = lambda: "bgp"


                        class AdvertiseTo(Entity):
                            """
                            ACL containing list of neighbors for BGP
                            route redistribution
                            
                            .. attribute:: peer_acl_name
                            
                            	Name of peer ACL
                            	**type**\:  str
                            
                            .. attribute:: type
                            
                            	advertise to peer acl type
                            	**type**\:   :py:class:`MplsLdpAdvertiseBgpAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpAdvertiseBgpAcl>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo, self).__init__()

                                self.yang_name = "advertise-to"
                                self.yang_parent_name = "bgp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                                self.type = YLeaf(YType.enumeration, "type")
                                self._segment_path = lambda: "advertise-to"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo, ['peer_acl_name', 'type'], name, value)


                        class As_(Entity):
                            """
                            MPLS LDP configuration for protocol
                            redistribution
                            
                            .. attribute:: as_xx
                            
                            	First half of BGP AS number in XX.YY format.  Mandatory Must be a non\-zero value if second half is zero
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: as_yy
                            
                            	Second half of BGP AS number in XX.YY format. Mandatory Must be a non\-zero value if first half is zero
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_, self).__init__()

                                self.yang_name = "as"
                                self.yang_parent_name = "bgp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.as_xx = YLeaf(YType.uint32, "as-xx")

                                self.as_yy = YLeaf(YType.uint32, "as-yy")
                                self._segment_path = lambda: "as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_, ['as_xx', 'as_yy'], name, value)


                class TrafficEngineering(Entity):
                    """
                    MPLS Traffic Engingeering parameters for LDP
                    
                    .. attribute:: auto_tunnel_mesh
                    
                    	MPLS Traffic Engineering auto\-tunnel mesh parameters for LDP
                    	**type**\:   :py:class:`AutoTunnelMesh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering, self).__init__()

                        self.yang_name = "traffic-engineering"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"auto-tunnel-mesh" : ("auto_tunnel_mesh", MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh)}
                        self._child_list_classes = {}

                        self.auto_tunnel_mesh = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh()
                        self.auto_tunnel_mesh.parent = self
                        self._children_name_map["auto_tunnel_mesh"] = "auto-tunnel-mesh"
                        self._children_yang_names.add("auto-tunnel-mesh")
                        self._segment_path = lambda: "traffic-engineering"


                    class AutoTunnelMesh(Entity):
                        """
                        MPLS Traffic Engineering auto\-tunnel mesh
                        parameters for LDP
                        
                        .. attribute:: group_all
                        
                        	Enable all MPLS TE auto\-tunnel mesh\-group interfaces
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: group_ids
                        
                        	Enable interfaces in specific MPLS TE auto\-tunnel mesh\-groups
                        	**type**\:   :py:class:`GroupIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh, self).__init__()

                            self.yang_name = "auto-tunnel-mesh"
                            self.yang_parent_name = "traffic-engineering"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"group-ids" : ("group_ids", MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds)}
                            self._child_list_classes = {}

                            self.group_all = YLeaf(YType.empty, "group-all")

                            self.group_ids = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds()
                            self.group_ids.parent = self
                            self._children_name_map["group_ids"] = "group-ids"
                            self._children_yang_names.add("group-ids")
                            self._segment_path = lambda: "auto-tunnel-mesh"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh, ['group_all'], name, value)


                        class GroupIds(Entity):
                            """
                            Enable interfaces in specific MPLS TE
                            auto\-tunnel mesh\-groups
                            
                            .. attribute:: group_id
                            
                            	Auto\-mesh group identifier to enable
                            	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds, self).__init__()

                                self.yang_name = "group-ids"
                                self.yang_parent_name = "auto-tunnel-mesh"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"group-id" : ("group_id", MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId)}

                                self.group_id = YList(self)
                                self._segment_path = lambda: "group-ids"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds, [], name, value)


                            class GroupId(Entity):
                                """
                                Auto\-mesh group identifier to enable
                                
                                .. attribute:: mesh_group_id  <key>
                                
                                	Mesh group ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId, self).__init__()

                                    self.yang_name = "group-id"
                                    self.yang_parent_name = "group-ids"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.mesh_group_id = YLeaf(YType.uint32, "mesh-group-id")
                                    self._segment_path = lambda: "group-id" + "[mesh-group-id='" + self.mesh_group_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId, ['mesh_group_id'], name, value)


        class Global_(Entity):
            """
            Default VRF Global configuration for MPLS LDP
            
            .. attribute:: graceful_restart
            
            	Configuration for per\-VRF LDP Graceful Restart parameters
            	**type**\:   :py:class:`GracefulRestart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.GracefulRestart>`
            
            .. attribute:: neighbor
            
            	Configuration related to Neighbors
            	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Neighbor>`
            
            .. attribute:: router_id
            
            	Configuration for LDP Router ID (LDP ID)
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: session
            
            	LDP Session parameters
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Session>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.DefaultVrf.Global_, self).__init__()

                self.yang_name = "global"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"graceful-restart" : ("graceful_restart", MplsLdp.DefaultVrf.Global_.GracefulRestart), "neighbor" : ("neighbor", MplsLdp.DefaultVrf.Global_.Neighbor), "session" : ("session", MplsLdp.DefaultVrf.Global_.Session)}
                self._child_list_classes = {}

                self.router_id = YLeaf(YType.str, "router-id")

                self.graceful_restart = MplsLdp.DefaultVrf.Global_.GracefulRestart()
                self.graceful_restart.parent = self
                self._children_name_map["graceful_restart"] = "graceful-restart"
                self._children_yang_names.add("graceful-restart")

                self.neighbor = MplsLdp.DefaultVrf.Global_.Neighbor()
                self.neighbor.parent = self
                self._children_name_map["neighbor"] = "neighbor"
                self._children_yang_names.add("neighbor")

                self.session = MplsLdp.DefaultVrf.Global_.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._children_yang_names.add("session")
                self._segment_path = lambda: "global"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.DefaultVrf.Global_, ['router_id'], name, value)


            class GracefulRestart(Entity):
                """
                Configuration for per\-VRF LDP Graceful Restart
                parameters
                
                .. attribute:: helper_peer
                
                	Configure parameters related to GR peer(s) opearating in helper mode
                	**type**\:   :py:class:`HelperPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Global_.GracefulRestart, self).__init__()

                    self.yang_name = "graceful-restart"
                    self.yang_parent_name = "global"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"helper-peer" : ("helper_peer", MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer)}
                    self._child_list_classes = {}

                    self.helper_peer = MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer()
                    self.helper_peer.parent = self
                    self._children_name_map["helper_peer"] = "helper-peer"
                    self._children_yang_names.add("helper-peer")
                    self._segment_path = lambda: "graceful-restart"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/%s" % self._segment_path()


                class HelperPeer(Entity):
                    """
                    Configure parameters related to GR peer(s)
                    opearating in helper mode
                    
                    .. attribute:: maintain_on_local_reset
                    
                    	Maintain the state of a GR peer upon a local reset
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer, self).__init__()

                        self.yang_name = "helper-peer"
                        self.yang_parent_name = "graceful-restart"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.maintain_on_local_reset = YLeaf(YType.str, "maintain-on-local-reset")
                        self._segment_path = lambda: "helper-peer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/graceful-restart/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer, ['maintain_on_local_reset'], name, value)


            class Neighbor(Entity):
                """
                Configuration related to Neighbors
                
                .. attribute:: dual_stack
                
                	Configuration related to neighbor transport
                	**type**\:   :py:class:`DualStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Neighbor.DualStack>`
                
                .. attribute:: ldp_ids
                
                	Configuration related to Neighbors using LDP Id
                	**type**\:   :py:class:`LdpIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds>`
                
                .. attribute:: password
                
                	Default password for all neigbors
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Global_.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "global"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"dual-stack" : ("dual_stack", MplsLdp.DefaultVrf.Global_.Neighbor.DualStack), "ldp-ids" : ("ldp_ids", MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds)}
                    self._child_list_classes = {}

                    self.password = YLeaf(YType.str, "password")

                    self.dual_stack = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack()
                    self.dual_stack.parent = self
                    self._children_name_map["dual_stack"] = "dual-stack"
                    self._children_yang_names.add("dual-stack")

                    self.ldp_ids = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds()
                    self.ldp_ids.parent = self
                    self._children_name_map["ldp_ids"] = "ldp-ids"
                    self._children_yang_names.add("ldp-ids")
                    self._segment_path = lambda: "neighbor"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.DefaultVrf.Global_.Neighbor, ['password'], name, value)


                class DualStack(Entity):
                    """
                    Configuration related to neighbor transport
                    
                    .. attribute:: tlv_compliance
                    
                    	Configuration to enable neighbor dual\-stack tlv\-compliance
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: transport_connection
                    
                    	Configuration related to neighbor transport
                    	**type**\:   :py:class:`TransportConnection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack, self).__init__()

                        self.yang_name = "dual-stack"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"transport-connection" : ("transport_connection", MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection)}
                        self._child_list_classes = {}

                        self.tlv_compliance = YLeaf(YType.empty, "tlv-compliance")

                        self.transport_connection = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection()
                        self.transport_connection.parent = self
                        self._children_name_map["transport_connection"] = "transport-connection"
                        self._children_yang_names.add("transport-connection")
                        self._segment_path = lambda: "dual-stack"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack, ['tlv_compliance'], name, value)


                    class TransportConnection(Entity):
                        """
                        Configuration related to neighbor transport
                        
                        .. attribute:: max_wait
                        
                        	Configuration related to neighbor dual\-stack xport\-connection max\-wait
                        	**type**\:  int
                        
                        	**range:** 0..60
                        
                        	**units**\: second
                        
                        .. attribute:: prefer
                        
                        	Configuration related to neighbor dual\-stack xport\-connection preference
                        	**type**\:   :py:class:`Prefer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection, self).__init__()

                            self.yang_name = "transport-connection"
                            self.yang_parent_name = "dual-stack"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"prefer" : ("prefer", MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer)}
                            self._child_list_classes = {}

                            self.max_wait = YLeaf(YType.uint32, "max-wait")

                            self.prefer = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer()
                            self.prefer.parent = self
                            self._children_name_map["prefer"] = "prefer"
                            self._children_yang_names.add("prefer")
                            self._segment_path = lambda: "transport-connection"
                            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/dual-stack/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection, ['max_wait'], name, value)


                        class Prefer(Entity):
                            """
                            Configuration related to neighbor
                            dual\-stack xport\-connection preference
                            
                            .. attribute:: ipv4
                            
                            	Configuration related to neighbor dual\-stack xport\-connection preference ipv4
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer, self).__init__()

                                self.yang_name = "prefer"
                                self.yang_parent_name = "transport-connection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ipv4 = YLeaf(YType.empty, "ipv4")
                                self._segment_path = lambda: "prefer"
                                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/dual-stack/transport-connection/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer, ['ipv4'], name, value)


                class LdpIds(Entity):
                    """
                    Configuration related to Neighbors using LDP
                    Id
                    
                    .. attribute:: ldp_id
                    
                    	LDP ID based configuration related to a neigbor
                    	**type**\: list of    :py:class:`LdpId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds, self).__init__()

                        self.yang_name = "ldp-ids"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"ldp-id" : ("ldp_id", MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId)}

                        self.ldp_id = YList(self)
                        self._segment_path = lambda: "ldp-ids"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds, [], name, value)


                    class LdpId(Entity):
                        """
                        LDP ID based configuration related to a
                        neigbor
                        
                        .. attribute:: lsr_id  <key>
                        
                        	LSR ID of neighbor
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: label_space_id  <key>
                        
                        	Label space ID of neighbor
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: password
                        
                        	Password for MD5 authentication for this neighbor
                        	**type**\:   :py:class:`Password <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId, self).__init__()

                            self.yang_name = "ldp-id"
                            self.yang_parent_name = "ldp-ids"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"password" : ("password", MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password)}
                            self._child_list_classes = {}

                            self.lsr_id = YLeaf(YType.str, "lsr-id")

                            self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                            self.password = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password()
                            self.password.parent = self
                            self._children_name_map["password"] = "password"
                            self._children_yang_names.add("password")
                            self._segment_path = lambda: "ldp-id" + "[lsr-id='" + self.lsr_id.get() + "']" + "[label-space-id='" + self.label_space_id.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/ldp-ids/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId, ['lsr_id', 'label_space_id'], name, value)


                        class Password(Entity):
                            """
                            Password for MD5 authentication for this
                            neighbor
                            
                            .. attribute:: command_type
                            
                            	Command type for password configuration
                            	**type**\:   :py:class:`MplsLdpNbrPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpNbrPassword>`
                            
                            .. attribute:: password
                            
                            	The neighbor password
                            	**type**\:  str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password, self).__init__()

                                self.yang_name = "password"
                                self.yang_parent_name = "ldp-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.command_type = YLeaf(YType.enumeration, "command-type")

                                self.password = YLeaf(YType.str, "password")
                                self._segment_path = lambda: "password"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password, ['command_type', 'password'], name, value)


            class Session(Entity):
                """
                LDP Session parameters
                
                .. attribute:: downstream_on_demand
                
                	ACL with the list of neighbors configured for Downstream on Demand
                	**type**\:   :py:class:`DownstreamOnDemand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand>`
                
                .. attribute:: protection
                
                	Configure Session Protection parameters
                	**type**\:   :py:class:`Protection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Session.Protection>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Global_.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "global"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"downstream-on-demand" : ("downstream_on_demand", MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand), "protection" : ("protection", MplsLdp.DefaultVrf.Global_.Session.Protection)}
                    self._child_list_classes = {}

                    self.downstream_on_demand = MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand()
                    self.downstream_on_demand.parent = self
                    self._children_name_map["downstream_on_demand"] = "downstream-on-demand"
                    self._children_yang_names.add("downstream-on-demand")

                    self.protection = MplsLdp.DefaultVrf.Global_.Session.Protection()
                    self.protection.parent = self
                    self._children_name_map["protection"] = "protection"
                    self._children_yang_names.add("protection")
                    self._segment_path = lambda: "session"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/%s" % self._segment_path()


                class DownstreamOnDemand(Entity):
                    """
                    ACL with the list of neighbors configured for
                    Downstream on Demand
                    
                    .. attribute:: peer_acl_name
                    
                    	Name of peer ACL
                    	**type**\:  str
                    
                    .. attribute:: type
                    
                    	Downstream on demand type
                    	**type**\:   :py:class:`MplsLdpDownstreamOnDemand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpDownstreamOnDemand>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand, self).__init__()

                        self.yang_name = "downstream-on-demand"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                        self.type = YLeaf(YType.enumeration, "type")
                        self._segment_path = lambda: "downstream-on-demand"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/session/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand, ['peer_acl_name', 'type'], name, value)


                class Protection(Entity):
                    """
                    Configure Session Protection parameters
                    
                    .. attribute:: duration
                    
                    	Holdup duration
                    	**type**\:  int
                    
                    	**range:** 30..2147483
                    
                    .. attribute:: peer_acl_name
                    
                    	Name of peer ACL
                    	**type**\:  str
                    
                    .. attribute:: protection_type
                    
                    	Session protection type
                    	**type**\:   :py:class:`MplsLdpSessionProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpSessionProtection>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.Session.Protection, self).__init__()

                        self.yang_name = "protection"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.duration = YLeaf(YType.uint32, "duration")

                        self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                        self.protection_type = YLeaf(YType.enumeration, "protection-type")
                        self._segment_path = lambda: "protection"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/session/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.DefaultVrf.Global_.Session.Protection, ['duration', 'peer_acl_name', 'protection_type'], name, value)


        class Interfaces(Entity):
            """
            MPLS LDP configuration pertaining to interfaces
            
            .. attribute:: interface
            
            	MPLS LDP configuration for a particular interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.DefaultVrf.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", MplsLdp.DefaultVrf.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.DefaultVrf.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MPLS LDP configuration for a particular
                interface
                
                .. attribute:: interface_name  <key>
                
                	Name of interface
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: afs
                
                	Address Family specific configuration for MPLS LDP intf
                	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs>`
                
                .. attribute:: enable
                
                	Enable Label Distribution Protocol (LDP) on thisinterface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: global_
                
                	Per VRF interface Global configuration for MPLS LDP
                	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"afs" : ("afs", MplsLdp.DefaultVrf.Interfaces.Interface.Afs), "global" : ("global_", MplsLdp.DefaultVrf.Interfaces.Interface.Global_)}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.afs = MplsLdp.DefaultVrf.Interfaces.Interface.Afs()
                    self.afs.parent = self
                    self._children_name_map["afs"] = "afs"
                    self._children_yang_names.add("afs")

                    self.global_ = MplsLdp.DefaultVrf.Interfaces.Interface.Global_()
                    self.global_.parent = self
                    self._children_name_map["global_"] = "global"
                    self._children_yang_names.add("global")
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface, ['interface_name', 'enable'], name, value)


                class Afs(Entity):
                    """
                    Address Family specific configuration for
                    MPLS LDP intf
                    
                    .. attribute:: af
                    
                    	Configure data for given Address Family
                    	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs, self).__init__()

                        self.yang_name = "afs"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"af" : ("af", MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af)}

                        self.af = YList(self)
                        self._segment_path = lambda: "afs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface.Afs, [], name, value)


                    class Af(Entity):
                        """
                        Configure data for given Address Family
                        
                        .. attribute:: af_name  <key>
                        
                        	Address Family name
                        	**type**\:   :py:class:`MplsLdpafName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafName>`
                        
                        .. attribute:: discovery
                        
                        	Configure interface discovery parameters
                        	**type**\:   :py:class:`Discovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery>`
                        
                        .. attribute:: enable
                        
                        	Enable Address Family
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: igp
                        
                        	LDP interface IGP configuration
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp>`
                        
                        .. attribute:: mldp
                        
                        	Interface configuration parameters for mLDP
                        	**type**\:   :py:class:`Mldp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af, self).__init__()

                            self.yang_name = "af"
                            self.yang_parent_name = "afs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"discovery" : ("discovery", MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery), "igp" : ("igp", MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp), "mldp" : ("mldp", MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp)}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.enable = YLeaf(YType.empty, "enable")

                            self.discovery = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery()
                            self.discovery.parent = self
                            self._children_name_map["discovery"] = "discovery"
                            self._children_yang_names.add("discovery")

                            self.igp = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._children_yang_names.add("igp")

                            self.mldp = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp()
                            self.mldp.parent = self
                            self._children_name_map["mldp"] = "mldp"
                            self._children_yang_names.add("mldp")
                            self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af, ['af_name', 'enable'], name, value)


                        class Discovery(Entity):
                            """
                            Configure interface discovery parameters
                            
                            .. attribute:: transport_address
                            
                            	MPLS LDP configuration for interface discovery transportaddress
                            	**type**\:   :py:class:`TransportAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery, self).__init__()

                                self.yang_name = "discovery"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"transport-address" : ("transport_address", MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress)}
                                self._child_list_classes = {}

                                self.transport_address = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress()
                                self.transport_address.parent = self
                                self._children_name_map["transport_address"] = "transport-address"
                                self._children_yang_names.add("transport-address")
                                self._segment_path = lambda: "discovery"


                            class TransportAddress(Entity):
                                """
                                MPLS LDP configuration for interface
                                discovery transportaddress.
                                
                                .. attribute:: address
                                
                                	IP address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: address_type
                                
                                	Transport address option
                                	**type**\:   :py:class:`MplsLdpTransportAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpTransportAddress>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, self).__init__()

                                    self.yang_name = "transport-address"
                                    self.yang_parent_name = "discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.address_type = YLeaf(YType.enumeration, "address-type")
                                    self._segment_path = lambda: "transport-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, ['address', 'address_type'], name, value)


                        class Igp(Entity):
                            """
                            LDP interface IGP configuration
                            
                            .. attribute:: disable_auto_config
                            
                            	Disable IGP Auto\-config on this interface
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.disable_auto_config = YLeaf(YType.empty, "disable-auto-config")
                                self._segment_path = lambda: "igp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp, ['disable_auto_config'], name, value)


                        class Mldp(Entity):
                            """
                            Interface configuration parameters for mLDP
                            
                            .. attribute:: disable
                            
                            	Disable mLDP on LDP enabled interface
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp, self).__init__()

                                self.yang_name = "mldp"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.disable = YLeaf(YType.empty, "disable")
                                self._segment_path = lambda: "mldp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp, ['disable'], name, value)


                class Global_(Entity):
                    """
                    Per VRF interface Global configuration for
                    MPLS LDP
                    
                    .. attribute:: discovery
                    
                    	Configure interface discovery parameters
                    	**type**\:   :py:class:`Discovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery>`
                    
                    .. attribute:: igp
                    
                    	LDP IGP configuration
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_, self).__init__()

                        self.yang_name = "global"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"discovery" : ("discovery", MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery), "igp" : ("igp", MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp)}
                        self._child_list_classes = {}

                        self.discovery = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery()
                        self.discovery.parent = self
                        self._children_name_map["discovery"] = "discovery"
                        self._children_yang_names.add("discovery")

                        self.igp = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "global"


                    class Discovery(Entity):
                        """
                        Configure interface discovery parameters
                        
                        .. attribute:: disable_quick_start
                        
                        	Disable discovery's quick start mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: link_hello
                        
                        	LDP Link Hellos
                        	**type**\:   :py:class:`LinkHello <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery, self).__init__()

                            self.yang_name = "discovery"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"link-hello" : ("link_hello", MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello)}
                            self._child_list_classes = {}

                            self.disable_quick_start = YLeaf(YType.empty, "disable-quick-start")

                            self.link_hello = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello()
                            self.link_hello.parent = self
                            self._children_name_map["link_hello"] = "link-hello"
                            self._children_yang_names.add("link-hello")
                            self._segment_path = lambda: "discovery"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery, ['disable_quick_start'], name, value)


                        class LinkHello(Entity):
                            """
                            LDP Link Hellos
                            
                            .. attribute:: dual_stack
                            
                            	Dual Stack Address Family Preference
                            	**type**\:   :py:class:`MplsLdpafName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafName>`
                            
                            	**default value**\: ipv4
                            
                            .. attribute:: hold_time
                            
                            	Time (seconds) \- 65535 implies infinite
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            	**units**\: second
                            
                            	**default value**\: 15
                            
                            .. attribute:: interval
                            
                            	Link Hello interval
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            	**units**\: second
                            
                            	**default value**\: 5
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello, self).__init__()

                                self.yang_name = "link-hello"
                                self.yang_parent_name = "discovery"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.dual_stack = YLeaf(YType.enumeration, "dual-stack")

                                self.hold_time = YLeaf(YType.uint32, "hold-time")

                                self.interval = YLeaf(YType.uint32, "interval")
                                self._segment_path = lambda: "link-hello"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello, ['dual_stack', 'hold_time', 'interval'], name, value)


                    class Igp(Entity):
                        """
                        LDP IGP configuration
                        
                        .. attribute:: sync
                        
                        	LDP IGP synchronization
                        	**type**\:   :py:class:`Sync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"sync" : ("sync", MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync)}
                            self._child_list_classes = {}

                            self.sync = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync()
                            self.sync.parent = self
                            self._children_name_map["sync"] = "sync"
                            self._children_yang_names.add("sync")
                            self._segment_path = lambda: "igp"


                        class Sync(Entity):
                            """
                            LDP IGP synchronization
                            
                            .. attribute:: delay
                            
                            	LDP IGP synchronization delay time
                            	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync, self).__init__()

                                self.yang_name = "sync"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"delay" : ("delay", MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay)}
                                self._child_list_classes = {}

                                self.delay = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay()
                                self.delay.parent = self
                                self._children_name_map["delay"] = "delay"
                                self._children_yang_names.add("delay")
                                self._segment_path = lambda: "sync"


                            class Delay(Entity):
                                """
                                LDP IGP synchronization delay time
                                
                                .. attribute:: on_session_up
                                
                                	Interface sync up delay after session up
                                	**type**\:   :py:class:`OnSessionUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay, self).__init__()

                                    self.yang_name = "delay"
                                    self.yang_parent_name = "sync"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"on-session-up" : ("on_session_up", MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp)}
                                    self._child_list_classes = {}

                                    self.on_session_up = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp()
                                    self.on_session_up.parent = self
                                    self._children_name_map["on_session_up"] = "on-session-up"
                                    self._children_yang_names.add("on-session-up")
                                    self._segment_path = lambda: "delay"


                                class OnSessionUp(Entity):
                                    """
                                    Interface sync up delay after session up
                                    
                                    .. attribute:: disable
                                    
                                    	Disable delay after session up
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: timeout
                                    
                                    	Time (seconds)
                                    	**type**\:  int
                                    
                                    	**range:** 5..300
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp, self).__init__()

                                        self.yang_name = "on-session-up"
                                        self.yang_parent_name = "delay"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.disable = YLeaf(YType.empty, "disable")

                                        self.timeout = YLeaf(YType.uint32, "timeout")
                                        self._segment_path = lambda: "on-session-up"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp, ['disable', 'timeout'], name, value)


    class Global_(Entity):
        """
        Global configuration for MPLS LDP
        
        .. attribute:: disable_implicit_ipv4
        
        	Disable the implicit enabling for IPv4 address family
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: discovery
        
        	Configure Discovery parameters
        	**type**\:   :py:class:`Discovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Discovery>`
        
        .. attribute:: enable_logging
        
        	Enable logging of events
        	**type**\:   :py:class:`EnableLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.EnableLogging>`
        
        .. attribute:: entropy_label
        
        	Configure for LDP Entropy\-Label
        	**type**\:   :py:class:`EntropyLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.EntropyLabel>`
        
        .. attribute:: graceful_restart
        
        	Configuration for LDP Graceful Restart parameters
        	**type**\:   :py:class:`GracefulRestart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.GracefulRestart>`
        
        .. attribute:: igp
        
        	LDP IGP configuration
        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Igp>`
        
        .. attribute:: ltrace_buf_multiplier
        
        	Configure Ltrace Buffer Multiplier
        	**type**\:  int
        
        	**range:** 1..5
        
        	**default value**\: 1
        
        .. attribute:: mldp
        
        	MPLS mLDP configuration
        	**type**\:   :py:class:`Mldp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp>`
        
        .. attribute:: nsr
        
        	Configure LDP Non\-Stop Routing
        	**type**\:   :py:class:`Nsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Nsr>`
        
        .. attribute:: session
        
        	LDP Session parameters
        	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Session>`
        
        .. attribute:: signalling
        
        	Configure LDP signalling parameters
        	**type**\:   :py:class:`Signalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Signalling>`
        
        

        """

        _prefix = 'mpls-ldp-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(MplsLdp.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "mpls-ldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"discovery" : ("discovery", MplsLdp.Global_.Discovery), "enable-logging" : ("enable_logging", MplsLdp.Global_.EnableLogging), "entropy-label" : ("entropy_label", MplsLdp.Global_.EntropyLabel), "graceful-restart" : ("graceful_restart", MplsLdp.Global_.GracefulRestart), "igp" : ("igp", MplsLdp.Global_.Igp), "mldp" : ("mldp", MplsLdp.Global_.Mldp), "nsr" : ("nsr", MplsLdp.Global_.Nsr), "session" : ("session", MplsLdp.Global_.Session), "signalling" : ("signalling", MplsLdp.Global_.Signalling)}
            self._child_list_classes = {}

            self.disable_implicit_ipv4 = YLeaf(YType.empty, "disable-implicit-ipv4")

            self.ltrace_buf_multiplier = YLeaf(YType.uint32, "ltrace-buf-multiplier")

            self.discovery = MplsLdp.Global_.Discovery()
            self.discovery.parent = self
            self._children_name_map["discovery"] = "discovery"
            self._children_yang_names.add("discovery")

            self.enable_logging = MplsLdp.Global_.EnableLogging()
            self.enable_logging.parent = self
            self._children_name_map["enable_logging"] = "enable-logging"
            self._children_yang_names.add("enable-logging")

            self.entropy_label = MplsLdp.Global_.EntropyLabel()
            self.entropy_label.parent = self
            self._children_name_map["entropy_label"] = "entropy-label"
            self._children_yang_names.add("entropy-label")

            self.graceful_restart = MplsLdp.Global_.GracefulRestart()
            self.graceful_restart.parent = self
            self._children_name_map["graceful_restart"] = "graceful-restart"
            self._children_yang_names.add("graceful-restart")

            self.igp = MplsLdp.Global_.Igp()
            self.igp.parent = self
            self._children_name_map["igp"] = "igp"
            self._children_yang_names.add("igp")

            self.mldp = MplsLdp.Global_.Mldp()
            self.mldp.parent = self
            self._children_name_map["mldp"] = "mldp"
            self._children_yang_names.add("mldp")

            self.nsr = MplsLdp.Global_.Nsr()
            self.nsr.parent = self
            self._children_name_map["nsr"] = "nsr"
            self._children_yang_names.add("nsr")

            self.session = MplsLdp.Global_.Session()
            self.session.parent = self
            self._children_name_map["session"] = "session"
            self._children_yang_names.add("session")

            self.signalling = MplsLdp.Global_.Signalling()
            self.signalling.parent = self
            self._children_name_map["signalling"] = "signalling"
            self._children_yang_names.add("signalling")
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsLdp.Global_, ['disable_implicit_ipv4', 'ltrace_buf_multiplier'], name, value)


        class Discovery(Entity):
            """
            Configure Discovery parameters
            
            .. attribute:: disable_instance_tlv
            
            	Disable transmit and receive processing for private Instance TLV in LDP discovery hello messages
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: disable_quick_start
            
            	Disable discovery's quick start mode
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: link_hello
            
            	LDP Link Hellos
            	**type**\:   :py:class:`LinkHello <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Discovery.LinkHello>`
            
            .. attribute:: targeted_hello
            
            	LDP Targeted Hellos
            	**type**\:   :py:class:`TargetedHello <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Discovery.TargetedHello>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.Discovery, self).__init__()

                self.yang_name = "discovery"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"link-hello" : ("link_hello", MplsLdp.Global_.Discovery.LinkHello), "targeted-hello" : ("targeted_hello", MplsLdp.Global_.Discovery.TargetedHello)}
                self._child_list_classes = {}

                self.disable_instance_tlv = YLeaf(YType.empty, "disable-instance-tlv")

                self.disable_quick_start = YLeaf(YType.empty, "disable-quick-start")

                self.link_hello = MplsLdp.Global_.Discovery.LinkHello()
                self.link_hello.parent = self
                self._children_name_map["link_hello"] = "link-hello"
                self._children_yang_names.add("link-hello")

                self.targeted_hello = MplsLdp.Global_.Discovery.TargetedHello()
                self.targeted_hello.parent = self
                self._children_name_map["targeted_hello"] = "targeted-hello"
                self._children_yang_names.add("targeted-hello")
                self._segment_path = lambda: "discovery"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Global_.Discovery, ['disable_instance_tlv', 'disable_quick_start'], name, value)


            class LinkHello(Entity):
                """
                LDP Link Hellos
                
                .. attribute:: hold_time
                
                	Time (seconds) \- 65535 implies infinite
                	**type**\:  int
                
                	**range:** 1..65535
                
                	**units**\: second
                
                	**default value**\: 15
                
                .. attribute:: interval
                
                	Link Hello interval
                	**type**\:  int
                
                	**range:** 1..65535
                
                	**units**\: second
                
                	**default value**\: 5
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Global_.Discovery.LinkHello, self).__init__()

                    self.yang_name = "link-hello"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.hold_time = YLeaf(YType.uint32, "hold-time")

                    self.interval = YLeaf(YType.uint32, "interval")
                    self._segment_path = lambda: "link-hello"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.Global_.Discovery.LinkHello, ['hold_time', 'interval'], name, value)


            class TargetedHello(Entity):
                """
                LDP Targeted Hellos
                
                .. attribute:: hold_time
                
                	Time (seconds) \- 65535 implies infinite
                	**type**\:  int
                
                	**range:** 1..65535
                
                	**units**\: second
                
                	**default value**\: 90
                
                .. attribute:: interval
                
                	Targeted Hello interval
                	**type**\:  int
                
                	**range:** 1..65535
                
                	**units**\: second
                
                	**default value**\: 10
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Global_.Discovery.TargetedHello, self).__init__()

                    self.yang_name = "targeted-hello"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.hold_time = YLeaf(YType.uint32, "hold-time")

                    self.interval = YLeaf(YType.uint32, "interval")
                    self._segment_path = lambda: "targeted-hello"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.Global_.Discovery.TargetedHello, ['hold_time', 'interval'], name, value)


        class EnableLogging(Entity):
            """
            Enable logging of events
            
            .. attribute:: adjacency
            
            	Enable logging of adjacency events
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: gr_session_changes
            
            	Enable logging of Graceful Restart (GR) events
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: neighbor_changes
            
            	Enable logging of neighbor events
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: nsr
            
            	Enable logging of NSR events
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: session_protection
            
            	Enable logging of session protection events
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.EnableLogging, self).__init__()

                self.yang_name = "enable-logging"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.adjacency = YLeaf(YType.empty, "adjacency")

                self.gr_session_changes = YLeaf(YType.empty, "gr-session-changes")

                self.neighbor_changes = YLeaf(YType.empty, "neighbor-changes")

                self.nsr = YLeaf(YType.empty, "nsr")

                self.session_protection = YLeaf(YType.empty, "session-protection")
                self._segment_path = lambda: "enable-logging"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Global_.EnableLogging, ['adjacency', 'gr_session_changes', 'neighbor_changes', 'nsr', 'session_protection'], name, value)


        class EntropyLabel(Entity):
            """
            Configure for LDP Entropy\-Label
            
            .. attribute:: enable
            
            	none
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.EntropyLabel, self).__init__()

                self.yang_name = "entropy-label"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "entropy-label"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Global_.EntropyLabel, ['enable'], name, value)


        class GracefulRestart(Entity):
            """
            Configuration for LDP Graceful Restart
            parameters
            
            .. attribute:: enable
            
            	none
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: forwarding_hold_time
            
            	Configure Graceful Restart Session holdtime
            	**type**\:  int
            
            	**range:** 60..1800
            
            	**units**\: second
            
            	**default value**\: 180
            
            .. attribute:: reconnect_timeout
            
            	Configure Graceful Restart Reconnect Timeout value
            	**type**\:  int
            
            	**range:** 60..1800
            
            	**units**\: second
            
            	**default value**\: 120
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.GracefulRestart, self).__init__()

                self.yang_name = "graceful-restart"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.forwarding_hold_time = YLeaf(YType.uint32, "forwarding-hold-time")

                self.reconnect_timeout = YLeaf(YType.uint32, "reconnect-timeout")
                self._segment_path = lambda: "graceful-restart"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Global_.GracefulRestart, ['enable', 'forwarding_hold_time', 'reconnect_timeout'], name, value)


        class Igp(Entity):
            """
            LDP IGP configuration
            
            .. attribute:: sync
            
            	LDP IGP synchronization
            	**type**\:   :py:class:`Sync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Igp.Sync>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.Igp, self).__init__()

                self.yang_name = "igp"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"sync" : ("sync", MplsLdp.Global_.Igp.Sync)}
                self._child_list_classes = {}

                self.sync = MplsLdp.Global_.Igp.Sync()
                self.sync.parent = self
                self._children_name_map["sync"] = "sync"
                self._children_yang_names.add("sync")
                self._segment_path = lambda: "igp"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()


            class Sync(Entity):
                """
                LDP IGP synchronization
                
                .. attribute:: delay
                
                	LDP IGP synchronization delay time
                	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Igp.Sync.Delay>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Global_.Igp.Sync, self).__init__()

                    self.yang_name = "sync"
                    self.yang_parent_name = "igp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"delay" : ("delay", MplsLdp.Global_.Igp.Sync.Delay)}
                    self._child_list_classes = {}

                    self.delay = MplsLdp.Global_.Igp.Sync.Delay()
                    self.delay.parent = self
                    self._children_name_map["delay"] = "delay"
                    self._children_yang_names.add("delay")
                    self._segment_path = lambda: "sync"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/igp/%s" % self._segment_path()


                class Delay(Entity):
                    """
                    LDP IGP synchronization delay time
                    
                    .. attribute:: on_proc_restart
                    
                    	Global sync up delay to be used after process restart
                    	**type**\:  int
                    
                    	**range:** 60..600
                    
                    	**units**\: second
                    
                    .. attribute:: on_session_up
                    
                    	Interface sync up delay after session up
                    	**type**\:  int
                    
                    	**range:** 5..300
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Global_.Igp.Sync.Delay, self).__init__()

                        self.yang_name = "delay"
                        self.yang_parent_name = "sync"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.on_proc_restart = YLeaf(YType.uint32, "on-proc-restart")

                        self.on_session_up = YLeaf(YType.uint32, "on-session-up")
                        self._segment_path = lambda: "delay"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/igp/sync/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.Global_.Igp.Sync.Delay, ['on_proc_restart', 'on_session_up'], name, value)


        class Mldp(Entity):
            """
            MPLS mLDP configuration
            
            .. attribute:: default_vrf
            
            	Default VRF attribute configuration for mLDP
            	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf>`
            
            .. attribute:: enable
            
            	Enable Multicast Label Distribution Protocol (mLDP)
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: mldp_global
            
            	Global configuration for mLDP
            	**type**\:   :py:class:`MldpGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.MldpGlobal>`
            
            .. attribute:: vrfs
            
            	VRF Table attribute configuration for MPLS LDP
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.Mldp, self).__init__()

                self.yang_name = "mldp"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"default-vrf" : ("default_vrf", MplsLdp.Global_.Mldp.DefaultVrf), "mldp-global" : ("mldp_global", MplsLdp.Global_.Mldp.MldpGlobal), "vrfs" : ("vrfs", MplsLdp.Global_.Mldp.Vrfs)}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.default_vrf = MplsLdp.Global_.Mldp.DefaultVrf()
                self.default_vrf.parent = self
                self._children_name_map["default_vrf"] = "default-vrf"
                self._children_yang_names.add("default-vrf")

                self.mldp_global = MplsLdp.Global_.Mldp.MldpGlobal()
                self.mldp_global.parent = self
                self._children_name_map["mldp_global"] = "mldp-global"
                self._children_yang_names.add("mldp-global")

                self.vrfs = MplsLdp.Global_.Mldp.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._children_yang_names.add("vrfs")
                self._segment_path = lambda: "mldp"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Global_.Mldp, ['enable'], name, value)


            class DefaultVrf(Entity):
                """
                Default VRF attribute configuration for mLDP
                
                .. attribute:: afs
                
                	Address Family specific operational data
                	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Global_.Mldp.DefaultVrf, self).__init__()

                    self.yang_name = "default-vrf"
                    self.yang_parent_name = "mldp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"afs" : ("afs", MplsLdp.Global_.Mldp.DefaultVrf.Afs)}
                    self._child_list_classes = {}

                    self.afs = MplsLdp.Global_.Mldp.DefaultVrf.Afs()
                    self.afs.parent = self
                    self._children_name_map["afs"] = "afs"
                    self._children_yang_names.add("afs")
                    self._segment_path = lambda: "default-vrf"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/%s" % self._segment_path()


                class Afs(Entity):
                    """
                    Address Family specific operational data
                    
                    .. attribute:: af
                    
                    	Operational data for given Address Family
                    	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs, self).__init__()

                        self.yang_name = "afs"
                        self.yang_parent_name = "default-vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"af" : ("af", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af)}

                        self.af = YList(self)
                        self._segment_path = lambda: "afs"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/default-vrf/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs, [], name, value)


                    class Af(Entity):
                        """
                        Operational data for given Address Family
                        
                        .. attribute:: af_name  <key>
                        
                        	Address Family name
                        	**type**\:   :py:class:`MplsLdpafName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafName>`
                        
                        .. attribute:: csc
                        
                        	MPLS mLDP CSC
                        	**type**\:   :py:class:`Csc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc>`
                        
                        .. attribute:: enable
                        
                        	Enable Multicast Label Distribution Protocol (mLDP) under AF
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: make_before_break
                        
                        	MPLS mLDP Make\-Before\-Break configuration
                        	**type**\:   :py:class:`MakeBeforeBreak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak>`
                        
                        .. attribute:: mldp_recursive_fec
                        
                        	MPLS mLDP Recursive FEC
                        	**type**\:   :py:class:`MldpRecursiveFec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec>`
                        
                        .. attribute:: mldp_rib_unicast_always
                        
                        	Enable MPLS MLDP RIB unicast\-always configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: mo_frr
                        
                        	MPLS mLDP MoFRR
                        	**type**\:   :py:class:`MoFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr>`
                        
                        .. attribute:: neighbor_policies
                        
                        	MLDP neighbor policies
                        	**type**\:   :py:class:`NeighborPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies>`
                        
                        .. attribute:: recursive_forwarding
                        
                        	Enable recursive forwarding
                        	**type**\:   :py:class:`RecursiveForwarding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af, self).__init__()

                            self.yang_name = "af"
                            self.yang_parent_name = "afs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"csc" : ("csc", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc), "make-before-break" : ("make_before_break", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak), "mldp-recursive-fec" : ("mldp_recursive_fec", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec), "mo-frr" : ("mo_frr", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr), "neighbor-policies" : ("neighbor_policies", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies), "recursive-forwarding" : ("recursive_forwarding", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding)}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.enable = YLeaf(YType.empty, "enable")

                            self.mldp_rib_unicast_always = YLeaf(YType.empty, "mldp-rib-unicast-always")

                            self.csc = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc()
                            self.csc.parent = self
                            self._children_name_map["csc"] = "csc"
                            self._children_yang_names.add("csc")

                            self.make_before_break = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak()
                            self.make_before_break.parent = self
                            self._children_name_map["make_before_break"] = "make-before-break"
                            self._children_yang_names.add("make-before-break")

                            self.mldp_recursive_fec = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec()
                            self.mldp_recursive_fec.parent = self
                            self._children_name_map["mldp_recursive_fec"] = "mldp-recursive-fec"
                            self._children_yang_names.add("mldp-recursive-fec")

                            self.mo_frr = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr()
                            self.mo_frr.parent = self
                            self._children_name_map["mo_frr"] = "mo-frr"
                            self._children_yang_names.add("mo-frr")

                            self.neighbor_policies = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies()
                            self.neighbor_policies.parent = self
                            self._children_name_map["neighbor_policies"] = "neighbor-policies"
                            self._children_yang_names.add("neighbor-policies")

                            self.recursive_forwarding = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding()
                            self.recursive_forwarding.parent = self
                            self._children_name_map["recursive_forwarding"] = "recursive-forwarding"
                            self._children_yang_names.add("recursive-forwarding")
                            self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/default-vrf/afs/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af, ['af_name', 'enable', 'mldp_rib_unicast_always'], name, value)


                        class Csc(Entity):
                            """
                            MPLS mLDP CSC
                            
                            .. attribute:: enable
                            
                            	Enable MPLS mLDP CSC
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc, self).__init__()

                                self.yang_name = "csc"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")
                                self._segment_path = lambda: "csc"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc, ['enable'], name, value)


                        class MakeBeforeBreak(Entity):
                            """
                            MPLS mLDP Make\-Before\-Break configuration
                            
                            .. attribute:: policy
                            
                            	Route policy name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: signaling
                            
                            	Enable MPLS mLDP MBB signaling
                            	**type**\:   :py:class:`Signaling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak, self).__init__()

                                self.yang_name = "make-before-break"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"signaling" : ("signaling", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling)}
                                self._child_list_classes = {}

                                self.policy = YLeaf(YType.str, "policy")

                                self.signaling = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling()
                                self.signaling.parent = self
                                self._children_name_map["signaling"] = "signaling"
                                self._children_yang_names.add("signaling")
                                self._segment_path = lambda: "make-before-break"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak, ['policy'], name, value)


                            class Signaling(Entity):
                                """
                                Enable MPLS mLDP MBB signaling
                                
                                .. attribute:: delete_delay
                                
                                	Delete Delay in seconds
                                	**type**\:  int
                                
                                	**range:** 0..60
                                
                                	**units**\: second
                                
                                .. attribute:: forward_delay
                                
                                	Forwarding Delay in Seconds
                                	**type**\:  int
                                
                                	**range:** 0..600
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling, self).__init__()

                                    self.yang_name = "signaling"
                                    self.yang_parent_name = "make-before-break"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.delete_delay = YLeaf(YType.uint32, "delete-delay")

                                    self.forward_delay = YLeaf(YType.uint32, "forward-delay")
                                    self._segment_path = lambda: "signaling"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling, ['delete_delay', 'forward_delay'], name, value)


                        class MldpRecursiveFec(Entity):
                            """
                            MPLS mLDP Recursive FEC
                            
                            .. attribute:: enable
                            
                            	Enable MPLS mLDP Recursive FEC
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Route policy name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec, self).__init__()

                                self.yang_name = "mldp-recursive-fec"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.policy = YLeaf(YType.str, "policy")
                                self._segment_path = lambda: "mldp-recursive-fec"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec, ['enable', 'policy'], name, value)


                        class MoFrr(Entity):
                            """
                            MPLS mLDP MoFRR
                            
                            .. attribute:: enable
                            
                            	Enable MPLS mLDP MoFRR
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Route policy name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr, self).__init__()

                                self.yang_name = "mo-frr"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.policy = YLeaf(YType.str, "policy")
                                self._segment_path = lambda: "mo-frr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr, ['enable', 'policy'], name, value)


                        class NeighborPolicies(Entity):
                            """
                            MLDP neighbor policies
                            
                            .. attribute:: neighbor_policy
                            
                            	Route Policy
                            	**type**\: list of    :py:class:`NeighborPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies, self).__init__()

                                self.yang_name = "neighbor-policies"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"neighbor-policy" : ("neighbor_policy", MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy)}

                                self.neighbor_policy = YList(self)
                                self._segment_path = lambda: "neighbor-policies"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies, [], name, value)


                            class NeighborPolicy(Entity):
                                """
                                Route Policy
                                
                                .. attribute:: root_address  <key>
                                
                                	Neighbor Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: policy_mode  <key>
                                
                                	Inbound/Outbound Policy
                                	**type**\:   :py:class:`MldpPolicyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MldpPolicyMode>`
                                
                                .. attribute:: route_policy
                                
                                	Route policy name
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy, self).__init__()

                                    self.yang_name = "neighbor-policy"
                                    self.yang_parent_name = "neighbor-policies"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.root_address = YLeaf(YType.str, "root-address")

                                    self.policy_mode = YLeaf(YType.enumeration, "policy-mode")

                                    self.route_policy = YLeaf(YType.str, "route-policy")
                                    self._segment_path = lambda: "neighbor-policy" + "[root-address='" + self.root_address.get() + "']" + "[policy-mode='" + self.policy_mode.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy, ['root_address', 'policy_mode', 'route_policy'], name, value)


                        class RecursiveForwarding(Entity):
                            """
                            Enable recursive forwarding
                            
                            .. attribute:: enable
                            
                            	Enable recursive forwarding
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Recursive forwarding policy name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding, self).__init__()

                                self.yang_name = "recursive-forwarding"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.policy = YLeaf(YType.str, "policy")
                                self._segment_path = lambda: "recursive-forwarding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding, ['enable', 'policy'], name, value)


            class MldpGlobal(Entity):
                """
                Global configuration for mLDP
                
                .. attribute:: logging
                
                	MPLS mLDP logging
                	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.MldpGlobal.Logging>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Global_.Mldp.MldpGlobal, self).__init__()

                    self.yang_name = "mldp-global"
                    self.yang_parent_name = "mldp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"logging" : ("logging", MplsLdp.Global_.Mldp.MldpGlobal.Logging)}
                    self._child_list_classes = {}

                    self.logging = MplsLdp.Global_.Mldp.MldpGlobal.Logging()
                    self.logging.parent = self
                    self._children_name_map["logging"] = "logging"
                    self._children_yang_names.add("logging")
                    self._segment_path = lambda: "mldp-global"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/%s" % self._segment_path()


                class Logging(Entity):
                    """
                    MPLS mLDP logging
                    
                    .. attribute:: notifications
                    
                    	MPLS mLDP logging notifications
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Global_.Mldp.MldpGlobal.Logging, self).__init__()

                        self.yang_name = "logging"
                        self.yang_parent_name = "mldp-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.notifications = YLeaf(YType.empty, "notifications")
                        self._segment_path = lambda: "logging"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/mldp-global/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.Global_.Mldp.MldpGlobal.Logging, ['notifications'], name, value)


            class Vrfs(Entity):
                """
                VRF Table attribute configuration for MPLS LDP
                
                .. attribute:: vrf
                
                	VRF attribute configuration for MPLS LDP
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Global_.Mldp.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "mldp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"vrf" : ("vrf", MplsLdp.Global_.Mldp.Vrfs.Vrf)}

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs, [], name, value)


                class Vrf(Entity):
                    """
                    VRF attribute configuration for MPLS LDP
                    
                    .. attribute:: vrf_name  <key>
                    
                    	VRF Name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: afs
                    
                    	Address Family specific operational data
                    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs>`
                    
                    .. attribute:: enable
                    
                    	Enable Multicast Label Distribution Protocol (mLDP)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Global_.Mldp.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"afs" : ("afs", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs)}
                        self._child_list_classes = {}

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.afs = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                        self._children_yang_names.add("afs")
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/vrfs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf, ['vrf_name', 'enable'], name, value)


                    class Afs(Entity):
                        """
                        Address Family specific operational data
                        
                        .. attribute:: af
                        
                        	Operational data for given Address Family
                        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs, self).__init__()

                            self.yang_name = "afs"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"af" : ("af", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af)}

                            self.af = YList(self)
                            self._segment_path = lambda: "afs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs, [], name, value)


                        class Af(Entity):
                            """
                            Operational data for given Address Family
                            
                            .. attribute:: af_name  <key>
                            
                            	Address Family name
                            	**type**\:   :py:class:`MplsLdpafName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafName>`
                            
                            .. attribute:: csc
                            
                            	MPLS mLDP CSC
                            	**type**\:   :py:class:`Csc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc>`
                            
                            .. attribute:: enable
                            
                            	Enable Multicast Label Distribution Protocol (mLDP) under AF
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: make_before_break
                            
                            	MPLS mLDP Make\-Before\-Break configuration
                            	**type**\:   :py:class:`MakeBeforeBreak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak>`
                            
                            .. attribute:: mldp_recursive_fec
                            
                            	MPLS mLDP Recursive FEC
                            	**type**\:   :py:class:`MldpRecursiveFec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec>`
                            
                            .. attribute:: mldp_rib_unicast_always
                            
                            	Enable MPLS MLDP RIB unicast\-always configuration
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mo_frr
                            
                            	MPLS mLDP MoFRR
                            	**type**\:   :py:class:`MoFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr>`
                            
                            .. attribute:: neighbor_policies
                            
                            	MLDP neighbor policies
                            	**type**\:   :py:class:`NeighborPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies>`
                            
                            .. attribute:: recursive_forwarding
                            
                            	Enable recursive forwarding
                            	**type**\:   :py:class:`RecursiveForwarding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af, self).__init__()

                                self.yang_name = "af"
                                self.yang_parent_name = "afs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"csc" : ("csc", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc), "make-before-break" : ("make_before_break", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak), "mldp-recursive-fec" : ("mldp_recursive_fec", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec), "mo-frr" : ("mo_frr", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr), "neighbor-policies" : ("neighbor_policies", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies), "recursive-forwarding" : ("recursive_forwarding", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding)}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.enable = YLeaf(YType.empty, "enable")

                                self.mldp_rib_unicast_always = YLeaf(YType.empty, "mldp-rib-unicast-always")

                                self.csc = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc()
                                self.csc.parent = self
                                self._children_name_map["csc"] = "csc"
                                self._children_yang_names.add("csc")

                                self.make_before_break = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak()
                                self.make_before_break.parent = self
                                self._children_name_map["make_before_break"] = "make-before-break"
                                self._children_yang_names.add("make-before-break")

                                self.mldp_recursive_fec = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec()
                                self.mldp_recursive_fec.parent = self
                                self._children_name_map["mldp_recursive_fec"] = "mldp-recursive-fec"
                                self._children_yang_names.add("mldp-recursive-fec")

                                self.mo_frr = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr()
                                self.mo_frr.parent = self
                                self._children_name_map["mo_frr"] = "mo-frr"
                                self._children_yang_names.add("mo-frr")

                                self.neighbor_policies = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies()
                                self.neighbor_policies.parent = self
                                self._children_name_map["neighbor_policies"] = "neighbor-policies"
                                self._children_yang_names.add("neighbor-policies")

                                self.recursive_forwarding = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding()
                                self.recursive_forwarding.parent = self
                                self._children_name_map["recursive_forwarding"] = "recursive-forwarding"
                                self._children_yang_names.add("recursive-forwarding")
                                self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af, ['af_name', 'enable', 'mldp_rib_unicast_always'], name, value)


                            class Csc(Entity):
                                """
                                MPLS mLDP CSC
                                
                                .. attribute:: enable
                                
                                	Enable MPLS mLDP CSC
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc, self).__init__()

                                    self.yang_name = "csc"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enable = YLeaf(YType.empty, "enable")
                                    self._segment_path = lambda: "csc"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc, ['enable'], name, value)


                            class MakeBeforeBreak(Entity):
                                """
                                MPLS mLDP Make\-Before\-Break configuration
                                
                                .. attribute:: policy
                                
                                	Route policy name
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                .. attribute:: signaling
                                
                                	Enable MPLS mLDP MBB signaling
                                	**type**\:   :py:class:`Signaling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak, self).__init__()

                                    self.yang_name = "make-before-break"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"signaling" : ("signaling", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling)}
                                    self._child_list_classes = {}

                                    self.policy = YLeaf(YType.str, "policy")

                                    self.signaling = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling()
                                    self.signaling.parent = self
                                    self._children_name_map["signaling"] = "signaling"
                                    self._children_yang_names.add("signaling")
                                    self._segment_path = lambda: "make-before-break"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak, ['policy'], name, value)


                                class Signaling(Entity):
                                    """
                                    Enable MPLS mLDP MBB signaling
                                    
                                    .. attribute:: delete_delay
                                    
                                    	Delete Delay in seconds
                                    	**type**\:  int
                                    
                                    	**range:** 0..60
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: forward_delay
                                    
                                    	Forwarding Delay in Seconds
                                    	**type**\:  int
                                    
                                    	**range:** 0..600
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling, self).__init__()

                                        self.yang_name = "signaling"
                                        self.yang_parent_name = "make-before-break"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.delete_delay = YLeaf(YType.uint32, "delete-delay")

                                        self.forward_delay = YLeaf(YType.uint32, "forward-delay")
                                        self._segment_path = lambda: "signaling"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling, ['delete_delay', 'forward_delay'], name, value)


                            class MldpRecursiveFec(Entity):
                                """
                                MPLS mLDP Recursive FEC
                                
                                .. attribute:: enable
                                
                                	Enable MPLS mLDP Recursive FEC
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: policy
                                
                                	Route policy name
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec, self).__init__()

                                    self.yang_name = "mldp-recursive-fec"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.policy = YLeaf(YType.str, "policy")
                                    self._segment_path = lambda: "mldp-recursive-fec"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec, ['enable', 'policy'], name, value)


                            class MoFrr(Entity):
                                """
                                MPLS mLDP MoFRR
                                
                                .. attribute:: enable
                                
                                	Enable MPLS mLDP MoFRR
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: policy
                                
                                	Route policy name
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr, self).__init__()

                                    self.yang_name = "mo-frr"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.policy = YLeaf(YType.str, "policy")
                                    self._segment_path = lambda: "mo-frr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr, ['enable', 'policy'], name, value)


                            class NeighborPolicies(Entity):
                                """
                                MLDP neighbor policies
                                
                                .. attribute:: neighbor_policy
                                
                                	Route Policy
                                	**type**\: list of    :py:class:`NeighborPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies, self).__init__()

                                    self.yang_name = "neighbor-policies"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"neighbor-policy" : ("neighbor_policy", MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy)}

                                    self.neighbor_policy = YList(self)
                                    self._segment_path = lambda: "neighbor-policies"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies, [], name, value)


                                class NeighborPolicy(Entity):
                                    """
                                    Route Policy
                                    
                                    .. attribute:: root_address  <key>
                                    
                                    	Neighbor Address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: policy_mode  <key>
                                    
                                    	Inbound/Outbound Policy
                                    	**type**\:   :py:class:`MldpPolicyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MldpPolicyMode>`
                                    
                                    .. attribute:: route_policy
                                    
                                    	Route policy name
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy, self).__init__()

                                        self.yang_name = "neighbor-policy"
                                        self.yang_parent_name = "neighbor-policies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.root_address = YLeaf(YType.str, "root-address")

                                        self.policy_mode = YLeaf(YType.enumeration, "policy-mode")

                                        self.route_policy = YLeaf(YType.str, "route-policy")
                                        self._segment_path = lambda: "neighbor-policy" + "[root-address='" + self.root_address.get() + "']" + "[policy-mode='" + self.policy_mode.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy, ['root_address', 'policy_mode', 'route_policy'], name, value)


                            class RecursiveForwarding(Entity):
                                """
                                Enable recursive forwarding
                                
                                .. attribute:: enable
                                
                                	Enable recursive forwarding
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: policy
                                
                                	Recursive forwarding policy name
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding, self).__init__()

                                    self.yang_name = "recursive-forwarding"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.policy = YLeaf(YType.str, "policy")
                                    self._segment_path = lambda: "recursive-forwarding"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding, ['enable', 'policy'], name, value)


        class Nsr(Entity):
            """
            Configure LDP Non\-Stop Routing
            
            .. attribute:: enable
            
            	none
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.Nsr, self).__init__()

                self.yang_name = "nsr"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "nsr"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Global_.Nsr, ['enable'], name, value)


        class Session(Entity):
            """
            LDP Session parameters
            
            .. attribute:: backoff_time
            
            	Configure Session Backoff parameters
            	**type**\:   :py:class:`BackoffTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Session.BackoffTime>`
            
            .. attribute:: hold_time
            
            	LDP Session holdtime
            	**type**\:  int
            
            	**range:** 15..65535
            
            	**units**\: second
            
            	**default value**\: 180
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"backoff-time" : ("backoff_time", MplsLdp.Global_.Session.BackoffTime)}
                self._child_list_classes = {}

                self.hold_time = YLeaf(YType.uint32, "hold-time")

                self.backoff_time = MplsLdp.Global_.Session.BackoffTime()
                self.backoff_time.parent = self
                self._children_name_map["backoff_time"] = "backoff-time"
                self._children_yang_names.add("backoff-time")
                self._segment_path = lambda: "session"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Global_.Session, ['hold_time'], name, value)


            class BackoffTime(Entity):
                """
                Configure Session Backoff parameters
                
                .. attribute:: initial_backoff_time
                
                	Initial session backoff time (seconds)
                	**type**\:  int
                
                	**range:** 5..2147483
                
                	**units**\: second
                
                	**default value**\: 15
                
                .. attribute:: max_backoff_time
                
                	Maximum session backoff time (seconds)
                	**type**\:  int
                
                	**range:** 5..2147483
                
                	**units**\: second
                
                	**default value**\: 120
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Global_.Session.BackoffTime, self).__init__()

                    self.yang_name = "backoff-time"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.initial_backoff_time = YLeaf(YType.uint32, "initial-backoff-time")

                    self.max_backoff_time = YLeaf(YType.uint32, "max-backoff-time")
                    self._segment_path = lambda: "backoff-time"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/session/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.Global_.Session.BackoffTime, ['initial_backoff_time', 'max_backoff_time'], name, value)


        class Signalling(Entity):
            """
            Configure LDP signalling parameters
            
            .. attribute:: dscp
            
            	DSCP for control packets
            	**type**\:  int
            
            	**range:** 0..63
            
            	**default value**\: 48
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Global_.Signalling, self).__init__()

                self.yang_name = "signalling"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.dscp = YLeaf(YType.uint32, "dscp")
                self._segment_path = lambda: "signalling"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Global_.Signalling, ['dscp'], name, value)


    class Vrfs(Entity):
        """
        VRF Table attribute configuration for MPLS LDP
        
        .. attribute:: vrf
        
        	VRF attribute configuration for MPLS LDP
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-ldp-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(MplsLdp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mpls-ldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", MplsLdp.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsLdp.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF attribute configuration for MPLS LDP
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: afs
            
            	Address Family specific configuration for MPLS LDP vrf
            	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs>`
            
            .. attribute:: enable
            
            	Enable VRF
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: global_
            
            	Per VRF Global configuration for MPLS LDP
            	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_>`
            
            .. attribute:: interfaces
            
            	MPLS LDP configuration pertaining to interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(MplsLdp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"afs" : ("afs", MplsLdp.Vrfs.Vrf.Afs), "global" : ("global_", MplsLdp.Vrfs.Vrf.Global_), "interfaces" : ("interfaces", MplsLdp.Vrfs.Vrf.Interfaces)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.afs = MplsLdp.Vrfs.Vrf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._children_yang_names.add("afs")

                self.global_ = MplsLdp.Vrfs.Vrf.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._children_yang_names.add("global")

                self.interfaces = MplsLdp.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.Vrfs.Vrf, ['vrf_name', 'enable'], name, value)


            class Afs(Entity):
                """
                Address Family specific configuration for MPLS
                LDP vrf
                
                .. attribute:: af
                
                	Configure data for given Address Family
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Vrfs.Vrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"af" : ("af", MplsLdp.Vrfs.Vrf.Afs.Af)}

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs, [], name, value)


                class Af(Entity):
                    """
                    Configure data for given Address Family
                    
                    .. attribute:: af_name  <key>
                    
                    	Address Family name
                    	**type**\:   :py:class:`MplsLdpafName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafName>`
                    
                    .. attribute:: discovery
                    
                    	Configure Discovery parameters
                    	**type**\:   :py:class:`Discovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Discovery>`
                    
                    .. attribute:: enable
                    
                    	Enable Address Family
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: label
                    
                    	Configure Label policies and control
                    	**type**\:   :py:class:`Label <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"discovery" : ("discovery", MplsLdp.Vrfs.Vrf.Afs.Af.Discovery), "label" : ("label", MplsLdp.Vrfs.Vrf.Afs.Af.Label)}
                        self._child_list_classes = {}

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.discovery = MplsLdp.Vrfs.Vrf.Afs.Af.Discovery()
                        self.discovery.parent = self
                        self._children_name_map["discovery"] = "discovery"
                        self._children_yang_names.add("discovery")

                        self.label = MplsLdp.Vrfs.Vrf.Afs.Af.Label()
                        self.label.parent = self
                        self._children_name_map["label"] = "label"
                        self._children_yang_names.add("label")
                        self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af, ['af_name', 'enable'], name, value)


                    class Discovery(Entity):
                        """
                        Configure Discovery parameters
                        
                        .. attribute:: transport_address
                        
                        	Global discovery transport address for address family
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Discovery, self).__init__()

                            self.yang_name = "discovery"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.transport_address = YLeaf(YType.str, "transport-address")
                            self._segment_path = lambda: "discovery"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Discovery, ['transport_address'], name, value)


                    class Label(Entity):
                        """
                        Configure Label policies and control
                        
                        .. attribute:: local
                        
                        	Configure local label policies and control
                        	**type**\:   :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local>`
                        
                        .. attribute:: remote
                        
                        	Configure remote/peer label policies and control
                        	**type**\:   :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label, self).__init__()

                            self.yang_name = "label"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"local" : ("local", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local), "remote" : ("remote", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote)}
                            self._child_list_classes = {}

                            self.local = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local()
                            self.local.parent = self
                            self._children_name_map["local"] = "local"
                            self._children_yang_names.add("local")

                            self.remote = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote()
                            self.remote.parent = self
                            self._children_name_map["remote"] = "remote"
                            self._children_yang_names.add("remote")
                            self._segment_path = lambda: "label"


                        class Local(Entity):
                            """
                            Configure local label policies and control
                            
                            .. attribute:: advertise
                            
                            	Configure outbound label advertisement
                            	**type**\:   :py:class:`Advertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise>`
                            
                            .. attribute:: allocate
                            
                            	Control local label allocation for prefix(es)
                            	**type**\:   :py:class:`Allocate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate>`
                            
                            .. attribute:: default_route
                            
                            	Enable MPLS forwarding for default route
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: implicit_null_override
                            
                            	Control use of implicit\-null label for set of prefix(es)
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local, self).__init__()

                                self.yang_name = "local"
                                self.yang_parent_name = "label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"advertise" : ("advertise", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise), "allocate" : ("allocate", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate)}
                                self._child_list_classes = {}

                                self.default_route = YLeaf(YType.empty, "default-route")

                                self.implicit_null_override = YLeaf(YType.str, "implicit-null-override")

                                self.advertise = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise()
                                self.advertise.parent = self
                                self._children_name_map["advertise"] = "advertise"
                                self._children_yang_names.add("advertise")

                                self.allocate = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate()
                                self.allocate.parent = self
                                self._children_name_map["allocate"] = "allocate"
                                self._children_yang_names.add("allocate")
                                self._segment_path = lambda: "local"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local, ['default_route', 'implicit_null_override'], name, value)


                            class Advertise(Entity):
                                """
                                Configure outbound label advertisement
                                
                                .. attribute:: disable
                                
                                	Disable label advertisement
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: explicit_null
                                
                                	Configure advertisment of explicit\-null for connected prefixes
                                	**type**\:   :py:class:`ExplicitNull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull>`
                                
                                .. attribute:: interfaces
                                
                                	Configure outbound label advertisement for an interface
                                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces>`
                                
                                .. attribute:: peer_advertise_policies
                                
                                	Configure peer centric outbound label advertisement using ACL
                                	**type**\:   :py:class:`PeerAdvertisePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise, self).__init__()

                                    self.yang_name = "advertise"
                                    self.yang_parent_name = "local"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"explicit-null" : ("explicit_null", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull), "interfaces" : ("interfaces", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces), "peer-advertise-policies" : ("peer_advertise_policies", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies)}
                                    self._child_list_classes = {}

                                    self.disable = YLeaf(YType.empty, "disable")

                                    self.explicit_null = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull()
                                    self.explicit_null.parent = self
                                    self._children_name_map["explicit_null"] = "explicit-null"
                                    self._children_yang_names.add("explicit-null")

                                    self.interfaces = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces()
                                    self.interfaces.parent = self
                                    self._children_name_map["interfaces"] = "interfaces"
                                    self._children_yang_names.add("interfaces")

                                    self.peer_advertise_policies = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies()
                                    self.peer_advertise_policies.parent = self
                                    self._children_name_map["peer_advertise_policies"] = "peer-advertise-policies"
                                    self._children_yang_names.add("peer-advertise-policies")
                                    self._segment_path = lambda: "advertise"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise, ['disable'], name, value)


                                class ExplicitNull(Entity):
                                    """
                                    Configure advertisment of explicit\-null
                                    for connected prefixes.
                                    
                                    .. attribute:: explicit_null_type
                                    
                                    	Explicit Null command variant
                                    	**type**\:   :py:class:`MplsLdpExpNull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpExpNull>`
                                    
                                    .. attribute:: peer_acl_name
                                    
                                    	Name of peer ACL
                                    	**type**\:  str
                                    
                                    .. attribute:: prefix_acl_name
                                    
                                    	Name of prefix ACL
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull, self).__init__()

                                        self.yang_name = "explicit-null"
                                        self.yang_parent_name = "advertise"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.explicit_null_type = YLeaf(YType.enumeration, "explicit-null-type")

                                        self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                                        self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                        self._segment_path = lambda: "explicit-null"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull, ['explicit_null_type', 'peer_acl_name', 'prefix_acl_name'], name, value)


                                class Interfaces(Entity):
                                    """
                                    Configure outbound label advertisement
                                    for an interface
                                    
                                    .. attribute:: interface
                                    
                                    	Control advertisement of interface's host IP address
                                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces, self).__init__()

                                        self.yang_name = "interfaces"
                                        self.yang_parent_name = "advertise"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"interface" : ("interface", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface)}

                                        self.interface = YList(self)
                                        self._segment_path = lambda: "interfaces"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces, [], name, value)


                                    class Interface(Entity):
                                        """
                                        Control advertisement of interface's
                                        host IP address
                                        
                                        .. attribute:: interface_name  <key>
                                        
                                        	Name of interface
                                        	**type**\:  str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                                        
                                        

                                        """

                                        _prefix = 'mpls-ldp-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, self).__init__()

                                            self.yang_name = "interface"
                                            self.yang_parent_name = "interfaces"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.interface_name = YLeaf(YType.str, "interface-name")
                                            self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, ['interface_name'], name, value)


                                class PeerAdvertisePolicies(Entity):
                                    """
                                    Configure peer centric outbound label
                                    advertisement using ACL
                                    
                                    .. attribute:: peer_advertise_policy
                                    
                                    	Control advertisement of prefix(es) using ACL
                                    	**type**\: list of    :py:class:`PeerAdvertisePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, self).__init__()

                                        self.yang_name = "peer-advertise-policies"
                                        self.yang_parent_name = "advertise"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"peer-advertise-policy" : ("peer_advertise_policy", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy)}

                                        self.peer_advertise_policy = YList(self)
                                        self._segment_path = lambda: "peer-advertise-policies"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, [], name, value)


                                    class PeerAdvertisePolicy(Entity):
                                        """
                                        Control advertisement of prefix(es)
                                        using ACL
                                        
                                        .. attribute:: label_space_id  <key>
                                        
                                        	Label space ID of neighbor
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lsr_id
                                        
                                        	keys\: lsr\-id
                                        	**type**\: list of    :py:class:`LsrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId>`
                                        
                                        .. attribute:: peer_advertise_policy_data
                                        
                                        	Data container
                                        	**type**\:   :py:class:`PeerAdvertisePolicyData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData>`
                                        
                                        

                                        """

                                        _prefix = 'mpls-ldp-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, self).__init__()

                                            self.yang_name = "peer-advertise-policy"
                                            self.yang_parent_name = "peer-advertise-policies"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"peer-advertise-policy-data" : ("peer_advertise_policy_data", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData)}
                                            self._child_list_classes = {"lsr-id" : ("lsr_id", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId)}

                                            self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                            self.peer_advertise_policy_data = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData()
                                            self.peer_advertise_policy_data.parent = self
                                            self._children_name_map["peer_advertise_policy_data"] = "peer-advertise-policy-data"
                                            self._children_yang_names.add("peer-advertise-policy-data")

                                            self.lsr_id = YList(self)
                                            self._segment_path = lambda: "peer-advertise-policy" + "[label-space-id='" + self.label_space_id.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, ['label_space_id'], name, value)


                                        class LsrId(Entity):
                                            """
                                            keys\: lsr\-id
                                            
                                            .. attribute:: lsr_id  <key>
                                            
                                            	LSR ID of neighbor
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: prefix_acl_name
                                            
                                            	Name of prefix ACL
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'mpls-ldp-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId, self).__init__()

                                                self.yang_name = "lsr-id"
                                                self.yang_parent_name = "peer-advertise-policy"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.lsr_id = YLeaf(YType.str, "lsr-id")

                                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                                self._segment_path = lambda: "lsr-id" + "[lsr-id='" + self.lsr_id.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId, ['lsr_id', 'prefix_acl_name'], name, value)


                                        class PeerAdvertisePolicyData(Entity):
                                            """
                                            Data container.
                                            
                                            .. attribute:: prefix_acl_name
                                            
                                            	Name of prefix ACL
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'mpls-ldp-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData, self).__init__()

                                                self.yang_name = "peer-advertise-policy-data"
                                                self.yang_parent_name = "peer-advertise-policy"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                                self._segment_path = lambda: "peer-advertise-policy-data"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData, ['prefix_acl_name'], name, value)


                            class Allocate(Entity):
                                """
                                Control local label allocation for
                                prefix(es)
                                
                                .. attribute:: allocation_type
                                
                                	Label allocation type
                                	**type**\:   :py:class:`MplsLdpLabelAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpLabelAllocation>`
                                
                                .. attribute:: prefix_acl_name
                                
                                	Name of prefix ACL
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate, self).__init__()

                                    self.yang_name = "allocate"
                                    self.yang_parent_name = "local"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.allocation_type = YLeaf(YType.enumeration, "allocation-type")

                                    self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                    self._segment_path = lambda: "allocate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate, ['allocation_type', 'prefix_acl_name'], name, value)


                        class Remote(Entity):
                            """
                            Configure remote/peer label policies and
                            control
                            
                            .. attribute:: accept
                            
                            	Configure inbound label acceptance
                            	**type**\:   :py:class:`Accept <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote, self).__init__()

                                self.yang_name = "remote"
                                self.yang_parent_name = "label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"accept" : ("accept", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept)}
                                self._child_list_classes = {}

                                self.accept = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept()
                                self.accept.parent = self
                                self._children_name_map["accept"] = "accept"
                                self._children_yang_names.add("accept")
                                self._segment_path = lambda: "remote"


                            class Accept(Entity):
                                """
                                Configure inbound label acceptance
                                
                                .. attribute:: peer_accept_policies
                                
                                	Configuration related to Neighbors for inbound label acceptance
                                	**type**\:   :py:class:`PeerAcceptPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept, self).__init__()

                                    self.yang_name = "accept"
                                    self.yang_parent_name = "remote"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"peer-accept-policies" : ("peer_accept_policies", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies)}
                                    self._child_list_classes = {}

                                    self.peer_accept_policies = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies()
                                    self.peer_accept_policies.parent = self
                                    self._children_name_map["peer_accept_policies"] = "peer-accept-policies"
                                    self._children_yang_names.add("peer-accept-policies")
                                    self._segment_path = lambda: "accept"


                                class PeerAcceptPolicies(Entity):
                                    """
                                    Configuration related to Neighbors for
                                    inbound label acceptance
                                    
                                    .. attribute:: peer_accept_policy
                                    
                                    	Control acceptasnce of labels from a neighbor for prefix(es) using ACL
                                    	**type**\: list of    :py:class:`PeerAcceptPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, self).__init__()

                                        self.yang_name = "peer-accept-policies"
                                        self.yang_parent_name = "accept"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"peer-accept-policy" : ("peer_accept_policy", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy)}

                                        self.peer_accept_policy = YList(self)
                                        self._segment_path = lambda: "peer-accept-policies"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, [], name, value)


                                    class PeerAcceptPolicy(Entity):
                                        """
                                        Control acceptasnce of labels from a
                                        neighbor for prefix(es) using ACL
                                        
                                        .. attribute:: label_space_id  <key>
                                        
                                        	Label space ID of neighbor
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lsr_id
                                        
                                        	keys\: lsr\-id
                                        	**type**\: list of    :py:class:`LsrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId>`
                                        
                                        .. attribute:: peer_accept_policy_data
                                        
                                        	Data container
                                        	**type**\:   :py:class:`PeerAcceptPolicyData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData>`
                                        
                                        

                                        """

                                        _prefix = 'mpls-ldp-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, self).__init__()

                                            self.yang_name = "peer-accept-policy"
                                            self.yang_parent_name = "peer-accept-policies"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"peer-accept-policy-data" : ("peer_accept_policy_data", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData)}
                                            self._child_list_classes = {"lsr-id" : ("lsr_id", MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId)}

                                            self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                            self.peer_accept_policy_data = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData()
                                            self.peer_accept_policy_data.parent = self
                                            self._children_name_map["peer_accept_policy_data"] = "peer-accept-policy-data"
                                            self._children_yang_names.add("peer-accept-policy-data")

                                            self.lsr_id = YList(self)
                                            self._segment_path = lambda: "peer-accept-policy" + "[label-space-id='" + self.label_space_id.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, ['label_space_id'], name, value)


                                        class LsrId(Entity):
                                            """
                                            keys\: lsr\-id
                                            
                                            .. attribute:: lsr_id  <key>
                                            
                                            	LSR ID of neighbor
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: prefix_acl_name
                                            
                                            	Name of prefix ACL
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'mpls-ldp-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId, self).__init__()

                                                self.yang_name = "lsr-id"
                                                self.yang_parent_name = "peer-accept-policy"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.lsr_id = YLeaf(YType.str, "lsr-id")

                                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                                self._segment_path = lambda: "lsr-id" + "[lsr-id='" + self.lsr_id.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId, ['lsr_id', 'prefix_acl_name'], name, value)


                                        class PeerAcceptPolicyData(Entity):
                                            """
                                            Data container.
                                            
                                            .. attribute:: prefix_acl_name
                                            
                                            	Name of prefix ACL
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'mpls-ldp-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData, self).__init__()

                                                self.yang_name = "peer-accept-policy-data"
                                                self.yang_parent_name = "peer-accept-policy"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")
                                                self._segment_path = lambda: "peer-accept-policy-data"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData, ['prefix_acl_name'], name, value)


            class Global_(Entity):
                """
                Per VRF Global configuration for MPLS LDP
                
                .. attribute:: graceful_restart
                
                	Configuration for per\-VRF LDP Graceful Restart parameters
                	**type**\:   :py:class:`GracefulRestart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.GracefulRestart>`
                
                .. attribute:: neighbor
                
                	Configuration related to Neighbors
                	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Neighbor>`
                
                .. attribute:: router_id
                
                	Configuration for LDP Router ID (LDP ID)
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: session
                
                	LDP Session parameters
                	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Session>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Vrfs.Vrf.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"graceful-restart" : ("graceful_restart", MplsLdp.Vrfs.Vrf.Global_.GracefulRestart), "neighbor" : ("neighbor", MplsLdp.Vrfs.Vrf.Global_.Neighbor), "session" : ("session", MplsLdp.Vrfs.Vrf.Global_.Session)}
                    self._child_list_classes = {}

                    self.router_id = YLeaf(YType.str, "router-id")

                    self.graceful_restart = MplsLdp.Vrfs.Vrf.Global_.GracefulRestart()
                    self.graceful_restart.parent = self
                    self._children_name_map["graceful_restart"] = "graceful-restart"
                    self._children_yang_names.add("graceful-restart")

                    self.neighbor = MplsLdp.Vrfs.Vrf.Global_.Neighbor()
                    self.neighbor.parent = self
                    self._children_name_map["neighbor"] = "neighbor"
                    self._children_yang_names.add("neighbor")

                    self.session = MplsLdp.Vrfs.Vrf.Global_.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"
                    self._children_yang_names.add("session")
                    self._segment_path = lambda: "global"

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.Vrfs.Vrf.Global_, ['router_id'], name, value)


                class GracefulRestart(Entity):
                    """
                    Configuration for per\-VRF LDP Graceful
                    Restart parameters
                    
                    .. attribute:: helper_peer
                    
                    	Configure parameters related to GR peer(s) opearating in helper mode
                    	**type**\:   :py:class:`HelperPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Global_.GracefulRestart, self).__init__()

                        self.yang_name = "graceful-restart"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"helper-peer" : ("helper_peer", MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer)}
                        self._child_list_classes = {}

                        self.helper_peer = MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer()
                        self.helper_peer.parent = self
                        self._children_name_map["helper_peer"] = "helper-peer"
                        self._children_yang_names.add("helper-peer")
                        self._segment_path = lambda: "graceful-restart"


                    class HelperPeer(Entity):
                        """
                        Configure parameters related to GR peer(s)
                        opearating in helper mode
                        
                        .. attribute:: maintain_on_local_reset
                        
                        	Maintain the state of a GR peer upon a local reset
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer, self).__init__()

                            self.yang_name = "helper-peer"
                            self.yang_parent_name = "graceful-restart"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.maintain_on_local_reset = YLeaf(YType.str, "maintain-on-local-reset")
                            self._segment_path = lambda: "helper-peer"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer, ['maintain_on_local_reset'], name, value)


                class Neighbor(Entity):
                    """
                    Configuration related to Neighbors
                    
                    .. attribute:: ldp_ids
                    
                    	Configuration related to Neighbors using LDP Id
                    	**type**\:   :py:class:`LdpIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds>`
                    
                    .. attribute:: password
                    
                    	Default password for all neigbors
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Global_.Neighbor, self).__init__()

                        self.yang_name = "neighbor"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ldp-ids" : ("ldp_ids", MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds)}
                        self._child_list_classes = {}

                        self.password = YLeaf(YType.str, "password")

                        self.ldp_ids = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds()
                        self.ldp_ids.parent = self
                        self._children_name_map["ldp_ids"] = "ldp-ids"
                        self._children_yang_names.add("ldp-ids")
                        self._segment_path = lambda: "neighbor"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.Vrfs.Vrf.Global_.Neighbor, ['password'], name, value)


                    class LdpIds(Entity):
                        """
                        Configuration related to Neighbors using LDP
                        Id
                        
                        .. attribute:: ldp_id
                        
                        	LDP ID based configuration related to a neigbor
                        	**type**\: list of    :py:class:`LdpId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds, self).__init__()

                            self.yang_name = "ldp-ids"
                            self.yang_parent_name = "neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"ldp-id" : ("ldp_id", MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId)}

                            self.ldp_id = YList(self)
                            self._segment_path = lambda: "ldp-ids"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds, [], name, value)


                        class LdpId(Entity):
                            """
                            LDP ID based configuration related to a
                            neigbor
                            
                            .. attribute:: lsr_id  <key>
                            
                            	LSR ID of neighbor
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: label_space_id  <key>
                            
                            	Label space ID of neighbor
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: password
                            
                            	Password for MD5 authentication for this neighbor
                            	**type**\:   :py:class:`Password <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId, self).__init__()

                                self.yang_name = "ldp-id"
                                self.yang_parent_name = "ldp-ids"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"password" : ("password", MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password)}
                                self._child_list_classes = {}

                                self.lsr_id = YLeaf(YType.str, "lsr-id")

                                self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                self.password = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password()
                                self.password.parent = self
                                self._children_name_map["password"] = "password"
                                self._children_yang_names.add("password")
                                self._segment_path = lambda: "ldp-id" + "[lsr-id='" + self.lsr_id.get() + "']" + "[label-space-id='" + self.label_space_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId, ['lsr_id', 'label_space_id'], name, value)


                            class Password(Entity):
                                """
                                Password for MD5 authentication for this
                                neighbor
                                
                                .. attribute:: command_type
                                
                                	Command type for password configuration
                                	**type**\:   :py:class:`MplsLdpNbrPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpNbrPassword>`
                                
                                .. attribute:: password
                                
                                	The neighbor password
                                	**type**\:  str
                                
                                	**pattern:** (!.+)\|([^!].+)
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password, self).__init__()

                                    self.yang_name = "password"
                                    self.yang_parent_name = "ldp-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.command_type = YLeaf(YType.enumeration, "command-type")

                                    self.password = YLeaf(YType.str, "password")
                                    self._segment_path = lambda: "password"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password, ['command_type', 'password'], name, value)


                class Session(Entity):
                    """
                    LDP Session parameters
                    
                    .. attribute:: downstream_on_demand
                    
                    	ACL with the list of neighbors configured for Downstream on Demand
                    	**type**\:   :py:class:`DownstreamOnDemand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Global_.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"downstream-on-demand" : ("downstream_on_demand", MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand)}
                        self._child_list_classes = {}

                        self.downstream_on_demand = MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand()
                        self.downstream_on_demand.parent = self
                        self._children_name_map["downstream_on_demand"] = "downstream-on-demand"
                        self._children_yang_names.add("downstream-on-demand")
                        self._segment_path = lambda: "session"


                    class DownstreamOnDemand(Entity):
                        """
                        ACL with the list of neighbors configured
                        for Downstream on Demand
                        
                        .. attribute:: peer_acl_name
                        
                        	Name of peer ACL
                        	**type**\:  str
                        
                        .. attribute:: type
                        
                        	Downstream on demand type
                        	**type**\:   :py:class:`MplsLdpDownstreamOnDemand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpDownstreamOnDemand>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand, self).__init__()

                            self.yang_name = "downstream-on-demand"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "downstream-on-demand"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand, ['peer_acl_name', 'type'], name, value)


            class Interfaces(Entity):
                """
                MPLS LDP configuration pertaining to
                interfaces
                
                .. attribute:: interface
                
                	MPLS LDP configuration for a particular interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(MplsLdp.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", MplsLdp.Vrfs.Vrf.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    MPLS LDP configuration for a particular
                    interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Name of interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: afs
                    
                    	Address Family specific configuration for MPLS LDP vrf intf
                    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs>`
                    
                    .. attribute:: enable
                    
                    	Enable Label Distribution Protocol (LDP) on thisinterface
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"afs" : ("afs", MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.afs = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                        self._children_yang_names.add("afs")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.Vrfs.Vrf.Interfaces.Interface, ['interface_name', 'enable'], name, value)


                    class Afs(Entity):
                        """
                        Address Family specific configuration for
                        MPLS LDP vrf intf
                        
                        .. attribute:: af
                        
                        	Configure data for given Address Family
                        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs, self).__init__()

                            self.yang_name = "afs"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"af" : ("af", MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af)}

                            self.af = YList(self)
                            self._segment_path = lambda: "afs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs, [], name, value)


                        class Af(Entity):
                            """
                            Configure data for given Address Family
                            
                            .. attribute:: af_name  <key>
                            
                            	Address Family name
                            	**type**\:   :py:class:`MplsLdpafName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafName>`
                            
                            .. attribute:: discovery
                            
                            	Configure interface discovery parameters
                            	**type**\:   :py:class:`Discovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery>`
                            
                            .. attribute:: enable
                            
                            	Enable Address Family
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af, self).__init__()

                                self.yang_name = "af"
                                self.yang_parent_name = "afs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"discovery" : ("discovery", MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery)}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.enable = YLeaf(YType.empty, "enable")

                                self.discovery = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery()
                                self.discovery.parent = self
                                self._children_name_map["discovery"] = "discovery"
                                self._children_yang_names.add("discovery")
                                self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af, ['af_name', 'enable'], name, value)


                            class Discovery(Entity):
                                """
                                Configure interface discovery parameters
                                
                                .. attribute:: transport_address
                                
                                	MPLS LDP configuration for interface discovery transportaddress
                                	**type**\:   :py:class:`TransportAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery, self).__init__()

                                    self.yang_name = "discovery"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"transport-address" : ("transport_address", MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress)}
                                    self._child_list_classes = {}

                                    self.transport_address = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress()
                                    self.transport_address.parent = self
                                    self._children_name_map["transport_address"] = "transport-address"
                                    self._children_yang_names.add("transport-address")
                                    self._segment_path = lambda: "discovery"


                                class TransportAddress(Entity):
                                    """
                                    MPLS LDP configuration for interface
                                    discovery transportaddress.
                                    
                                    .. attribute:: address
                                    
                                    	IP address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: address_type
                                    
                                    	Transport address option
                                    	**type**\:   :py:class:`MplsLdpTransportAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpTransportAddress>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, self).__init__()

                                        self.yang_name = "transport-address"
                                        self.yang_parent_name = "discovery"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_type = YLeaf(YType.enumeration, "address-type")
                                        self._segment_path = lambda: "transport-address"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, ['address', 'address_type'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsLdp()
        return self._top_entity

